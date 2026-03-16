# thankyou — Thank-You & Follow-Up Draft Generation

Generate personalized thank-you messages for interviewers, with timing guidance and interview-specific callbacks.

## Input Requirements

- **From candidate**: Interview just completed, interviewer name(s), any specific moments or exchanges to reference
- **From coaching_state.md**: Interview Loops entry for company (stories used, signals observed), Interviewer Intelligence (if interviewer was researched)

## State Files Needed

- `coaching_state.md` → Interview Loops (company context, stories used, round info, interviewer names)
- `coaching_state.md` → Interview Intelligence (interviewer profiles, if researched)
- `coaching_state.md` → Storybank (to reference stories that landed well)

## Workflow

1. **Load coaching state context**. Pull Interview Loops entry for the company: what round they're in, what stories were used, what signals came through. Pull any recruiter/interviewer intel from Interview Intelligence if the interviewer was researched during `prep`.

2. **Timing advisory** (upfront, before drafting):
   - Same day (2-4 hours): Standard best practice. Shows enthusiasm without desperation.
   - Next morning: Acceptable if interview was late in day. Can feel more thoughtful.
   - Never later than 24 hours: After that, the window has closed.
   - If no response by expected timeline: Wait 1-2 business days past stated timeline, then send brief check-in. Don't follow up more than twice.

3. **Multi-interviewer routing**: If the candidate met multiple interviewers in the same round:
   - Ask: "Who did you meet with? What stood out from each conversation?"
   - Generate separate drafts for each person (don't send identical notes — interviewers compare)
   - Each note should reference something specific to that interviewer's questions or conversation
   - Vary the tone slightly while keeping core message similar

4. **Callback material extraction** (one question at a time):
   - Ask: "What was a specific moment or exchange that stood out?"
   - If no strong specific moment, ask: "Did the interviewer share anything about their own background or experience?" or "Was there a particular question that got interesting?"
   - Pull from analyze/mock data if available: "Looking at question 3 in your transcript..."
   - Pull from debrief notes: story that landed well, interviewer's own experience they shared
   - Keep it brief — one specific callback per note, not a recap of the entire interview

5. **Draft generation** (one draft per interviewer):
   - Opening: Lead with genuine gratitude + timing-appropriate enthusiasm
   - Callback: One specific moment from the conversation. Reference by topic or exchange, not the full story. Example: "I especially enjoyed our discussion about how you approach data governance challenges — that's where I've built most of my expertise."
   - Credibility reinforcement (optional, if relevant): One sentence on why their question stuck or how it confirmed fit
   - Close: Natural, not effusive. "Looking forward to next steps" if advancing, "would love to stay in touch" if awaiting outcome
   - Length: Under 120 words

6. **Tone variants** (if candidate requests): Generate alternate tone if appropriate — more formal for enterprise, conversational for startup, technical for engineer interviewers

7. **Rejection pathway** (if candidate wants to ask): Generate 2-3 learning questions they could ask recruiter if rejected (not accusatory, genuinely curious)

8. **Advancement reinforcement** (if advancing): Generate 2-3 talking points they carried strongest from this round that they should lean into next round

## Output Schema

```markdown
## Timing
- Recommended send time: [within X hours of interview end]
- Follow-up if no response by: [date based on stated timeline]

## Thank-You Draft: [Interviewer Name] (<120 words)
[draft with specific interview callback — direct paste-ready]

## Thank-You Draft: [Interviewer 2 Name] (if applicable, <120 words)
[draft with different callback from this interviewer's specific conversation]

## Alternate Tone (optional)
[if requested — e.g., more formal, more technical]

## If Rejected: Learning Questions
1. [question to ask recruiter — genuine curiosity, not accusatory]
2. [another angle on what might have affected fit]

## If Advancing: Reinforcement Points
1. [dimension/story that landed strongest with this interviewer — double down next round]
2. [specific exchange that showed strong fit — reference again if relevant]
3. [question or topic the interviewer owned vs. just asked — you now know what they care about]

**Recommended next**: `debrief` — capture interview impressions while fresh (if not already done). **Alternatives**: `analyze` (if transcript available), `prep [company]` (for next round), `progress`
```

## State Write Targets

- **Interview Loops**: Update under the company entry → round completed date
- **Application Tracker**: If entry exists for this company, note thank-you sent
- No state write required if thank-you is standalone (state updates happen at `debrief` or `analyze`)

## Recommended Next

**State-aware next step**:
- If this was the final interview round and an offer may be coming → suggest `negotiate` (prepare in case)
- If next round is scheduled → suggest `prep [company]` (prepare for next round)
- If debrief wasn't captured → suggest `debrief` (capture interview data while fresh)
- Otherwise → `progress` (track advancement, if applicable)

**Alternatives**: `analyze` (if transcript available), `concerns` (if advancing but want to anticipate next round objections), `questions` (to prepare questions for next round)
