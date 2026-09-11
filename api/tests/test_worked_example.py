"""The arithmetic printed in the README must be reproducible.

Section 5 invites the reader to check the worked example on paper. These
tests are the same check, run automatically, so the claim cannot quietly
drift away from the code.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from engine.capacity import Capacity                      # noqa: E402
from engine.load import band_of, estimate_day             # noqa: E402
from engine.vectors import Task, task_demand              # noqa: E402

CAPACITY = Capacity(baseline="moderate", focus_hours=5.0)
ASSIGNMENT = Task("assignment", 3.0, "high", "academic")
ERRAND = Task("errand", 1.0, "medium", "errands")


def test_ceiling_matches_readme():
    assert CAPACITY.ceiling() == pytest.approx((2.0, 2.0, 1.25, 1.25, 1.0))


def test_task_demand_matches_readme():
    assert task_demand(ASSIGNMENT) == pytest.approx((2.31, 1.26, 0.21, 0.21, 0.21))


def test_single_task_day_is_93_576_percent():
    day = estimate_day([ASSIGNMENT], CAPACITY)
    assert round(day.percentage, 3) == 93.576
    assert day.displayed == 94


def test_adding_one_errand_hour_gives_101_616_percent():
    day = estimate_day([ASSIGNMENT, ERRAND], CAPACITY)
    assert round(day.percentage, 3) == 101.616
    assert day.displayed == 102


def test_mental_axis_warning_is_120_5_percent():
    day = estimate_day([ASSIGNMENT, ERRAND], CAPACITY)
    assert day.warnings["mental"] == 120.5


def test_three_hours_of_two_kinds_are_not_the_same_load():
    """The whole premise: same hours, different cost."""
    academic = estimate_day([Task("a", 3.0, "high", "academic")], CAPACITY)
    social = estimate_day([Task("b", 3.0, "high", "social")], CAPACITY)
    assert academic.percentage != social.percentage
    assert academic.demand[0] > social.demand[0]   # mental
    assert social.demand[3] > academic.demand[3]   # social


def test_bands_are_half_open_and_classified_before_rounding():
    assert band_of(49.999) == "light"
    assert band_of(50.0) == "manageable"
    assert band_of(69.999) == "manageable"
    assert band_of(70.0) == "heavy"
    assert band_of(89.999) == "heavy"     # displays as 90%, still Heavy
    assert band_of(90.0) == "overload"


def test_priority_cannot_change_a_load_figure():
    """Calling something important must never make it heavier."""
    low = estimate_day([Task("t", 3.0, "high", "academic", priority="low")], CAPACITY)
    high = estimate_day([Task("t", 3.0, "high", "academic", priority="high")], CAPACITY)
    assert low.percentage == high.percentage


def test_same_inputs_always_give_the_same_number():
    first = estimate_day([ASSIGNMENT, ERRAND], CAPACITY).percentage
    second = estimate_day([ERRAND, ASSIGNMENT], CAPACITY).percentage
    assert first == second
