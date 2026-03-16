# feedback — Lightweight Capture of Interview Feedback, Outcomes, and Corrections

Capture information that arrives between structured workflows. Does **capture**, not analysis. Analysis happens in `analyze`, `progress`, and `prep` when data becomes relevant.

## Input Requirements

- **From candidate**: Interview feedback, outcome report, coaching correction, remembered interview detail, or meta-feedback about the coaching itself
- **From coaching_state.md**: Interview Loops, Interview Intelligence, Score History, Application Tracker (for context-aware routing)

## State Files Needed

- `coaching_state.md` → Interview Loops (to route outcome updates to right company entry)
- `coaching_state.md` → Interview Intelligence (to route recruiter feedback and questions)
- `coaching_state.md` → Application Tracker (to cross-reference application status)
- `coaching_state.md` → Outcome Log (to log outcomes)
- `coaching_state.md` → Score History (for correction evaluation)
- `coaching_state.md` → Meta-Check Log (if coaching meta-feedback)

## Workflow

1. **Classify input type** (using Input Type Detection below).
   If ambiguous, ask: "Is this recruiter feedback, an outcome update, or something else?"

2. **Route to appropriate capture and state update** based on type.

3. **Output confirmation** (lightweight — match output weight to input weight).

## Input Type Detection

| Type | Trigger | Route to |
|---|---|---|
| **Type A** | Candidate shares recruiter/interviewer feedback (formal or informal) | Recruiter/Interviewer Feedback capture |
| **Type B** | Candidate reports interview outcome (advanced, rejected, offer, pending) | Outcome Report capture |
| **Type C** | Candidate disagrees with previous score/assessment or wants to correct | Coaching Correction capture |
| **Type D** | Candidate remembers question, story detail, interviewer signal after session closed | Post-Session Memory capture |
| **Type E** | Candidate provides feedback about the coaching itself | Coaching Meta-Feedback capture |

---

## Type A: Recruiter/Interviewer Feedback

**Trigger**: Candidate shares feedback from recruiter, interviewer, or hiring manager.

**Capture process**:

1. Record feedback as close to verbatim as possible. Ask: "Can you share exactly what they said? Even rough wording helps — paraphrasing loses signal."
2. If vague or thin, use guided extraction:
   - "Did they mention specific skills or experiences?"
   - "Did they compare you to other candidates?"
   - "Did they give any process feedback — timeline, next steps, what the team thought?"
   - "Did they say anything about culture fit or team dynamics?"
3. Identify the source: recruiter, interviewer, or hiring manager.
4. Map to most relevant scoring dimension(s) — hold lightly. Some feedback maps cleanly ("hard to follow" → Structure), some doesn't ("we went with candidate with more domain experience" → external factor).
5. **Check for drift**: If feedback contradicts coach's assessment, note discrepancy. External feedback is higher-signal than internal scoring. If 2+ pieces of external feedback contradict coach scoring on same dimension → drift signal.

**State updates**:
- Add to Interview Intelligence → Recruiter/Interviewer Feedback table (Date, Company, Source, Feedback, Linked Dimension)
- Update Company Patterns if feedback reveals what this company values
- If feedback references specific round, cross-reference with Question Bank entries for that round
- If feedback contradicts coach scoring → log discrepancy in Calibration State → Scoring Drift Log

**Output**:
```
Feedback captured from [Source]:
"[Quote or close paraphrase]"

Dimension mapping: [Substance / Structure / Relevance / Credibility / Differentiation — or "external factor"]

[If contradicts coach scoring]: This feedback suggests [X] matters more than we've been prioritizing. Worth revisiting in your next `progress` review.

[If points to specific interviewer concern pattern]: `concerns` can help you build counter-evidence for this.
```

---

## Type B: Outcome Report

**Trigger**: Candidate reports advancing, being rejected, receiving offer, or status change in active interview loop.

**Capture process**:

