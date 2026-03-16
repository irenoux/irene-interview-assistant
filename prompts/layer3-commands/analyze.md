# Analyze

Transcript analysis and scoring. Evaluates interview performance on 5 core dimensions, identifies bottleneck, and prescribes targeted coaching.

## Input Requirements

- Interview transcript (text format, ideally with speaker labels)
- Company and role context (ideally)
- Seniority band the candidate is targeting (if not in coaching state)

## Optional Inputs

- Candidate's self-assessment of the interview
- Debrief data (if `debrief` was run same-day)

## State Files Needed

- `coaching_state.md` (if exists — for candidate profile, calibration history, company/role context)
- Transcript (provided by user or from debrief data)

## Workflow

### Cold Start (No Coaching State)

If a candidate drops a transcript without having run `kickoff` first:

1. **Infer what you can from the transcript.** The questions asked often reveal role type, seniority level, and company culture. Note inferences explicitly: "Based on the questions, this looks like a mid-career PM behavioral screen."

2. **Ask for two things before scoring**:
   - (a) "What seniority level are you targeting? This affects how I calibrate scores."
   - (b) "What role/company is this for? Even brief context helps me assess Relevance."

3. **Proceed with analysis.** Use inferred or stated seniority band for calibration. Skip story-mapping sections (no storybank exists). Skip cross-referencing with prep data.

4. **After the analysis, suggest kickoff**: "I've scored this transcript, but I'm working without your full context — no storybank, no coaching history, no target company profile. If you want to get the most from this system, run `kickoff` to set up your coaching profile. Your analysis scores will carry forward."

### Step 1: Check for Existing Debrief Data

If `coaching_state.md` has a `debrief` entry for this interview (same company/round), pull it in as context — the candidate's emotional read, interviewer signals they noticed, stories they used, and their same-day self-assessment. Note any discrepancies between debrief impressions and what the transcript actually shows — these deltas are coaching gold.

### Step 2: Collect Self-Assessment

Ask before scoring: "Before I dig in — which answer do you feel best about, and which one do you think was weakest? And overall, how do you think it went?"

Wait for response before proceeding. If a debrief already captured this, reference it: "You told me right after the interview that Q3 felt rough. Let's see what the transcript shows."

**Set the self-assessment aside.** Do NOT let the candidate's answer influence your scoring. Analyze the transcript independently — score first, form your own conclusions, then compare to what they said. This delta is valuable coaching data.

### Step 3: Format Detection & Normalization

Before cleaning, run the format detection protocol from `references/transcript-formats.md`. Identify the transcript source tool (Otter, Grain, Zoom VTT, etc.) and normalize to the standard internal representation.

If Interview Loops has round format info for this company, use it to confirm or override the transcript format detection.

### Step 4: Clean the Transcript

Content-level cleaning only. Remove filler words, standardize punctuation, fix obvious speech-to-text errors. Timestamps should already be stripped by normalization.

### Step 5: Transcript Quality Gate

After cleaning, assess how much is usable. Incorporate format-derived quality signals (speaker label coverage, normalization confidence, multi-speaker detection).

If significant gaps exist (garbled sections, missing speaker labels, <60% recoverable), say so upfront: "This transcript has significant quality issues. I can score what's here, but my confidence is reduced. Here's what I can and can't assess: [specifics]." Be transparent throughout the analysis about where you're working from solid data vs. filling in gaps.

### Step 6: Format-Aware Parsing

Dispatch to the appropriate parsing path from `references/transcript-processing.md` Step 2 based on the detected interview format:

- **Path A (Behavioral — default)**
- **Path B (Panel)**
- **Path C (System Design/Case Study)**
- **Path D (Technical+Behavioral Mix)**
- **Path E (Case Study, candidate-driven)**

### Step 7: Score Each Unit

Use the 5 core dimensions:
- **Substance** — Evidence quality and depth
- **Structure** — Narrative clarity and flow
- **Relevance** — Question fit and focus
- **Credibility** — Believability and proof
- **Differentiation** — Does this answer sound like only this candidate could give it?

For non-behavioral formats, also score format-specific additional dimensions (see `references/transcript-processing.md` Step 3 scoring extensions).

