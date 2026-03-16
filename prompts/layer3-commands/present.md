# present — Presentation Round Coaching

Coach the structure, timing, and Q&A preparation for presentation rounds (system design, portfolio review, strategy presentation, technical deep dive, 90-day plans, case presentations, etc.).

## Purpose

Build and optimize presentation structure, timing, opening/closing, and Q&A preparation. Coaching boundaries: structure, narrative, timing, audience calibration, Q&A strategy. NOT visual design, technical correctness (beyond framework rigor), or vocal delivery.

## Input Requirements

- Presentation context: What's the topic/prompt? Who's the audience? What's the time limit? What format expectations did the company share?
- Presentation content: Whatever they have (nothing yet, outline, slides content, talk track text)

## Optional Inputs

- Depth level: Quick Structure / Standard / Deep Prep (default: Standard)
- Specific concerns (e.g., "I always run over time," "I don't know how to start," "I'm worried about Q&A")
- Talk track text (for timing analysis and clarity review)
- Company/role context (for audience calibration — or pulled from coaching_state.md)

## State Files Needed

- `coaching_state.md` — Load Profile (target role, seniority), Interview Loops (company/role/format details), Prep Brief (if prep was run — evaluation criteria, culture, interviewer intel), Storybank (supporting stories to incorporate)

## Workflow

### Priority Check

- If no `kickoff`: Soft gate — "I can help structure your presentation, but without your target role context I can't calibrate for your audience. Run `kickoff` first, or tell me about the audience and I'll work with what we have."
- If interview within 48 hours AND this is the presentation round: This IS the priority. Proceed immediately.
- If interview within 48 hours but the presentation round is NOT next: "You have a [format] round in [X] hours. Want to focus on `hype`/`prep` for that first and come back to presentation prep?"
- If Prep Brief exists for this company: Use it (evaluation criteria, culture, interviewer intel feed into audience calibration and Q&A prediction).

### How Presentation Rounds Actually Work (Reference Knowledge)

**Format Prevalence**: Presentation rounds appear across seniority levels and functions:
- Senior+ engineering: system design presentations, architecture reviews, tech deep dives
- Product management: product sense, business case, strategy presentations
- Design: portfolio reviews, design critiques
- Data science: analysis presentations, methodology reviews
- Executive roles: strategic vision, 90-day plans, board-style presentations
- Consulting: case presentations
- Pre-sales/solutions engineering: technical demos, solution presentations

**What Evaluators Actually Assess**:
1. Communication clarity — Can they explain complex ideas simply? Do they calibrate to the audience?
2. Structured thinking — Does the presentation have a logical arc? Can you follow the reasoning?
3. Audience calibration — Did they pitch at the right level?
4. Time management — Did they stay within bounds? Going over time is the #1 presentation failure mode.
5. Depth vs. breadth judgment — Do they know when to go deep and when to stay high-level?
6. Q&A handling — Can they think on their feet? Do they admit what they don't know? Do they redirect constructively?
7. Confidence and poise — Not arrogance, but comfort with the material and the format.

**Narrative Arc Frameworks**:
- **Situation-Complication-Resolution** (SCR) — Most versatile. Present the context, introduce the tension, deliver the resolution. Works for most technical and business presentations.
- **Problem-Approach-Results-Learnings** (PARL) — Best for technical/analytical presentations. Shows methodology and rigor.
- **Context-Challenge-Options-Recommendation** (CCOR) — Best for business case and strategy presentations. Shows decision-making process.
- **Hook-Build-Deliver-Land** (HBDL) — Best for executive audiences. Start with the punchline, build the evidence, close with the ask.

**Time Estimation**: ~130-150 words per minute for a well-paced spoken presentation. A 15-minute presentation = ~2000-2250 words of talk track. A 10-minute presentation = ~1300-1500 words. Most candidates over-prepare content and under-prepare delivery. The #1 timing failure is spending too long on context/setup and rushing through insights/results.

**Slide-Count Heuristic**: Plan ~1-2 minutes per content slide (excluding title, divider, and closing slides). A 15-minute presentation = 8-12 content slides. A 10-minute presentation = 5-8 content slides. Slides with dense data or complex diagrams take longer — budget 2-3 minutes for those.

