# Running what exists

The deterministic engine is written and tested. Everything that writes to a
database is specified but not built, and says so when called.

## The arithmetic, verified

Section 5 of the [README](README.md#how-the-estimate-works) invites you to check
the worked example on paper. This runs the same check:

```bash
pip install pytest
python -m pytest api/tests -q
```

`api/tests/test_worked_example.py` asserts the exact figures printed in the
README: a three-hour high-effort academic task is `93.576%`, adding one hour of
medium-effort errands makes it `101.616%`, and the mental axis warns at `120.5%`.
If someone edits a coefficient without editing the README, these fail.

The engine needs no dependencies at all. `pytest` is only the runner.

## The API

```bash
pip install -r api/requirements.txt
uvicorn main:app --reload --app-dir api
# http://127.0.0.1:8000/docs
```

Implemented, because they only need the engine and write nothing:

| Route | What it does |
|---|---|
| `POST /load` | What a day currently costs, with per-axis warnings |
| `POST /impact-preview` | Prices an unsaved task. Returns `"saved": false` |
| `POST /rebalance` | Feasible moves for a crowded day. Returns `"applied": false` |

Declared and returning `501`, because they need the database and a signed-in
student: `/commitments`, `/rebalance/apply`, `/recovery/log`. A route that
silently pretends to save is worse than one that admits it cannot yet.

Try it:

```bash
curl -X POST localhost:8000/impact-preview -H "content-type: application/json" -d '{
  "capacity": {"baseline": "moderate", "focus_hours": 5},
  "tasks": [{"id": "assignment", "duration_hours": 3, "effort": "high", "category": "academic"}],
  "candidate": {"id": "club", "duration_hours": 1, "effort": "medium", "category": "social"}
}'
```

## The app

`app/` holds the Flutter skeleton: the dependency set, the theme entry point,
and the two types the rest of the UI is built on. The screens themselves are
designed in Figma and listed in section 3; building them is week one and two of
the [plan](README.md#build-plan--scope).

## What the tests actually protect

| File | The promise it keeps |
|---|---|
| `test_worked_example.py` | The README's arithmetic is reproducible, and priority can never change a load figure |
| `test_invariants.py` | A fixed commitment is never moved, a move never overloads its destination, preview writes nothing, no feasible plan returns nothing rather than pretending |
| `test_recovery.py` | Overlapping logs count once, today is not a missed day, extra rest does not repay an earlier shortfall, debt never lowers capacity |
| `test_engine_is_isolated.py` | The engine imports nothing that can reach a network or a model, and never reads a clock |
| `test_parser.py` | Typed text is read by rules, effort stays Medium unless the student said otherwise, nothing is saved without confirmation |