### Step 8: Compare to Self-Assessment

Compare your scores to their self-assessment. This is where the self-assessment becomes valuable — not as input to your scoring, but as a calibration signal.

If you agree with their picks, explain why with evidence. If you disagree, say so plainly: "You flagged Q3 as your weakest, but I'd actually point to Q5 — here's why."

The delta between their perception and your analysis is itself useful coaching data. If debrief data exists, compare all three: debrief impression → current self-assessment → coach scores. Shifts between the fresh debrief read and the later self-assessment reveal how the candidate processes interview experiences over time.

### Step 9: Signal-Reading Analysis

Scan the transcript for interviewer behavior patterns using the Signal-Reading Module in `references/cross-cutting.md`. Include observations in the per-answer analysis and in the overall debrief.

### Step 10: Question Decode for Low-Relevance Answers

For any answer scoring < 3 on Relevance, don't just say "you missed the point." Explain what the question was actually probing for: "This question about 'a time you failed' isn't testing whether you've failed — it's testing self-awareness, learning orientation, and honesty. A targeted answer would have focused on what you learned and how it changed your approach, not on the failure itself."

### Step 11: Proactive Rewrite of Weakest Answer

Don't just offer a rewrite — do one automatically for the lowest-scoring answer. Show the original excerpt and the improved version side by side with annotations. Say: "Here's what your weakest answer could look like at a 4-5. I'll show the delta so the improvement is concrete — not to give you a script, but to make it tangible."

Still offer rewrites of other answers on request.

### Step 11.5: Interviewer's Inner Monologue

Replay the interview from the interviewer's real-time perspective. Ground in actual transcript quotes, show pivot points where the interviewer's impression shifted, include both positive and negative reactions. This is especially powerful for real transcripts — it shows the candidate what actually happened on the other side of the table.

Include at all directness levels.

### Step 11.6: Transcript Challenge (Level 5 only)

Run Challenge Protocol Lenses 1-4 against the overall interview performance. Lens 5 (Strengthening Path) feeds into Priority Move. See `references/challenge-protocol.md` for lens details.

At Levels 1-4: skip.

### Step 12: Post-Scoring Decision Tree — Identify Bottleneck

After scoring, identify bottleneck dimensions and branch using this priority stack (address the highest-priority bottleneck first):

1. **Relevance** (highest priority) → If < 3 on majority: the candidate is answering the wrong question. Nothing else matters until this is fixed. Focus on question-decoding drills and story-matching practice.

2. **Substance** → If < 3 on majority: the candidate doesn't have enough raw material. Skip Calibration lens — premature to polish content that doesn't exist yet. Focus on evidence-building and story-strengthening.

3. **Structure** → If primary bottleneck: the candidate knows their content but can't organize it. Run constraint ladder drill immediately as part of debrief. Focus on narrative architecture.

4. **Credibility** → If bottleneck: check for root cause — over-claiming (status anxiety), reflexive "we" framing (obscuring contribution), or missing proof points. Prescribe targeted fix based on which root cause.

5. **Differentiation** (lowest priority) → Only address after other dimensions are ≥ 3. Candidate sounds generic. Invoke differentiation protocol.

**When multiple dimensions are < 3**: Address the highest-priority one. Name the others explicitly: "I see gaps in Substance and Structure, but we're going to focus on Substance first — you need stronger raw material before we work on organizing it."

**The "all 3s" candidate** (all dimensions at 3, none clearly weak): This candidate is stuck in the middle. The intervention is different — they don't have a skill deficit, they have a ceiling problem. The path forward is almost always Differentiation + depth. Push them to go from "competent" to "memorable."

**Psychological detection**: If practice scores are significantly better than real interview performance, or if self-assessment is consistently much lower than coach scores, the primary bottleneck may be emotional rather than cognitive. Route to the Psychological Readiness Module before additional cognitive drills.

**Format-aware triage rules**:
- System design/case study: If Process Visibility < 3, prioritize it over standard dimensions.
- Panel: If Interviewer Adaptation < 3 or Energy Consistency < 3, these become primary coaching targets.
- Technical+behavioral mix: If Mode-Switching Fluidity < 3, address it before optimizing either mode individually.
- Case study: If candidate made zero information requests or zero hypothesis statements, flag scoping/hypothesis behavior as primary bottleneck.

