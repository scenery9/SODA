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
