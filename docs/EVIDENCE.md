# SODA research and evaluation

Supporting detail for [the submission](../README.md). The README presents the main case directly; this appendix retains research context, evaluation criteria and references. Theories inform the design but do not validate the five-axis model or establish a health outcome.

## Target users and stakeholder context

The four workload situations (working, over-committed, final-year and quiet-grinder students) can overlap. The common need is to make decisions among both fixed and flexible commitments. Teammates, lecturers, employers and family may benefit from earlier communication, but do not receive a student's personal records by default. Campus services provide support beyond SODA's planning role.

The 209-response Australian study is by **Gilmore, Glozier and Ashton-James (2025)**. Pandemic-era burnout findings (Abraham et al., 2024) establish a research concern, not a current Malaysian prevalence estimate. Associations between time management and learning outcomes (Liu et al., 2026) support investigating planning; they do not show that SODA improves grades.

The design also considers two possible reinforcing cycles: avoidance can leave more work unfinished, and overload can make seeking support harder. These are hypotheses to investigate, not outcomes observed in a SODA study. The informal task-entry timings in the source draft are not a controlled usability result.

## Mechanisms and illustrative outcomes

Our case for effectiveness is **theory-informed and testable**, not demonstrated. The prototype shows the
intended interaction; sustained behavioural effects require evaluation.

