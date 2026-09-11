"""SODA API.

What is implemented: the deterministic engine and the two routes that only
need it, /impact-preview and /rebalance. Both are read-only by design, so
they can be honest without a database behind them.

What is not: anything that writes. Those routes are declared here with the
contract they will honour and a 501, because a route that silently pretends
to save is worse than one that says it cannot yet.

Run it:  uvicorn main:app --reload --app-dir api
"""

from __future__ import annotations

from typing import Literal

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

from engine.capacity import Capacity
from engine.impact import preview
from engine.load import estimate_day
from engine.rebalance import plan
from engine.vectors import AXES, Task

app = FastAPI(
    title="SODA",
    version="0.1.0",
    summary="Student workload planning. The arithmetic is in engine/ and never calls a model.",
)


# --- request shapes ----------------------------------------------------------

class TaskIn(BaseModel):
    id: str
    duration_hours: float = Field(gt=0)
    effort: Literal["low", "medium", "high", "very_high", "extra_high"] = "medium"
    category: Literal["academic", "work", "social", "errands", "other"] = "academic"
    priority: Literal["low", "medium", "high"] = "medium"
    fixed: bool = False

    def to_task(self) -> Task:
        return Task(self.id, self.duration_hours, self.effort,
                    self.category, self.priority, self.fixed)


class CapacityIn(BaseModel):
    baseline: Literal["light", "moderate", "heavy"] = "moderate"
    focus_hours: float = Field(default=5.0, gt=0)
    recovery_minutes: int = Field(default=45, ge=0, le=1440)

    def to_capacity(self) -> Capacity:
        return Capacity(self.baseline, self.focus_hours, self.recovery_minutes)


class DayIn(BaseModel):
    capacity: CapacityIn = CapacityIn()
    tasks: list[TaskIn] = []


class PreviewIn(DayIn):
    candidate: TaskIn


class WeekIn(BaseModel):
    capacity: CapacityIn = CapacityIn()
    days: dict[str, list[TaskIn]]
    crowded_day: str


# --- implemented -------------------------------------------------------------

@app.post("/load", summary="What a day currently costs")
def load(body: DayIn) -> dict:
    day = estimate_day([t.to_task() for t in body.tasks], body.capacity.to_capacity())
    return {
        "percentage": round(day.percentage, 3),
        "displayed": day.displayed,
        "band": day.band,
        "axes": dict(zip(AXES, [round(v * 100, 1) for v in day.utilisation])),
        "warnings": day.warnings,
    }


@app.post("/impact-preview", summary="Price a task before it is saved")
def impact_preview(body: PreviewIn) -> dict:
    """Writes nothing. A student can ask what a commitment costs and walk away."""
    cap = body.capacity.to_capacity()
    result = preview([t.to_task() for t in body.tasks], body.candidate.to_task(), cap)
    return {
        "before": {"displayed": result.before.displayed, "band": result.before.band},
        "after": {"displayed": result.after.displayed, "band": result.after.band,
                  "warnings": result.after.warnings},
        "axis_deltas": result.axis_deltas,
        "crosses_limit": result.crosses_limit,
        "summary": result.summary(),
        "saved": False,
    }


@app.post("/rebalance", summary="Feasible ways to bring one day down")
def rebalance(body: WeekIn) -> dict:
    """Proposes. Never applies. An empty list means no feasible plan exists,
    which the interface must say rather than disguise."""
    cap = body.capacity.to_capacity()
    days = {label: [t.to_task() for t in tasks] for label, tasks in body.days.items()}
    if body.crowded_day not in days:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "crowded_day is not in days")
    moves, after = plan(days, body.crowded_day, cap)
    return {
        "moves": [
            {"task": m.task.id, "to": m.to_day,
             "reduction": round(m.reduction, 1),
             "destination_after": round(m.destination_after)}
            for m in moves
        ],
        "resulting": {"displayed": after.displayed, "band": after.band},
        "feasible": bool(moves),
        "applied": False,
    }


# --- declared, not yet built -------------------------------------------------

_NOT_YET = "Needs the database and an authenticated session. See docs/BUILD.md."


@app.post("/commitments", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def create_commitment() -> None:
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, _NOT_YET)


@app.post("/rebalance/apply", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def apply_rebalance() -> None:
    """Will take the approved candidate plus the selected moves in one
    transaction, against the expected schedule revision, and return an undo
    token."""
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, _NOT_YET)


@app.post("/recovery/log", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def log_recovery() -> None:
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, _NOT_YET)


@app.get("/health")
def health() -> dict:
    return {"ok": True, "engine": "deterministic", "writes_enabled": False}