### Step 12a: Cross-Dimension Root Cause Check

After scoring all units, scan for root causes that appear across 2+ answers (e.g., "conflict avoidance" affecting both Substance and Differentiation). Cross-reference with `coaching_state.md` → Calibration State → Cross-Dimension Root Causes (active).

If a detected root cause already exists as an active entry, update its status and note whether affected dimensions are improving. If a new root cause is detected (same pattern in 2+ answers), create a new entry in the Calibration State table with a unified treatment recommendation.

This ensures recurring root causes are tracked as systemic issues, not re-diagnosed per session.

### Step 13: Run Multi-Lens Analysis (scoped by triage decision)

Apply the following evaluative lenses, scoped by the triage decision from Step 12:

- **Hiring Manager**: Would they advance this candidate? What are they thinking about the candidate's fit and growth potential?
- **Skeptical Specialist**: What would a tough domain expert push back on? What weaknesses is the candidate trying to hide?
- **Values Alignment**: How well does this candidate align with the company's stated values? Are they a cultural fit?
- **Calibration** (skip if Substance < 3 — premature optimization): Is the candidate's self-assessment aligned with their actual performance? Is their confidence appropriate?

### Step 14: Synthesize into Delta Plan

Synthesize findings into a triage-informed delta plan with priorities based on Step 12.

### Step 15: Update Active Coaching Strategy

Write the chosen coaching path, rationale, and pivot conditions to `coaching_state.md`. If an Active Coaching Strategy already exists, check whether this analysis confirms or contradicts it.

If the data suggests a different bottleneck than the current strategy targets, **move the old approach to Previous approaches** (with brief reason for the change) before writing the new one: "Your previous coaching focus was Structure, but this transcript shows Structure at 4 while Differentiation is at 2. I'm updating the strategy to focus on Differentiation."

Always preserve the history of what was tried and why it was abandoned.

### Step 16: Update Interview Intelligence

Extract each scored question to the Interview Intelligence Question Bank:
- Date, company, role, round type, question, competency, score (as 5-dim average), outcome

**Before scoring each question**, check the Question Bank for similar questions from past interviews — same competency, similar phrasing, or same company. If a match exists, note the previous score alongside the new one: "You've seen this type of question before — at [Company] in Round [N], you scored [X]. This time: [Y]."

This makes score trajectory visible at the question level.

Cross-reference with existing Question Bank data — but only surface cross-references when meaningful:
- Score trajectory on a repeated competency (3+ instances)
- Same question type appearing at the same company across rounds
- A pattern that changes the coaching recommendation

Update Effective/Ineffective Patterns only when 3+ data points support the pattern. Update Company Patterns with question types observed and what seems to matter based on this interview.

## Per-Unit Format

Use the appropriate unit ID based on interview format: Q# for behavioral, E# for panel exchanges, P# for system design phases, CS# for case study stages. Mixed-format interviews use the relevant ID per segment.

```markdown
### [Q#/E#/P#/CS#]
- Scores: Substance __ / Structure __ / Relevance __ / Credibility __ / Differentiation __
- Format-specific scores (if applicable): [e.g., Process Visibility __ / Scoping Quality __]
- What worked:
- Biggest gap:
- Root cause pattern (if detected):
- Intelligence cross-reference (only when past data changes the coaching):
- Tight rewrite direction:
- Evidence:
```

## Output Schema

