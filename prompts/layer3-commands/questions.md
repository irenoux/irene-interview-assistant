# questions — Tailored Interview Questions

Generate 5 strategic questions to ask interviewers with clear intent, interviewer fit, and follow-up preparation.

## Purpose

Questions are strategic tools, not afterthoughts. Each question should serve at least one purpose:
- **Information gathering**: Surface something the candidate needs to know to evaluate the role
- **Concern mitigation**: Indirectly demonstrate a strength that addresses a known concern
- **Differentiation**: Show depth of thinking that makes the candidate memorable
- **Rapport building**: Connect with the interviewer's specific interests or background

## Input Requirements

- Optionally: stage specification (phone screen, hiring manager, final round, peer interview)
- If not specified, will ask for stage

## State Files Needed

- `coaching_state.md` — Load active Interview Loops (for company-specific round context), Effective Patterns from Interview Intelligence (to inform question style), Company Patterns (to calibrate to what this specific company values in candidate questions)

## Workflow

### Stage Detection (Priority Order)

1. If the user specified a stage in the command (e.g., `questions hiring manager`), use that.
2. If `coaching_state.md` has an active Interview Loop for a company with a known next round, use that stage.
3. If a `prep` brief was recently generated, infer from the format identified there.
4. If none of the above, ask: "What stage is this for? Phone screen, hiring manager, final round, or peer interview? The questions I generate will be very different depending on who you're talking to."

### Stage-Specific Question Guidance

- **Phone screen / recruiter call**: Focus on logistics, role clarity, and process. "What does success look like in the first 90 days?" Don't ask deep strategic questions — save those.
- **Hiring manager round**: Focus on team dynamics, priorities, and how they evaluate. "What's the biggest challenge the team is facing right now?"
- **Final round / exec**: Focus on company direction, strategic bets, and culture. "What's the most important thing this team needs to get right in the next year?"
- **Peer round**: Focus on collaboration, day-to-day, and honest experience. "What's something you wish you'd known before joining?"

### Intelligence-Informed Question Generation

If Interview Intelligence → Effective Patterns exists with 3+ data points, use it to inform question style. If the candidate's best interviews correlated with asking "how" questions (probing team process), weight toward that style. If Company Patterns shows what this specific company values in candidate questions, calibrate accordingly.

### Questions to Avoid

Flag these common mistakes:
- Questions easily answered by the company website or JD ("What does your company do?")
- Questions about benefits, perks, or time off in early rounds (signals wrong priorities)
- Questions that reveal insecurity ("Do you think I'm qualified for this role?")
- Questions so generic they could apply to any company ("What's the team culture like?")
- Questions that put the interviewer on the spot ("What's the worst thing about working here?")

## Output Schema

```markdown
## Questions To Ask Interviewers

1. **Question**: [The question, word-for-word]
   - **Strategic purpose**: [information / concern mitigation / differentiation / rapport]
   - **Best for**: [specific round or interviewer type]
   - **Why this is strong**: [explanation of why this question works]
   - **They might ask back**: [likely follow-up or reversal]
   - **Your prepared response**: [1-2 sentence answer ready to go]

2. **Question**: [...]
   - [same format for questions 2-5]

## Questions To Avoid This Round
- [1-2 specific questions the candidate might be tempted to ask, with brief explanation of why to skip them]

## Additional Notes
[If using Effective Patterns or Company Patterns data: brief reference to how the candidate's best interviews informed these questions]

**Recommended next**: `hype` — build your pre-interview confidence plan with these questions loaded. **Alternatives**: `prep [company]`, `mock [format]`
```

## State Write Targets

After generating questions, save the top 3 to `coaching_state.md`:
- **In Interview Loops** (if company-specific): Add `- Prepared questions: [top 3, one-line each]` under the relevant company entry.
- **Why**: `hype` generates its own "3 Questions To Ask" section. If `questions` has already been run for this interview, `hype` should pull from those (already tailored) rather than generating fresh ones. This prevents contradictory advice between commands.

## Recommended Next

State-aware recommendation:
- If interview is within 48 hours → `hype` (time-sensitive confidence boost)
- If interview is further out → `prep [company]` (if prep not yet run) or `mock [format]` (for practice)
- Default fallback → `hype`

Format: `**Recommended next**: `hype` — build your pre-interview confidence plan with these questions loaded. **Alternatives**: `prep [company]`, `mock [format]`
