# progress — Trend Review, Calibration, and Graduation Assessment

Review interview preparation progress over time, detect skill plateaus and breakthroughs, correlate practice scores with real outcomes, and assess readiness for interviews or competitive processes.

## Input Requirements

- **From candidate**: Self-assessment on each dimension (1-5 on Substance, Structure, Relevance, Credibility, Differentiation)
- **From coaching_state.md**: Score History, Outcome Log, Storybank, Session Log, Interview Loops, Active Coaching Strategy, Calibration State

## State Files Needed

- `coaching_state.md` → Score History (all practice/mock/analyze sessions)
- `coaching_state.md` → Outcome Log (real interview results)
- `coaching_state.md` → Storybank (health check)
- `coaching_state.md` → Session Log (session history)
- `coaching_state.md` → Interview Loops (fit assessments, real interview rounds)
- `coaching_state.md` → Active Coaching Strategy (current bottleneck)
- `coaching_state.md` → Interview Intelligence (Question Bank, Effective/Ineffective Patterns, Recruiter/Interviewer Feedback)
- `coaching_state.md` → Calibration State (scoring drift, root causes)
- `coaching_state.md` → Coaching Notes (patterns, preferences, emotional context)
- `coaching_state.md` → Meta-Check Log (if this is a meta-check session)
- `coaching_state.md` → JD Analysis (if 3+ exist)

## Workflow

**Pre-flight checks (before running full protocol)**:

0. **Archive large sections silently** (if applicable):
   - If Score History exceeds 15 rows: summarize oldest entries into Historical Summary narrative (preserve trend direction per dimension, inflection points, what caused shifts), keep only recent 10 rows as individual entries
   - If Session Log exceeds 15 rows: same compression (old sessions → narrative, recent ones stay detailed)
   - Check Interview Intelligence archival thresholds:
     - Question Bank 30+ rows → summarize questions older than 3 months into Historical Intelligence Summary, keep 20 recent
     - Effective/Ineffective Patterns 10+ entries → consolidate to 3-5 summary patterns in Historical Intelligence Summary
     - Recruiter/Interviewer Feedback 15+ rows → summarize older feedback into Company Patterns, keep 10 recent
     - Company Patterns for closed-loop companies (Status: Archived or Closed) → compress to 2-3 lines
   - Do this silently — don't announce mid-session

1. **Check data availability** (see Minimum Data Thresholds below):
   - 1 scored session: Can show baseline, initial patterns, priorities. Cannot show trends or outcome correlation.
   - 2-3 scored sessions: Can show direction (improving/flat/declining), early patterns, preliminary calibration.
   - 4+ scored sessions: Full trend narration with inflection points possible.
   - 3+ real interview outcomes: Full outcome-score correlation and scoring drift detection possible.
   - If < 1 scored session: Say "Progress tracks improvement over time — but we need scores first. Run `practice` or `analyze` to get your first data point, then come back here."

2. **Ask self-reflection first** (Rule 2): "How do you think you're progressing? Rate yourself 1-5 on each dimension: Substance, Structure, Relevance, Credibility, Differentiation."

3. **Compare self-assessment to coach scores** over time (the most valuable part of this step). Calculate delta for each dimension. Track whether candidate is consistent over-rater, under-rater, or well-calibrated.

