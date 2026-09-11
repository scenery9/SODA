"""Capacity ceiling.

Onboarding asks four questions. Three of them end up here. The fourth, how
the student recharges, is a recovery preference and deliberately never
reaches this file: a preference about resting must not move a load figure.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Tuple

from .vectors import Vector

Baseline = Literal["light", "moderate", "heavy"]

#: Q1, "what does a normal week look like for you?"
#: A student who calls their normal week heavy is telling us their ceiling is
#: lower, not that they are more capable.
BASELINE_SCALE: dict[Baseline, float] = {"light": 1.15, "moderate": 1.00, "heavy": 0.85}

#: Relative axis ceilings. These are shares of the ceiling, not shares of the
#: day: mental and time carry more than physical, social or errands because
#: that is where student work lands.
AXIS_CEILING: Vector = (0.40, 0.40, 0.25, 0.25, 0.20)

#: Q2 offers ranges; each initialises an editable number of focus hours.
FOCUS_HOURS: dict[str, float] = {"2-4": 3.0, "4-6": 5.0, "6-8": 7.0, "8+": 8.0}

#: Q3 does the same for daily protected recovery, in minutes.
RECOVERY_MINUTES: dict[str, int] = {"0-30": 15, "30-60": 45, "60-90": 75, "90+": 90}


@dataclass(frozen=True)
class Capacity:
    baseline: Baseline = "moderate"
    focus_hours: float = 5.0
    recovery_minutes: int = 45

    def __post_init__(self) -> None:
        if self.focus_hours <= 0:
            raise ValueError("focus hours must be positive")
        if not 0 <= self.recovery_minutes <= 1440:
            raise ValueError("recovery minutes must be a real part of a day")
        if self.baseline not in BASELINE_SCALE:
            raise ValueError(f"unknown baseline {self.baseline!r}")

    def ceiling(self) -> Vector:
        """C = B x H x k, in load-hours per axis."""
        scale = BASELINE_SCALE[self.baseline] * self.focus_hours
        return tuple(scale * k for k in AXIS_CEILING)  # type: ignore[return-value]

    def weekly_recovery_target_minutes(self) -> int:
        """The starting number shown beside Recovery Debt. Editable, and a
        planning default rather than advice about how much rest a person needs."""
        return self.recovery_minutes * 7
