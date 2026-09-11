"""The rule parser is the default path, so it is tested like one."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from language.fallback_parser import parse   # noqa: E402


def test_the_prototype_demo_sentence():
    """The exact sentence the prototype types on screen."""
    d = parse("Presentation prep Friday evening, around 3 hours")
    assert d.duration_minutes == 180
    assert d.category == "academic"
    assert d.weekday == "friday"
    assert "Presentation prep" in d.title


def test_half_an_hour_is_understood():
    assert parse("laundry tomorrow half an hour").duration_minutes == 30


def test_minutes_and_hours_both_work():
    assert parse("read for 45 minutes").duration_minutes == 45
    assert parse("shift 6h").duration_minutes == 360
    assert parse("gym 1.5 hours").duration_minutes == 90


def test_a_clock_time_is_read():
    assert parse("revision Sunday 2pm").start_minute == 14 * 60
    assert parse("standup at 9:30am").start_minute == 9 * 60 + 30


def test_effort_stays_medium_unless_the_student_said_otherwise():
    """Guessing high makes someone's day look worse than they described it."""
    assert parse("assignment on Friday").effort == "medium"
    assert parse("easy assignment").effort == "low"
    assert parse("brutal assignment").effort == "extra_high"


def test_category_comes_from_words_students_use():
    assert parse("paid shift Saturday").category == "work"
    assert parse("dinner with friends").category == "social"
    assert parse("groceries").category == "errands"


def test_what_it_cannot_tell_is_reported_rather_than_invented():
    d = parse("do the thing")
    assert "duration" in d.unresolved
    assert "when" in d.unresolved
    assert d.category == "other"


def test_empty_input_still_returns_a_usable_draft():
    d = parse("")
    assert d.title == "Untitled task"
    assert d.unresolved


def test_nothing_is_ever_saved_without_confirmation():
    assert parse("anything at all").needs_confirmation is True


def test_the_same_sentence_always_parses_the_same_way():
    a, b = parse("shift 6h Saturday"), parse("shift 6h Saturday")
    assert (a.title, a.duration_minutes, a.category, a.weekday) == \
           (b.title, b.duration_minutes, b.category, b.weekday)