**Illustrative persona: Aina, a working undergraduate (fictional, not a research participant).**
Use the [shared schedule and decision](DEMO-AND-VALIDATION.md#one-case-across-all-three-experiences): move flexible laundry, preserve two hours of drafting, and retain the fixed class, shift and recovery interval. No load percentage has been calculated for this partial schedule. The benefit being tested is a clearer trade-off and a usable plan; changes in burnout have not been measured.

| Problem | Research basis | SODA intervention |
|---|---|---|
| Combined load is hard to recognise | Self-regulation depends on detecting a gap between current and reference state (Carver & Scheier, 1982) | My Backpack makes concentration of load visible, creating the reference point |
| Future cost is less salient than present benefit | Decisions underweight delayed consequences (Thaler & Sunstein, 2008) | Impact Preview drags the delayed cost into the present moment |
| Task estimates are optimistic | People underestimate completion times despite past overruns (Buehler et al., 1994) | Reality Check collects feedback intended to correct future estimates |
| Recovery stays an unprotected intention | Specifying when and where an action happens supports follow-through (Gollwitzer, 1999) | Smart Rebalance places explicit recovery blocks in the plan |
| Missed recovery persists | Incomplete recovery leaves residual load reactions (Meijman & Mulder, 1998) | Recovery Debt carries shortfalls across weeks instead of resetting |
| Recovery needs differ | Recovery research distinguishes detachment, relaxation, mastery and control (Sonnentag & Fritz, 2007) | Recovery Island offers varied, axis-matched actions |

> These theories support the **design rationale**. They do not validate SODA's five dimensions, its
> weights, its recovery percentages, or the effectiveness of any specific recommendation.

The README's before/after decision table uses this same case. The demonstration pack includes a no-feasible-adjustment variant so evaluation does not assume that every student can move their responsibilities.

**Limits of the claim.** The model depends on recorded information, missing commitments produce false
confidence. Capacity and Recovery Debt are personal estimates, not universal thresholds. Reality Check
currently demonstrates broad duration-and-effort feedback and must not be described as a validated
learning multiplier.

## How we would know if we are wrong: eight falsifiable predictions

Success is measured by changes in decisions and behaviour, not app opens. These are proposed for a future
evaluation; **none of them are current results.**

| # | Prediction | Success indicator | Finding that would challenge it |
|---|---|---|---|
| P1 | Lower workload peaks | Lower peak daily load; fewer days above the limit | Peaks unchanged despite feasible adjustments |
| P2 | Better commitment decisions | Some previewed tasks are modified, deferred or declined | Previews rarely change decisions where alternatives exist |
| P3 | Better estimates | Fewer repeated "longer than expected" responses within a category | Feedback produces no change in estimates or overruns |
| P4 | More completed recovery | Protected blocks completed more often than unscheduled intentions | Scheduling produces no follow-through improvement |
| P5 | Reduced recovery accumulation | Debt stabilises or falls when recovery opportunities exist | Shortfalls keep growing despite usable recommendations |
| P6 | Reduced exhaustion | A controlled study shows greater improvement on a validated exhaustion measure | An adequately powered study finds no meaningful difference |
| P7 | Better data coverage | More commitments captured; fewer major late additions | Important tasks stay missing and repeatedly alter forecasts |
| P8 | Retention under load | Target users keep using it during demanding periods | Students abandon it exactly when workload rises |

**Guard against fooling ourselves:** a lower workload percentage could come from *missing tasks* or a
*changed ceiling* rather than a better schedule. Any model-based improvement must be cross-checked against
recorded behaviour, and Recovery Debt must be read alongside actual recorded recovery.

**Proposed first evaluation:** recruit 8 consenting students who combine coursework with paid work,
leadership or caring. Use two matched synthetic weeks with equivalent constraints in a calendar-only task and a SODA task; counterbalance both the interface order and the week assignment to reduce practice effects, and ask participants to identify the overloaded day, explain the estimate, and choose a
feasible adjustment. Record completion, misunderstandings, time and reasons for rejecting suggestions.
Provisional usability gates: at least 6 of 8 complete the main loop without help, at least 6 of 8 explain
that the percentage is an estimate, and zero accepted moves violate a fixed event, deadline or protected
block. Any constraint breach blocks release. This small study tests comprehension and usability, not
clinical effectiveness; longer-term claims need a separate evaluation with appropriate oversight.

## Rollout conditions

Start on one campus and evaluate comprehension, feasible decisions and entry burden. Expand across universities only if usefulness survives different assessment patterns. Adapting the model to postgraduate or early-career users requires renewed evaluation. Institutional summaries would require separate consent, aggregation safeguards and governance; they are not in the first build.

## References

Research supports the design rationale, not the particular SODA weights or clinical effectiveness.
Provider documentation and competitor descriptions were checked for this review; access, terms and
pricing must be rechecked at build integration.

Abraham, A. Chaabna, K. Sheikh, J. I. Mamtani, R. Jithesh, A. Khawaja, S. & Cheema, S. (2024).
Burnout increased among university students during the COVID-19 pandemic: A systematic review and
meta-analysis. *Scientific Reports, 14*, 2569. https://doi.org/10.1038/s41598-024-52923-6

Alhammad, N., Alajlani, M., Abd-Alrazaq, A., Epiphaniou, G., & Arvanitis, T. (2024). Patients'
perspectives on the data confidentiality, privacy, and security of mHealth apps: Systematic review.
*Journal of Medical Internet Research, 26*, e50715. https://doi.org/10.2196/50715

Bakker, A. B. & Mostert, K. (2024). Study Demands–Resources Theory: Understanding student well-being in
higher education. *Educational Psychology Review, 36*, Article 92. https://doi.org/10.1007/s10648-024-09940-8

Buehler, R. Griffin, D. & Ross, M. (1994). Exploring the "planning fallacy": Why people underestimate
their task completion times. *Journal of Personality and Social Psychology, 67*(3), 366–381.
https://doi.org/10.1037/0022-3514.67.3.366

Carmona-Halty, M. Alarcón-Castillo, K. Semir-González, C. Sepúlveda-Páez, G. & Schaufeli, W. B.
(2024). Burnout Assessment Tool for Students (BAT-S): Evidence of validity in a Chilean sample of
undergraduate university students. *Frontiers in Psychology, 15*, 1434412.
https://doi.org/10.3389/fpsyg.2024.1434412

Carver, C. S. & Scheier, M. F. (1982). Control theory: A useful conceptual framework for
personality–social, clinical, and health psychology. *Psychological Bulletin, 92*(1), 111–135.
https://doi.org/10.1037/0033-2909.92.1.111

Creed, P. A. Hood, M. Bialocerkowski, A. Machin, M. A. Brough, P. Kim, S. Winterbotham, S. &
Eastgate, L. (2023). Students managing work and study role boundaries: A person-centred approach.
*Frontiers in Psychology, 14*, 1116031. https://doi.org/10.3389/fpsyg.2023.1116031

Firebase. (2026, September 1). *Learn about usage levels, quotas, and pricing for Hosting.*
https://firebase.google.com/docs/hosting/usage-quotas-pricing

Finch Care. (2026, September 3). *Finch: Self-care pet* [Mobile app]. Google Play.
https://play.google.com/store/apps/details?id=com.finch.finch

Flutter. (n.d.). *Build apps for any screen.* Retrieved September 2, 2026, from https://flutter.dev/

Gollwitzer, P. M. (1999). Implementation intentions: Strong effects of simple plans.
*American Psychologist, 54*(7), 493–503. https://doi.org/10.1037/0003-066X.54.7.493

Google AI for Developers. (n.d.). *Gemini API terms, models and rate limits.*
https://ai.google.dev/gemini-api/terms · https://ai.google.dev/gemini-api/docs/models

Google AI for Developers. (n.d.). *Gemini API rate limits.* Retrieved September 7, 2026, from
https://ai.google.dev/gemini-api/docs/rate-limits

Iqra. (2024). A systematic review of academic stress intended to improve the educational journey of
learners. *Methods in Psychology, 11*, 100163. https://doi.org/10.1016/j.metip.2024.100163

Liu, B. Ma, P. & Jia, F. (2026). Systematic review and meta-analysis of the impact of time management
on college students' learning outcomes. *Frontiers in Psychology, 17*, 1700298.
https://doi.org/10.3389/fpsyg.2026.1700298

Meijman, T. F. & Mulder, G. (1998). Psychological aspects of workload. In P. J. D. Drenth, H. Thierry, &
C. J. de Wolff (Eds.), *Handbook of work and organizational psychology* (2nd ed. Vol. 2, pp. 5–33).
Psychology Press.

Milne-Ives, M., Homer, S. R., Andrade, J., & Meinert, E. (2023). Potential associations between
behavior change techniques and engagement with mobile health apps: A systematic review.
*Frontiers in Psychology, 14*, 1227443. https://doi.org/10.3389/fpsyg.2023.1227443

Gilmore, A. H., Glozier, N., & Ashton-James, C. E. (2025). Australian university student perspectives on the factors influencing
student wellbeing: A content and relational analysis. *Higher Education Research & Development, 44*(4), 914–931.
https://doi.org/10.1080/07294360.2024.2442636


Ollama. (n.d.). *Qwen3.* Retrieved September 7, 2026, from https://ollama.com/library/qwen3

Olson, N. Oberhoffer-Fritz, R. Reiner, B. & Schulz, T. (2023). Study related factors associated with
study engagement and student burnout among German university students. *Frontiers in Public Health, 11*,
1168264. https://doi.org/10.3389/fpubh.2023.1168264

Patzak, A., Zhang, X., & Vytasek, J. (2025). Boosting productivity and wellbeing through time
management: Evidence-based strategies for higher education and workforce development.
*Frontiers in Education, 10*, 1623228. https://doi.org/10.3389/feduc.2025.1623228

Penn State Accessibility. (n.d.). *Charts & accessibility.* Retrieved September 7, 2026, from
https://accessibility.psu.edu/images/charts/

Personal Data Protection Commissioner Malaysia. (n.d.). *Principles of personal data protection.*
Retrieved September 2, 2026, from https://www.pdp.gov.my/ppdpv1/en/principles-of-personal-data-protection/

Railway. (n.d.). *Pricing.* Retrieved September 7, 2026, from https://railway.com/pricing

Räihä, K. Asikainen, H. & Katajavuori, N. (2024). Changes in university students' behaviour and study
burnout risk during ACT-based online course intervention: A mixed methods study. *Journal of Contextual
Behavioral Science, 34*, 100845. https://doi.org/10.1016/j.jcbs.2024.100845

Reclaim.ai. (n.d.). *Reclaim: AI calendar for work and life.* Retrieved September 5, 2026, from
https://reclaim.ai/

Reschke, T., Lobinger, T., & Reschke, K. (2024). Examining recovery experiences as a mediator between
physical activity and study-related stress and well-being during prolonged exam preparation at
university. *PLOS ONE, 19*(7), e0306809. https://doi.org/10.1371/journal.pone.0306809

Sonnentag, S. & Fritz, C. (2007). The Recovery Experience Questionnaire: Development and validation of a
measure for assessing recuperation and unwinding from work. *Journal of Occupational Health Psychology,
12*(3), 204–221. https://doi.org/10.1037/1076-8998.12.3.204

Supabase. (n.d.-a). *API keys.* Retrieved September 2, 2026, from
https://supabase.com/docs/guides/getting-started/api-keys

Supabase. (n.d.-b). *Pricing.* Retrieved September 7, 2026, from https://supabase.com/pricing

Supabase. (n.d.-c). *Project pausing.* Retrieved September 2, 2026, from
https://supabase.com/docs/guides/platform/free-project-pausing

Supabase. (n.d.-d). *Row level security.* Retrieved September 2, 2026, from
https://supabase.com/docs/guides/database/postgres/row-level-security

Thaler, R. H. & Sunstein, C. R. (2008). *Nudge: Improving decisions about health, wealth, and happiness.*
Yale University Press.

Thornby, K. Brazeau, G. A. & Chen, A. M. (2023). Reducing student workload through curricular
efficiency. *American Journal of Pharmaceutical Education, 87*(8), 100015.
https://doi.org/10.1016/j.ajpe.2022.12.002

Todoist. (2026, September 4). *Use the Calendar integration.*
https://www.todoist.com/help/todoist/integrations/use-the-calendar-integration-rCqwLCt3G

W3C. (2023). *Web Content Accessibility Guidelines (WCAG) 2.2.* https://www.w3.org/TR/WCAG22/