**Q&A Dynamics**:
- Q&A is often weighted MORE heavily than the presentation itself — it tests real understanding vs. rehearsed content.
- Common Q&A patterns: "Tell me more about X" (positive — genuine interest), "What about Y?" (they think you missed something important), "How did you decide Z?" (testing your process), "What would you do differently?" (testing self-awareness), "What if [constraint changed]?" (testing adaptability).
- Best Q&A answers: concise (30-60 seconds), acknowledge the question, answer directly, then bridge to evidence.
- "I don't know, but here's how I'd find out" is always better than a fabricated answer.

**Time Allocation Guidelines**:
- Context/setup: 10-15% of presentation time
- Core content: 40-55% of presentation time
- Conclusion/recommendation: 10-15% of presentation time
- Q&A buffer: 25-40% of TOTAL time (this is where most candidates under-allocate)

**Common Presentation Mistakes**:
1. Starting with background/context instead of the punchline
2. Too much content for the time allotted
3. Not leaving enough time for Q&A
4. Reading from slides instead of presenting
5. No clear "so what" — what should the audience do with this information?
6. Not anticipating objections or alternative approaches
7. Spending too long on context, too little on insight and results
8. Not practicing transitions
9. Uniform depth across all sections

### Coaching Boundaries

**What the coach CAN evaluate** (text-in/text-out):
- Narrative structure and logical flow
- Content density vs. time allocation
- Opening and closing effectiveness
- Q&A preparation completeness
- Audience calibration (based on described audience)
- Transition quality
- Talk track clarity (if provided)
- Argument strength and evidence quality

**What the coach CANNOT evaluate**:
- Visual design quality (cannot see slides)
- Domain-specific technical correctness
- Body language, vocal delivery, eye contact, stage presence
- Actual slide readability or data visualization quality

State this boundary explicitly at the start: "I'll coach the structure, narrative, timing, and Q&A preparation. I can't evaluate your visual design or the technical correctness of your domain content. For those, get feedback from a domain peer."

### Step 1: Context Assembly

Pull from coaching_state.md: Profile (target role, seniority), Interview Loops (company/role/format details), Prep Brief (if prep was run), Storybank (supporting stories to incorporate).

Gather from candidate (one question at a time):
1. What's the presentation topic/prompt? (exact wording if they have it)
2. Who's the audience? (seniority level, function, number of people, decision-makers vs. peers)
3. Time limit? (total time including Q&A — if company specified a split, capture that)
4. What have you prepared so far? (nothing / rough ideas / outline / full slides / talk track)
5. Any specific guidance from the company about format or expectations?

### Presentation-Type Content Patterns

Different presentation types have distinct content expectations:

| Presentation Type | Core Content Expectation | Common Trap | Key Differentiator |
|---|---|---|---|
| **System Design / Architecture Review** | Problem → constraints → approach → tradeoffs → results | Jumping to the solution without establishing constraints | Showing tradeoff reasoning |
| **Business Case / Strategy** | Market context → problem framing → options considered → recommendation → expected impact | Presenting only the chosen path without showing alternatives considered | Decision-making process visibility |
| **Portfolio Review (Design)** | Project context → design challenge → process → iteration → outcome + learnings | Showing only final designs without the messy middle | The iteration story |
| **Data / Analysis Presentation** | Question → methodology → findings → "so what" → recommendations | Over-explaining methodology at the expense of insights | The "so what" |
| **90-Day / Strategic Vision** | Current state assessment → vision → priorities → how you'd sequence → how you'd measure | Being too abstract or too granular — missing the strategic sweet spot | Showing you understand the org's current reality |
| **Technical Deep Dive** | Problem → approach → implementation details → results → what you'd do differently | Going so deep that the audience loses the thread | Calibrating depth to audience |
| **Case Presentation (Consulting)** | Situation → framework → analysis → recommendation → risks + mitigations | Framework overload | Synthesizing to a recommendation |

Apply the relevant type pattern when structuring content.

### Step 2: Framework Selection

