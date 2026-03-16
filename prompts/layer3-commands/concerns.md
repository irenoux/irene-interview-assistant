# Concerns

Concern anticipation and counter-strategy development. Identifies likely interviewer concerns and builds multi-layered counter-narratives.

## Input Requirements

- Company and role context (ideally — from prep or coaching state)
- Candidate's anticipated concerns (ask first)

## Optional Inputs

- Resume (for gap analysis)
- Storybank (for evidence-backed counters)
- Prep data (for role-specific concerns)

## State Files Needed

- `coaching_state.md` (if exists — for candidate profile, resume analysis, storybank, interview history)
- Resume Analysis (from kickoff)
- Storybank (for counter-evidence)
- Interview Loops (for past round analysis)
- Outcome Log (for past rejection patterns)

## Workflow

### Step 1: Ask Candidate What Concerns They Expect

"What concerns do you expect an interviewer might have about your background or fit for this role?"

Wait for their response. Validate correct concerns and add any they missed.

### Step 2: Generate Concerns from Real Data

Don't work in a vacuum. Pull from:

1. **Resume analysis** (from kickoff): career gaps, short tenures, domain switches, seniority mismatches
2. **Storybank gaps** (from storybank or gap analysis): competencies with no strong story
3. **Previous analyze results** (from transcript analyses): patterns and weak dimensions that appeared in real interviews
4. **The specific role/company** (from prep or JD): does the JD require something the candidate lacks?
5. **Career narrative gaps**: transitions that need explaining
6. **Outcome Log** (if real interview outcomes exist): Use past rejections as counter-evidence for current concerns. If the candidate was previously rejected for "not enough leadership experience" but has since advanced at two other companies on leadership questions, that outcome data weakens this concern. Conversely, if the same concern has driven 2+ rejections, it's confirmed — escalate its severity.

### Step 3: Rank by Severity

Not all concerns are equal. Assign each one:

- **Dealbreaker**: This could single-handedly end the candidacy if not addressed well (e.g., missing a core required skill, a very short recent tenure that looks like termination)
- **Significant**: Will come up and needs a strong counter, but won't kill the candidacy alone (e.g., no direct industry experience, a slightly junior background)
- **Minor**: Might come up as a probe but unlikely to be decisive (e.g., a 2-year-old role change, a less prestigious school)

### Step 4: Attach Multi-Layered Counter Strategies

For each significant+ concern, provide **multiple framings**:

1. **The direct question**: How to answer if asked head-on. Example: "Why did you leave after 8 months?" → Direct answer with honest context.

2. **The subtle probe**: How to handle when they're really asking about the concern but phrasing it differently. Example: "Tell me about a time things didn't work out" → Use a story that preemptively addresses the short tenure concern.

3. **The follow-up challenge**: How to handle "But wouldn't that be a risk in this role too?" after your initial counter. Example: "Yes, but here's what's different about this situation..."

For minor concerns, provide a one-liner counter that's confident but not defensive.

### Step 5: Identify Best Stories

For each concern, identify which story (if any) from the storybank provides the strongest counter-evidence. If no story exists, flag it for `stories add`.

### Step 6: Immediate Practice Option

After generating concerns, offer to drill the top concern right now:

"Your biggest concern is [X]. Want to practice handling it? I'll throw the direct question, then the subtle probe version, and we'll see how you do."

If they accept, run a mini pushback drill (2-3 rounds) focused on the top 1-2 concerns:
- Round 1: Direct question version
- Round 2: Subtle probe version
- Round 3: Follow-up challenge after their counter

Score each round and add to Score History in `coaching_state.md` (Type: practice). Update Session Log with the concern-focused drill.

## Output Schema

```markdown
## Likely Interviewer Concerns (ranked by severity)

### Dealbreakers
1. Concern: [what they might worry about]
   Severity: Dealbreaker
   Source: [resume / storybank gap / JD mismatch / outcome log / etc.]
   Counter (direct question): [how to answer if asked head-on]
   Counter (subtle probe): [how to address if it comes up indirectly]
   Counter (follow-up challenge): [how to handle pushback on your counter]
   Best story: [S### or "no story — need to add"]
   Confidence in counter: [High / Medium / Low]

2. [repeat for each dealbreaker concern]

### Significant
1. Concern: [what they might worry about]
   Severity: Significant
   Source: [source]
   Counter (direct question): [answer]
   Counter (subtle probe): [answer]
   Counter (follow-up challenge): [answer]
   Best story: [S### or "no story — need to add"]
   Confidence in counter: [High / Medium / Low]

2. [repeat for each significant concern]

### Minor
1. Concern: [what they might worry about]
   Severity: Minor
   Source: [source]
   Counter (one-liner): [quick, confident response]

2. [repeat for each minor concern]

## Recommendations
- Dealbreaker concerns: [focus coaching recommendation if weak counters]
- Storybank gaps: [any new stories needed to support counters]
- Practice priority: [which concerns to drill first]

**Recommended next**: `practice pushback` — drill your top concern under pressure. **Alternatives**: `prep [company]`, `mock [format]`
```

## State Write Targets

After generating, save the ranked concerns to `coaching_state.md`:

- **Interview Loops** (company-specific): Under the relevant company's Concerns surfaced field, add the full ranked concern list
- **Active Coaching Strategy** (if general concerns): Add top concerns to the strategy if they represent systemic bottlenecks

This allows:
- `prep` to pull from previously generated concerns instead of re-deriving them
- `hype` to reference the top concern + counter in the 3x3 plan
- `progress` to track whether concerns are being addressed over time
- `mock` to include questions targeting known concerns

## Recommended Next

**Recommended next**: `practice pushback` — drill your top concern under pressure. **Alternatives**: `prep [company]`, `mock [format]`, `stories add` (if storybank gaps identified)

---

## Mode Detection

- **`concerns [company]` explicit command** → Execute for that company
- **`concerns` with no company specified** → Ask for company, or run for all target companies
- **"What concerns will they have?"** → Route to `concerns`
- **After `prep` completes** → Suggest `concerns` as next step

## Multi-Step Intent

"Prepare me for my interview at [company]" → `research` → `prep` → `concerns` → `practice pushback` (on top concern) → `hype` (if ≤48h)
