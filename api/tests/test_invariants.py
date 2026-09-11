"""Rules the engine must never break.

Each of these is a promise the README makes to a student. If one fails, the
product is lying to someone, so they are written as invariants rather than
examples.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from engine.capacity import Capacity                       # noqa: E402
from engine.impact import preview                          # noqa: E402
from engine.load import estimate_day                       # noqa: E402
from engine.rebalance import apply, candidates, plan       # noqa: E402
from engine.vectors import Task                            # noqa: E402

CAP = Capacity()


def week():
    return {
        "fri": [
            Task("class", 2.0, "medium", "academic", fixed=True),
            Task("shift", 4.0, "medium", "work", priority="high", fixed=True),
            Task("laundry", 1.0, "low", "errands", priority="low"),
            Task("revision", 1.5, "medium", "academic", priority="medium"),
        ],
        "sat": [],
        "sun": [],
    }


# --- Impact Preview writes nothing -------------------------------------------

def test_preview_does_not_touch_the_saved_week():
    existing = [Task("a", 2.0, "medium", "academic")]
    snapshot = list(existing)
    preview(existing, Task("b", 1.0, "low", "social"), CAP)
    assert existing == snapshot


def test_preview_reports_when_a_day_crosses_the_limit():
    existing = [Task("a", 2.5, "high", "academic")]
    impact = preview(existing, Task("club", 1.0, "medium", "social"), CAP)
    assert impact.after.percentage > impact.before.percentage
    assert impact.crosses_limit is (impact.before.band != "overload"
                                    and impact.after.band == "overload")


# --- Smart Rebalance ---------------------------------------------------------

def test_a_fixed_commitment_is_never_offered_as_a_move():
    """A student who loses a paid shift loses income. It is not ours to move."""
    for move in candidates(week(), "fri", CAP):
        assert move.task.fixed is False


def test_a_move_never_pushes_the_destination_into_overload():
    """Relocating a problem is not solving it."""
    for move in candidates(week(), "fri", CAP):
        assert move.destination_after < 90.0


def test_low_priority_work_is_offered_before_medium_and_high():
    offered = candidates(week(), "fri", CAP)
    priorities = [m.task.priority for m in offered]
    assert priorities == sorted(priorities, key={"low": 0, "medium": 1, "high": 2}.get)


def test_the_same_week_always_produces_the_same_suggestion():
    first = [m.describe() for m in candidates(week(), "fri", CAP)]
    second = [m.describe() for m in candidates(week(), "fri", CAP)]
    assert first == second


def test_applying_moves_leaves_the_original_week_untouched():
    original = week()
    snapshot = {k: list(v) for k, v in original.items()}
    moves = candidates(original, "fri", CAP)[:1]
    apply(original, moves)
    assert original == snapshot


def test_no_task_is_lost_or_duplicated_when_moves_are_applied():
    original = week()
    moves = candidates(original, "fri", CAP)[:2]
    after = apply(original, moves)
    before_ids = sorted(t.id for day in original.values() for t in day)
    after_ids = sorted(t.id for day in after.values() for t in day)
    assert before_ids == after_ids


def test_a_week_with_no_feasible_move_returns_nothing_rather_than_pretending():
    stuck = {"fri": [Task("exam", 6.0, "extra_high", "academic", fixed=True)]}
    moves, after = plan(stuck, "fri", CAP)
    assert moves == []
    assert after.band == "overload"


# --- Input validation --------------------------------------------------------

@pytest.mark.parametrize("bad", [0, -1])
def test_a_task_cannot_have_no_duration(bad):
    with pytest.raises(ValueError):
        Task("t", bad, "medium", "academic")


def test_unknown_effort_or_category_is_refused():
    with pytest.raises(ValueError):
        Task("t", 1.0, "catastrophic", "academic")   # type: ignore[arg-type]
    with pytest.raises(ValueError):
        Task("t", 1.0, "medium", "vibes")            # type: ignore[arg-type]


def test_check_ins_cannot_silently_lower_capacity():
    """Capacity comes from onboarding and nothing else edits it here."""
    before = CAP.ceiling()
    estimate_day([Task("a", 3.0, "high", "academic")], CAP)
    assert CAP.ceiling() == before