Based on presentation type + audience, recommend one of the 4 narrative arc frameworks:
- Technical/analytical audience → Problem-Approach-Results-Learnings (PARL)
- Business case/strategy → Context-Challenge-Options-Recommendation (CCOR)
- Executive audience → Hook-Build-Deliver-Land (HBDL)
- General/flexible/mixed audience → Situation-Complication-Resolution (SCR)

Explain WHY this framework fits this specific presentation. If the candidate already has a structure, assess it against the recommended framework — adapt their existing work rather than replacing it wholesale.

### Step 3: Content Structuring

For each section of the presentation:
- What belongs in this section (content guidance specific to their topic)
- Time allocation (minutes + percentage of total)
- What to cut FIRST if over time (priority ranking)
- Transition to next section (exact transition language draft)

Apply the time allocation guidelines:
- Context/setup: 10-15% of presentation time
- Core content: 40-55%
- Conclusion/recommendation: 10-15%
- Q&A: 25-40% of TOTAL time

Flag misallocations explicitly: "You're spending 40% of your time on context. Your audience already knows this. Cut to 10% and give that time to your analysis."

### Step 4: Opening & Closing Optimization

The first 30 seconds and last 30 seconds are the highest-leverage moments.

**Opening** must accomplish 3 things in <30 seconds:
- Establish why this matters to THIS audience (not generic importance)
- Create a reason to keep listening (curiosity gap, surprising finding, counterintuitive conclusion)
- Signal the structure ("I'll cover X, Y, Z — then we'll have time for questions")

Provide 2 opening options with rationale for each. Let the candidate choose what sounds like them.

**Closing** must accomplish 3 things:
- Synthesize the key insight (not a summary of everything — THE insight)
- State the recommendation or conclusion directly
- Land with energy (the closing sets the tone for Q&A — end strong, not trailing off)

Provide a closing draft.

### Step 5: Q&A Preparation

Predict 10 likely questions based on:
- Content gaps (what the candidate chose NOT to cover)
- Controversial choices (assumptions, tradeoffs, recommendations)
- Depth probes (areas covered at high level)
- "What about..." questions (adjacent topics, edge cases, competitive alternatives)
- Process questions ("How did you approach this?", "What data informed this?")
- Stress tests ("What if [constraint changed]?", "How does this scale?")

For each predicted question:
| # | Question | Why They'll Ask | Answer Strategy (key points, not a script) | If You Don't Know |

