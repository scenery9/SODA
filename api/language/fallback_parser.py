"""The default path for real student text.

Section 5 says free-form entry is read by server rules, not by a model. This
is those rules. It is deterministic, it runs offline, and it never leaves the
machine, which is why it is the default rather than the fallback its filename
suggests.

What it returns is a *draft*. The student confirms every field before anything
is saved, so a wrong guess costs a tap, not a corrupted week.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Literal

Effort = Literal["low", "medium", "high", "very_high", "extra_high"]
Category = Literal["academic", "work", "social", "errands", "other"]

#: Words students actually use, mapped to the category weights in the engine.
CATEGORY_HINTS: dict[Category, tuple[str, ...]] = {
    "academic": ("assignment", "essay", "revision", "study", "lecture", "class",
                 "exam", "quiz", "presentation", "lab", "tutorial", "report"),
    "work":     ("shift", "work", "meeting", "client", "intern", "job"),
    "social":   ("dinner", "birthday", "party", "hangout", "catch up", "coffee",
                 "club", "society", "friend"),
    "errands":  ("laundry", "groceries", "shopping", "clean", "bank", "post",
                 "appointment", "chores"),
}

#: Only phrases that clearly indicate weight. Anything else stays Medium,
#: because guessing high makes a day look worse than the student said it was.
EFFORT_HINTS: dict[Effort, tuple[str, ...]] = {
    "extra_high": ("brutal", "killer", "nightmare"),
    "very_high":  ("really hard", "very hard", "very heavy", "huge"),
    "high":       ("hard", "heavy", "difficult", "tough", "big", "draining"),
    "low":        ("easy", "quick", "light", "simple", "small"),
}

_DURATION = re.compile(
    r"(?P<value>\d+(?:\.\d+)?)\s*(?P<unit>hours?|hrs?|h|minutes?|mins?|m)\b",
    re.IGNORECASE,
)
_HALF = re.compile(r"\b(?:an?\s+)?half\s+an?\s+hour\b", re.IGNORECASE)
_TIME = re.compile(r"\b(?P<h>[01]?\d|2[0-3])(?::(?P<m>[0-5]\d))?\s*(?P<ap>am|pm)\b",
                   re.IGNORECASE)
_WEEKDAY = re.compile(
    r"\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday|today|tomorrow)\b",
    re.IGNORECASE,
)


@dataclass
class Draft:
    """Everything the parser is willing to claim, plus what it could not tell."""

    title: str
    duration_minutes: int | None = None
    effort: Effort = "medium"
    category: Category = "other"
    weekday: str | None = None
    start_minute: int | None = None
    unresolved: list[str] = field(default_factory=list)

    @property
    def needs_confirmation(self) -> bool:
        """Always true. The student confirms before anything is written."""
        return True


def _duration_minutes(text: str) -> int | None:
    if _HALF.search(text):
        return 30
    match = _DURATION.search(text)
    if not match:
        return None
    value = float(match.group("value"))
    unit = match.group("unit").lower()
    minutes = value * 60 if unit.startswith(("h", "hr")) else value
    minutes = int(round(minutes))
    return minutes if 0 < minutes <= 24 * 60 else None


def _start_minute(text: str) -> int | None:
    match = _TIME.search(text)
    if not match:
        return None
    hour = int(match.group("h")) % 12
    if match.group("ap").lower() == "pm":
        hour += 12
    return hour * 60 + int(match.group("m") or 0)


def _category(text: str) -> Category:
    lowered = text.lower()
    for category, words in CATEGORY_HINTS.items():
        if any(word in lowered for word in words):
            return category
    return "other"


def _effort(text: str) -> Effort:
    lowered = text.lower()
    for level, words in EFFORT_HINTS.items():
        if any(word in lowered for word in words):
            return level
    return "medium"


def _title(text: str) -> str:
    """Strip the scheduling words back out, so the title reads like a task."""
    cleaned = _DURATION.sub("", text)
    cleaned = _HALF.sub("", cleaned)
    cleaned = _TIME.sub("", cleaned)
    cleaned = _WEEKDAY.sub("", cleaned)
    cleaned = re.sub(r"\b(around|about|at|on|for|roughly|next|this)\b", "", cleaned,
                     flags=re.IGNORECASE)
    cleaned = re.sub(r"[,\s]+", " ", cleaned).strip(" ,.-")
    return cleaned[:1].upper() + cleaned[1:] if cleaned else "Untitled task"


def parse(text: str) -> Draft:
    """Read one sentence into a draft. Never raises: unreadable input comes
    back as a draft with everything unresolved, which the form can still show."""
    text = (text or "").strip()
    if not text:
        return Draft(title="Untitled task", unresolved=["title", "duration", "when"])

    weekday = _WEEKDAY.search(text)
    draft = Draft(
        title=_title(text),
        duration_minutes=_duration_minutes(text),
        effort=_effort(text),
        category=_category(text),
        weekday=weekday.group(0).lower() if weekday else None,
        start_minute=_start_minute(text),
    )
    if draft.duration_minutes is None:
        draft.unresolved.append("duration")
    if draft.weekday is None and draft.start_minute is None:
        draft.unresolved.append("when")
    if draft.category == "other":
        draft.unresolved.append("category")
    return draft
