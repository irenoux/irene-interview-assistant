# pitch — Core Positioning Statement

Build the candidate's atomic unit of self-presentation: a positioning statement that distills who they are into a compelling, memorable core. The positioning statement is saved to coaching state and consumed by resume, linkedin, and outreach for cross-surface consistency.

## Purpose

Create a compelling, memorable positioning statement (30-45 seconds) that works as an atomic unit across "tell me about yourself," networking, recruiter calls, and LinkedIn headlines.

## Input Requirements

- Target role context (from coaching_state.md Profile, or ask)
- Candidate background (from Resume Analysis + Storybank, or ask through guided conversation)

## Optional Inputs

- Depth level: Quick Draft / Standard / Deep Positioning (default: Standard)
- Specific context to optimize for (e.g., "networking event Thursday")
- Existing pitch attempt (for critique + rewrite)

## State Files Needed

- `coaching_state.md` — Load Profile (target role, seniority), Resume Analysis (positioning strengths, career narrative gaps), Storybank (earned secrets from stories rated 3+, narrative identity themes), Active Coaching Strategy (if Differentiation is gap, pitch addresses it directly), LinkedIn Analysis (current headline/about — for consistency check), Resume Optimization (current summary — for consistency check), Interview Intelligence Effective/Ineffective Patterns (if positioning-related feedback exists from real interviews)

## Workflow

### Priority Check

Before running full positioning exercise:
- If no `kickoff` has been run: Soft gate — "I can build your positioning statement, but without your target role context I'll be working from conversation alone instead of your full profile. Want to run `kickoff` first, or proceed and we'll work with what we have?"
- If the candidate has an interview within 48 hours: Redirect — "You have an interview in [X] hours. Let's focus on `hype` / `prep` first. Come back to `pitch` after — it's a foundational exercise, not an emergency one."
- If storybank is empty but kickoff exists: Proceed with resume analysis data, note the limitation — "Your storybank is empty, so I can't anchor the positioning to earned secrets from your stories. I'll work from your resume analysis data. After this, consider running `stories` — earned secrets make the positioning much stronger."

### How Pitches Actually Work (Reference Knowledge)

**The 10-20-30 Rule**: 10 seconds to earn 20 more. 30 seconds earns the conversation. Most candidates start with credentials — but credentials don't create curiosity.

**The Curiosity Gap (Loewenstein)**: People pay attention when a gap opens between what they know and what they want to know. "I help growth-stage companies stop losing their best engineers" creates a gap. "I'm a VP of Engineering with 15 years of experience" closes it.

**Neural Coupling**: Stories synchronize brains. 63% remember stories; 5% remember statistics. A pitch with a micro-story activates narrative processing.

**Primacy Effect**: First sentence becomes the lens. 100ms to form a judgment.

**Present-Past-Future Formula**: For "tell me about yourself" — present (what you do now), past (relevant experience), future (why this role).

**Hook-Context-Ask**: For networking — hook that creates curiosity, context that establishes credibility, ask that gives the listener a way to help.

**Context-Specific Durations**: Elevator 15-30s, networking 30-45s, career fair 30-60s, interview TMAY 60-90s, LinkedIn above-fold ~300 chars.

**Consistency Multiplier**: Consistent messaging across platforms = 33% more reliable to recruiters, 45% higher response rates.

### Step 1: Context Assembly

Pull from coaching_state.md:
- Profile (target role, seniority band)
- Resume Analysis (positioning strengths, career narrative gaps)
- Storybank (earned secrets from stories rated 3+, narrative identity themes)
- Active Coaching Strategy (if Differentiation is the gap, pitch addresses it directly)
- LinkedIn Analysis (current headline/about — for consistency check)
- Resume Optimization (current summary — for consistency check)
- Positioning performance data (if `debrief` or `analyze` have notes on how positioning landed in real interviews): Check Interview Intelligence → Effective/Ineffective Patterns for signals about how the candidate's self-introduction landed. Use this to refine positioning.

### Step 2: Raw Material Extraction

Guided conversation, one question at a time:
1. The differentiator question: "What do you do that other [target role] candidates at your level don't?" If storybank earned secrets exist, offer as starting points.
2. The audience question: "Who needs to hear this pitch, and what do they care about?"
3. The 'so what' question: "If someone heard your pitch and thought 'so what?' — what would make them change their mind?"

