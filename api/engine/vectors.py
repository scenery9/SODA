"""Demand vectors.

Every constant here is the one printed in section 5 of the README, under
"How the estimate works". If you change a number, change it there too and
re-run the tests: test_worked_example.py fails loudly when they drift apart.

The five axes are always in this order: mental, time, physical, social, errands.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Literal, Tuple

AXES: Tuple[str, ...] = ("mental", "time", "physical", "social", "errands")

Vector = Tuple[float, float, float, float, float]

Effort = Literal["low", "medium", "high", "very_high", "extra_high"]
Category = Literal["academic", "work", "social", "errands", "other"]

#: How demanding the student says the task is. Their own judgement, and the
#: only load input they set by opinion rather than fact, so the range is fixed
#: and published rather than tuneable per user.
EFFORT_MULTIPLIER: dict[Effort, float] = {
    "low": 0.6,
    "medium": 1.0,
    "high": 1.4,
    "very_high": 1.7,
    "extra_high": 2.0,
}

#: Where an hour of this kind of work actually lands. Two tasks can take the
#: same hour and cost completely different things.
CATEGORY_WEIGHT: dict[Category, Vector] = {
    "academic": (0.55, 0.30, 0.05, 0.05, 0.05),
    "work":     (0.25, 0.35, 0.25, 0.10, 0.05),
    "social":   (0.10, 0.25, 0.10, 0.50, 0.05),
    "errands":  (0.10, 0.30, 0.25, 0.05, 0.30),
    "other":    (0.20, 0.20, 0.20, 0.20, 0.20),
}


@dataclass(frozen=True)
class Task:
    """A commitment the student has confirmed.

    ``priority`` is carried here but never read by this module. It exists so
    that rebalance.py can order what it is allowed to move; letting it touch
    the load would mean calling something important made it heavier, which is
    exactly what the model refuses to do.
    """

    id: str
    duration_hours: float
    effort: Effort
    category: Category
    priority: Literal["low", "medium", "high"] = "medium"
    fixed: bool = False

    def __post_init__(self) -> None:
        if self.duration_hours <= 0:
            raise ValueError(f"{self.id}: duration must be positive")
        if self.effort not in EFFORT_MULTIPLIER:
            raise ValueError(f"{self.id}: unknown effort {self.effort!r}")
        if self.category not in CATEGORY_WEIGHT:
            raise ValueError(f"{self.id}: unknown category {self.category!r}")


def task_demand(task: Task) -> Vector:
    """L = duration x effort x w[c], in load-hours per axis."""
    scale = task.duration_hours * EFFORT_MULTIPLIER[task.effort]
    w = CATEGORY_WEIGHT[task.category]
    return tuple(scale * wi for wi in w)  # type: ignore[return-value]


def day_demand(tasks: Iterable[Task]) -> Vector:
    """Sum of every task's demand on one day."""
    total = [0.0] * len(AXES)
    for task in tasks:
        for i, value in enumerate(task_demand(task)):
            total[i] += value
    return tuple(total)  # type: ignore[return-value]
