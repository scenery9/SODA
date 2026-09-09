# Team Soda — 4:30 Video Presentation

Target duration: **4:30**. Keep the final upload below **5:00**. Upload to YouTube as **Unlisted** and title it **Team Soda** only.

## Recording layout

- 1920 × 1080, 30 fps for the final edit.
- Presenter video: lower left, about 15–17% of the frame width.
- Captions: lower centre/right so they do not sit behind the presenter.
- Use the supplied 40-second opening at normal speed. Record the prototype at normal speed, then shorten only cursor travel and loading gaps.
- Speak at a calm 135–145 words per minute. Do not speed the voice above approximately 1.15×.

## 0:00–0:40 — Solution and difference

**Visual:** Use `SODA-opening-40s.mp4`. The last frame says “Now, meet Sam” and should cut directly to the Home prototype.

**Narration:**

> An assignment, a paid shift and a club request can each look manageable. The difficulty appears when they all land in the same week. Students can see what they scheduled, but they may not see what one more commitment will cost.
>
> SODA is a student workload planner for that decision. It combines recorded commitments, shows which day needs attention, and lets the student preview a new request before accepting it.
>
> Here is the twist: most planners show what you have already agreed to. SODA shows the cost while you can still change the decision.

## 0:40–1:04 — My Backpack and Life Forecast

**Prototype:** Start from `▶ Main demo — start here`. Pause on Friday 82%, then point to Wednesday 104%. Open Forecast briefly and return to Add.

**Narration:**

> This is Sam’s week. My Backpack combines recorded commitments across mental, time, physical, social and errands demand. Friday is already heavy at 82 percent, while the weekly forecast identifies Wednesday at 104 percent. The percentage is an explainable planning estimate based on recorded tasks and editable assumptions. It is not a health score or diagnosis.

**Design decision to show:** The number is always paired with a named state, and the day that needs attention is written in words rather than communicated through colour alone.

## 1:04–1:34 — Add and confirm the task

**Prototype:** Open Add. Select “Presentation prep Friday, around 3 hours”. Let the reading state advance. On Tell SODA, point to Friday 19:00, 3h 30m suggested and Extra High. Select Check impact.

**Narration:**

> Sam receives a presentation request for Friday evening and enters it in one sentence. Language assistance only interprets the words; it does not calculate the workload or decide what should move. SODA confirms the date, time and effort before saving anything. It suggests three and a half hours because Sam’s earlier presentations took longer than expected. That assumption is visible, explained and reversible.

## 1:34–2:08 — Impact Preview

**Prototype:** Hold on the Impact Preview. Point to 82% → 112%, Mental 91% → 118%, Time 87% → 109% and rest 2h 10m → 25m. Select Fix my week.

**Narration:**

> Before Sam says yes, Impact Preview simulates the consequence without saving the task. Friday rises from 82 to 112 percent. Mental and time demand cross their limits, while the planned rest remaining falls from two hours and ten minutes to only twenty-five minutes.
>
> Sam can leave with no changes, knowingly accept the heavy day, or ask SODA to find room. The decision stays with the student.

**On-screen emphasis:** “See the cost before saying yes.”

## 2:08–2:48 — Smart Rebalance and fixed commitments

**Prototype:** Show the two selected changes. Point to both Flexible labels and the 112% → 89% result. Apply two changes, open the confirmation, return to the updated week, then open Forecast to show the saved 89% state. Insert the Wednesday rebalance screen for about five seconds to show the Fixed shift and manager confirmation.

**Narration:**

> SODA checks the destination days and proposes two flexible changes. Presentation preparation moves to Saturday, and revision moves to Sunday. Friday returns to 89 percent. It remains a heavy day, but it is now below Sam’s limit.
>
> Fixed commitments are treated differently. SODA does not silently shorten or move a paid shift. A swap remains a request until the manager confirms it, and it is never counted as a completed improvement. Sam reviews the trade-off, approves the two changes, and the same updated state remains visible in Home and Forecast.

## 2:48–3:24 — Recovery Island

**Prototype:** Open Recover and show 2h 35m across four weeks. Enter Recovery Island, start the recommended 20-minute reset, briefly show Pause and Resume, then choose Demo: finish session. Show 20 minutes logged and debt changing to 2h 15m. Show the check-in for no more than three seconds.

**Narration:**

> Busy weeks do not disappear when the calendar resets. Recovery Debt keeps planned but unrecorded recovery visible across four weeks. It is a planning record, not a judgement about the student.
>
> Recovery Island turns that record into a manageable next step. Sam chooses a twenty-minute reset, can pause or end it early, and receives credit only after completing it. The record changes from two hours and thirty-five minutes to two hours and fifteen minutes, while the tasks themselves remain unchanged. An optional check-in records how the student feels without diagnosing them.

## 3:24–4:05 — Tech stack and three-week build plan

**Visual:** Animate the architecture from left to right: Flutter → FastAPI → deterministic Python engine → Supabase. Then reveal Google Calendar, Drift/SQLite, optional language assistance, Firebase Hosting and Railway. Finish with a three-week timeline.

**Narration:**

> The proposed application uses Flutter for Android and web, FastAPI for validated requests, a deterministic Python calculation engine, and Supabase for authentication and user-owned data. Drift keeps cached views and drafts available offline. Google Calendar import is optional and read-only. Firebase Hosting serves the web application, while Railway hosts the API.
>
> AI is limited to interpreting synthetic language input and writing explanations. It never generates load scores or moves tasks. Structured manual entry keeps the main workflow available without AI.
>
> In week one, we build the data model, manual entry and My Backpack. Week two completes Impact Preview, constrained rebalance and recovery logging. Week three covers integration, accessibility checks, deployment, testing and rehearsal.

## 4:05–4:30 — Concrete impact and close

**Visual:** Before/after split. Left: “Accept now → discover overload later.” Right: “Preview → understand → adjust or decline.” Finish on the SODA mark and tagline for two seconds.

**Narration:**

> SODA changes one concrete moment: whether a student accepts, adjusts, defers or declines a new commitment. Sam keeps the fixed shift, moves only flexible work, and sees the recovery trade-off before approving anything.
>
> The model and outcomes still require testing with students. What this prototype demonstrates is a clearer, explainable and more responsible planning decision.
>
> SODA helps students carry life, not overload.

## Final export checklist

- Final duration is between 4:20 and 4:40 and never above 5:00.
- The voice remains understandable at normal playback speed.
- Prototype cursor is visible but does not circle or shake.
- All captions match the spoken words.
- Do not claim that the backend, AI, wearable integration or health outcomes are already implemented.
- YouTube visibility is Unlisted.
- YouTube title is `Team Soda` only.
- Test YouTube, slides and Figma links in an incognito window.
- Add both the YouTube and presentation-slide links to README.md.

