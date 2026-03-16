# Stories

Storybank management and narrative identity development. Build, improve, and optimize stories for interview deployment.

## Input Requirements

- Story action (view, add, improve, find gaps, retire, drill, narrative identity)
- For add/improve: Story content or guided discovery responses
- Optional: Target role/company context (for gap prioritization)

## State Files Needed

- `coaching_state.md` (for storybank, target roles, competency needs)

## Workflow

### Step 1: Show Storybank Menu

Display the menu:

```
Storybank Menu
1) View           — See all indexed stories
2) Add            — Build a new story
3) Improve        — Strengthen an existing story
4) Find gaps      — Identify missing competencies
5) Retire/archive — Remove or deprioritize stories
6) Drill          — Rapid-fire retrieval practice
7) Narrative identity — Extract career themes and narrative arc
```

### Step 2: Route to Selected Action

#### Action: Add (Guided Discovery)

Don't jump straight to STAR format. Most people can't produce stories on command. Use guided exploration prompts to surface stories first, *then* structure them.

1. Ask one reflective prompt at a time. Wait for the response.
2. Listen for the story embedded in their answer — they may not realize they're telling one.
3. When you hear a promising story, say: "That's a strong story. Let's capture it." Then walk through STAR.

**Reflective Prompts** (from `references/storybank-guide.md`):
- Peak experiences: "Tell me about a time when you felt like you were at your best professionally. What made you proud?"
- Challenge/growth: "When have you had to learn something quickly, or adapt to a situation you weren't prepared for?"
- Impact/influence: "Tell me about a time when you influenced a decision or outcome. What did you do, and what was the result?"
- Failure/learning: "Tell me about a time something didn't go the way you planned. What did you learn?"

After STAR, extract the **earned secret** (see `references/differentiation.md` for extraction protocol).

Index it in the storybank table.

**CRITICAL**: When adding a story, write the **full STAR text** to the Story Details section in `coaching_state.md` — not just the index row in the Storybank table. The table is a quick-reference index. The Story Details section is where the actual story lives, including Situation, Task, Action, Result, Earned Secret, deploy use-case, and version history. Without the full text, the coach can't help improve the story in a future session without asking the candidate to retell it from scratch.

#### Action: Improve (Structured Upgrade Protocol)

Don't just say "add more specifics." Walk through a diagnostic sequence:

1. **Read the current story aloud** (or have the candidate deliver it). Score it on 5 dimensions. Identify which dimensions are dragging it down.

2. **Diagnose the gap type:**
   - **Score 1-2 → Missing raw material.** Ask: "What's missing from this story that you remember but haven't included?" and "What was actually hard about this situation?" Often the candidate stripped the tension out.
   - **Score 3 → Good bones, missing proof.** Target: quantified impact, alternatives considered, or earned secret. Ask: "What numbers could you attach to this?" and "What other approaches did you consider before this one?"
   - **Score 4 → Strong, missing differentiation.** Target: earned secret and spiky POV. Ask: "What do you know from this experience that most people in your role wouldn't know?" and "What would surprise someone who wasn't there?"

3. **Apply the specific fix.** Don't do a full rewrite — make the minimum change that moves the score up. Show the before/after for the specific section that changed.

4. **Re-score after the improvement.** Show the candidate what moved and why.

5. **Update the storybank record** with new strength score and version note.

#### Action: Find Gaps (Prioritized Gap Analysis)

Don't just list missing competencies — rank them by how much they matter for this candidate's target roles:

1. Cross-reference the candidate's target roles/companies (from `coaching_state.md`) with the storybank's skill coverage. **Check both Primary and Secondary Skills** — a competency may be covered as a secondary skill in an existing story, which changes the gap from "no story" to "workable coverage".

