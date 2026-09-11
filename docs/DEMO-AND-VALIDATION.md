# SODA demonstration and validation pack

Team preparation material supporting [the submission](../README.md). The schedule is synthetic, the speaking script is a draft, and all study results are uncollected. This document does not change the Section 3 prototype or establish deployment readiness.

## One case across all three experiences

**Aina is a fictional working undergraduate.** Use the same case in the README, walkthrough and future fixture. All times use Asia/Kuala_Lumpur. These selected commitments illustrate the decision; they are not a complete dataset for calculating a daily percentage.

| Commitment | Original plan | Constraint |
|---|---|---|
| Class | Thursday 09:00–11:00 | Fixed |
| Laundry | Thursday 12:00–13:00 | Flexible, Low priority; Saturday 10:00–11:00 is available |
| Assignment drafting | Thursday 13:00–15:00 | Flexible, High priority; two hours required; due Friday 12:00; splitting is allowed in this example |
| Paid shift | Thursday 16:00–20:00 | Fixed |
| Protected recovery | Thursday 20:30–21:00 | Preserve the full 30-minute interval |
| New club request | Thursday 13:00–14:00 | Candidate only, Medium priority; not saved yet |

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

For the prototype round, demonstrate the designed states and label them as illustrative. For the build, use versioned inputs and executed checks. The existing 82% → 112% → 89% storyboard target is a separate, unverified numerical fixture; do not attach those scores to this schedule. The model appendix's worked arithmetic is independent too.

## Implementation responsibilities

The following building-phase allocation defines each member's ownership. Deliverables are planned work, not claims that implementation or testing has already been completed.

| Team Member | Primary Responsibility | Key Deliverables |
|---|---|---|
| **Samantha Chan Pei Yin** | **Recovery Island Development & Submission Integration** | Develop the recovery activity selection, protected-time and completion-recording interfaces; integrate Recovery Debt data with the backend; coordinate the final README, slides and demonstration using contributions from all members. |
| **Lee Jia Yin** | **Frontend Development & UI/UX** | Build shared Flutter components and navigation, task-entry screens, My Backpack and Impact Preview interfaces; maintain consistency with the Figma design and implement accessible interaction states. |
| **Yeap Boon Shen** | **Backend Development & Calculation Engine** | Implement the five-dimensional load model, database and APIs, Impact Preview calculations, Smart Rebalance constraints, recovery data services, and safe save/undo behaviour. |
| **Muhammad Ikhlas bin Mohd Faizal** | **Testing & Quality Assurance** | Prepare test plans and synthetic data; perform functional, integration and regression testing; verify calculation outputs, scheduling constraints and account isolation; track defects, retest fixes and validate the complete demonstration flow. |

### Collaboration and hand-offs

- **Samantha and Jia Yin:** agree on shared components, navigation and frontend conventions before building their separate screens. Samantha owns recovery interfaces; Jia Yin owns My Backpack, task entry and Impact Preview interfaces.
- **Boon Shen and both frontend developers:** agree on API request/response fields and error states before integration. Boon Shen owns server-side recovery calculations and persistence; Samantha owns how students interact with those services.
- **Ikhlas and all developers:** define acceptance cases early. Developers supply module checks and resolve defects in their own code; Ikhlas performs independent verification, integration checks and regression testing.
- **All members:** supply accurate content for their own workstream, review the demonstration and participate in rehearsal. Samantha coordinates document and presentation assembly rather than writing every member's contribution alone.

### Testing and QA across three weeks

| Week | Ikhlas's QA deliverables | Developer collaboration |
|---|---|---|
| **1: Establish coverage** | Test plan, synthetic input data, task-entry checks, expected calculation outputs and two-account isolation cases. | Agree on acceptance criteria; provide reproducible module checks and error states. |
| **2: Verify the decision loop** | Integration tests for preview, fixed commitments, deadlines, protected recovery, infeasible adjustments, save/undo and recovery logging. | Fix assigned defects and provide steps for verification. |
| **3: Validate readiness** | Regression results, cross-device checks, accessibility review, defect retests and an end-to-end demonstration checklist. | Resolve release-blocking defects and rehearse the final flow together. |

The **120-hour workstream estimate** remains backend 36, frontend 36, UX/accessibility 18, integration/testing 18 and contingency 12. It does not imply equal hours per person or that Ikhlas owns every developer check. Review availability and technical support needs at kickoff; reduce optional integrations before weakening the three core experiences.

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

### 2:15–2:50 | Recovery Island

**Show:** Action choice, protected interval and simulated completion.

“The third experience is Recovery Island. Aina chooses a manageable action for her protected recovery time, rather than receiving a general reminder to rest. Completing an action creates a recovery record. Recovery Debt supports this by keeping the difference between planned and logged recovery visible across weeks. A missing log does not prove someone failed to rest. Optional feedback later helps Aina reconsider future estimates.”

### 2:50–3:20 | Tech stack

**Show:** Figure 5.2, the architecture and data flow.

“This submission is a prototype and a specification. The planned build is Flutter on Android and web, FastAPI for every request, and Supabase for authentication and user data. One deterministic Python engine produces capacity, Impact Preview, Life Forecast and Recovery Debt. It makes no network calls, so the same inputs always return the same number. A language model only puts results into words. It never decides your schedule.”

### 3:20–3:50 | Build plan

**Show:** Figure 5.3, the three-week build plan. Reveal the full figure, then bring up the three gate
bars together, then each week column with its gate in turn, then the cut-order strip.

“Three weeks, a hundred and twenty team hours, four people with one job each. Every week ends on a gate we can demonstrate. Week one proves the data is isolated. Week two closes the decision loop: preview, approve, undo. Week three rehearses it with the AI switched off. The cut order is decided in advance. The three core experiences are the last things to go.”

Sixty-seven words, about 135 words per minute. The pacing is deliberately unhurried so each highlight
lands. If the segment has to reach 25 seconds, drop “Week one proves the data is isolated”; account
isolation is covered in the README's data handling section. If it can run to 35 seconds, add
“Hosting for a small demo costs five to ten US dollars a month, subject to actual usage.”

### 3:50–4:35 | Impact and close

**Show:** Life Forecast with Wednesday at 104%, then the same week after the fix at 80%. Hold on the
after screen and bring up "Moved to Sat", then "Unchanged, fixed shift", then "Rest is safe". Close on
the three main experiences, then the end card.

“The number went from a hundred and four to eighty. But that is not the point. What matters is that she can explain it: what moved, what stayed, and why recovery survived. That is the behaviour we want to test with students, and we have not proved it yet. No usability results, no health outcomes, and no claim to detect or prevent burnout. The estimate is arithmetic a student can check on paper, and the decision stays with her. Understand what you are carrying. Decide before adding more. Give recovery a place in the plan. SODA: carry life, not overload.”

One hundred words, about 42 seconds. Let the red Wednesday hold for two seconds before the first line.
The admission that nothing is proven is deliberate and should be delivered evenly, not apologetically.
Slow down across the final three short sentences and again on the last line.

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
