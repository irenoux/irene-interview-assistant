# Debrief

Post-interview rapid capture workflow. Captures what happened in a real interview while fresh. Bridge between the real interview and `analyze`.

## Input Requirements

- Interview just completed (ideally within 1-2 hours)
- Company and round info
- Candidate's emotional state and impressions

## Optional Inputs

- Transcript or recording (if available)
- Specific questions or situations candidate wants to discuss

## State Files Needed

- `coaching_state.md` (if exists — for candidate profile, storybank, company context)

## Workflow

### Step 1: Emotional Check First

Before anything tactical, ask: "How are you feeling about it? One word."

This serves two purposes:
1. It surfaces emotional state that affects memory quality
2. It shows the coach cares about the person, not just the performance

Don't skip this.

### Step 2: Rapid Question Capture

"What questions did they ask? Don't worry about exact wording — just get them down."

Capture as many as they can remember. Prompt with format cues: "Was there a behavioral question? A 'tell me about a time' question? Anything unexpected?"

### Step 3: Per-Question Self-Assessment

For each question they remember: "How did you feel about your answer? Strong, okay, or rough?"

Don't score yet — capture their in-the-moment read.

### Step 4: Signal Reading

"Did you notice any signals from the interviewer? Follow-up questions that showed interest? Moments where they seemed to lose interest or redirect? Any body language that stood out?"

Capture these — they're high-value data even without a transcript.

**Signal Interpretation Guide** — Help the candidate read the signals they noticed:

| Signal | Likely Meaning | Confidence |
|---|---|---|
| Extended follow-ups on one topic | Genuine interest or evaluating depth — positive either way | HIGH |
| Interviewer moved on quickly after your answer | Your answer either fully satisfied them or didn't land — look at their energy after moving on | MEDIUM |
| "That's interesting" + follow-up | Usually positive — they want more | HIGH |
| Interviewer checked the time or clock | Running behind schedule, not necessarily boredom — but if repeated, you may be going long | MEDIUM |
| "Let me push back on that" | Testing conviction, not disagreeing — this is often a positive signal | HIGH |
| Interviewer started selling the role/company to you | Strong buy signal — they want you interested | HIGH |
| Short, closed-ended follow-ups | They may have already formed their assessment — neutral to negative | MEDIUM |
| "We'll be in touch" with no specifics | Standard — don't read into it either way | LOW |

**Caveat**: "These are common patterns, not certainties. Interviewers have different styles — some are naturally warm regardless of assessment, some are naturally terse even when impressed. Use these as directional signals, not verdicts."

See also the Signal-Reading Module in `references/cross-cutting.md` for the full positive/negative/neutral signal framework and cross-interview pattern detection.

### Step 5: Surprise Capture

"Was there anything you didn't expect? A question you weren't prepared for, a format difference, something about the interviewer or environment?"

Unexpected moments are often the most informative for coaching.

### Step 6: Story Usage Log

"Which stories did you use? Did any of them land differently than in practice?"

Cross-reference with storybank — update `Last Used` dates, increment `Use Count` for each story used, and add performance notes.

### Step 7: Immediate Tactical Notes

"Is there anything you want to do differently for the next round, based on this one?"

Capture their own coaching instinct.

### Step 8: Positioning Performance Check

"How did your introduction / 'tell me about yourself' land? Did the interviewer seem engaged, or did they jump to questions quickly?"

Capture this signal — it feeds back to `pitch` for positioning iteration. Record in Interview Intelligence → Effective/Ineffective Patterns if the response reveals something actionable about how the candidate's positioning lands.

### Step 9: Recruiter/Interviewer Feedback Capture

"Did you get any feedback from the recruiter about this round? Even informal comments — 'they really liked your background' or 'the interviewer had some concerns about X' — are valuable signal."

If feedback exists, record it for the Recruiter/Interviewer Feedback table in Interview Intelligence.

### Step 10: Past Question Similarity Check

Scan the Interview Intelligence Question Bank for questions similar to what the candidate recalled. If matches exist, note them briefly: "You've seen a prioritization question like Q2 before — at [Company] in Round [N]. Your score on that one was [X]."

Only surface matches that are useful (same competency tested, score trajectory, or company pattern). Don't force connections.

### Step 11: Transcript Availability Check

"Do you have a recording or transcript? If so, we can do a full `analyze` later. If not, I'll work from what you've captured here."

If they do have a transcript, mention the tool so they know they can paste raw output: "You can paste the raw transcript directly from Otter, Zoom, Grain, or whatever tool you used — I'll detect the format and clean it up automatically."