If existing pitch provided, skip to Step 3.

### Step 3: Existing Pitch Diagnostic (if existing pitch provided)

Score on 5 dimensions (1-5):
- **Hook strength**: Does the opening create curiosity?
- **Differentiation**: Could another candidate say this?
- **Specificity**: Concrete details or vague claims?
- **Audience fit**: Optimized for the intended listener?
- **Memorability**: Would they remember this an hour later?

Diagnose primary weakness, feed into rewrite.

### Step 4: Core Positioning Statement Construction

Three layers:
- **Layer 1 — The Hook** (10s): One sentence, curiosity gap. Test: would they want to hear more?
- **Layer 2 — The Context** (adds 10-20s): Evidence the hook is real. Micro-story, metric, or earned secret.
- **Layer 3 — The Bridge** (adds 10-20s): Connects to specific context (role, company, opportunity).

Present to candidate. Ask: "Does this sound like you?" Iterate. Must sound like the candidate, not the coach.

### Step 5: Context Variants (5 variants)

1. **Interview TMAY** (60-90s): Present-Past-Future. Must survive TMAY evaluation criteria: communication clarity, narrative coherence, role relevance, self-awareness, energy.
2. **Networking Event** (30-45s): Hook-Context-Ask. Ends with question, not monologue.
3. **Recruiter Call** (30-60s): Keyword-aware, signals seniority, clear "what I'm looking for."
4. **Career Fair** (30-60s): High-energy, leads with strongest credential, memorable phrase.
5. **LinkedIn Summary Hook** (~300 chars): Above-fold, keywords + curiosity gap. Written for reading, not speaking.

### Step 6: Positioning Consistency Check (Standard + Deep)

Cross-reference against:
- Resume summary (if Resume Optimization exists)
- LinkedIn headline/about (if LinkedIn Analysis exists)
- Interview narrative (if narrative identity exists)

Don't just flag gaps — provide the specific language change for each surface. Example: "Your resume summary leads with 'experienced product manager.' Your positioning hook is 'I help growth-stage teams ship 3x faster by killing the right features.' The resume summary should echo the positioning — here's a rewrite: [specific rewrite]."

### Step 7: Differentiation Audit (Deep only)

- **Is the differentiator defensible?** Evidence from storybank/resume — not just a claim.
- **Spiky enough?** Apply Spiky POV test — does it make some people disagree?
- **Earned vs. borrowed?** Based on direct experience, or something learned from a podcast/book?
- **Substitution test**: Replace the candidate's name with another candidate at their level. Does the positioning still work? If yes, it's not differentiated enough.
- **Constraint ladder**: Same positioning at 15s, 30s, 60s, 90s. What stays at every level = the irreducible core.

### Step 8: Challenge Protocol (Deep, Level 5 only)

