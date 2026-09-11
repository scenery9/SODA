"""Recovery Debt behaves like a ledger, not a score."""

import sys
from datetime import date
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from engine.capacity import Capacity                                  # noqa: E402
from engine.recovery import RecoveryEntry, debt, union_minutes        # noqa: E402

TODAY = date(2026, 10, 1)


def on(day_offset: int, start: int, end: int) -> RecoveryEntry:
    from datetime import timedelta
    return RecoveryEntry(TODAY - timedelta(days=day_offset), start, end)


def test_overlapping_sessions_count_once():
    """Logging the same rest twice is not twice the rest."""
    assert union_minutes([on(1, 600, 630), on(1, 620, 650)]) == 50


def test_a_retried_log_cannot_inflate_recovery():
    assert union_minutes([on(1, 600, 630), on(1, 600, 630)]) == 30


def test_today_is_not_counted_as_a_missed_day():
    """A day still in progress has not failed to contain rest yet."""
    full = [on(offset, 0, 45) for offset in range(1, 29)]
    assert debt(full, 45, TODAY).minutes == 0


def test_a_completely_unlogged_month_is_the_full_target():
    assert debt([], 45, TODAY).minutes == 45 * 28


def test_extra_rest_does_not_repay_an_earlier_shortfall():
    """Resting three hours today does not give back the evening you lost."""
    entries = [on(1, 0, 300)]              # five hours, one day
    shortfall = debt(entries, 45, TODAY)
    assert shortfall.minutes == 45 * 27    # every other day still owes


def test_history_coverage_is_reported_so_gaps_are_visible():
    """Missing logs are not proof of missing rest, so say how much we know."""
    result = debt([on(1, 0, 45)], 45, TODAY)
    assert result.days_with_no_record == 27
    assert result.coverage_is_complete is False


def test_debt_is_shown_as_a_duration():
    assert debt([], 45, date(2026, 10, 1)).formatted().endswith("m")
    assert "%" not in debt([], 45, TODAY).formatted()


def test_debt_never_changes_the_capacity_ceiling():
    """Being behind on rest must not quietly tell a student they can do less."""
    cap = Capacity()
    before = cap.ceiling()
    debt([], 45, TODAY)
    assert cap.ceiling() == before


def test_the_weekly_target_comes_from_the_daily_answer():
    assert Capacity(recovery_minutes=45).weekly_recovery_target_minutes() == 315


@pytest.mark.parametrize("bad", [(-1, 10), (600, 600), (600, 1441)])
def test_an_impossible_interval_is_refused(bad):
    with pytest.raises(ValueError):
        RecoveryEntry(TODAY, bad[0], bad[1])