### Emotional Triage

Based on the emotional check in step 1, adapt:

- **Candidate feels good**: Proceed normally. Capture data. Offer `analyze` or `thankyou` as next steps.
- **Candidate feels terrible**: Don't jump to tactical feedback. Acknowledge it: "That sounds rough. Let's capture what happened while it's fresh — we can analyze it later when there's some distance." Focus on capture, not coaching. Offer `hype` if another interview is coming soon. Reference the Psychological Readiness Module's rejection reframe if needed.
- **Candidate is uncertain**: This is actually the most valuable state — they don't know how it went. Say: "Uncertainty is normal. Let's capture the data and see what it actually tells us."

## With vs. Without Transcript

**If transcript is available (or coming):**
- Save the debrief data to coaching state
- Tell the candidate: "Great — I have your impressions. When you're ready, run `analyze` with the transcript and I'll compare your read to what the data shows. The gap between how you felt and how it actually went is some of the most useful coaching data."
- The debrief becomes input to `analyze`, not a replacement for it

**If no transcript exists:**
- This debrief IS the data. Run a lighter version of analysis:
  - Score what you can from the candidate's recollection (flag lower confidence)
  - Focus on signal-reading data (interviewer behavior is easier to remember than exact words)
  - Identify which dimensions you can assess vs. which require a transcript
  - Say: "I'm working from your memory here, which means my confidence is lower than a transcript analysis. I can give you directional feedback, but I wouldn't hang precise scores on this."

## Output Schema

```markdown
## Interview Debrief: [Company] - [Round]
- Date: [date of interview]
- Interviewer(s): [names if known]
- Format: [behavioral screen / system design / etc.]
- Emotional read: [candidate's one-word + brief context]

## Questions Recalled
1. [Question as remembered]
   - Self-assessment: [strong / okay / rough]
   - Story used: [S### or none]
   - Notes: [any details about how it went]

2. [Question as remembered]
   - Self-assessment:
   - Story used:
   - Notes:

[...etc, all questions recalled]

## Interviewer Signals Observed
- Positive signals (interest, follow-ups, engagement): [specific behaviors noticed]
- Negative signals (redirects, loss of interest, clock-checking): [specific behaviors noticed]
- Neutral/ambiguous: [signals that were hard to read]

## Surprises
- [anything unexpected — questions, format, environment, interviewer behavior]

## Stories Used
| Story | Question | How It Landed (candidate read) |
|-------|----------|-------------------------------|
| S### | Q# | [strong / okay / rough] |

## Candidate's Own Takeaways
- What to do differently:
- What worked:

## Feedback Received
- Date: [when you got the feedback]
- Company: [company name]
- Source: [recruiter / interviewer / hiring manager / none]
- Feedback: [verbatim or close to it]
- Linked dimension: [if mappable to Substance / Credibility / etc.]

## Intelligence Notes
- Questions matched from past interviews: [any Question Bank matches, or "no prior data"]
- Company pattern observations: [anything learned about this company's interview approach]

## Transcript Status
- [ ] Transcript available → run `analyze` when ready
- [ ] No transcript → directional analysis above is what we have

**Recommended next**: `analyze` — run full transcript analysis while impressions are fresh (if transcript available). **Alternatives**: `thankyou`, `hype`, `progress`
```

## State Write Targets

Update `coaching_state.md` per the State Update Triggers:

- **Storybank updates**: Last Used dates, increment Use Count for each story used, performance notes
- **Interview Loop updates**: round completed, stories used, signals noted
- **Outcome Log**: add entry with Result: pending
- **Interview Intelligence updates**:
  - Recalled questions to Question Bank (marked "recall-only")
  - Recruiter/interviewer feedback to Recruiter/Interviewer Feedback table
  - Company Patterns if new observations emerged

## Recommended Next

**Recommended next**: `analyze` — run full transcript analysis while impressions are fresh (if transcript available). **Alternatives**: `thankyou`, `hype`, `progress`

---

## Mode Detection

- **"I just finished an interview" + no transcript yet** → Route to `debrief`
- **"I just had an interview" + candidate wants to process it** → Route to `debrief`
- **Transcript provided same-day without debrief first** → Could run `debrief` first for impressions, then `analyze`, or go straight to `analyze`

## Multi-Step Intent

"I just finished my interview at [company]" → `debrief` (same day) → `analyze` (when transcript ready) → `progress` (if 3+ outcomes)
