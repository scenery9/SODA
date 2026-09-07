# SODA demonstration and validation pack

Team preparation material supporting [the submission](../README.md). The schedule is synthetic, the speaking script is a draft, and all study results are uncollected. This document does not change the Section 3 prototype or establish deployment readiness.

## One case across all three experiences

**Aina is a fictional working undergraduate.** Use the same case in the README, walkthrough and future fixture. All times use Asia/Kuala_Lumpur. These selected commitments illustrate the decision; they are not a complete dataset for calculating a daily percentage.

| Commitment | Original plan | Constraint |
|---|---|---|
| Class | Thursday 09:00–11:00 | Fixed |
| Laundry | Thursday 12:00–13:00 | Flexible; Saturday 10:00–11:00 is available |
| Assignment drafting | Thursday 13:00–15:00 | Two hours required; due Friday 12:00; splitting is allowed in this example |
| Paid shift | Thursday 16:00–20:00 | Fixed |
| Protected recovery | Thursday 20:30–21:00 | Preserve the full 30-minute interval |
| New club request | Thursday 13:00–14:00 | Candidate only; not saved yet |

**Decision:** the request overlaps the assignment. Aina can accept only after reviewing a feasible revised plan. The proposed change moves laundry to Saturday and splits drafting into Thursday 12:00–13:00 and 14:00–15:00. The class, shift, deadline and recovery block stay unchanged. The destination interval is available by construction; a real schedule must check it again.

**Visible result:** two hours of assignment work remain; the club task gets one hour; laundry is deferred rather than deleted; 30 minutes of recovery remain protected. Moving work does not remove it from the week. This demonstrates a scheduling trade-off, not a measured reduction in stress or a computed load-score improvement.

**Failure variant:** make laundry immovable and disallow splitting the assignment. Keep the other constraints. Reject this proposed plan and explain the conflict. Offer defer/decline/accept-as-is with the conflict visible, rather than silently moving a fixed commitment.

**Recovery step:** demonstrate choosing a quiet reset in the protected interval and marking it complete in the synthetic scenario. A planned block is not a completed recovery record. Today remains provisional in the ledger until the local date ends.

## Evidence to capture for the three main experiences

| Experience | Starting state | Required result | Failure handling |
|---|---|---|---|
| My Backpack | Confirmed task inputs and an editable baseline | Five-axis values, clearly labelled daily/weekly summary and input coverage; editing a task updates the estimate | Missing input is visible; offline estimates carry their last-update time |
| Impact Preview | Unsaved club task and current schedule revision | Before/after simulation without saving; approved candidate and selected changes persist together | No feasible move is explained; stale approval recalculates; undo cannot overwrite later edits |
| Recovery Island | A preference and an available protected interval | Select an action, retain the interval, record completion once and update the appropriate history | Cancelling records no completion; overlapping or retried logs cannot inflate recovery |

For the prototype round, demonstrate the designed states and label them as illustrative. For the build, use versioned inputs and executed checks. The existing 82% → 107% → 89% storyboard target is a separate, unverified numerical fixture; do not attach those scores to this schedule. The model appendix's worked arithmetic is independent too.

## Proposed implementation allocation

This is a coordination proposal based on documented contributions, **not an agreed assignment or evidence of technical proficiency**. Confirm skills, availability and ownership before kickoff.

| Proposed accountable member | Workstream | Proposed collaborator | Confirmation needed |
|---|---|---|---|
| Yeap Boon Shen | Python model, API and data integration | Muhammad Ikhlas bin Mohd Faizal on constraints and fixture cases | Backend availability and implementation experience |
| Lee Jia Yin | Flutter core journey and design translation | Yeap Boon Shen on API integration | Flutter availability and implementation experience |
| Muhammad Ikhlas bin Mohd Faizal | Scenario coverage, acceptance checks and requirements traceability | Samantha Chan Pei Yin on participant tasks | Testing capacity and access to target participants |
| Samantha Chan Pei Yin | Integration coordination, evaluation records and presentation | Lee Jia Yin on walkthrough continuity | Recording, editing and integration availability |

The 120-hour estimate is a shared workstream budget, not four independently assigned workloads. Confirm who covers backend 36, frontend 36, UX/accessibility 18, integration/testing 18 and contingency 12 hours. If skills or time are insufficient, reduce optional scope before promising delivery. Confirmed changes belong in the README's build plan.

## Draft video script: target 4 minutes 30 seconds

Rehearse and adjust pacing to the actual recording. Use the final Section 3 screens supplied by the design owner. Do not describe designed interactions as a live implementation. If screens cannot show this case consistently, reconcile the case and screens before recording.

### 0:00–0:30 | The decision

**Show:** Aina's commitments and the club request.

