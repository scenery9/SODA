# SODA build specification

> Supporting detail for section 5 of the [README](../README.md). Everything here is **proposed**; no application or deployed service exists yet.

## Product hierarchy and minimum experience

The three main experiences are **My Backpack**, **Impact Preview** and **Recovery Island**. Module boundaries do not imply equal product prominence.

| Main experience | Required supporting behaviour |
|---|---|
| My Backpack | Authenticated manual entry, deterministic calculation, recorded-data coverage and readable explanations. |
| Impact Preview | Unsaved simulation, response choice, constrained Smart Rebalance, explicit approval and safe undo. |
| Recovery Island | A small set of preference-sensitive recovery choices, protected time, completion logging and the rolling Recovery Debt ledger. |

Daily Check-in, Reality Check Lite, richer forecasts, guided timers and Insights extend the experience after the required path works. The minimum Recovery Island cannot be deferred while its underlying ledger alone is presented as the recovery experience.

## Repository structure

```
soda/
├── README.md                    ← submission overview
├── assets/                      ← numbered figures (problem tree, mindmaps, architecture)
├── images/                      ← prototype screen exports
├── docs/                        ← this file, plus the model, evidence and demo notes
├── app/                         ← Flutter (Android + web)
│   ├── lib/
│   │   ├── main.dart
│   │   ├── core/                ← theme, tokens, severity bands, a11y helpers
│   │   ├── data/                ← Drift local DB, Supabase client, repositories
│   │   ├── models/              ← Task, LoadVector, Capacity, RecoveryEntry
│   │   ├── features/
│   │   │   ├── onboarding/      ← 3-question calibration
│   │   │   ├── backpack/        ← My Backpack (home)
│   │   │   ├── capture/         ← add sheet, Tell SODA, manual entry
│   │   │   ├── impact/          ← Impact Preview + Protection Mode
│   │   │   ├── rebalance/       ← Smart Rebalance
│   │   │   ├── forecast/        ← Life Forecast + Day Detail
│   │   │   ├── recovery/        ← Recovery Island, timer, Recovery Debt
│   │   │   ├── checkin/         ← daily check-in
│   │   │   └── insights/        ← trends, weekly review, How SODA Calculates
│   │   └── widgets/             ← charts (each wrapped in Semantics)
│   └── pubspec.yaml
└── api/                         ← FastAPI
    ├── main.py
    ├── routers/                 ← tasks, calendar, load, recovery, checkin, parse
    ├── engine/                  ← ★ deterministic load model, no network calls in here
    │   ├── vectors.py           ← category weights, effort multipliers
    │   ├── capacity.py          ← calibration → ceiling
    │   ├── load.py              ← day/week aggregation, severity bands
    │   ├── impact.py            ← simulation (pure function, no writes)
    │   ├── rebalance.py         ← constrained greedy move search
    │   └── recovery.py          ← recovery debt ledger
    ├── language/                ← OPTIONAL: gemini.py, ollama.py, fallback_parser.py
    └── tests/                   ← arithmetic fixtures, boundary and invariant checks
```