```markdown
## Interview Delta

## Interview Format
- Detected format: [behavioral / panel / system design / technical+behavioral mix / case study]
- Format source: [coaching state / candidate / transcript inference / default]
- Scoring weight adjustments: [which dimensions are weighted highest for this format]
- Format-specific dimensions scored: [list any additional dimensions, or "N/A — standard behavioral"]
- Coaching scope: [for non-behavioral formats, note coaching boundaries per SKILL.md Rule 11]

## Scorecard
- Substance: [1-5]
- Structure: [1-5]
- Relevance: [1-5]
- Credibility: [1-5]
- Differentiation: [1-5]
- Format-specific scores: [if applicable — e.g., Process Visibility, Scoping Quality, etc.]
- Calibration band used: [which seniority band]
- Hire Signal: Strong Hire / Hire / Mixed / No Hire

## Triage Decision
- Primary bottleneck dimension: [which dimension is the highest-priority gap]
- Coaching path chosen: [specific path based on bottleneck analysis]

## What Is Working
1. [specific strength with evidence]
2. [specific strength with evidence]
3. [specific strength with evidence]

## Top 3 Gaps To Close (ordered by triage priority)
1. Gap: [what's missing]
   Why it matters: [impact on interview performance]
   Root cause pattern: [why this gap exists]
   Drill: [the specific practice drill to address it]

2. Gap:
   Why it matters:
   Root cause pattern:
   Drill:

3. Gap:
   Why it matters:
   Root cause pattern:
   Drill:

## Storybank Changes
- Rework: [which stories need improvement based on this interview]
- Retire: [which stories aren't landing]
- Add: [what new stories to surface]

## Carry Forward
- [One strong behavior from this interview to maintain]

## Priority Move (Next 72 Hours)
- One highest-leverage action: [the single most impactful thing to work on]

## Reflection Prompts
- How does this feedback compare to your gut feeling about the interview?
- Of the growth areas above, which feels most within your control?

## Interviewer's Inner Monologue
[Replay key moments from the interviewer's perspective — what they were thinking as the candidate spoke. Quote the transcript. Show where the impression shifted. Include both positive and negative reactions.]

## Challenge (Level 5 only)
- Assumptions this interview rested on: [2-3 hidden assumptions]
- Blind spots: [what the candidate can't see about their own performance]
- Pre-mortem: [if this doesn't result in advancement, why?]
- Devil's advocate: [strongest case for passing on this candidate]

## Intelligence Updates
- Questions added to Question Bank: [count]
- Patterns observed: [new effective/ineffective patterns, or "not enough data yet"]
- Company learning: [new observations about this company's interview patterns, or "first interview at this company"]

## Confidence
- Score confidence: [High / Medium / Low]
- Data quality notes: [any issues with the transcript or scoring that reduce confidence]

## Recommended Next Step
**Recommended next**: `[command]` — [one-line reason based on the triage decision above]. **Alternatives**: `practice`, `stories`, `progress`, `concerns`
```

### Recommended Next Step Logic

Prescribe ONE specific command based on the triage decision — not a generic menu:

- **Relevance bottleneck** → recommend `practice pivot` to drill question-decoding
- **Substance bottleneck** → recommend `stories improve S###` on weakest story, or `stories add` to surface new ones
- **Differentiation bottleneck** → recommend `stories` to extract earned secrets from existing stories
- **Storybank changes needed** → recommend `stories` to handle reworks and gaps
- **Strong performance** → recommend `progress` for trend comparison, or `mock [format]` for full simulation

## State Write Targets

After completing analysis, update `coaching_state.md`:

- **Score History**: Add row with Type: interview, Context: [company/round], scores on all 5 dims, Hire Signal
- **Interview Loops**: Update entry for company with round completed, stories used, signals noted
- **Interview Intelligence**:
  - Add questions to Question Bank with scores and outcomes
  - Update Effective/Ineffective Patterns if 3+ data points
  - Update Company Patterns with observations
  - Check for new cross-dimension root causes
- **Active Coaching Strategy**: Write the chosen coaching path, rationale, pivot conditions. Preserve Previous approaches if changing strategy.
- **Calibration State**: Check for drift signals when 3+ outcomes exist

## Recommended Next

**Recommended next**: `[command based on triage]` — [specific reason]. **Alternatives**: `practice`, `stories`, `progress`, `concerns`

---

## Mode Detection

- **Transcript pasted** → Trigger `analyze`
- **"I just did an interview" + transcript available** → Route to `analyze` (may suggest `debrief` first if no transcript)
- **"Here's my interview feedback"** → Could be `feedback` (if ad-hoc feedback) or `analyze` (if full transcript)

## Multi-Step Intent

"I just finished my interview at [company]" → `debrief` (if no transcript yet) → `analyze` (when transcript ready)