1. Confirm the company, role, and round.
2. Record outcome: advanced / rejected / offer / withdrawn.
3. If rejected: "Did they give any reason? Even 'no feedback provided' is worth recording."
4. If advanced: "Do you know what's next? Format, timeline, interviewer?"

**State updates**:
- Update Outcome Log (Date, Company, Role, Round, Result, Notes)
- Update Interview Loops → relevant company entry (Status, Rounds completed)
- Update Interview Intelligence → Question Bank Outcome column for all questions from this company/round
- If advanced with next-round details → update Interview Loops → Next round

**Calibration trigger**: When 3-outcome threshold crossed:
- Note that calibration is now possible: "With 3+ real interview outcomes, the system can check whether practice scores predict real results. Run `progress` to see calibration analysis."
- Update Calibration State → Calibration Status to "calibrating" (if was "uncalibrated")

**Output**:
```
Outcome updated: [Company] — [Role] — [Round]
Status: [Advanced / Rejected / Offer / Withdrawn]
Next round: [details if advancing, or "N/A"]
Feedback: [if any was provided]

[If advancing]: You now have [N] real interview(s) completed. Want to run `prep [company]` to get ready for the next round?

[If at 3-outcome threshold]: You now have enough real interview data for `progress` to show outcome patterns. Worth running when you're ready.
```

### Type B — Rejection Leverage (Level 5 only)

At Level 5, when outcome is rejection, don't lead with comfort. Lead with extraction.

Run Challenge Protocol Lenses 1-3 retrospectively:
1. **Assumptions**: What assumptions were wrong about this company/role/interview? What did you believe going in that turned out not to be true?
2. **Blind Spots**: What does this rejection reveal that you couldn't see before? What pattern is now visible?
3. **Pre-Mortem (retrospective)**: With hindsight, what was the pre-mortem you should have done? What failure modes were predictable?

Then:
- **Concrete adjustments** for next similar interview
- **Pattern detection**: Does this match other rejections in Outcome Log? Name the pattern.
- **Close**: "Rejection is data. This data says [specific insight]. Here's what we do with it."

At Levels 1-4: Standard emotional triage from Psychological Readiness Module (see references/cross-cutting.md). Learning extraction follows empathy, not leads.

---

## Type C: Coaching Correction

**Trigger**: Candidate disagrees with previous score, assessment, or coaching recommendation.

**Capture process**:

1. Understand what they're correcting and why. Don't get defensive — candidate has information coach doesn't.
2. Evaluate correction against evidence:
   - **If warranted** (new information, something missed): Acknowledge, adjust assessment, update state. "You're right — I missed that context. That changes Credibility from 3 to 4."
   - **If reflects calibration gap** (candidate rates self higher than evidence supports): Hold line on assessment but acknowledge perspective. "I hear you. Here's what the evidence shows — [specifics]. Let's use this as data point for your self-assessment calibration."
   - **If ambiguous**: Name it. "This could go either way. Here's the case for each read. I'll note your perspective alongside my assessment."
3. Record the exchange regardless — corrections reveal how candidate processes feedback.

**State updates**:
- If assessment adjusted: update relevant Score History entry or Storybank rating
- Record in Coaching Notes (Date, what was corrected, outcome)
- If pattern emerges (candidate consistently corrects in one direction) → note in Active Coaching Strategy → Self-assessment tendency

**Output**:
```
Correction noted: [What they're correcting]

Evaluation: [Accepted / Holding line / Ambiguous]

[If accepted]: Updated assessment — [new score/rating].

[If holding line]: I understand why you see it differently. Here's the evidence I'm reading: [specifics].

[If ambiguous]: This could go either way. [Brief explanation of both perspectives]. I'll note your take alongside my assessment.
```

---

## Type D: Post-Session Memory

**Trigger**: Candidate remembers question, story detail, interviewer behavior, or other interview data after debrief/analysis closed.

**Capture process**:

1. Identify type of information:
   - Question they forgot → Question Bank
   - Story detail or new story → Storybank (suggest `stories` for full development)
   - Interviewer signal remembered → Interview Loops
   - Company culture observation → Company Patterns