**The single most important structural rule:** `api/engine/` makes **no network calls and imports
nothing from `api/language/`**. That separation is what makes the "deterministic core" claim in
[the architecture](../README.md#system-architecture) true rather than aspirational, and it is enforceable
by a lint rule.

## Data model

```sql
-- every user-owned table follows the same RLS pattern

create table profiles (
  id            uuid primary key references auth.users(id) on delete cascade,
  display_name  text,
  baseline      text    check (baseline in ('light','moderate','heavy')),
  focus_hours   numeric not null default 5 check (focus_hours > 0),     -- Q2: daily focus budget H
  recovery_mins integer not null default 45 check (recovery_mins between 0 and 1440),    -- Q3: daily recovery target R
  created_at    timestamptz default now()
);

create table commitments (
  id            uuid primary key default gen_random_uuid(),
  user_id       uuid not null references auth.users(id) on delete cascade,
  title         text not null,
  starts_at     timestamptz not null,
  duration_min  integer not null check (duration_min > 0),
  effort        text    check (effort in ('low','medium','high','very_high','extra_high')) default 'medium',
  priority      text    not null check (priority in ('low','medium','high')) default 'medium',
  category      text    check (category in ('academic','work','social','errands','other')),
  is_fixed      boolean not null default false, -- classes, shifts: never movable
  deadline_at   timestamptz,                    -- rebalance may not cross this
  source        text    check (source in ('manual','chat','calendar')) default 'manual',
  status        text    check (status in ('planned','done','auto_done','dropped')) default 'planned',
  created_at    timestamptz default now()
);

create table daily_checkins (
  id         uuid primary key default gen_random_uuid(),
  user_id    uuid not null references auth.users(id) on delete cascade,
  on_date    date not null,
  energy     smallint, mood smallint, mental smallint,
  physical   smallint, social smallint,          -- each 1..5
  unique (user_id, on_date)
);

create table recovery_entries (
  id           uuid primary key default gen_random_uuid(),
  user_id      uuid not null references auth.users(id) on delete cascade,
  on_date      date not null,
  axis         text check (axis in ('mental','physical','time','social')),
  minutes      integer not null check (minutes > 0),
  was_protected boolean default false,
  completed    boolean default false
);

create table estimate_feedback (             -- Reality Check
  id            uuid primary key default gen_random_uuid(),
  user_id       uuid not null references auth.users(id) on delete cascade,
  commitment_id uuid references commitments(id) on delete cascade,
  category      text not null,
  duration_fb   text check (duration_fb in ('less','about','a_little_more','much_more')),
  effort_fb     text check (effort_fb  in ('lighter','expected','heavier')),
  created_at    timestamptz default now()
);

-- Profiles use id, unlike the other tables' user_id.
alter table profiles enable row level security;
create policy own_profile on profiles for all
  using (auth.uid() = id) with check (auth.uid() = id);

do $$
declare t text;
begin
  foreach t in array array['commitments','daily_checkins','recovery_entries','estimate_feedback'] loop
    execute format('alter table %I enable row level security', t);
    execute format('create policy own_rows on %I for all using (auth.uid() = user_id) with check (auth.uid() = user_id)', t);
  end loop;
end $$;

-- Cross-user references must be impossible, even if a task UUID is known.
alter table commitments add constraint commitments_id_owner unique (id, user_id);
alter table estimate_feedback add constraint feedback_owned_commitment
  foreign key (commitment_id, user_id) references commitments(id, user_id) on delete cascade;
```

**Schema status:** the SQL above is a starting schema, not the complete migration. The build must add
profile timezone; model version; task `updated_at`/revision; immutable recovery-target history;
recovery start/end intervals for deduplication; unique calendar event identity; and rebalance audit
records with before/after versions for atomic apply/undo. Normal user requests must carry the user's
JWT through the Supabase client so RLS applies; using a service-role key for every request would bypass it.

> Ship nothing until a **second test account** has been used to confirm it cannot read the first
> account's rows. RLS that is enabled but wrongly scoped looks identical to RLS that works.

## API surface

| Method | Route | Purpose | Writes? |
|---|---|---|---|
| `POST` | `/auth/session` | Validate the Supabase session; no custom password handling | No application-data write |
| `GET` | `/week?start=YYYY-MM-DD` | Week commitments + per-day load + capacity + coverage | No |
| `POST` | `/commitments` | Create a commitment | Yes |
| `PATCH` | `/commitments/{id}` | Edit / reschedule / complete | Yes |
| `POST` | **`/impact-preview`** | Simulate adding a candidate task, returns before/after vectors, deltas, breaking day, recovery impact, suggested moves | **No** |
| `POST` | `/rebalance` | Generate constrained move set for a day | No |
| `POST` | `/rebalance/apply` | Atomically save the approved candidate and selected moves against the expected revision (returns an `undo_token`) | Yes |
| `POST` | `/rebalance/undo` | Revert an applied move set | Yes |
| `POST` | `/checkin` | Submit daily check-in | Yes |
| `GET` | `/recovery/debt` | Rolling 4-week ledger | No |
| `POST` | `/recovery/log` | Record a completed recovery session | Yes |
| `POST` | `/feedback` | Reality Check response | Yes |
| `POST` | `/calendar/import` | Read-only Google Calendar pull → staged for confirmation | Staged |
| `POST` | **`/parse`** | Real text → server rule parser. Optional AI route accepts only an allowlisted synthetic `example_id`; timeout falls back to rules. | No |

`/impact-preview` and `/parse` are both **non-writing** by design: a student can explore a decision and
change their mind without creating a commitment, and a parse failure can never corrupt data.

## Demo seed data

The [shared Aina case](DEMO-AND-VALIDATION.md#one-case-across-all-three-experiences) supplies the qualitative scheduling walkthrough and its constraints. It is not the numerical `decision-loop` fixture below. Do not reuse illustrative percentages for that schedule without specifying and calculating the complete inputs.

The demo account needs enough history for Recovery Debt and Reality Check to be non-empty:

- **4 weeks** of past commitments across all five categories, with realistic clustering (assignments
  bunching near deadlines, shifts on fixed weekdays)
- Recovery entries producing a **total debt of ~2h 35m**, distributed 0h20 / 0h45 / 0h55 / 0h35 across
  the four weeks, to match the Recovery Debt screen
- **14 imported tasks** in the review window, grouped as 5 Academic, 3 Work, 3 Social, 2 Errands
  and 1 Self-care, matching the Calendar Review screen. Where an import covers only part of the
  range, say so on screen rather than presenting the estimate as complete
- Use separate named fixtures: `decision-loop` targets 82% → 112% → 89% (Heavy, below the overload threshold); `worked-model` reproduces the [load model](MODEL.md#step-3-utilisation-and-the-day-figure) example (93.576% → 101.616%). Do not splice them into one continuous demo.
- At least 5 completed tasks in the Academic category with "took longer" feedback, so Reality Check has a
  live directional suggestion to show

## Integration contracts and acceptance

- **Candidate approval:** `/impact-preview` returns a schedule revision and an unsaved candidate. `/rebalance/apply` accepts that candidate plus explicitly selected moves in one transaction; `/commitments` handles acceptance without adjustments. Both reject stale revisions and use an idempotency key to prevent duplicate tasks after retries.
- **Authentication:** validate issuer, audience, signature and expiry of the user JWT. Pass the user token to database calls so RLS remains effective. Keep service-role credentials out of normal user request paths.
- **Calendar import:** stage read-only events before confirmation. Deduplicate by user, calendar and event/recurrence identity; re-import must not duplicate load. Never write to Google Calendar.
- **Model identity:** persist capacity inputs, timezone and model version with fixture outputs. Use precise scores for classification; format only for display.
- **Recovery records:** add interval start/end, target history and timezone before implementing the ledger. The starter `minutes` field alone cannot deduplicate overlaps or reconstruct historical targets.
- **Feedback:** add one response per owned commitment, validate completion status, and reject empty or duplicate responses. Use five distinct confirmed tasks for the directional suggestion.
- **Server validation:** require valid effort, priority and category values, bounded check-in answers (1–5), positive durations, and a deadline compatible with all resulting segments. Do not rely on form validation alone.
- **Offline:** queue structured drafts with unique operation IDs. On reconnect, validate and recalculate against current server state; require renewed approval if the plan changed.

The `decision-loop` numbers are design targets until a complete fixture reproduces them. Store the input tasks, fixed intervals, capacity, approved moves and expected outputs together; do not hard-code scores to imitate a screenshot. Validate the arithmetic example, threshold edges, cross-midnight tasks, recovery overlap, no-feasible-plan handling, stale apply/undo and two-user isolation before demonstration. Record executed results separately from these planned checks.
