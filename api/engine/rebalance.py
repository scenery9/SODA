"""Smart Rebalance.

Priority lives here and nowhere else. Effort says how heavy a task is and
feeds the load; priority says which task SODA is allowed to move first, and
never touches the arithmetic. Keeping them apart is what stops a student from
lowering their own workload figure by calling everything important.

Nothing in this module applies anything. It proposes; the student approves.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .capacity import Capacity
from .load import DayEstimate, estimate_day
from .vectors import Task

#: Lower moves first. A student's own Low-priority work is tried before
#: anything they marked Medium, and High is only ever rescheduled, never cut.
PRIORITY_ORDER: dict[str, int] = {"low": 0, "medium": 1, "high": 2}


@dataclass(frozen=True)
class Move:
    task: Task
    to_day: str
    reduction: float          # percentage points removed from the crowded day
    destination_after: float  # what the destination day becomes

    def describe(self) -> str:
        return f"{self.task.id} to {self.to_day}, -{self.reduction:.0f}%"


def _rank(move: Move) -> tuple:
    """The documented order, with the task id last so the same inputs always
    produce the same suggestion."""
    return (
        PRIORITY_ORDER[move.task.priority],   # lower priority first
        -move.reduction,                      # then what helps most
        0 if not move.task.fixed else 1,      # never a fixed commitment
        move.task.id,                         # deterministic tie-break
    )


def candidates(
    days: dict[str, list[Task]],
    crowded: str,
    capacity: Capacity,
    overload_at: float = 90.0,
) -> list[Move]:
    """Feasible single moves out of the crowded day.

    A move is rejected when it would simply relocate the problem: if the
    destination lands in overload, it is not an improvement, it is a different
    bad day.
    """
    if crowded not in days:
        raise KeyError(f"{crowded!r} is not in this week")

    before = estimate_day(days[crowded], capacity).percentage
    found: list[Move] = []

    for task in days[crowded]:
        if task.fixed:
            continue
        remaining = [t for t in days[crowded] if t.id != task.id]
        after_source = estimate_day(remaining, capacity).percentage
        reduction = before - after_source
        if reduction <= 0:
            continue
        for label, tasks in days.items():
            if label == crowded:
                continue
            after_dest = estimate_day([*tasks, task], capacity).percentage
            if after_dest >= overload_at:
                continue
            found.append(
                Move(task=task, to_day=label, reduction=reduction,
                     destination_after=after_dest)
            )
    return sorted(found, key=_rank)


def apply(days: dict[str, list[Task]], moves: Sequence[Move]) -> dict[str, list[Task]]:
    """Return a new week with the approved moves in it. The input is untouched,
    so an unapproved preview can never leak into saved state."""
    out = {label: list(tasks) for label, tasks in days.items()}
    for move in moves:
        for label in out:
            out[label] = [t for t in out[label] if t.id != move.task.id]
        out[move.to_day].append(move.task)
    return out


def plan(
    days: dict[str, list[Task]],
    crowded: str,
    capacity: Capacity,
    target: float = 90.0,
    max_moves: int = 3,
) -> tuple[list[Move], DayEstimate]:
    """Fewest moves that bring the crowded day under the target.

    Returns whatever it managed plus the resulting estimate. A week with no
    feasible improvement returns an empty list, and the caller is expected to
    say so rather than pretend.
    """
    week = {label: list(tasks) for label, tasks in days.items()}
    chosen: list[Move] = []
    for _ in range(max_moves):
        current = estimate_day(week[crowded], capacity)
        if current.percentage < target:
            break
        options = candidates(week, crowded, capacity, overload_at=target)
        if not options:
            break
        best = options[0]
        chosen.append(best)
        week = apply(week, [best])
    return chosen, estimate_day(week[crowded], capacity)
