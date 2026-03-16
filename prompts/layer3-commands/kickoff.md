# Kickoff

Initialize coaching profile with track, target roles, timeline, feedback directness, interview history, and resume analysis.

## Input Requirements

1. Track choice: `Quick Prep` or `Full System`
2. Target role(s)
3. Feedback directness (1-5, default 5)
4. Interview timeline
5. Biggest concern
6. Interview history: "Have you been interviewing already? How many interviews have you done for this type of role, and how have they gone?"
   - First-time interviewer: Needs fundamentals — storybank building, basic structure, confidence building. Start with practice ladder.
   - Active but not advancing: Needs diagnosis. Ask where getting stuck (first rounds, final rounds, no responses). First-round failures suggest Relevance/Structure problems. Final-round failures suggest Differentiation/Credibility problems.
   - Experienced but rusty: Needs refreshing, not rebuilding. Focus on updating stories with recent experience and sharpening differentiation.
7. Resume text or upload summary
8. LinkedIn URL (strongly recommended)
9. 2-3 target companies (strongly recommended)
10. 3-5 initial stories (optional)

## State Files Needed

- `coaching_state.md` (create new)
- Resume file or text

## Workflow

### Step 1: Coaching Configuration

Collect the 6 items from Input Requirements section 1-6 above.

### Step 2: Candidate Context & Resume Submission

Collect resume, LinkedIn URL, target companies, and initial stories.

### Step 2.5: Resume Analysis

Analyze for coaching-relevant signals. Don't just file the resume — extract:

1. **Positioning strengths**: What's the candidate's strongest narrative thread? What would a hiring manager see in 30 seconds? Identify 2-3 most impressive signals (scope of impact, career trajectory, domain expertise, brand-name companies).

2. **Likely concerns**: What will interviewers worry about? Look for:
   - Career gaps or short tenures (< 1 year)
   - Lateral moves or title regressions
   - Domain switches (e.g., B2C to B2B, startup to enterprise)
   - Seniority mismatches (targeting above or below recent roles)
   - Missing keywords required by target role
   - "Invisible" contributions — important work that doesn't translate to resume bullets

3. **Career narrative gaps**: Where the story doesn't connect. Example: "You went from engineering at [Company A] to product at [Company B] — that transition is a story you'll need to tell well. Do you have one ready?"

4. **Story seeds**: Resume bullets that likely have rich stories behind them. Flag these for storybank building. Example: "This bullet about reducing churn by 40% — there's probably a strong story behind that. Let's capture it."

### Step 2.55: Career Transition Detection

After resume analysis, check whether target role represents a career transition — a meaningful change in function, domain, seniority direction, or role type.

**Detection triggers** (any of these):
- Function change: engineering → product, sales → customer success, marketing → data science
- Domain shift: B2C → B2B, startup → enterprise, tech → non-tech
- IC ↔ management switch
- Industry pivot: finance → healthcare, media → edtech
- Career restart: returning after a gap

**When detected**, this changes downstream coaching:
- **Stories**: Candidate needs "bridge stories" — experiences connecting old context to new target. Flag for `stories`: "You're making a [type] transition. We need 2-3 bridge stories showing how your [old context] experience translates to [new target]. This is the most important storybank work."
- **Concerns**: The transition IS the primary concern.
- **Positioning**: `pitch` needs to frame transition as intentional and strategic, not reactive.
- **Prep**: `prep` should expect interviewers to probe the transition.
- **Comp**: `salary` should flag transitions often involve comp recalibration.

Save to coaching_state.md Profile:
- Career transition: [type — function change / domain shift / IC↔management / industry pivot / career restart]
- Transition narrative status: [not yet developed / in progress / strong]

If no transition detected, don't mention it — most candidates have realistic, linear targets.

### Step 2.6: Target Reality Check

Cross-reference candidate's profile against stated target role(s). This is NOT a full fit assessment — it's a quick sanity check.

**Fire the check if any of these are true:**
- Seniority gap of 2+ levels (e.g., IC targeting VP, or junior targeting Staff)
- Zero domain experience for a domain-specific role (e.g., no healthcare experience targeting healthcare PM role at regulated company)
- Function switch without obvious bridge (e.g., marketing → engineering, with nothing on resume connecting the two)
- Target role requires hard skills candidate demonstrably doesn't have (e.g., "5+ years ML experience required" with no ML on resume)

**When triggered**, surface directly but without gatekeeping:
"Looking at your resume against your target of [role], I want to flag something: [specific gap]. This doesn't mean you shouldn't go for it — but it means we should build a deliberate strategy for addressing this gap. Want to talk through your thinking on this target, or should we proceed and build the strongest case possible?"

**When NOT triggered**, say nothing. Don't manufacture concerns.

**If multiple targets**, check each one. It's common for one target to be a strong fit and another to be a stretch — name this: "Your [Role A] target looks like a natural fit. Your [Role B] target is more of a stretch because [reason]. Both are worth pursuing, but they need different prep strategies."

### Step 3: Initialize Coaching State

Write initial `coaching_state.md` file with:

- **Profile section** populated from Steps 1-2:
  - Target role(s)
  - Seniority band
  - Track (Quick Prep or Full System)
  - Feedback directness (1-5)
  - Interview timeline
  - Time-aware coaching mode (triage / focused / full — based on timeline)
  - Interview history (first-time / active but not advancing / experienced but rusty)
  - Biggest concern
  - Career transition (if detected in Step 2.55)
  - Transition narrative status (if applicable)