Also provide general Q&A principles:
- Pause before answering (2-3 seconds shows confidence, not hesitation)
- Answer the question asked (don't pivot to a prepared talking point)
- Keep answers to 30-60 seconds unless asked to elaborate
- "Great question" is a crutch — just answer
- "I don't know, but here's how I'd figure it out" is always valid

### Step 6: Timing Calibration

If talk track provided: word count ÷ 140 (conservative wpm) = estimated presentation time. Add 10% for natural pauses.
If outline only: estimate based on section count × expected depth.

Assessment:
- Over time? Flag which sections to cut and by how much.
- Under time? Flag where to add depth (usually core content, not context).
- Q&A time adequate? If presentation fills >75% of total time, Q&A is squeezed — restructure.

For Deep Prep: create constraint versions:
- 5-minute version: what survives?
- 10-minute version: what survives?
- 15-minute version: what survives?
- Irreducible core: the 3-5 sentences that must survive at ANY length.

### Step 7: Challenge Protocol (Deep Prep, Level 5 only)

Lenses 1, 2, 4, 5 (Pre-Mortem replaced with devil's advocate Q&A):
- **Assumption Audit**: What must be true for this presentation to land with this audience?
- **Blind Spot Scan**: What can't you see about your own presentation? (common: underestimating audience knowledge, overestimating interest in your process)
- **Devil's Advocate**: If an audience member was looking for reasons to be unconvinced...
- **Strengthening Path**: The single change that most improves the presentation.

## Output Schema — Quick Structure

```markdown
## Presentation Framework: [Topic]

## Recommended Approach
- **Framework**: [name] — [why it fits this presentation and audience]
- **Total time**: [X min presentation + Y min Q&A]

## Outline
### [Section 1: e.g., "The Problem"] — [X min, Y%]
- Key point: [what to cover]
- Transition → next section: [draft transition]

### [Section 2] — [X min, Y%]
...

### Q&A — [X min, Y%]

## Opening (first 30 seconds)
[Draft opening with rationale]

## Top 3 Pitfalls to Avoid
1. [specific to this presentation type and audience]
2. [specific to this topic/format]
3. [specific to common mistakes at this seniority level]

**Recommended next**: `present` (Standard) with your content for full coaching. **Alternatives**: `prep [company]`, `practice`
```

## Output Schema — Standard

```markdown
## Presentation Coaching: [Topic]

## Context
- Audience: [who — seniority, function, decision-making power]
- Time: [X min presentation + Y min Q&A]
- Framework: [selected — with rationale]

## Structural Analysis
- Current structure: [assessment of what works and what doesn't]
- Recommended structure: [section-by-section with time allocation]

## Content Density
- Estimated duration: [at 130 wpm / at 150 wpm]
- Assessment: [over / under / well-calibrated for time limit]
- Cut list: [what to remove if over time, priority order]
- Deepen list: [what's missing or thin, if under time]

## Opening (first 30 seconds)
### Option A
[Draft with rationale]
### Option B
[Alternative with rationale]

## Closing (last 30 seconds)
[Draft with rationale]

## Transitions
[Section → section transition language for each major transition]

## Audience Calibration
- Currently pitched at: [level — too technical / too high-level / well-calibrated]
- Audience needs: [what this audience cares about, based on their seniority and function]
- Adjustments: [specific changes to match audience]

## Q&A Preparation
| # | Question | Why They'll Ask | Answer Strategy | If You Don't Know |
|---|---|---|---|---|
| 1 | ... | ... | ... | ... |

## Timing Assessment
- Estimated duration: [X min at 130 wpm / Y min at 150 wpm]
- Q&A time: [adequate / tight / insufficient]
- Recommendation: [specific adjustments]

**Recommended next**: Practice delivering with a timer. Or `present` (Deep Prep) for final polish. **Alternatives**: `hype` (before the round), `prep [company]`
```

## Output Schema — Deep Prep

```markdown
## Presentation Deep Prep: [Topic]

[All Standard sections, expanded]

## Talk Track Review [if provided]
- Clarity: [section-by-section assessment]
- Jargon check: [terms that need explanation for this audience]
- Filler/hedge language: [specific instances to remove]
- Strongest passages: [what to keep exactly as-is — and why]
- Weakest passages: [specific rewrites]

## Constraint Versions
### 5-Minute Version
[What stays, what goes, modified structure]

### 10-Minute Version
[What stays, what goes, modified structure]

### 15-Minute Version
[What stays, what goes, modified structure]

### Irreducible Core
[The 3-5 sentences that survive at ANY length. This is the presentation's DNA.]

## Devil's Advocate Q&A
[5 hardest possible questions with detailed answer strategies]

## Challenge (Level 5 only)
- **Assumptions**: [what must be true for this to land]
- **Blind spots**: [what you can't see about your own presentation]
- **Devil's advocate**: [strongest case that this falls flat]
- **Highest-leverage fix**: [the one change that improves everything]

## Priority Moves (ordered)
1. [highest-impact change — do this first]
2. [second]
3. [third]

**Recommended next**: Practice delivering with a timer. Then `hype` before the actual round. **Alternatives**: `mock` (for Q&A simulation), `prep [company]`
```

## State Write Targets

Save to coaching_state.md as a top-level section (matching the schema in SKILL.md). Include the company name in the section header when company-specific:

```markdown
## Presentation Prep: [Topic / Company]
- Date: [date]
- Depth: [Quick Structure / Standard / Deep Prep]
- Framework: [selected narrative arc]
- Time target: [X min presentation + Y min Q&A]
- Content status: [outline only / full content / talk track reviewed]
- Top predicted questions: [top 3]
- Key adjustment: [the single biggest change recommended]
```

## Recommended Next

State-aware recommendation:
- If interview within 48 hours → `hype` (final boost before the round)
- If interview 1-7 days away → `mock` (Q&A simulation) or continue refining
- If interview further out → `prep [company]` (if not yet run) or other company prep
- Default → `hype` (before the actual presentation)
