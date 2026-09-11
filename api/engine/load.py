"""Day figure and severity bands.

The blend is deliberate. A pure average lets one saturated axis hide behind
four quiet ones, and a pure maximum ignores everything else. Taking most of
the busiest axis plus some of the weighted average keeps a student whose
mental load is at 118% from being told their day is fine.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Literal, Tuple

from .capacity import Capacity
from .vectors import AXES, Task, Vector, day_demand

Band = Literal["light", "manageable", "heavy", "overload"]

#: How much each axis contributes to the averaged half of the day figure.
BLEND_WEIGHT: Vector = (0.30, 0.30, 0.15, 0.15, 0.10)

#: Share of the figure taken from the busiest axis alone.
PEAK_SHARE = 0.6

#: Lower bounds, half open. Classified before rounding, so 89.6% is Heavy and
#: displays as 90% rather than being promoted into Overload by the rounding.
BAND_FLOOR: tuple[tuple[float, Band], ...] = (
    (90.0, "overload"),
    (70.0, "heavy"),
    (50.0, "manageable"),
    (0.0, "light"),
)

#: An axis at or above this raises its own warning even when the blended day
#: figure looks acceptable.
AXIS_WARNING_AT = 1.0


def utilisation(demand: Vector, capacity: Capacity) -> Vector:
    """U = L_day / C, per axis. Never clamped: 118% is information."""
    ceiling = capacity.ceiling()
    return tuple(d / c for d, c in zip(demand, ceiling))  # type: ignore[return-value]


def day_percentage(u: Vector) -> float:
    """100 x ( 0.6 x max(U) + 0.4 x sum(lambda x U) ). Unrounded."""
    weighted = sum(w * ui for w, ui in zip(BLEND_WEIGHT, u))
    return 100.0 * (PEAK_SHARE * max(u) + (1 - PEAK_SHARE) * weighted)


def band_of(percentage: float) -> Band:
    """Classify on the unrounded score."""
    for floor, band in BAND_FLOOR:
        if percentage >= floor:
            return band
    return "light"


def axis_warnings(u: Vector) -> dict[str, float]:
    """Axes at or over their own ceiling, as percentages."""
    return {
        axis: round(value * 100, 1)
        for axis, value in zip(AXES, u)
        if value >= AXIS_WARNING_AT
    }


@dataclass(frozen=True)
class DayEstimate:
    demand: Vector
    utilisation: Vector
    percentage: float
    band: Band
    warnings: dict[str, float]

    @property
    def displayed(self) -> int:
        """What the screen shows. The band is already fixed by then."""
        return round(self.percentage)


def estimate_day(tasks: Iterable[Task], capacity: Capacity) -> DayEstimate:
    demand = day_demand(tasks)
    u = utilisation(demand, capacity)
    pct = day_percentage(u)
    return DayEstimate(
        demand=demand,
        utilisation=u,
        percentage=pct,
        band=band_of(pct),
        warnings=axis_warnings(u),
    )


def peak_day(days: dict[str, list[Task]], capacity: Capacity) -> tuple[str, DayEstimate]:
    """The week headline. The maximum daily figure, never an average: an
    average of one terrible day and six calm ones reads as a calm week."""
    if not days:
        raise ValueError("no days to compare")
    scored = {label: estimate_day(tasks, capacity) for label, tasks in days.items()}
    label = max(scored, key=lambda k: scored[k].percentage)
    return label, scored[label]