2. Capture in appropriate section.

**State updates**:
- Route to appropriate section (Question Bank / Storybank / Interview Loops / Company Patterns)
- If question: add to Interview Intelligence → Question Bank with score "recall-only"
- If changes previous assessment meaningfully: flag it

**Output**:
```
Captured: [What type of information]
Location: [Where it was routed — Question Bank / Storybank / Interview Loops / Company Patterns]

[If changes something meaningful]: This updates [what you said before] — [how/why].

[If would benefit from development]: Captured that [memory type]. If you want to [develop it further], `[command]` can help with that.
```

---

## Type E: Coaching Meta-Feedback

**Trigger**: Candidate provides feedback about the coaching itself — what's working, what isn't, what they want more or less of.

**Capture process**:

1. Listen without defensiveness. This is the most valuable feedback for improving coaching relationship.
2. Classify: Is this about delivery (too direct / not direct enough), content (wrong focus area / missing something), or process (too structured / not structured enough)?
3. Identify any immediate adjustment that can be made.

**State updates**:
- Record in Meta-Check Log (Session, Candidate Feedback, Adjustment Made)
- If delivery feedback: consider adjusting Feedback Directness level in Profile
- If content feedback: evaluate against Active Coaching Strategy — does this warrant a pivot?
- Record in Coaching Notes if it reveals a preference coach should remember

**Output**:
```
Meta-feedback received: [Classification: delivery / content / process]

Feedback: "[What they said]"

Adjustment: [Immediate change being made, or explanation of why the current approach stands]

Going forward: [What will change based on this feedback]
```

---

## Design Principles

- **Capture first, analyze later**: `feedback` does capture; `analyze`, `progress`, and `prep` make it actionable. Don't over-analyze in moment — confirm what was captured and move on.
- **Flexible output**: No fixed schema. Confirmation adapts to input type — sometimes one line, sometimes paragraph. Match output weight to input weight.
- **Optional next step**: After capturing, suggest most natural next command if relevant. Don't force it.
- **Don't duplicate existing workflows**: If candidate starts full debrief during `feedback`, redirect: "This sounds like a full debrief — want to switch to `debrief` so we capture everything systematically?" Same for detailed corrections that become re-analysis — redirect to `analyze`.

## State Write Targets

- **Interview Intelligence**: Recruiter/Interviewer Feedback (Type A), Question Bank (Type D)
- **Outcome Log**: Outcome updates (Type B)
- **Interview Loops**: Round completions, next-round details, interviewer signals (Type B, Type D)
- **Company Patterns**: Company-specific observations (Type D)
- **Score History** or **Storybank**: If correction warrants assessment adjustment (Type C)
- **Calibration State → Scoring Drift Log**: If feedback contradicts coach scoring (Type A)
- **Meta-Check Log**: If coaching meta-feedback (Type E)
- **Coaching Notes**: If correction reveals pattern or if feedback reveals preference to remember (Type C, Type E)

## Recommended Next

**State-aware sequence** (only if relevant to captured data):

- Type A (recruiter feedback): Suggest `concerns` if feedback pointed to specific concern, or `progress` if 3+ outcomes now exist
- Type B (outcome — advanced): Suggest `prep [company]` for next round, or `hype` if within 48h
- Type B (outcome — rejected): At Level 5, extraction is complete in this session. At Levels 1-4, suggest `progress` later if 3+ outcomes exist
- Type B (outcome — at 3-outcome threshold): Mention `progress` is now available for full calibration analysis
- Type C (correction): Continue with original workflow unless correction triggers new direction
- Type D (post-session memory): Brief confirmation. Suggest `stories` if it's a story worth developing, or `practice` if question should be drilled
- Type E (coaching meta-feedback): Confirm adjustment. Continue with coaching.

**Alternatives**: `analyze`, `progress`, `concerns`, `prep [company]`, `practice`