Lenses 1, 2, 4, 5 (Pre-Mortem omitted — doesn't apply to a positioning artifact):
- **Assumption Audit**: What must be true for this positioning to land? (e.g., "Assumes hiring managers in your target space care about shipping speed more than process maturity.")
- **Blind Spot Scan**: What can't the candidate see about how they present? (e.g., "You think you come across as strategic. From the outside, your pitch sounds tactical.")
- **Devil's Advocate**: If a hiring manager heard this and was looking for reasons to pass... (e.g., "Sounds like a builder, not a leader. Where's the people dimension?")
- **Strengthening Path**: Single highest-leverage change.

## Output Schema — Quick Draft

```markdown
## Positioning Statement — Quick Draft

## Core Statement (30-45s)
[The full hook + context + bridge]

## Hook (10s)
[The curiosity-gap opener alone]

## Key Differentiator
[One sentence]

## Context Variants

### Interview TMAY (60-90s)
[Present-Past-Future format]

### [Requested Context] ([duration])
[Variant optimized for the specific context the candidate asked about]

**Recommended next**: `pitch` (Standard) — get all 5 context variants and a positioning consistency check. **Alternatives**: `stories`, `prep [company]`
```

## Output Schema — Standard

```markdown
## Positioning Statement: [Name]

## Core Statement (30-45s)
[The full hook + context + bridge]

## Hook (10s)
[The curiosity-gap opener alone]

## Key Differentiator
[One sentence]

## Earned Secret Anchor
[The earned secret or spiky POV powering the positioning — from storybank if available]

## Pitch Diagnostic (if existing pitch was provided)
| Dimension | Score (1-5) | Notes |
|---|---|---|
| Hook strength | | |
| Differentiation | | |
| Specificity | | |
| Audience fit | | |
| Memorability | | |
- Primary weakness: [diagnosis]

## Context Variants

### 1. Interview TMAY (60-90s)
[Present-Past-Future format. Designed to survive TMAY evaluation criteria.]

### 2. Networking Event (30-45s)
[Hook-Context-Ask. Ends with a question.]

### 3. Recruiter Call (30-60s)
[Keyword-aware, seniority-signaling, clear "what I'm looking for."]

### 4. Career Fair (30-60s)
[High-energy, leads with strongest credential, memorable phrase.]

### 5. LinkedIn Summary Hook (~300 chars)
[Above-fold, keywords + curiosity gap. Written for reading.]

## Positioning Consistency Check
- Resume summary: [aligned / misaligned — specific fix if needed]
- LinkedIn headline/about: [aligned / misaligned — specific fix if needed]
- Interview narrative: [aligned / misaligned — specific fix if needed]

**Recommended next**: `[command]` — [reason]. **Alternatives**: `[command]`, `[command]`
```

## Output Schema — Deep Positioning

```markdown
## Positioning Statement — Deep Positioning: [Name]

## Core Statement (30-45s)
[The full hook + context + bridge]

## Hook (10s)
[The curiosity-gap opener alone]

## Key Differentiator
[One sentence]

## Earned Secret Anchor
[The earned secret or spiky POV powering the positioning]

## Pitch Diagnostic (if existing pitch was provided)
[same as Standard]

## Context Variants
[all 5 variants — same as Standard]

## Constraint Ladder
| Duration | Version | What Stays |
|---|---|---|
| 15s | [compressed to one sentence] | |
| 30s | [hook + context] | |
| 60s | [hook + context + bridge] | |
| 90s | [full TMAY version] | |
- **Irreducible core**: [the element that stays at every duration — this is the positioning's essence]

## Differentiation Audit
- Defensible? [yes/no — evidence]
- Spiky enough? [Spiky POV test result]
- Earned vs. borrowed? [assessment]
- Substitution test: [pass/fail — explanation]

## Positioning Consistency Check
- Resume summary: [aligned / misaligned — specific fix]
- LinkedIn headline/about: [aligned / misaligned — specific fix]
- Interview narrative: [aligned / misaligned — specific fix]

## Cross-Surface Coherence
[Assessment of how all candidate surfaces work together — do they tell one story or three?]

## Challenge (Level 5 only)
- Assumptions this positioning rests on: [2-3]
- Blind spots: [what you can't see about how you present]
- Devil's advocate: [strongest case for a hiring manager to tune out]
- Highest-leverage fix: [the one thing that changes the positioning's impact]

## Priority Moves (ordered)
1. [highest-impact change]
2. [second]
3. [third]

**Recommended next**: `[command]` — [reason]. **Alternatives**: `[command]`, `[command]`
```

## State Write Targets

After running `pitch`, save to coaching_state.md:

```markdown
## Positioning Statement
- Date: [date]
- Depth: [Quick Draft / Standard / Deep Positioning]
- Core statement: [the full hook + context + bridge — 30-45 second version]
- Hook (10s): [the curiosity-gap opener alone]
- Key differentiator: [one sentence]
- Earned secret anchor: [the earned secret or spiky POV powering the positioning]
- Target audience: [primary audience this was optimized for]
- Variant status: [which variants were produced]
- Consistency status: [aligned / gaps identified — brief summary]
```

## Recommended Next

State-aware recommendation:
- If interview within 48 hours → `hype` (positioning anchors confidence)
- If no Positioning Statement before → default to `pitch` for foundation building
- If LinkedIn/Resume need updates → guide to `resume`/`linkedin` after pitch is complete
- If no Storybank → suggest `stories` (earned secrets strengthen pitch)
- If networking focus → `outreach` (positioning seeds outreach messages)