2. For each gap, assess: **Critical** (this competency will definitely be tested and no story exists, even as secondary skill), **Important** (likely to come up, only weak stories or secondary-skill-only coverage available), **Nice-to-have** (might come up, but won't make or break the interview).

3. For critical gaps, check: can an existing story be reframed to cover this competency (using its secondary skill or an adjacent experience), or does the candidate need to surface a new experience entirely?

4. Prescribe gap-handling patterns from the Gap-Handling Module in `references/cross-cutting.md` for any competencies where no real story exists. Use the Pattern Selection by Storybank Score table: strength 2 → Adjacent Bridge, strength 1 → Reframe to Strength or Growth Narrative, no story → Hypothetical with Self-Awareness.

5. **Cross-reference with active prep briefs**: If the candidate has active prep briefs (from `prep`), check predicted questions against gaps. A gap that maps to a predicted question at a current target company is elevated to Critical.

6. **Consume narrative identity output** (if `stories narrative identity` has been run): Use the candidate's core themes and sharpest edge to inform gap prioritization. Gaps in the candidate's dominant themes are more damaging than gaps in peripheral areas.

A PM interviewing at Stripe with no "influence without authority" story has a critical gap. The same candidate missing a "technical depth" story has a nice-to-have gap. Rank accordingly.

#### Action: Retire/Archive

When the candidate selects "Retire," assess which stories are candidates for removal:

- **Story with strength < 2 that has been attempted twice and not improved**: Suggest retiring and replacing with a new story.
- **Story that keeps scoring below 3 in real interviews** (check Outcome Log and Interview Intelligence): Flag it as ineffective and suggest retiring.
- **Orphan story that doesn't connect to narrative identity** (if narrative identity has been extracted): Suggest retiring or reframing through the theme lens.

#### Action: Drill (Rapid-Retrieval Practice)

See the `practice retrieval` protocol in the Practice command file. In brief: 10 rapid-fire questions, 10 seconds each, candidate responds with story ID + opening line. Also available via `practice retrieval`.

#### Action: Narrative Identity (Theme Extraction)

Requires 5+ stories in the storybank. If fewer exist, redirect: "Narrative identity works best with 5+ stories to find patterns across. You have [N]. Want to add a few more first?"

**Analysis Protocol:**

1. Read every story's full STAR text, earned secret, and deploy use-case from `coaching_state.md`.

2. Cluster stories by **underlying theme** — not surface skill. Surface skills are things like "leadership" or "communication." Themes are specific patterns like "building systems where none existed," "translating between worlds that don't naturally talk to each other," or "making unpopular bets that paid off." If the theme could describe a generic candidate, go deeper.

3. Identify **2-3 dominant themes.** Most candidates have 2. Three is rare and usually means one is weak.

4. Name the **sharpest edge** — the theme that is most distinctive to this candidate, hardest to replicate, and most likely to make an interviewer remember them.

5. Flag **orphan stories** — stories that don't connect to any theme. These dilute the narrative and may be retirement candidates.

6. Flag **fragile themes** — themes with only 1 story supporting them. One story is an anecdote; two or more is a pattern.

7. Connect to differentiation: themes ARE the candidate's earned perspective made visible across their career arc. A strong narrative identity is how a candidate scores 4-5 on Differentiation consistently — not by forcing earned secrets into individual answers, but by having every answer reinforce the same coherent thesis.

### Step 3: Story Strength Audit (when 8+ stories exist)

Periodically run a portfolio-level audit (suggest during `progress` when storybank health shows issues):

- **Distribution check**: Are all stories from the same job? Same domain? Same skill? Flag clustering. For portfolio-level gaps, flag in coaching notes.
- **Strength curve**: How many at 4+? How many below 3? A healthy storybank has at least 60% at 4+.
- **Earned secret coverage**: How many stories have a real earned secret vs. a placeholder? Stories without earned secrets are incomplete.
- **Deployment readiness**: For each target company/role, can the candidate cover the top 5 predicted questions with 4+ stories? If not, which gaps need new stories vs. improved existing ones?
- **Retirement candidates**: Any story below 3 for more than 2 improvement attempts? Suggest retiring and replacing.

### Step 4: Story Versioning

When improving a story, preserve the previous version in the Story Details section:

- In the Version history field, add: "[date] — [brief description of what changed]"
- Update the STAR text in Story Details with the improved version
- This serves two purposes: (1) the candidate can see their progress over time, and (2) if the "improved" version stops landing in interviews, the coach can reference what changed and potentially revert.

### Step 5: Story Red Team (Level 5 only)

After `stories add` or `stories improve`, run all 5 Challenge Protocol lenses against the story:

1. **Assumption Audit**: What must be true for this story to land? What interviewer framework is it assuming?
2. **Blind Spot Scan**: What's invisible to the candidate about their own story? What context do they take for granted?
3. **Pre-Mortem**: How does this story fail in a real interview? Where does it lose attention or raise doubt?
4. **Devil's Advocate**: Where does a skeptical interviewer attack? What follow-up questions expose weaknesses?
5. **Strengthening Path**: One specific change that makes it airtight.

At Levels 1-4: Skip. The standard improve diagnostic is sufficient.

### Step 6: Force Specificity on All Stories

When adding or improving stories, force specificity on:

- **Candidate-specific contribution** (not "we" — what did *you* do?)
- **Quantified impact** (or explicit non-quant reason)
- **Tradeoff/constraint detail**
- **Earned secret extraction and validation** (see `references/differentiation.md`)
- **One-line deploy use-case**

## Output Schema

**After `stories view`:**
```markdown
## Your Storybank
[Table of all indexed stories with columns: ID, Title, Primary Skill, Secondary Skill, Strength (1-5), Use Count, Last Used, Earned Secret (brief)]

[If narrative identity exists, show the core themes here too]

**Recommended next**: `stories improve S###` (improve your weakest story) or `stories find gaps` (identify gaps for your target role)
```

**After `stories add`:**
```markdown
## Story Added: [Title]
- ID: S###
- Primary Skill: [competency]
- Secondary Skill: [competency if applicable]
- Earned Secret: [the key insight from this story]
- Strength: [1-5 — initial scoring]
- Deploy for: [one-line use case]

[Full STAR text below]
- Situation: [context]
- Task: [your responsibility]
- Action: [what you did]
- Result: [what happened]
- Earned Secret: [what you learned that most people wouldn't]

## Story Red Team (Level 5 only)
- Assumption: [what must be true for this to land]
- Blind spot: [what you can't see about your own story]
- Failure mode: [how this fails in a real interview]
- Attack surface: [where a skeptic probes]
- Fix: [one change that makes it airtight]

**Recommended next**: `stories improve S###` — strengthen the story based on the red team findings. **Alternatives**: `stories find gaps`, `practice retrieval`, `concerns`
```

**After `stories improve`:**
```markdown
## Story Improved: [Title] (S###)
- Previous strength: __ → New strength: __
- What changed: [brief description of the edit]
- Version history updated

[Show before/after excerpt with annotations]

## Story Red Team (Level 5 only)
- [same as after add]

**Recommended next**: `practice` — test the improved story under pressure. **Alternatives**: `stories view`, `stories improve S###`, `analyze`
```

**After `stories find gaps`:**
```markdown
## Storybank Gap Analysis

### Critical Gaps (must fill for target roles)
1. [competency] — No story exists. Recommended: [surface new story / reframe existing S###]
   Gap-handling pattern if asked before a story exists: [Pattern 1-4 from Gap-Handling Module]

### Important Gaps (likely to come up)
1. [competency] — Only weak story (S###, strength __). Recommended: [improve / replace]

### Nice-to-Have (might come up)
1. [competency]

**Recommended next**: `stories add` — fill the highest-priority gap. **Alternatives**: `practice gap`, `prep [company]`
```

**After `stories narrative identity`:**
```markdown
## Your Narrative Identity

### Core Themes
1. **[Theme]** — [one-line description of the pattern]. Stories: S###, S###, S###
2. **[Theme]** — [one-line description]. Stories: S###, S###
3. **[Theme]** — [one-line description]. Stories: S### (fragile — only 1 story)

### Your Sharpest Edge
[Which theme is most distinctive to you — the one an interviewer would remember. How many of your stories currently leverage it vs. how many could. This is your highest-leverage positioning move.]

### Theme Coverage
- Stories reinforcing a theme: __ of __
- Orphan stories (no clear theme connection): [list with S### IDs — consider retiring or reframing]
- Fragile themes (only 1 story): [list — need reinforcement]

### How To Use This
- **In answers**: [Specific advice on connecting answers back to core themes without being heavy-handed]
- **In questions you ask**: [How to ask questions that reinforce your themes]
- **In positioning**: [How themes inform your "why this role / why this company" narrative]

**Recommended next**: `stories improve S###` — strengthen your sharpest-edge stories. **Alternatives**: `stories add`, `practice`, `prep [company]`
```

## State Write Targets

After completing stories actions, update `coaching_state.md`:

- **Storybank table**: Add/update rows with story metadata (ID, Title, Primary Skill, Secondary Skill, Strength, Use Count, Last Used, Earned Secret)
- **Story Details section**: Add full STAR text for each new or improved story
- **Session Log**: Note which stories were added/improved/retired
- **Coaching Notes**: Any relevant observations about narrative identity or story development patterns

## Recommended Next

**Recommended next**: `stories improve S###` (strengthen the story) or `practice retrieval` (test retrieval skills). **Alternatives**: `stories add`, `practice`, `prep [company]`

---

## Mode Detection

- **`stories [action]` explicit command** → Execute the specified action
- **`stories` with no action specified** → Show the menu
- **"I want to build my story bank"** → Route to `stories add`
- **"Help me improve my stories"** → Route to `stories improve` or `stories find gaps`

## Multi-Step Intent

"I'm starting my job search" → `kickoff` → `stories add` (build 5+ core stories) → `stories find gaps` (identify needs for target roles) → `prep [company]`
