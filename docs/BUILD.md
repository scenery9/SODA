# SODA build specification

> Supporting detail for section 5 of the [README](../README.md). Everything here is **proposed**; no application or deployed service exists yet.

## Repository structure

<details>
<summary><strong>▸ Open repo layout</strong></summary>

```
soda/
├── README.md                    ← this file
├── assets/                      ← figures referenced above
│   └── ideation/
├── design-previews/             ← storyboard exports
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
    └── tests/                   ← ★ engine/ must be 100% covered; it is pure arithmetic
```

**The single most important structural rule:** `api/engine/` makes **no network calls and imports
nothing from `api/language/`**. That separation is what makes the "deterministic core" claim in
[§5.3](#53-the-language-layer-what-we-corrected) true rather than aspirational, and it is enforceable
by a lint rule.

</details>

## Data model

<details>
<summary><strong>▸ Open full SQL schema with RLS policy</strong></summary>

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
  effort        text    check (effort in ('low','medium','high')) default 'medium',
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

</details>

## API surface

<details>
<summary><strong>▸ Open the API surface (14 endpoints)</strong></summary>

| Method | Route | Purpose | Writes? |
|---|---|---|---|
| `POST` | `/auth/session` | Exchange Supabase session |: |
| `GET` | `/week?start=YYYY-MM-DD` | Week commitments + per-day load + capacity + coverage | No |
| `POST` | `/commitments` | Create a commitment | Yes |
| `PATCH` | `/commitments/{id}` | Edit / reschedule / complete | Yes |
| `POST` | **`/impact-preview`** | Simulate adding a candidate task, returns before/after vectors, deltas, breaking day, recovery impact, suggested moves | **No** |
| `POST` | `/rebalance` | Generate constrained move set for a day | No |
| `POST` | `/rebalance/apply` | Apply an approved move set (returns an `undo_token`) | Yes |
| `POST` | `/rebalance/undo` | Revert an applied move set | Yes |
| `POST` | `/checkin` | Submit daily check-in | Yes |
| `GET` | `/recovery/debt` | Rolling 4-week ledger | No |
| `POST` | `/recovery/log` | Record a completed recovery session | Yes |
| `POST` | `/feedback` | Reality Check response | Yes |
| `POST` | `/calendar/import` | Read-only Google Calendar pull → staged for confirmation | Staged |
| `POST` | **`/parse`** | Real text → server rule parser. Optional AI route accepts only an allowlisted synthetic `example_id`; timeout falls back to rules. | No |

`/impact-preview` and `/parse` are both **non-writing** by design: a student can explore a decision and
change their mind without creating a commitment, and a parse failure can never corrupt data.

</details>

## Demo seed data

<details>
<summary><strong>▸ Open demo seed-data requirements</strong></summary>

The demo account needs enough history for Recovery Debt and Reality Check to be non-empty:

- **4 weeks** of past commitments across all five categories, with realistic clustering (assignments
  bunching near deadlines, shifts on fixed weekdays)
- Recovery entries producing a **total debt of ~2h 35m**, distributed 0h20 / 0h45 / 0h55 / 0h35 across
  the four weeks, to match the Recovery Debt screen
- **12 calendar events, 9 imported**, so the coverage line reads *"Based on 9 of your 12 calendar events"*
  and the honesty principle is visible rather than merely claimed
- Use separate named fixtures: `decision-loop` targets 82% → 107% → 89%; `worked-model` reproduces §5.4’s 94% example. Do not splice them into one continuous demo.
- At least 5 completed tasks in the Academic category with "took longer" feedback, so Reality Check has a
  live directional suggestion to show

</details>
