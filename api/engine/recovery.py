"""Recovery Debt.

A duration, never a score. The ledger exists so that rest postponed three
weeks ago is still visible, because the week does not reset just because the
calendar does. It never reduces capacity: being tired is not a reason to be
told you can do less than you can.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from typing import Iterable, Sequence

WINDOW_DAYS = 28


@dataclass(frozen=True)
class RecoveryEntry:
    """One completed recovery session. Intervals, not just a count of minutes,
    because two overlapping logs are one rest, not two."""

    on_date: date
    start_minute: int
    end_minute: int

    def __post_init__(self) -> None:
        if not 0 <= self.start_minute < self.end_minute <= 1440:
            raise ValueError("recovery interval must be inside one day and non-empty")

    @property
    def minutes(self) -> int:
        return self.end_minute - self.start_minute


def union_minutes(entries: Iterable[RecoveryEntry]) -> int:
    """Overlapping sessions count once."""
    spans = sorted((e.start_minute, e.end_minute) for e in entries)
    total = 0
    current_start: int | None = None
    current_end = 0
    for start, end in spans:
        if current_start is None:
            current_start, current_end = start, end
            continue
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            total += current_end - current_start
            current_start, current_end = start, end
    if current_start is not None:
        total += current_end - current_start
    return total


@dataclass(frozen=True)
class Debt:
    minutes: int
    days_counted: int
    days_with_no_record: int

    def formatted(self) -> str:
        return f"{self.minutes // 60}h {self.minutes % 60:02d}m"

    @property
    def coverage_is_complete(self) -> bool:
        return self.days_with_no_record == 0


def debt(
    entries: Sequence[RecoveryEntry],
    daily_target_minutes: int,
    today: date,
    since: date | None = None,
) -> Debt:
    """Shortfall over the last 28 completed days.

    Today is excluded on purpose: a day still in progress has not failed to
    contain rest yet. Extra rest on one day does not repay an earlier day,
    because the point was to rest then.
    """
    by_day: dict[date, list[RecoveryEntry]] = {}
    for entry in entries:
        by_day.setdefault(entry.on_date, []).append(entry)

    total = 0
    counted = 0
    blank = 0
    for offset in range(1, WINDOW_DAYS + 1):
        day = today - timedelta(days=offset)
        if since is not None and day < since:
            continue
        counted += 1
        logged = union_minutes(by_day.get(day, []))
        if day not in by_day:
            blank += 1
        total += max(0, daily_target_minutes - logged)
    return Debt(minutes=total, days_counted=counted, days_with_no_record=blank)