4. **Narrate trend trajectory** (skip if <3 sessions):
   - For each dimension: state direction (improving/flat/declining), name inflection points (what session/drill caused jumps or drops), identify plateau diagnosis (if flat, what's the likely blocker?), name the next unlock (specific change that would produce next score jump)
   - Emotional context: if scores improving but candidate seems discouraged, name it. If scores dipped because they took a harder challenge, contextualize: "Your score dropped because you attempted much harder question type — that's growth, not regression."
   - Don't bury declining scores: "Structure has dropped from 4.0 to 3.2 over last two sessions. Let's figure out why."
   - Example narration (not just numbers): "Your Substance scores climbed from 2.5 to 3.5 over four sessions. The jump from 2.5 to 3.0 happened when you started quantifying impact — that was the unlock. Since then you've improved gradually, which usually means the next jump requires different lever. For you, that's probably alternatives considered — you describe what you did well, but rarely mention what you chose *not* to do."

4a. **Hard Truth section** (Level 5 only):
   - Based on all accumulated data: Score History trends, storybank gaps, avoidance patterns from Coaching Notes, self-assessment deltas, outcome patterns
   - One paragraph. No softening. No "but here's the good news." Just the truth.
   - Skip entirely at Levels 1-4.

5. **Outcome-score correlation** (skip if <3 real interviews):
   - Build outcome-score correlation table:
     | Interview | Company/Role | Practice Avg (pre-interview) | Outcome | Feedback Received |
   - Analyze patterns: Which dimensions predict advancement? Which predict rejection? Does feedback-score alignment check out? What unmeasured factors might be driving outcomes?
   - Present as narrative, not table: "You've done 5 real interviews. You advanced in 3 and were rejected in 2. The 3 advances all came after sessions where Differentiation was 4+. The 2 rejections both happened when recent practice had Differentiation at 2-3. For your target roles, standing out matters more than being polished. Let's prioritize earned secrets and spiky POVs."

5a. **Scoring Drift Detection** (Level 5 requires this; Levels 1-4: run if 3+ outcomes exist):
   - Run Scoring Drift Detection Protocol from `references/calibration-engine.md`:
     1. Build outcome-score matrix (each real interview → pre-interview practice scores → outcome)
     2. Check for systematic drift per dimension: Are some dimensions consistently overestimating or underestimating outcomes?
     3. Check feedback contradictions: When interviewer feedback contradicts coach scores, note discrepancy
     4. Generate drift report (which dimensions need recalibration?)
     5. Present adjustments to candidate (reframed as "improved predictive accuracy, not goalpost-moving")
   - Update `coaching_state.md` → Calibration State → Scoring Drift Log
   - Update `coaching_state.md` → Calibration State → Calibration Status (uncalibrated → calibrating → calibrated)

5b. **Cross-Dimension Root Cause Review** (if Calibration State exists with active root causes):
   - For each active root cause: assess whether treatment is working (affected dimensions improving in tandem?), check resolution criteria (1+ point improvement sustained over 3+ sessions?), update status
   - If a root cause isn't responding after 3+ sessions of treatment: Recommend pivot: "We've been treating [root cause] with [treatment] for [N] sessions. Affected dimensions aren't improving together. Let's try a different approach."

5c. **Success Pattern Analysis** (if 1+ advancement or offer exists):
   - Run Learning from Successes protocol from `references/calibration-engine.md`:
     1. Validate fit assessments: Did fit verdicts predict outcomes correctly?
     2. Track positive dimension-outcome correlation: Which dimensions correlate with advancement?
     3. Update storybank with success annotations
     4. Extract success patterns from 3+ successes
   - Ensures system learns from what it got right, not just failures

5.5. **Outcome-Based Targeting Insights** (if 3+ real interview outcomes):
   - Rejection clustering: Are rejections concentrated by company type, seniority level, domain, or process stage?
   - Stage analysis: Where in funnel do rejections cluster (not hearing back / first-round / final-round)?
   - Feedback mining: Do multiple rejections mention same theme? ("not enough experience at scale")
   - Fit assessment accuracy: Did "Strong Fit" verdicts predict advancement? If not, why?
   - Present as narrative: "You've applied to 6 roles. You advanced at 3 mid-stage startups, rejected by all 3 enterprise companies. Enterprise rejections all mentioned 'experience at scale.' This isn't a practice problem — it's a targeting pattern. Your skills are landing where they fit."
   - When pattern suggests retargeting: Don't prescribe — inform: "The data suggests a pattern. Want to discuss whether adjusting your target companies would help, or do you want to keep pushing on current targets?"

6. **Check graduation criteria** (skip if <3 sessions):
   - Interview-ready bar: 3+ scores of 4+ across dimensions? No dimension consistently below 3? 8+ stories with 5+ at strength 4+? Critical competency gaps covered? Can handle gap questions without freezing? Self-assessment calibrated within 0.5?
   - Competitive-ready bar: All dimensions averaging 4+? 3+ earned secrets deployable? Differentiation 4+ on signature stories? Can compress/expand answers fluidly? Handled skeptical pushback without defensiveness? Real interview advancement rate 60%+?
   - When graduation criteria met: Say explicitly: "Based on your scores, storybank, and real interview results, I think you're ready for [target company/role]. Here's what the data shows: [evidence]. You don't need more practice — you need the real thing."
   - When criteria not met after 5+ sessions: "We've been working on Structure for 5 sessions and it's not moving. That usually means we need a different approach, not more repetition. Let's try [specific new drill/technique]."
   - Data-driven trigger for targeting adjustment: If Outcome-Based Targeting Insights (Step 5.5) revealed clustering, reference instead of waiting for score plateau. "Your rejections clustered by company type — targeting issues often masquerade as skill gaps."

7. **Identify top priorities** (based on triage, not just lowest scores):
   - What's blocking real interview advancement? (correlation data if exists)
   - What's been flat longest? (trend data)
   - What's in storybank gaps? (competency coverage)
   - What pattern keeps showing up in rejections? (outcome data)

8. **Recommend specific drills** based on gaps identified

9. **Review and update Active Coaching Strategy**:
   - Is current approach producing results? If scores flat for 3+ sessions on target dimension: "We've been focused on [X] for [N] sessions and it's not moving. That usually means we need different approach."
   - Record old approach in Previous approaches with reason abandoned
   - Write new approach with rationale and pivot conditions
   - Update to `coaching_state.md`

10. **Run coaching meta-check** (every 3rd session or when triggered):
    - Count Session Log rows: if count is multiple of 3, include meta-check
    - Or if candidate seems disengaged, defensive, stuck
    - Or reference previous Meta-Check Log and build on past conversations
    - Ask: "Is this feedback landing? Are we focused on the right bottleneck? Anything to change about our approach?"
    - Record response in Meta-Check Log

## Output Schema

```markdown
## Progress Snapshot
- Sessions analyzed: [N]
- Real interviews completed: [N]
- Real interview outcomes: __ advanced / __ rejected / __ pending
- Current trend: Improving / Flat / Regressing

## Your Trajectory
[Narrate each dimension: direction, inflection points, what caused shifts, what's next]
- Substance: [score history e.g., 2.5 → 3.0 → 3.2 → 3.5] — [narration]
- Structure: [score history] — [narration]
- Relevance: [score history] — [narration]
- Credibility: [score history] — [narration]
- Differentiation: [score history] — [narration]

## Hard Truth (Level 5 only)
[One paragraph. No softening. Just the truth. Drawn from: Score History trends, storybank gaps, avoidance patterns, self-assessment deltas, outcome patterns.]

## Self-Assessment Calibration
- Your average self-ratings vs. my scores:
  - Substance: You __ / Me __
  - Structure: You __ / Me __
  - Relevance: You __ / Me __
  - Credibility: You __ / Me __
  - Differentiation: You __ / Me __
- Pattern: [over-rater / under-rater / well-calibrated]
- What this means for your prep: [implications]

## Outcome Correlation (if 3+ real interviews)
[Narrate which dimensions predict your outcomes, what feedback says, what's unmeasured]
- Dimensions that predict advancement for you: [list]
- Dimensions linked to rejections: [list]
- Feedback-to-dimension mapping: [patterns from interviewer feedback]
- Unmeasured factors to investigate: [e.g., energy, pacing, rapport]

## Targeting Insights (if 3+ outcomes)
- Rejection pattern: [clustered by company type / seniority / domain / stage — or no pattern]
- Stage analysis: [where in funnel rejections cluster]
- Feedback signals: [recurring themes from recruiter/interviewer feedback]
- Fit assessment accuracy: [did fit verdicts predict outcomes?]
- Recommendation: [continue current targeting / consider adjusting — with specifics]

## Graduation Check
- Interview-ready criteria: __ of 6 met
  - [ ] 3+ scores of 4+ across dimensions
  - [ ] No dimension consistently below 3
  - [ ] 8+ stories, 5+ rated 4+ strength
  - [ ] Critical competency gaps covered
  - [ ] Gap questions handled in practice
  - [ ] Self-assessment calibrated (within 0.5)
- Competitive-ready criteria: __ of 6 met (if applicable)
- Assessment: [Not yet ready / Ready for interviews / Ready for competitive processes]
- What's between you and ready: [specific gaps]

## Question Type Performance (if 5+ Question Bank entries)
- Strongest competency areas: [competency — avg score — count]
- Weakest competency areas: [competency — avg score — count]
- Targeting recommendation: [specific competency to drill, if gap is actionable]

## Calibration Check (if 3+ outcomes)
- Calibration status: [uncalibrated / calibrating / calibrated / miscalibrated]
- Drift detected: [per dimension — direction and magnitude, or "no drift detected"]
- Adjustments made this review: [any scoring recalibrations, or "none needed"]
- Candidate framing: [how drift was presented to candidate]

## Active Root Causes (if applicable)
| Root Cause | Affected Dimensions | Status | Treatment | Progress |
|---|---|---|---|---|
[from Calibration State — only active root causes with treatment effectiveness assessment]

## Intelligence Freshness
- Question Bank entries flagged as historical (3-6 months): [count]
- Question Bank entries archived (>6 months): [count]
- Company Patterns flagged as stale (>6 months): [list companies]
- Patterns needing re-test (>3 months old): [list]

## Patterns
- Repeating strengths: [observable patterns across sessions]
- Repeating failure modes: [observable patterns across sessions]
- Confirmed effective patterns (3+ data points): [from Interview Intelligence]
- Confirmed ineffective patterns (3+ data points): [from Interview Intelligence]
- Confirmed success patterns: [from calibration — what correlates with advancement]
- Feedback-outcome correlation: [if sufficient data]

## Revisit Queue
- Past weaknesses to retest: [list with context]

## Top 2 Priorities (Next 2 Weeks)
1. Priority:
   Why:
   Drill:
   Success metric:
2. Priority:
   Why:
   Drill:
   Success metric:

## JD Pattern Analysis (if 3+ JD Analyses)
- Recurring competencies across decoded JDs: [competencies appearing in 3+ JDs — market-validated sweet spot]
- Emerging requirements: [competencies in recent JDs not in earlier ones]
- Competency coverage: [which recurring competencies have strong storybank coverage vs. gaps]
- Targeting signal: [what JD patterns reveal about actual market position]

## Storybank Health
- Total stories: __ (target: 8-12)
- Strong stories (4-5): __ (target: at least 60%)
- Stories needing rework (1-3): __ [list with S### IDs]
- Retirement candidates (below 3 after 2+ improvement attempts): __
- Earned secret coverage: __ of __ stories have real earned secrets
- Competency coverage: [list critical gaps for target roles]
- Retrieval readiness: [has candidate run retrieval drill? last retrieval score?]
- Assessment: [Healthy / Needs work / Critical gaps]

## Coaching Meta-Check
- Is this feedback landing?
- Are we focused on the right bottleneck?
- Anything to change about our approach?

**Recommended next**: [State-aware recommendation based on top priority and bottleneck]. **Alternatives**: `practice`, `stories`, `prep [company]`, `mock [format]`
```

## State Write Targets

- **Score History**: Add entry if new scores produced in this session
- **Calibration State → Scoring Drift Log**: Add drift detection findings
- **Calibration State → Cross-Dimension Root Causes**: Update treatment status, resolution progress
- **Calibration State → Calibration Status**: Update (uncalibrated → calibrating → calibrated)
- **Active Coaching Strategy**: Update with new approach if pivot needed; move old approach to Previous approaches
- **Meta-Check Log**: Record candidate response and any coaching adjustment (if meta-check was run)
- **Session Log**: Add entry for progress session

## Recommended Next

**State-aware sequence** (in order of priority):

1. If graduation-ready and interview within 48h → `hype` (confidence + 3x3 plan)
2. If graduation-ready but no near-term interview → `prep [company]` (target-specific drill) or `concerns` (anticipate objections)
3. If not graduation-ready AND top priority is a specific dimension → `practice [role/format]` or `mock [format]` (drill)
4. If not graduation-ready AND storybank has gaps → `stories improve` (fix weakest stories)
5. If outcome data revealed targeting pattern → discuss `jobs` or `decode` (adjust pipeline)
6. If across 5+ sessions no progress on target dimension → discuss strategy pivot with candidate

**Alternatives**: `stories improve`, `practice [role/format]`, `mock [format]`, `prep [company]`, `concerns`, `progress` (if scheduling another review)

## Minimum Data Thresholds

| Data Available | What You Can Do | What You Can't Do |
|---|---|---|
| **1 scored session** | Show baseline, identify initial patterns, set priorities. Say: "This is your starting point. I need 2-3 more data points for trends." | Trend narration, outcome correlation, graduation check |
| **2-3 scored sessions** | Show direction (improving/flat/declining), early patterns, preliminary self-assessment calibration | Reliable trend narration (need inflection points), outcome correlation (need 3+ real interviews) |
| **4+ scored sessions** | Full trend narration with inflection points and plateau diagnosis | Outcome correlation still needs 3+ real interviews |
| **3+ real interview outcomes** | Full outcome-score correlation analysis | Nothing — full protocol available |

When data is thin (1-2 sessions): Focus on (1) what available scores tell right now, (2) most important next step, (3) what data needed before next progress review useful. Don't run hollow version of full protocol.