“Aina has a class, an assignment due Friday and a fixed paid shift. Then a club asks for another hour on Thursday. Each commitment sounds manageable. Together, they compete for the same time, and recovery is easy to push aside. SODA helps her answer one question before she agrees: can I take this on, and what would need to change?”

### 0:30–1:10 | My Backpack

**Show:** Overview, five-axis breakdown and coverage explanation.

“Our first core experience is My Backpack. It brings recorded commitments into one overview across mental, time, physical, social and errands demand. Two tasks can take the same time and make different demands. Aina can see where the pressure comes from and review the assumptions behind the estimate. This is a personal planning tool, not a health score. Missing commitments mean an incomplete picture, so coverage stays visible.”

### 1:10–2:15 | Impact Preview

**Show:** Unsaved club request, conflict, proposed changes and confirmation.

“Impact Preview is the moment where that understanding becomes a decision. The club request has not been saved. It overlaps assignment work. Aina reviews an option: move laundry to Saturday and split the two hours of drafting around the request. Her class and paid shift stay fixed, the assignment still finishes before its deadline, and recovery remains protected.

“Smart Rebalance supports this experience. It checks the destination as well as the busy day. Aina approves the changes herself. If nothing fits, SODA explains why and leaves the choice with her. The useful outcome is a feasible plan she understands, not simply a lower-looking number.”

### 2:15–2:55 | Recovery Island

**Show:** Action choice, protected interval and simulated completion.

“The third experience is Recovery Island. Aina chooses a manageable action for her protected recovery time, rather than receiving a general reminder to rest. Completing an action creates a recovery record. Recovery Debt supports this by keeping the difference between planned and logged recovery visible across weeks. A missing log does not prove someone failed to rest. Optional feedback later helps Aina reconsider future estimates.”

### 2:55–3:45 | Why this is feasible

**Show:** Architecture and three-week plan.

“This submission is a prototype and specification. The planned implementation uses Flutter, FastAPI and Supabase. Python calculates the estimates from confirmed inputs; the core journey does not depend on a language model. Week one establishes task entry and the load view. Week two connects preview, approved adjustments and recovery logging. Week three focuses on integration, accessibility checks and demonstration readiness. Optional integrations are cut before these three experiences. Our small-demo hosting allowance is five to ten US dollars per month, subject to actual usage.”

### 3:45–4:30 | Difference, impact and close

**Show:** Original/revised case and the three main experiences.

“Calendars and scheduling tools already help organise time, and self-care tools support reflection. SODA connects a five-axis view to the next commitment and the recovery that follows. In this example, Aina can explain what she changed and what she preserved. That is the behaviour we intend to test with target students. We have not yet established usability or health outcomes. Our focus is simple: understand what you are carrying, decide before adding more, and give recovery a place in the plan. SODA: carry life, not overload.”

## Short formative usability session

**Purpose:** find confusing interactions, not prove effectiveness. Start with a small convenience sample of consenting target students; report the actual count. This preliminary walkthrough is separate from the planned eight-person counterbalanced comparison in the README. Do not apply the 6-of-8 gate to a smaller sample.

Use synthetic tasks, participant IDs and voluntary participation. Explain that the prototype is being tested, not the participant; they may skip or stop. Do not request real health details. Obtain separate permission before recording and agree on deletion of recordings.

| Task prompt | Observe without coaching | Record |
|---|---|---|
| “What does this overview tell you about Aina's week?” | Whether they find the source of pressure and understand coverage | Their explanation; incorrect assumptions |
| “What does this percentage mean to you?” | Planning estimate versus health measurement | Verbatim explanation with permission |
| “Aina receives this request. Decide what she should do.” | Whether they preview before saving and notice fixed constraints | Chosen response, reasons and help needed |
| “Find a way to preserve recovery, or explain why that is not possible.” | Whether suggestions are understandable and feasible | Missed constraint or rejected suggestion |
| “Choose a recovery action and show how you would record it.” | Planned versus completed recovery; ability to finish the flow | Completion, hesitation and assistance |

For every task, record **completed unaided / completed with help / not completed**. If measuring time, start after the prompt and stop when the participant completes or abandons the task; log prototype limitations separately. A click-through mockup cannot verify actual database security, arithmetic or persistence.

### Unfilled observation record

| Participant ID | Task | Completion/help | Observation and reason | Proposed change | Retest result |
|---|---|---|---|---|---|
| Not collected | Not collected | Not collected | Not collected | Not decided | Not run |

Report the actual number approached and completed, recruitment limitations, concrete misunderstandings and changes made. A few favourable comments do not establish reduced burnout or superior effectiveness. Retain negative findings, and never fill this record with invented responses.
