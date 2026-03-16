# reflect — Post-Search Retrospective and Archive

Close the loop on a coaching engagement through retrospective analysis. Run when candidate has accepted an offer, decided to pause search, or wants to assess impact of coaching after sustained effort.

## Input Requirements

- **From candidate**: Statement of closure (accepted offer / pausing search / taking stock)
- **From coaching_state.md**: All sections — Score History, Outcome Log, Storybank, Session Log, Interview Loops, Active Coaching Strategy, all other accumulated data

## State Files Needed

- `coaching_state.md` → ALL SECTIONS (this is a comprehensive review):
  - Score History (full journey: baseline to current)
  - Outcome Log (all interviews and outcomes)
  - Storybank (evolution of stories, strengths)
  - Session Log (list of sessions completed)
  - Interview Loops (companies interviewed)
  - Active Coaching Strategy (what was prioritized)
  - Storybank improvements over time
  - Coaching Notes (preferences, patterns, growth)
  - If applicable: Presentation Prep, Comp Strategy, LinkedIn Analysis, Resume Optimization, Positioning Statement

## Workflow

1. **Acknowledge the milestone**: Whether offer accepted, search paused, or extended effort completed, name it clearly. "You've been at this for [duration]. Let's look at the full arc." Candidate deserves recognition for work.

2. **Pull the full data** (review all of coaching_state.md):
   - Score History: baseline to current
   - Outcome Log: all interview results
   - Storybank: how stories evolved
   - Session Log: sessions completed
   - Interview Loops: companies progressed through
   - Active Coaching Strategy: priorities over time

3. **Narrate the journey** (not a progress report — a story of growth):
   - **Starting point**: Where did they begin? (kickoff baseline, initial storybank size, initial concerns, initial self-assessment)
   - **Breakthroughs**: What were 2-3 moments where something clicked? (Name what changed and when — inflection points from score history, stories that suddenly landed, realizations about themselves)
   - **Hard parts**: What was hardest to improve? (persistent patterns that never fully resolved, dimensions that plateaued, emotional or structural blocks)
   - **Genuine difference**: What's genuinely different about how they interview now vs. when they started? (not just "scores went up" — what changed about their approach, their thinking, their presence?)
   - **Self-assessment calibration**: Pull initial concerns and self-assessment from kickoff. Compare to most recent progress calibration. Show the delta: "You started thinking your biggest weakness was [X]. Turns out it was [Y]. Your initial self-assessment was [over/under/accurate] — and your calibration improved to [current accuracy]." This bookend comparison makes growth tangible.

4. **Extract transferable lessons** (goes beyond this job search):
   - Communication skills that transfer to the job itself
   - Self-awareness insights (self-assessment calibration patterns, blind spots identified)
   - Storytelling ability that helps in presentations, stakeholder management, etc.
   - Thinking under pressure
   - Self-direction and accountability

5. **If offer accepted**: What made the difference?
   - Which dimensions were strongest in interviews that advanced? (correlation data from progress, if exists)
   - Which stories landed hardest? (use Use Count and storybank notes)
   - What changed between early rejections and later advances? (pattern detection from Outcome Log, score history)
   - What were the turning points that led to this offer?

6. **If no offer received (or pausing search)**: Honest diagnosis without blame.
   - What are the remaining gaps? (dimension scores, storybank coverage)
   - Are gaps coachable with more practice, or do they suggest targeting adjustment? (targeting insights from progress)
   - What should they focus on if/when they resume? (specific next steps)
   - What did they learn that's still valuable?

7. **Archive and close**:
   - Mark coaching_state.md with `Status: Archived [date] — [reason: accepted offer / paused search / etc.]` at the top
   - Do NOT delete coaching_state.md — preserve it so candidate can reference later or resume
   - If candidate later runs `kickoff` again, coach can reference archived state: "I see you went through coaching before. Want to build on that foundation or start fresh?"

## Output Schema

```markdown
## Retrospective: [Candidate Name]'s Interview Journey

## The Arc
- Duration: [first session to now]
- Sessions completed: [count]
- Real interviews: [count]
- Outcomes: [__ offers / __ advances / __ rejections]
- Final result: [accepted offer at X / pausing search / continuing elsewhere]

## Where You Started
- Initial scores: [from first practice/analyze session]
- Initial storybank: [count, strength distribution e.g., "4 stories, 1 at strength 3, rest at 2"]
- Initial assessment: [from kickoff — what was the baseline?]
- Biggest concern at start: [what they worried about most]

## Where You Are Now
- Current scores: [most recent — each dimension]
- Storybank health: [count, strength distribution, earned secrets coverage]
- Overall change: [narrated, not just numbers — "Your Substance improved from 2.5 to 3.8 because you started including impact quantification..."]

## Breakthroughs
[The 2-3 moments where something clicked. Name what changed and when.]
1. [breakthrough with evidence/context]
2. [breakthrough with evidence/context]
3. [breakthrough with evidence/context]

## Persistent Challenges
[What remained hard throughout. Honest assessment of what didn't fully resolve.]
1. [challenge + whether it improved, plateaued, or stayed hard]
2. [challenge + context]

## What Made the Difference (if offer received)
- The dimensions that predicted your advances: [which scored highest in advancing interviews]
- The stories that landed: [which stories appear in Use Count data, which feedback called out]
- The change between early rounds and later rounds: [evidence of progression]
- The shift in how you showed up: [behavioral/mindset change reflected in interviews]

## What's Still Open (if no offer / pausing)
- Remaining gaps: [scored dimensions, storybank coverage]
- Honest diagnosis: [is this a skill gap or targeting issue? practice problem or something else?]
- If you resume, start here: [specific next steps — which dimensions, which stories, which companies to target]

## Transferable Skills
[What they built that goes beyond interviewing]
- Storytelling and communication: [specific skill built]
- Self-awareness and calibration: [what they learned about themselves]
- Thinking under pressure: [how their thinking evolved]
- [other relevant skills]:

## Self-Assessment Growth
- Started thinking: [initial kickoff self-assessment]
- Reality revealed: [what was actually the biggest gap vs. what they thought]
- Calibration improvement: [went from [over/under/accurate] to [current]]

## Storybank Snapshot (archived)
[Final state of storybank for future reference — count, strength distribution, earned secrets]

## Coaching State Archived
[Note that coaching_state.md is being preserved, not deleted — available if they resume]

**Recommended next**: `kickoff` — start a fresh coaching cycle if beginning a new search. **Alternatives**: `help` (explore other tools/workflows)
```

## State Write Targets

- **coaching_state.md header**: Add `Status: Archived [date] — [reason]`
- **coaching_state.md preserved**: Do NOT delete. Keep as reference for future resume.

## Recommended Next

**Primary**: If candidate is wrapping up → acknowledge completion. "Your coaching journey is archived. You can reference it anytime."

**If they're continuing to look**: `kickoff` — start fresh coaching cycle for next search phase

**Alternatives**: `help` — explore other tools or workflows if redirecting to different focus

## When to Trigger reflect

- Candidate reports accepting an offer
- Candidate says they're pausing or stopping their search
- 8+ sessions completed with no recent activity
- Candidate asks "what did I learn?" or "how did I do overall?"

## Coaching State Handling

**Preserve, don't delete**:
- Mark as archived with date: `Status: Archived [date] — [reason: accepted offer / paused search / etc.]`
- If candidate later runs `kickoff` again, reference archived state: "I see you went through coaching before. Want to build on that foundation or start fresh?"
- All data remains available for analysis and future reference
