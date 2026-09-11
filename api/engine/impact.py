"""Impact Preview.

The point of this module is what it does not do: it writes nothing. A student
can price a commitment and walk away, and nothing in their week has changed.
Saving is a separate, explicitly approved call.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .capacity import Capacity
from .load import DayEstimate, estimate_day
from .vectors import AXES, Task


@dataclass(frozen=True)
class Impact:
    before: DayEstimate
    after: DayEstimate

    @property
    def delta(self) -> float:
        return self.after.percentage - self.before.percentage

    @property
    def axis_deltas(self) -> dict[str, float]:
        return {
            axis: round((a - b) * 100, 1)
            for axis, b, a in zip(AXES, self.before.utilisation, self.after.utilisation)
        }

    @property
    def crosses_limit(self) -> bool:
        """True when accepting this would push a day that was under the
        overload threshold over it. The moment worth interrupting for."""
        return self.before.band != "overload" and self.after.band == "overload"

    def summary(self) -> str:
        return (
            f"{self.before.displayed}% to {self.after.displayed}%"
            f" ({self.after.band})"
        )


def preview(existing: Sequence[Task], candidate: Task, capacity: Capacity) -> Impact:
    """Simulate adding one unsaved task. Pure: no writes, no network."""
    return Impact(
        before=estimate_day(existing, capacity),
        after=estimate_day([*existing, candidate], capacity),
    )


def preview_week(
    days: dict[str, list[Task]], day: str, candidate: Task, capacity: Capacity
) -> tuple[Impact, dict[str, DayEstimate]]:
    """The same, but keeping the whole week visible: a change that fixes one
    day by wrecking another is not an improvement."""
    if day not in days:
        raise KeyError(f"{day!r} is not in this week")
    impact = preview(days[day], candidate, capacity)
    after = {
        label: estimate_day([*tasks, candidate] if label == day else tasks, capacity)
        for label, tasks in days.items()
    }
    return impact, after