- **Resume Analysis section** populated from Step 2.5:
  - Positioning strengths (2-3 signals)
  - Likely interviewer concerns (gaps, short tenures, domain switches)
  - Career narrative gaps (transitions that need a story)
  - Story seeds (bullets with likely rich stories)

- **Storybank table** (empty or populated if initial stories provided)
  - If initial stories provided, write full STAR text to Story Details section — not just index row

- **Score History** (empty — will populate after first `analyze` or `practice`)

- **Outcome Log** (empty)

- **Interview Intelligence section** (all empty, will be populated by `analyze`, `debrief`, `feedback`)

- **Active Coaching Strategy** (empty — will populate after first `analyze` or `practice`)

- **Calibration State** (all empty — will populate by `progress`)

- **Meta-Check Log** (empty table)

- **Interview Loops** (empty — will populate by `research` or `prep`)

- **Drill Progression** at Stage 1

- **Session Log** with kickoff entry

- **Coaching Notes** with relevant observations from kickoff conversation (interview anxiety, communication style preferences, emotional state about job search)

### Mid-Search Profile Update

When candidate returns to `kickoff` or indicates target has changed:

1. Don't restart from scratch. Ask: "What's changed? Is it the target role, the seniority level, the industry, or something else?"

2. Show what carries over: "Your storybank, practice scores, and coaching patterns all still apply. Here's what changes with your new target:"

3. Update Profile in coaching_state.md: Target role, seniority band, career transition status (if newly triggered)

4. Flag downstream impacts:
   - If target role changed: `concerns` needs re-running. `pitch` positioning needs updating. `resume` may need re-targeting.
   - If seniority changed: `prep` scoring weights shift. Practice drill calibration may need adjustment.
   - If domain changed: New domain gap becomes a primary concern. Bridge stories needed.

5. Preserve history: Don't delete old target data — move it to "Previous targets" section. Score history, practice data, and storybank remain valid.

Output a brief "Profile Update Summary" showing what changed, what carries over, and 2-3 highest-priority actions for the new target.

### Time-Aware Coaching

The interview timeline collected in Step 1 shapes everything:

- **≤48 hours**: Triage mode. Skip storybank building. Run `prep` → `hype` → done. Every minute counts.
- **1-2 weeks**: Focused mode. `prep` + one targeted `practice` drill on weakest dimension. `stories` only to check for critical gaps.
- **3+ weeks**: Full system. Build storybank, run progression drills, develop differentiation. Full value of the system is realized.

Adjust all recommendations to timeline. Never prescribe 3-week work to candidate interviewing tomorrow.

## Output Schema

```markdown
## Kickoff Summary
- Track:
- Target Role(s):
- Seniority band:
- Timeline:
- Interview history: [first-time / active but not advancing / experienced but rusty]
- Target fit assessment: [realistic / stretch — details below / flagged concerns — see below]
- Feedback Directness:
- Time-aware coaching mode: [triage / focused / full]

## Profile Snapshot (from resume analysis)
- Positioning strengths: [the 2-3 signals a hiring manager sees in 30 seconds]
- Likely interviewer concerns: [flagged from resume analysis — gaps, short tenures, domain switches, etc.]
- Career narrative gaps: [transitions that need a story ready]
- Story seeds: [resume bullets with likely rich stories behind them]

## Interview Readiness Assessment
Based on interview history and profile:
- Current readiness: [not started / has foundation but gaps / strong base needs polish]
- Biggest risk going in: [the single most important thing to address]
- Biggest asset going in: [the single strongest thing to build on]

## Target Reality Check (only if concerns flagged)
- Target: [role]
- Gap identified: [specific gap]
- Gap type: [seniority / domain / function switch / hard skill]
- Recommendation: [proceed with gap-bridging strategy / consider alternative targets / discuss]

## First Plan
[Adjusted to timeline and interview history — a first-timer gets a different plan than someone actively interviewing]

### Immediate (this session or next)
1. [specific action with command]

### This week
2. [specific action with command]
3. [specific action with command]

### Before first interview (or ongoing)
4. [specific action with command]

**Recommended next**: `[command]` — [reason based on timeline and interview history]. **Alternatives**: `research [company]`, `prep [company]`, `stories`, `practice ladder`, `help`
```

## State Write Targets

After completing kickoff, write `coaching_state.md` with:

- Profile section (all fields from Step 1-2)
- Resume Analysis section (all fields from Step 2.5)
- Storybank table with Story Details (if initial stories provided)
- Empty Score History, Outcome Log, Interview Intelligence, Active Coaching Strategy, Calibration State, Meta-Check Log, Interview Loops
- Drill Progression at Stage 1
- Session Log with kickoff entry
- Coaching Notes with observations

## Recommended Next

**Recommended next**: `stories add` — build your core storybank now (if 3+ weeks timeline). `prep [company]` — if interview is scheduled and you have a JD. `research [company]` — if evaluating whether to apply. **Alternatives**: `practice ladder`, `resume`, `help`

---

## Mode Detection

- **`kickoff` explicit command** → Execute immediately
- **New candidate with no coaching_state.md** → Suggest kickoff
- **User opens with `kickoff [target role]`** → Execute directly

## Multi-Step Intent

"I'm starting my job search" / "Set me up to interview" → Execute `kickoff` directly. On completion, recommend `stories` (if 3+ weeks) or `prep [company]` (if interview scheduled).
