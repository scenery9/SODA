# SODA (Student Overloaded by Deadlines and Activities) by Team Soda

<table>
<tr><td><b>Team</b></td><td>Samantha Chan Pei Yin, Lee Jia Yin, Yeap Boon Shen, Muhammad Ikhlas bin Mohd Faizal</td></tr>
<tr><td><b>Problem Statement</b></td><td>Stress &amp; Workload Manager</td></tr>
<tr><td><b>Video Presentation</b></td><td><i>pending</i></td></tr>
<tr><td><b>Presentation Slides</b></td><td><i>pending</i></td></tr>
</table>

---

**Explore:** [Overview](#1-project-overview) · [Ideation](#2-ideation--process) · [Prototype](#3-design--prototype) · [Difference & impact](#4-what-makes-it-different) · [Feasibility](#5-technical-architecture--feasibility)

## 1. Project Overview

### The Problem

An assignment, a paid shift and a club request can each look manageable. When they all land in the same week, students need to see the combined demand and decide what can change before recovery becomes the leftover.

**SODA addresses a workload visibility and decision-making gap.** Students may know their individual commitments while struggling to judge their combined demand. The challenge therefore calls for more than tracking: students need help recognising pressure, finding feasible adjustments and making space for recovery.

Research informs this direction. A study analysing **209 open-text responses** found academic workload was the most frequently mentioned influence on students' daily wellbeing, with links to stress and balance between study and life ([Gilmore et al., 2025](https://doi.org/10.1080/07294360.2024.2442636)). Research on working students also highlights differences in conflict between work and study, supporting a design that distinguishes fixed responsibilities from flexible tasks ([Creed et al., 2023](https://doi.org/10.3389/fpsyg.2023.1116031)). These findings support the problem framing; they do not validate SODA's calculations.

> **Our design question:** How might we help students see their combined workload and adjust it while they still have options?

<p align="center">
  <img src="assets/ideation/figure-1-1-problem-tree.png" alt="Figure 1.1: Six contributing causes converge on difficulty judging total demand: fragmented commitments, unrecorded life demands, optimistic estimates, accepting without preview, leftover recovery time and hidden recovery shortfalls." width="880">
</p>

*Figure 1.1: The problem tree connects six contributing causes to the shared visibility problem and its possible consequences. It is a design hypothesis about accumulation, not a diagnostic model.*

### Who we are designing for

Our primary users are **undergraduates balancing coursework with substantial responsibilities outside class**, such as paid work, society leadership or caring. The four situations below can overlap; they are not personality labels.

| Student situation | Decision SODA should make easier |
|---|---|
| **Working student** | Fit coursework around a fixed shift without quietly sacrificing recovery. |
| **Over-committed student** | Understand the effect of a new request before agreeing. |
| **Final-year student** | Allow realistic time for open-ended project work alongside deadlines. |
| **Quiet grinder** | Notice when finishing the work repeatedly means postponing rest. |

Teammates, lecturers and employers may benefit from earlier conversations about conflicts. Campus support services remain the source of help beyond planning. **Personal schedules and check-ins are not automatically shared with any of these stakeholders.**

### Existing approaches and the remaining opportunity

| Existing approach | Useful strength | What SODA adds to the decision |
|---|---|---|
| [Todoist](https://www.todoist.com/help/todoist/integrations/use-the-calendar-integration-rCqwLCt3G) | Organises tasks alongside calendar events. | An editable estimate of five kinds of demand, not just a list of commitments. |
| [Reclaim](https://reclaim.ai/) | Adaptive scheduling, workload visibility and preview/approval. | A student-focused five-axis estimate connected to planned versus logged recovery. |
| [Finch](https://finchcare.com/) | Self-care activities, check-ins and a companion. | A planning loop that previews an additional commitment and offers schedule adjustments. |

These are selected product comparisons, not an exhaustive benchmark. SODA's distinction is the **connection between demand, the next decision and recovery**, rather than the invention of scheduling or self-care.

### Our Solution

SODA is a proposed student workload planner that combines recorded commitments across **mental, time, physical, social and errands** demand. It compares these with an editable personal baseline and previews the effect of a new task before the student accepts it. When the plan is too demanding, it proposes changes that respect fixed commitments, deadlines and protected recovery. Recovery logging and optional completion feedback then inform the student's next planning decision.

> **See total load → preview a commitment → choose a feasible change → protect recovery → improve the next estimate.**

**Current status:** a Figma prototype and supporting specifications, with exported screens in Section 3. The application and hosted services are proposed for the building phase; effectiveness has not yet been evaluated. SODA provides planning estimates, not diagnoses or burnout-risk measurements.

### Three core experiences

SODA centres on three experiences: **understand what I am carrying, decide what I can take on, and make room to recover.** Supporting functions make these experiences usable without becoming separate product promises.

| Student question | Main feature | Supporting functions |
|---|---|---|
| **“Why does my week feel so heavy?”** | **My Backpack:** see combined demand and identify the main source of pressure. | Task entry and calendar review supply commitments; Life Forecast adds the weekly outlook. |
| **“Can I realistically say yes?”** | **Impact Preview:** see the cost of a new commitment and choose what can change. | Protection Mode sets the response; Smart Rebalance offers feasible adjustments and safe undo. |
| **“What can I do to recover now?”** | **Recovery Island:** choose a suitable recovery action and give it a place in the plan. | Protected time, recovery logging and a timer support action; Recovery Debt keeps planned-versus-logged recovery visible. |

**Support across the journey:** Daily Check-in provides optional reflection and preference context. Reality Check helps students reconsider future estimates; Insights and How SODA Calculates explain patterns and assumptions. These improve the three experiences rather than adding more main features.


---

## 2. Ideation & Process

### 2.1 Ideas We Considered

We compared four approaches against **challenge fit, user need, originality, feasibility and demonstration clarity**. Backpack offered the clearest route from seeing demand to making a decision; parts of the other concepts improved that route.

| Idea | Decision | Reason and trade-off |
|---|---|---|
| **Backpack (personal capacity model)** | **Chosen as the core** | Connects combined demand to the cost of a new commitment. We accepted the need to explain uncertainty and let students correct inputs. |
| **Streak (habit and self-care tracker)** | **Companion retained; rewards dropped** | A companion can communicate state. Streaks, XP and resets could make taking a needed break feel like failure, so they were removed. |
| **Echo (AI journaling coach)** | **Brief check-ins retained; journaling dropped** | Reflection was useful, but daily writing adds effort and does not itself identify which commitment can change. |
| **Sync (shared group calendar)** | **Deferred** | Group coordination needs multiple adopters, permissions and synchronisation. We prioritised a useful individual workflow before adding sharing. |

**Why this selection matters:** SODA retained the companion and reflection without becoming a reward tracker or journal. Its central interaction stayed **My Backpack → Impact Preview → Smart Rebalance**.

### 2.2 Ideation Boards

The problem tree above explains **why** overload can accumulate. The three boards below show **who needs help, what we considered, and how principles shaped the selected features**. They separate the original dense mindmap in response to mentor feedback.

#### Figure 1.2a: Users and needs

<p align="center">
  <img src="assets/ideation/figure-1-2a-users-needs.png" alt="Figure 1.2a: Working, over-committed, final-year and quiet-grinder situations share five load dimensions and needs to see demand, preview commitments, adjust plans, log recovery and revise estimates." width="880">
</p>

*Different student situations converge on shared planning needs. This led to one personal model with editable inputs, rather than separate modes for each type of student.*

#### Figure 1.2b: Concepts and selection

<p align="center">
  <img src="assets/ideation/figure-1-2b-concepts-explored.png" alt="Figure 1.2b: Streak contributes a companion without penalties; Sync remains a future group-visibility option; Echo contributes short check-ins; Backpack becomes the capacity and preview core." width="880">
</p>

*The arrows trace what survived each concept and the trade-off behind it. Choosing Backpack preserved useful ideas while keeping the first build focused on the individual student.*

#### Figure 1.2c: Principles that shaped the features

<p align="center">
  <img src="assets/ideation/figure-1-2c-features-principles.png" alt="Figure 1.2c: Five complete principle-to-decision-to-feature paths connect low input effort to derived load, no guilt mechanics to recovery logging, correctable assumptions to feedback, deterministic calculations to previews, and approval plus text alternatives to accessible adjustments." width="880">
</p>

*Each connected row shows a principle changing a concrete design decision. The board includes both main and supporting functions; it is not a list of five main features. Privacy, accessibility and student control apply throughout.*

#### Figure 1.3: From the chosen idea to a usable flow

<p align="center">
  <img src="assets/ideation/figure-1-3-core-user-flow-final.png" alt="Figure 1.3: Capture, calculate, preview, choose, confirm, recover and reflect. Only approved changes are saved; confirmed estimate corrections feed future calculations. An infeasible adjustment leaves the student in control." width="880">
</p>

*The student can accept, adjust, defer or decline. Confirmation saves only the chosen changes; optional feedback improves the next estimate without silently rewriting the plan.*

### How the idea evolved

| Stage | Earlier direction | Change and reason | Trade-off accepted |
|---|---|---|---|
| **Explore** | Four separate product concepts | Chose Backpack; retained a companion and short check-ins. | Prioritised decision support over a broad feature collection. |
| **Simplify capture** | Five dimension ratings for every task | Derive defaults from duration, effort and category to reduce repeated input. | Defaults are coarser and must remain inspectable and correctable. |
| **Narrow scope** | The Crew / shared workload | Deferred collaboration until the personal workflow is useful. | Less group coordination in the first release. |
| **Correct estimates** | Strong forecast and “AI prediction” wording | Added visible assumptions and optional Reality Check feedback. | Present an estimate rather than promising prediction accuracy. |
| **Make recovery actionable** | Generic “take a break” reminders | Added choices, protected time, a reset timer and recovery history. | Requires preferences and logging; a suggestion cannot prove recovery occurred. |
| **Improve the explanation** | One dense ideation board | Split users, concepts and principles into connected diagrams. | More focused figures, each with a short explanation instead of repeated prose. |

**Two changes made concrete**

| Iteration | Earlier proposal → revised design | Why the change matters | Evidence and limit |
|---|---|---|---|
| **Task capture** | Rate five dimensions for every task → enter duration, effort and category, then inspect derived defaults. | Removes repeated abstract ratings while preserving correction. The trade-off is coarser defaults, not proven measurement accuracy. | [Figure 1.2c](#figure-12c-principles-that-shaped-the-features) and the [specified inputs](docs/MODEL.md#step-1-a-task-becomes-a-five-dimensional-vector). The earlier state is documented concept history, not a recovered old screenshot; informal timing claims are not a user benchmark. |
| **Recovery** | General reminder to rest → choose an action, protect time and record completion in Recovery Island. | Gives the student a next step and a visible record. It requires preferences and logging rather than assuming a reminder caused recovery. | [Core flow](#figure-13-from-the-chosen-idea-to-a-usable-flow) and [completion criteria](#minimum-completion-standard). The flow specifies intended behaviour; actual follow-through remains untested. |

### 2.3 Mentor Consultation

The supplied consultation record names **Khor Jia Quan, 7 September 2026**. The table distinguishes documentation changes from design responses that the prototype team must verify in the final screens.

| Feedback received | Response | Evidence / status |
|---|---|---|
| Split the dense ideation mindmap and explain each part. | Separate users/needs, concepts, and principles-to-features. | Figures 1.2a–c above, with visible captions. |
| Include recognisable backend technology logos. | Retain a labelled architecture diagram with the selected technologies. | Figure 5.2 and its accompanying stack table. |
| Explain chart alternatives and the relevance of screen-reader / colour-blind support. | Include text descriptions of diagrams; specify non-colour cues and accessible chart values. | Diagram descriptions here; design documentation in Section 3. Device verification remains a build gate. |
| Remove the separate Chat/Manual chooser before Impact Preview. | Document one entry screen with manual input available in place. | Design response for the prototype team to reconcile with the final capture screens; real text uses forms or rules. |
| Give the backpack companion a more functional role; consider the navigation icon and dialogue. | Use the companion to reinforce load and recovery states, accompanied by text. | Final dialogue, icon treatment and interactions remain with the Section 3 design owner. |

The intent of the capture feedback is fewer unnecessary decisions. Keeping manual entry available also preserves the workflow when optional language assistance is unavailable. Documentation responses are complete here; final screen behaviour and assistive-technology testing are not claimed as verified.

---


## 3. Design & Prototype

**UI Prototype:** [SODA Figma design file](https://www.figma.com/design/izVJIUjNyiSDu0ivUEOtw5)

SODA is used by people who are already depleted. That single fact drives every decision in this
section: the interface has to be readable in ten seconds, honest about what it does not know, and
incapable of making a tired student feel worse for opening it.

### Key screens

> [!IMPORTANT]
> **Storyboard consistency note.** The saved screens contain separate illustrative states: Impact
> Preview 82% → 107%, Rebalance 112% → 89%, and Forecast 94%. They are not a continuous computed run.
> The intended demo story below uses **82% → 107% → 89%**; the designer must update those screens to
> one fixture before recording. Earlier move labels also totalled 19, although 112 − 89 = 23.
> All headline, per-axis and screen-reader values must be generated from the same fixture in the build.


24 screens across five storyboards. Every screen below exists in the Figma prototype.

**Storyboard 1: Onboarding to first capacity reading (Screens 01–06)**

<p align="center">
  <img src="design-previews/soda-storyboard-v1/01-onboarding-home-light.png" alt="Onboarding and My Backpack" width="100%">
</p>

*Splash → Welcome → **Capacity Baseline** (three calibration questions: what a normal week feels like,
focused hours per day, protected recovery per day) → Connect Your Week (Google Calendar read-only,
notifications, optional health) → Calendar Review (imported commitments grouped by category, confirmed
before anything is calculated) → **My Backpack** (82% capacity, the five-dimension bubble chart inside
the backpack, overload risk banner naming Thursday, and the week bar chart).*

**Storyboard 2: Capture to decision (Screens 07–12)**

<p align="center">
  <img src="design-previews/soda-storyboard-v1/02-add-task-impact-light.png" alt="Add task, Impact Preview, Protection Mode and Smart Rebalance" width="100%">
</p>

*Add sheet → **Tell SODA** (natural-language capture, parsed fields shown for confirmation with a
thumbs up/down) → Manual entry (reached via "Edit details") → **Impact Preview** (`82% → 107%`, per-dimension
deltas, recovery window shrinking by 1h 45m) → **Protection Mode** (Protect Recovery / Warn Only / Accept
Without Protection) → **Smart Rebalance** (saved screen: `112% → 89%`; intended fixture: `107% → 89%`, three named moves and a protected-recovery line; the old −19% total is inconsistent and must be replaced).*

<details>
<summary><strong>▸ Storyboards 3–5: week, day detail, check-in, recovery, insights, trust screens and dark mode (Screens 13–24)</strong></summary>

**Storyboard 3: Week, day, check-in and recovery (Screens 13–18)**

<p align="center">
  <img src="design-previews/soda-storyboard-v1/03-schedule-recovery.png" alt="Week updated, Life Forecast, Day Detail, Check-in, Recovery Island and Timer" width="100%">
</p>

*Week Updated (89%, Heavy but below the warning threshold) → **Life Forecast** (7-day curve with Thursday at 94% flagged OVERLOAD) →
Day Detail (timeline with per-item load share and energy remaining) → **Daily Check-in** (five sliders) →
**Recovery Island** (matched to the most depleted dimension) → **Recovery Timer** (20-minute reset, dark,
no screens).*

**Storyboard 4: Insight, honesty and trust (Screens 19–24)**

<p align="center">
  <img src="design-previews/soda-storyboard-v1/04-insights-trust-light.png" alt="Recovery complete, Insights, Recovery Debt, Weekly Review, Settings and How SODA Calculates" width="100%">
</p>

*Recovery Complete → **Insights** (capacity trend, load by category, most overloaded day, positive
highlight) → **Recovery Debt** (2h 35m across four weeks, with the explicit disclaimer that it is a
planning signal and not a medical score) → Weekly Review → Settings → **How SODA Calculates** (the model,
its determinism, the narrow role of AI, and the privacy position, all in plain language).*

**Storyboard 5: Dark mode**

<p align="center">
  <img src="design-previews/soda-storyboard-v1/05-dark-mode-showcase.png" alt="Dark mode showcase" width="100%">
</p>

</details>

### Design principles

SODA is built around one uncomfortable moment: the second before a student says "yes" to something they do not have room for. Every screen in the prototype is shaped by five rules.

**1. Show the cost before the commitment.**
Most planners tell you what you agreed to after you agreed. SODA shows the damage first. Adding a task opens an Impact Preview that puts the week's load before and after side by side: 82% becomes
107%, and the day that breaks is named. The primary action is not "Save", it is "Fix my week".

**2. Plan, never diagnose.**
SODA reports capacity, not health. Copy throughout the app repeats the boundary in plain words: "This is for planning. It is not a health score." Body signals are compared to the student's own
normal, never to a population baseline, and the app states that it works with no wearable connected at all.

**3. Nothing is saved until the student approves it.**
When a task is typed in conversationally, SODA shows what it understood and asks "Did I get that right?" before anything is written. The same line, "Nothing is saved until you approve", sits under the input field. The system proposes; the student decides.

**4. One way in, not a menu.**
Adding something is a single screen. The chat input is there immediately, with a "Type it in yourself" option that expands the manual form in place. Students who prefer forms are never forced through a conversation, and neither group has to pick a mode before they start.

**5. Give the time back, don't just warn.**
Flagging an overloaded week is not help. Every warning is paired with an action: Smart Rebalance proposes specific changes, and Recovery Island turns owed rest into short, concrete options with
the time each one returns.

<details>
<summary><strong>User flow, end to end</strong></summary>

The prototype covers five flows. Every screen listed here exists in the Figma file and is wired, in both light and dark mode.

#### First run

`Splash → Welcome → Capacity Baseline → Connect Your Week → Calendar Review → Home (day one)`

Onboarding asks for two things only: a rough sense of how much the student can take on, and permission to read their calendar. Both optional steps can be skipped: "Later" on the calendar step and "I'll check them later" on the review step both land on the same first-run Home, so a student who declines everything still reaches a working app. Day-one Home carries a Learning Card that opens a short check-in, because SODA has no history to work from yet.

#### Adding a commitment: the core loop

`Home → Add → SODA reads it → Confirms understanding → Impact Preview → Smart Rebalance → Week Updated`

The backpack button in the tab bar opens a single Add screen. The student can type in their own words, tap a worked example, or open "Type it in yourself" to expand a manual form in place; no screen asks them to choose a mode first.

Typed input goes through two checks before anything is saved. SODA shows its working (found the date, estimated the effort from past tasks), then states what it understood and asks the student to confirm or correct it. Manual entry skips the confirmation step and goes straight to Impact Preview, because the student typed the details themselves.

Impact Preview is the decision point. It shows the week's load before and after, names the day that breaks, and offers two routes: Smart Rebalance, which proposes specific changes, or Accept anyway, which requires the student to pass through a confirmation overlay. Either way the outcome is visible before the commitment is real.

#### Seeing the week ahead

`Forecast → Day Plan → Smart Rebalance`

The forecast is read-only until something looks wrong. Any day opens its plan, and an overloaded day routes into the same Smart Rebalance screen used by the add flow: one repair mechanism, not
several. The same is true of "What Breaks" on Home.

#### Recovering owed rest

`Recover → Recovery Island → pick a type → Timer → Complete → Daily Check-in`

Recover shows accumulated recovery debt. Recovery Island reports which parts of the student's capacity are actually low and recommends one option. Choosing a type opens a single screen with Physical, Time and Mental as tabs, so switching between them takes one tap instead of returning to the menu. Each option states the time it gives back. Physical and Mental options run a timer; Time options remove work instead of adding rest, and end in a "tasks batched" confirmation rather than a timer.

#### Degraded states

Calendar sync failure, offline, and save failure are designed as banners on the working screen rather than separate error pages. The student keeps the last known data, keeps adding tasks, and SODA syncs when it can. Nothing is lost and nothing is blocked.

</details>

<details>
<summary><strong>Six friction points we designed around</strong></summary>

Six friction points we designed around. Each was a real change, and each cost us something.

| # | Change | Why | Traded |
|---|---|---|---|
| 1 | Five-field entry → **one-tap category defaults** | The team’s own logging exercise reported 40–55s for full entry and ~8s for the revised path; this is not a user benchmark. The vector still exists, pre-filled and collapsed. | Per-task precision, for a populated model. |
| 2 | Activity view only → **dual view toggle** | The category breakdown showed *where hours go*, quietly contradicting our "capacity, not time" claim. *By activity ⇄ By what it costs you* makes the model visible without losing the readable view. | One extra control on the home screen. |
| 3 | Effort as a single chip → **chip that pre-fills a vector** | Kept one-tap speed, restored the five dimensions underneath. | Nothing; this one was free. |
| 4 | Generic nudges → **axis-matched recovery** | "Take a break" replaced by recovery matched to the depleted dimension, with social suggestions guided by an explicit preference/check-in, not inferred from low recorded social demand. | A larger recovery content set to author. |
| 5 | Warning-only → **warning plus the swaps** | An overload warning with no action is just anxiety. Every red state routes to concrete moves with savings attached. | Screen density on the preview. |
| 6 | Confident percentage → **percentage plus coverage** | We first displayed the headline figure alone. It looked more authoritative and was less honest. | Visual cleanliness, for a number a student can trust. |

</details>

<details>
<summary><strong>Accessibility: what is designed, what is still unverified</strong></summary>

Accessibility is not a compliance annex here; it is load-bearing. Our users are, by definition, tired,
and fatigue degrades exactly the capacities (sustained attention, colour discrimination under low
contrast, working memory) that a careless interface assumes are intact. Designing for permanent
impairment produces an interface that also works for someone reading it at 1 a.m. after a shift.

<details>
<summary><strong>▸ Why colour-blind and screen-reader design specifically matters for these users (with the exact announcements)</strong></summary>

#### Why colour-blind design matters for *this* product specifically

Roughly **8% of men and 0.5% of women** have a colour vision deficiency, overwhelmingly red–green
([insightsoftware](https://insightsoftware.com/blog/visualizing-for-the-color-blind/);
[Rigor Data Solutions](https://www.rigordatasolutions.com/post/visualizing-data-inclusively-addressing-color-blindness-in-data-visualizations)).
In a mixed cohort of engineering and computing undergraduates (a substantial slice of our target
users) that is not an edge case; it is one or two students in a tutorial group.

The specific hazard in SODA is that **our entire severity system is natively red–green**: Light /
Manageable / Heavy / Overload maps to green → amber → orange → red. For a student with deuteranopia or
protanopia, the Life Forecast curve and the weekly bar chart would collapse into a set of
indistinguishable muddy bars, and the single most important message in the product, *Thursday is the
day that breaks*, would be silently lost. The failure would be invisible to us and invisible to them:
they would simply see a chart and take no action.

Our rule, therefore, is **colour is never the only carrier of meaning**. Every severity state is
encoded three times over:

| Severity | Colour | Text label | Numeral | Non-colour cue |
|---|---|---|---|---|
| Light | Green | "Light" | 0–49% | Short bar, no icon, flat mascot posture |
| Manageable | Amber | "Manageable" | 50–69% | Medium bar |
| Heavy | Orange | "Heavy" | 70–89% | Tall bar + weather icon (cloud) |
| Overload | Red | "OVERLOAD" | 90%+ | Full bar + storm icon + warning glyph + strained mascot |

This is why Life Forecast shows `Thu · 94% · OVERLOAD · ⛈ Storm Warning` rather than a red row: the
word, the number, the icon and the mascot each independently carry the message, so removing colour
entirely removes nothing. This satisfies WCAG **1.4.1 Use of Colour** and, for the chart strokes and
bar fills themselves, **1.4.11 Non-text Contrast**, colour is the most commonly cited accessibility
failure in data visualisation, and the fix is not avoiding colour but never *relying* on it
([DubBot](https://dubbot.com/dubblog/2024/charts-graphs.html);
[216digital](https://216digital.com/creating-accessible-data-for-charts-and-graphs/)).

#### Why screen-reader support matters for *this* product specifically

SODA's core value is delivered through three charts: the Backpack bubble chart, the weekly bar chart
and the Life Forecast curve. **To a screen reader, an unlabelled chart is nothing at all.** A blind or
low-vision student using TalkBack or VoiceOver would hear "image" and receive zero information from the
single screen the whole product is built around. Under WCAG, charts count as complex images: the text
alternative must convey the same information and function as the visual, which for data means naming
the chart type, summarising the trend, and exposing the underlying values
([Penn State](https://accessibility.psu.edu/images/charts/); [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)).

Each chart has a proposed text alternative. The samples below illustrate wording; the build must generate labels from the same data as the chart:

| Element | What a screen reader announces |
|---|---|
| Backpack bubble chart | *"Peak day this week: Thursday, 94%, overload. Five dimensions: mental 115.5%, time 63%, physical 16.8%, social 16.8%, errands 21%. Mental exceeds its axis ceiling. Based on 9 of your 12 calendar events."* |
| Weekly bar chart | *"Week load by day. Monday 46% light. Tuesday 61% manageable. Wednesday 78% heavy. Thursday 94% overload, highest day. Friday 65%. Saturday 48%. Sunday 35%."* |
| Life Forecast curve | *"7-day overload forecast, line chart. Rises from 46% Monday to a peak of 94% on Thursday, then falls to 35% Sunday. Thursday exceeds your limit."* |
| Load-by-category donut | *"Recorded load by task category: academic 31%, work 23%, social 17%, errands 13%, other 16%. Illustrative shares; not capacity utilisation."* |
| Recovery Debt bars | *"Recovery debt by week. Most recent completed seven-day block 20 minutes. Previous blocks 45, 55 and 35 minutes. Total 2 hours 35 minutes."* |

Each chart should expose a **visible, keyboard-focusable data table button** (not a long-press-only route), which
is the recommended fallback where the actual values matter more than the shape
([Tableau best practice](https://help.tableau.com/current/pro/desktop/en-us/accessibility_best_practice.htm)).

</details>


#### Full accessibility position

| Requirement | Status | Detail |
|---|---|---|
| Colour-blind safe | **Implemented in design** | Severity carries label + numeral + fill treatment + icon; never hue alone. Deuteranopia/protanopia simulation must be documented before calling the palette verified. |
| Screen-reader chart alternatives | **Implemented in design** | Text alternatives above; Flutter `Semantics` widgets specified per chart in the implementation notes in the accessibility fold. |
| Text contrast | **Verification pending** | Target 4.5:1 for normal text and 3:1 for large text. Retain measured colour-pair evidence; re-check small Day Detail figures. |
| Non-text contrast (1.4.11) | **Verification pending** | Target 3:1 for essential chart boundaries and controls. Measure final foreground/background pairs. |
| Dynamic type | **Specified; build verification pending** | Test 200% text scaling, reflow and clipped labels on real devices. |
| Touch targets | **Implemented in design** | Target ≥48×48 logical pixels for Android controls; verify web target sizes and spacing separately. |
| Reduced motion | **Implemented in design** | `prefers-reduced-motion` respected; the mascot's idle animation and the recovery timer's breathing ring both degrade to static states. |
| No time limits, no flashing | **Implemented in design** | Nothing in SODA expires or flashes. This app is used by people who are exhausted. |
| Light theme | **Partial** | Designed and shown in the storyboards; full token coverage on the roadmap. |
| Screen-reader testing on device | **Planned, not done** | TalkBack pass scheduled in Phase 6. We are not claiming a verified screen-reader experience until it has been run. |

> **Honest limits.** Everything marked *Implemented in design* exists in the Figma prototype and in the
> component specification, not yet in shipped Flutter code. We have not run a TalkBack audit or tested
> with a colour-blind or screen-reader user. The partial-implementation allowance in the challenge
> stipulations is the reason we can say that plainly instead of overclaiming.

---

#### Implementation notes

<details>
<summary><strong>▸ Open Flutter Semantics implementation notes</strong></summary>

```dart
// Every chart is wrapped so a screen reader receives the summary given above,
// and the raw chart is hidden from the accessibility tree rather than announced as "image".
Semantics(
  label: buildAccessibleLoadSummary(weekSnapshot), // uses the chart's exact data + model version
  child: ExcludeSemantics(child: BackpackBubbleChart(...)))
```

- Severity is produced by a single `SeverityBand` enum that returns **colour + label + icon together**,
  so callers can consistently provide all three cues.
- `MediaQuery.of(context).disableAnimations` gates the mascot idle loop and the timer breathing ring.
- Target Android controls at ≥ 48×48 logical pixels; no fixed-height text containers, so dynamic type reflows.
- Charts expose a visible, keyboard-focusable "View as table" button for exact values.
- **Phase 6 must include a real TalkBack pass.** Until it runs, [the accessibility fold](#3-design--prototype) says
  "implemented in design", not "verified".

</details>

</details>

---

## 4. What Makes It Different

**SODA makes the next “yes” a capacity decision.** Its distinctive combination is an editable five-axis estimate, a preview before commitment, feasible adjustments and a recovery record that spans weeks.

### Three experiences, one decision journey

#### My Backpack: “Now I understand what is making the week heavy.”

The student starts with an overview of combined demand, then sees which of the five dimensions needs attention. A three-hour assignment and a three-hour social event occupy the same time but receive different proposed demand vectors. The value is understanding the pressure behind the task list, not simply counting more tasks.

Task entry makes the overview possible, and Life Forecast extends it across the week. The assumptions and recorded-data coverage remain visible so the student can correct an incomplete picture.

#### Impact Preview: “I can decide before I commit.”

**This is SODA's central demonstration moment.** The student previews an unsaved task against the current plan, sees the trade-off, and chooses whether to accept, adjust, defer or decline.

Protection Mode and Smart Rebalance support that same decision. They preserve fixed shifts, deadlines and protected recovery while offering feasible changes to flexible work. Each selected change is checked against the whole week, including its destination. If nothing fits, the app explains why. Nothing moves without approval, and approved changes can be undone when later edits do not conflict.

#### Recovery Island: “I have a manageable next step for recovery.”

The student chooses a recovery action suited to their preferences and current context, protects time for it, and records what they completed. The experience turns a general reminder into a concrete action.

Recovery Debt supports this experience by showing planned-versus-logged recovery across 28 completed days. It keeps postponed recovery visible across calendar boundaries without becoming a separate score to chase. Missing logs do not prove missing rest, extra rest does not erase an earlier daily shortfall, and the ledger does not lower the student's capacity baseline.

**What helps the next visit:** optional Reality Check feedback can prompt an approved estimate adjustment when tasks repeatedly take longer than expected. This follows the planning-fallacy rationale ([Buehler et al., 1994](https://doi.org/10.1037/0022-3514.67.3.366)); it does not establish accurate automated learning. Check-ins, explanations and Insights support understanding and continuity across all three main experiences.

### Comparison with existing solutions

The comparison below uses one synthetic decision rather than comparing feature counts. These are capability-level examples, not a hands-on benchmark or a claim that any named competitor lacks all of SODA's functions.

| Approach | What it helps Aina understand | SODA's proposed addition |
|---|---|---|
| Task-list view | What must be completed and by when. | Explain recorded demand across five dimensions against an editable personal baseline. |
| Calendar / adaptive scheduling | Where events overlap and which flexible work could move. | Connect that scheduling decision to the demand estimate and explicitly protected recovery. |
| Self-care view | Which recovery or reflection activity she might choose. | Keep the chosen action in the same journey as the commitment decision and recovery history. |

### What changes for the student

**Aina is a fictional working undergraduate.** On Thursday she has class from 09:00–11:00, laundry from 12:00–13:00, two hours of assignment drafting from 13:00–15:00, a fixed shift from 16:00–20:00 and protected recovery from 20:30–21:00. Her assignment is due Friday at noon. A club asks her to help on Thursday from 13:00–14:00.

| Experience | What Aina sees or does | Concrete outcome in this synthetic case |
|---|---|---|
| **My Backpack** | Reviews the combined demand and the commitments behind it. | Recognises that the new request competes with existing assignment work. |
| **Impact Preview** | Reviews moving laundry to an available Saturday slot and splitting drafting into 12:00–13:00 and 14:00–15:00. | Can accept with explicit changes: two drafting hours remain, the deadline is met, and class and shift do not move. |
| **Recovery Island** | Chooses a quiet reset for the protected interval and records completion when it happens. | Keeps 30 minutes available for recovery; the ledger distinguishes a plan from a completed action. |

The trade-off is explicit: **laundry moves to Saturday; it does not disappear from the week.** If laundry cannot move or the assignment cannot be split, that option is rejected. Aina can defer, decline or knowingly accept the conflict rather than receive an impossible “fixed” schedule.

This example establishes an intended decision path, not observed benefits or a complete numerical fixture. The [demonstration pack](docs/DEMO-AND-VALIDATION.md#one-case-across-all-three-experiences) records its constraints and failure variant. Do not attach the storyboard's unverified **82% → 107% → 89%** values to this schedule. Any future displayed scores must come from the same complete, versioned inputs; 89% is **Heavy** under the specified bands.

**Why the mechanism is plausible:** Study Demands–Resources theory links demands, resources and proactive adjustment ([Bakker & Mostert, 2024](https://doi.org/10.1007/s10648-024-09940-8)). SODA brings those decisions together rather than leaving recovery separate from planning. The theory informs the design; it does not validate our weights, thresholds or effects on wellbeing.

### How we would evaluate it

First, recruit **8 consenting students** who combine coursework with work, leadership or caring. Compare a calendar-only task with a SODA task using two matched synthetic weeks. Counterbalance the interface order and week assignment to reduce practice effects. Ask students to identify pressure, explain the estimate and choose a feasible response.

| Question | Proposed first-study gate | What would challenge the design |
|---|---|---|
| Can students use the core loop? | At least 6 of 8 complete it without help. | Repeated confusion, abandoned entry or unusable suggestions. |
| Do they understand the percentage? | At least 6 of 8 explain that it depends on recorded tasks and assumptions. | Treating it as a health measurement or overlooking missing commitments. |
| Are the changes actually feasible? | Zero approved changes violate a fixed event, deadline or protected block. | Any constraint breach blocks release. |
| Does the preview support a decision? | Record accept/modify/defer/decline choices and participants' reasons. | Students cannot explain the trade-off or find the information irrelevant. |

A later longitudinal evaluation would track estimate overruns, completed recovery, missed commitments and continued use during busy periods. Lower model scores alone are insufficient: they can result from missing tasks or a changed baseline. **No usability or health outcomes have yet been established.** The [research and evaluation appendix](docs/EVIDENCE.md) retains the fuller rationale and falsifiable predictions.

### Reach and scalability

Start with students at one campus through societies and student-support channels. Expand to other universities only after checking that the workflow remains useful across different timetables and assessment patterns. Supporting postgraduate or early-career users would require revalidating the assumptions, not simply changing the labels. Institutional analytics are outside the first build and would require separate consent and governance; individual wellbeing records are not a default institutional data source.

---

## 5. Technical Architecture & Feasibility

### Tech stack

The proposed build uses **Flutter → FastAPI → Supabase**, with a pure Python calculation engine. The main workflow must work with language assistance disabled.

| Component | Selection and reason | Constraint we plan for |
|---|---|---|
| **Flutter / Dart** | Shared Android and web UI; custom workload visuals. | Test layout, permissions and accessibility on each target. |
| **Riverpod + fl_chart** | Separate application state from widgets; common charts plus a custom Backpack visual. | Charts need readable text values and semantic labels, not colour alone. |
| **FastAPI + Python** | Validated API requests and deterministic calculations using the same confirmed inputs. | Fresh previews require the server; model assumptions require evaluation. |
| **Supabase Auth + PostgreSQL** | Authentication and user-owned data with Row Level Security. | Free-tier limits and inactivity pausing; verify isolation with two accounts. |
| **Google Calendar API** | Optional read-only event import to reduce repeated entry. | OAuth, deduplication and student review; imported events lack effort information. |
| **Drift / SQLite** | Client cache and structured draft queue. | Mark stale results; recalculate after reconnect before applying a plan. |
| **Firebase Hosting + Railway** | Host the Flutter web build and FastAPI service respectively. | Provider quotas, backend usage costs and network availability. |
| **Optional Gemini / local Ollama** | Synthetic task-entry demonstrations; Ollama `qwen3:4b` remains a local experiment. | No real student text in the external demo adapter; no model-generated load scores. |

### System architecture

<p align="center">
  <img src="assets/figure-5-2-system-architecture-data-flow-v3.png" alt="Figure 5.2: Flutter collects task and check-in inputs. FastAPI validates requests and mediates a Python engine and Supabase storage. Language assistance is optional; client-side cache and notifications support the interface." width="880">
</p>

*Figure 5.2: Logical components and data hand-offs. FastAPI mediates database access; the engine itself has no network calls. The dashed outlines group components rather than indicating optional connections.*

**A preview request, end to end:** the app sends a confirmed candidate and user token to FastAPI; the API reads the authorised schedule and capacity; Python simulates the before/after result; the app displays it without saving a task. A separate approval saves the candidate and selected adjustments atomically against the schedule revision. If the schedule changed, the student receives a fresh preview instead of overwriting newer edits.

**Language boundary:** the diagram's “ONE sentence” refers to an allowlisted synthetic example for the optional Gemini demonstration. Real student entry uses structured fields or server rules. Gemini's unpaid terms exclude personal or sensitive submissions, so a small payload alone would not make real task text suitable. The adapter remains disabled unless the demo's audience, region and provider access are eligible. [Gemini API terms](https://ai.google.dev/gemini-api/terms)

**Offline boundary:** cached views and drafts remain available with their last-update time. The client cannot produce a fresh Python preview or safely apply an old rebalance while disconnected. Local notifications are an Android implementation task; web behaviour requires separate testing.

### How the estimate works

1. **Describe the task:** duration, effort and category produce a five-axis demand vector.
2. **Set the baseline:** onboarding supplies an editable focus budget and relative capacity assumptions. Check-ins do not silently reduce capacity.
3. **Compare demand with capacity:** combine the axis utilisation values into a daily planning estimate while preserving separate axis warnings.
4. **Simulate a change:** recalculate the candidate and any proposed moves across the week; check actual time overlaps independently of weighted demand.

**Reproducible example.** With a moderate baseline and five-hour focus budget, a three-hour high-effort academic task produces a daily estimate of **93.576% (displayed as 94%)**. Adding one hour of medium-effort errands produces **101.616% (102%)**. The [model specification](docs/MODEL.md) provides every vector and formula needed to reproduce both results.

| Display rule | Meaning |
|---|---|
| **Light / Manageable / Heavy / Overload** | Respectively below 50%, 50–<70%, 70–<90%, and 90% or more, classified before rounding. |
| **Any axis reaches 100%** | Show its own warning even if the combined score is below the overload threshold. |
| **Peak day this week** | Maximum daily estimate in the displayed week, not a weekly average. |
| **Recovery Debt** | Duration of planned-versus-logged shortfalls over 28 completed local days; overlaps count once and history coverage is visible. |

These are proposed planning rules. Recovery Debt does not lower the capacity baseline, and low social demand does not imply loneliness. Recovery choices follow explicit preferences and context.

### Build plan & scope

**The three-week goal is a complete path through the three main experiences:** My Backpack → Impact Preview with feasible adjustments → Recovery Island with a completed recovery record.

Product hierarchy and build priority are different. Task entry, Smart Rebalance and recovery logging are supporting functions, but the core experience cannot work without them. The first release includes a small, usable Recovery Island; more activity choices can follow.

| Priority | Building-phase scope |
|---|---|
| **Must** | Authenticated manual entry; five-axis model and My Backpack; Impact Preview; Protection Mode; constrained Smart Rebalance with safe undo; a basic Recovery Island with recovery choice, protected time, completion logging and Debt; text alternatives; synthetic demo data. |
| **Should** | Calendar review; richer Life Forecast; Daily Check-in; Reality Check Lite; expanded Recovery Island choices and guided timer; offline drafts and local notifications. |
| **Could** | Optional language demonstration, expanded Insights and additional recovery content. |
| **Outside this build** | Friend circle, university dashboard, wearable companion and clinical assessment. |

| Week | Responsible roles | Evidence of completion |
|---|---|---|
| **1: Establish the core** | Backend + frontend leads | Sign in → save manual task → reproduce the load view; two-account isolation check passes. |
| **2: Complete the decision loop** | Backend + frontend leads | Preview → approve selected changes → persist → undo safely; basic Recovery Island choice → protected time → completed log → updated ledger works on fixtures. |
| **3: Integrate and rehearse** | Integration/QA + UX leads | Resolve core defects; keyboard/TalkBack review; web deployment and planned Android APK; rehearse without AI and on another network. |

**Cut order:** optional language → extra Insights/content → Reality Check Lite → calendar import and enhanced offline sync. Preserve all three main experiences, including their required task entry, feasible adjustments and recovery logging. A schedule with no feasible improvement must be handled honestly rather than treated as a failed demo.

### Minimum completion standard

| Main experience | Must be demonstrable | Failure state that must also work |
|---|---|---|
| **My Backpack** | A confirmed task appears in the breakdown; editing its inputs updates the estimate; coverage and assumptions are readable. | Missing data and dated offline results are visibly labelled. |
| **Impact Preview** | Preview saves nothing; approval applies the candidate and selected feasible changes together; safe undo is available. | No-feasible-plan, stale approval and conflicting undo are explained without overwriting newer work. |
| **Recovery Island** | Select an action, protect its time, record completion once and see the recovery history update. | Cancellation does not count as recovery; overlapping or retried logs do not inflate it. |

These are build acceptance criteria, not completed tests. Prototype screens illustrate the states; executed fixtures and integration checks must establish the behaviour during the build.

### Team, time and cost

| Member | Current contribution |
|---|---|
| **Muhammad Ikhlas bin Mohd Faizal** | Research, alternative concepts, idea evolution and mentor feedback. |
| **Lee Jia Yin** | UI/UX, design system and interactive Figma prototype. |
| **Yeap Boon Shen** | Feasibility, architecture, ideation diagrams and Figma support. |
| **Samantha Chan Pei Yin** | Impact, presentation and submission integration. |

The building-phase estimate is **120 additional team hours**: backend 36, frontend 36, UX/accessibility 18, integration/testing 18 and contingency 12. This is a proposed allocation, not recorded work. Named implementation owners and their availability must be confirmed at kickoff; scope is reduced if the available hours are lower. A [proposed named allocation](docs/DEMO-AND-VALIDATION.md#proposed-implementation-allocation) links these workstreams to current contributions, subject to team confirmation of skills and availability.

| Resource | Demo budget and constraint |
|---|---|
| Open-source app/backend libraries | USD 0 licence budget. |
| Supabase Free | USD 0 within quotas; 500 MB database allowance per project and inactivity pausing. [Current plan](https://supabase.com/pricing) |
| Firebase Hosting | USD 0 within free quotas: 10 GB storage and 10 GB monthly transfer. [Hosting quotas](https://firebase.google.com/docs/hosting/usage-quotas-pricing) |
| Railway Hobby | USD 5 monthly minimum including USD 5 usage; additional metered usage can increase the bill. [Pricing](https://docs.railway.com/pricing) |
| Figma / optional language demo | Education access and unpaid API use depend on eligibility; language assistance can be disabled. |
| **Planning allowance** | **USD 5–10/month for a small hosted demo**, subject to actual usage, taxes and quotas. This is not a measured bill or a spending cap. |

The current Figma prototype does not require these deployments. Provider terms and quotas must be checked again at integration; the Python backend budget excludes hosted local-model inference.

### Risks and release gates

| Risk | Required response before the build demo |
|---|---|
| **Misleading or inconsistent estimates** | Reproduce versioned fixtures, check threshold labels and expose missing input coverage; reconcile illustrative screen values before using them as live results. |
| **Impossible or stale adjustments** | Preserve fixed tasks, deadlines and protected intervals; check destination days, atomic apply and safe undo. A constraint breach blocks release. |
| **Exposed personal records** | Validate user tokens; enforce RLS for reads and writes; test isolation with a second account. Keep service-role keys outside normal user requests. |
| **Missing logs or duplicate imports** | Show recovery history coverage, count overlapping recovery once and deduplicate calendar events. |
| **AI, network or hosting failure** | Complete the main loop without AI; label cached views; test on another network and prepare a backup recording. |
| **Entry or accessibility friction** | Test core actions with target students, keyboard and TalkBack; expose chart values and severity in text. |

Collect only task, account, check-in and recovery data needed for the workflow. Calendar import omits descriptions, attendees and locations; provide disconnect, correction, export and deletion controls. Do not automatically contact lecturers, employers or family about a student's load. Students needing support beyond planning should be directed to appropriate services without a diagnostic claim.

### Supporting detail

The essential case is above. These documents retain the material needed to examine the proposal more closely:

- [Demonstration and validation pack](docs/DEMO-AND-VALIDATION.md): the shared case, proposed allocation, 4:30 speaking script and unfilled participant observation sheet.
- [Research, evaluation and references](docs/EVIDENCE.md): research-to-design mapping, proposed measures, stakeholder context and source list.
- [Calculation and architecture specification](docs/MODEL.md): formulas, worked example, recovery rules, constrained adjustments and language modes.
- [Build specification](docs/BUILD.md): proposed repository layout, starter SQL/RLS, API contracts, fixtures and integration checks.

---

<div align="center">

**SODA: Carry life, not overload.**

Built for CodeNection 2026 · Lifestyle Track: Beating the Burnout

</div>
