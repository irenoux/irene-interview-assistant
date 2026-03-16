# decode — JD Analysis + Batch Triage

Analyze job descriptions using 6 decoding lenses (repetition frequency, order & emphasis, required vs. nice-to-have, verb choices, between-the-lines signals, what's missing) with confidence labeling. Fit assessment against profile. Batch triage for multiple JDs.

## Purpose

Understand what a JD actually signals about the role, assess fit, predict likely questions, and prioritize across multiple JDs.

## Input Requirements

- At least one JD (pasted text or key details)
- For batch triage: 2-5 JDs

## Optional Inputs

- Depth level: Quick Scan / Standard / Deep Decode (default: Standard)
- Specific questions about the JD
- Target priority (is this a top target or early-stage exploration?)

## State Files Needed

- `coaching_state.md` — Load Profile (target role, seniority band), Resume Analysis (skills, experience, positioning strengths), Storybank (skills coverage), Positioning Statement (key differentiator), Interview Loops (is this company already in progress?), JD Analyses (previous decodes for pattern comparison)

## Workflow

### Priority Check

- If no `kickoff`: Soft gate — "I can decode the JD's language and structure, but without your profile I can't assess fit. Run `kickoff` first for a fit assessment, or proceed with a general decode?"
- If interview within 48 hours: Redirect to `hype`/`prep`.
- If JD Analysis already exists for this company+role: Show the existing decode and ask if the JD has changed. Don't re-decode unchanged JDs.

### How JDs Actually Work (Reference Knowledge)

**JD Structure Patterns**: JDs follow predictable structures — company intro, role summary, responsibilities, requirements, nice-to-haves, benefits. But the signal isn't in the structure, it's in the language.

**Signal Density by Section**:
- Requirements = screening criteria. What gets you through the door.
- Responsibilities = what the role actually does. Often more honest than requirements.
- Nice-to-haves = the ideal candidate profile. What "Strong Hire" looks like beyond baseline.
- Company intro = culture signals and positioning.
- Benefits = comp philosophy signals.

**The 6 Decoding Lenses**:

1. **Repetition frequency** — Count how often key themes appear. If "cross-functional collaboration" appears 3 times, it is a primary evaluation criterion. Most repeated = most important.

2. **Order and emphasis** — What's listed first in responsibilities/requirements? First = highest priority. The first 3 bullets typically reflect the top 3 evaluation criteria.

3. **Required vs. nice-to-have** — Required = screening criteria that filter before a human looks. Nice-to-have = what differentiates "Hire" from "Strong Hire."

4. **Verb choices** — "Own" vs. "support" vs. "contribute to" signal autonomy and scope. "Own end-to-end" is a fundamentally different job from "contribute to team efforts." "Drive" vs. "execute" signals strategy vs. implementation.

5. **Between-the-lines signals** — Euphemisms decoded. "Fast-paced environment" = likely understaffed or rapid change. "Comfortable with ambiguity" = undefined role or early-stage. "Stakeholder management" = political environment. "Wear many hats" = no clear role boundaries. These are interpretations, not facts — confidence-label accordingly.

6. **What's missing** — Absence is information. A PM JD that doesn't mention data/analytics signals team maturity (or lack of PM influence on data). An engineering JD that doesn't mention testing may indicate culture.

**What JDs Don't Tell You** (honest limitations):
- Actual day-to-day work (JDs describe the ideal, not the reality)
- Team dynamics, manager quality, internal politics
- Whether the role is backfill vs. new headcount
- Whether the req is actually open vs. evergreen posting
- Real comp range (unless required by jurisdiction or voluntarily disclosed)
- Internal candidate preference
- Hiring timeline urgency

**Batch Triage Research**:
- Average job search involves 100-200 applications. Hit rate is 2-8%.
- Time per application: 30-90 minutes.
- Improving triage accuracy by 20% saves 20-40 hours of application effort.
- Signal: candidates who apply to Strong Fit roles have materially better outcomes.

### Confidence Labeling System

Every interpretation gets a confidence label. This is non-negotiable.

| Label | Meaning | Example |
|---|---|---|
| **HIGH** | Directly stated in JD, standard industry meaning | "5+ years of Python required" → HIGH |
| **MEDIUM** | Reasonable inference from language patterns or industry norms | "Cross-functional leadership" repeated 3x → MEDIUM |
| **LOW** | Interpretation of ambiguous language, euphemism decoding | "Fast-paced environment" → LOW |
| **UNKNOWN** | Cannot determine from JD alone | Team size, reporting structure, actual day-to-day → UNKNOWN |

**Rule**: Every LOW and UNKNOWN interpretation MUST be paired with a specific recruiter verification question. The candidate should never walk away believing a LOW-confidence interpretation is fact.

### Step 1: JD Intake

Accept JD in any format — full posting, bullet-point paste, screenshot description, even "here's roughly what the JD says." Parse into sections (responsibilities, requirements, nice-to-haves, etc.). If sections aren't clearly labeled, infer from content. Flag if the JD is unusually short (may be incomplete) or unusually long (may be a kitchen-sink posting).

### Step 2: Context Assembly

Pull from coaching_state.md: Profile (target role, seniority band), Resume Analysis (skills, experience, positioning strengths), Storybank (skills coverage), Positioning Statement (key differentiator), Interview Loops (is this company already in progress?), JD Analyses (previous decodes for pattern comparison).

### Step 3: 6-Lens Decode

Apply all 6 decoding lenses. For each finding:
- State the finding
- Assign confidence label (HIGH/MEDIUM/LOW/UNKNOWN)
- Provide evidence (what in the JD supports this)
- For MEDIUM/LOW/UNKNOWN: provide the recruiter verification question

Group findings by lens in Standard/Deep output. In Quick Scan, surface only the top 3 highest-signal findings.

For Lens 5 (between-the-lines signals), use the "decode + verify" pattern:
- State the euphemism or signal
- Provide the most likely interpretation
- Label confidence (almost always LOW or MEDIUM)
- Provide the verification question: what to ask, why it matters, how to ask it naturally

For Lens 6 (what's missing), explicitly state what the absence might mean AND what it might not mean. Absence is ambiguous — don't present a single interpretation as truth.

### Step 4: Competency Extraction

Extract top 5-7 competencies in priority order. For each:
- The competency (specific, not vague)
- Source section(s) (where in the JD it appears)
- Confidence level
- Repetition count (how many times it appears across sections)
- Type: Screening (required, filters in/out) or Differentiating (nice-to-have, separates Hire from Strong Hire)

### Step 5: Fit Assessment (if Profile exists)

Map extracted competencies against candidate profile. For each competency:
- **Match**: Direct evidence from resume/storybank (cite specific evidence)
- **Partial**: Adjacent experience, frameable with narrative (explain the bridge)
- **Gap**: No evidence, structural gap (name it honestly)
- **Unknown**: Can't assess without more information from candidate

Produce fit verdict using the Role-Fit Assessment from cross-cutting.md (5 dimensions: Requirement Coverage, Seniority Alignment, Domain Relevance, Competency Overlap, Trajectory Coherence). Classify gaps as Frameable (narrative can bridge) or Structural (real limitation).

Verdict: **Strong Fit / Investable Stretch / Long-Shot Stretch / Weak Fit**

For Long-Shot Stretch and Weak Fit: be honest. "This JD targets [X], and your profile shows [Y]. You could apply, but you should know the gap is structural, not just a framing issue."

### Step 6: Recruiter Verification Questions

Compile all MEDIUM, LOW, and UNKNOWN confidence interpretations into a prioritized list of questions to ask the recruiter. For each:
- What you want to verify
- Why it matters for your decision/preparation
- How to ask it naturally (not "your JD said X, what does that mean?" but "Can you tell me more about [topic]?")

Order by impact on the apply/don't-apply decision.

### Step 7: Batch Triage (if multiple JDs provided)

For each JD: run Steps 1-6 individually (can be abbreviated for Quick Scan depth).

Then produce comparative analysis:
- **Rank by fit** (highest fit first, with evidence for each)
- **Overlapping competencies** across JDs — this reveals the candidate's market-validated sweet spot
- **Divergent requirements** — where JDs pull in different directions, signaling scope decisions the candidate needs to make
- **Allocation recommendation**: which to pursue first, which to skip, which to research more. Honest about skips.
- **Target profile synthesis** — what these JDs collectively reveal about what the market wants from someone like the candidate

### Teaching Layer

This is what differentiates decode from prep's JD parsing. Quick Scan includes a lighter version (a single "Decode Tip" — one teaching insight per scan, rotating through the 6 lenses). Standard and Deep include the full "Learn to Read This Yourself" section:
- **Pattern spotted**: A specific decoding insight from THIS JD that the candidate can apply to future JDs
- **Trap to watch for**: A common misread THIS JD exemplifies
- **Self-decode prompt**: A question the candidate should ask themselves when reading the NEXT JD

## Output Schema — Quick Scan

```markdown
## JD Quick Scan: [Company] — [Role]

## Top 5 Competencies (priority order)
| # | Competency | Confidence | Type | Source |
|---|---|---|---|---|
| 1 | ... | HIGH/MEDIUM | Screening/Differentiating | [section, repetition count] |

## Key Signals
- [Signal 1] — [Confidence] — [what it means]
- [Signal 2] — [Confidence] — [what it means]
- [Signal 3] — [Confidence] — [what it means]

## Fit Verdict [if Profile exists]
[Strong Fit / Investable Stretch / Long-Shot Stretch / Weak Fit] — [1-line evidence]
- Strongest match: [competency + evidence]
- Biggest gap: [competency + gap type]

## Verify With Recruiter
1. [Question — for the highest-impact LOW/UNKNOWN item]
2. [Question — second priority]

## Decode Tip
[One teaching insight from this JD]

**Recommended next**: `decode` (Standard) for full analysis. **Alternatives**: `prep [company]`, `research [company]`
```

## Output Schema — Standard

```markdown
## JD Decode: [Company] — [Role]

## Decode Summary
- Role type: [what this role actually is — in plain language]
- Seniority signal: [what level this targets — with evidence and confidence]
- Team signal: [what the JD reveals about the team — with confidence]
- JD quality: [well-written / kitchen-sink / sparse / standard — what that implies]

## Competency Map (priority order)
| # | Competency | Confidence | Type | Repetition | Source |
|---|---|---|---|---|---|
| 1 | ... | HIGH | Screening | 3x | Requirements, Responsibilities |

## 6-Lens Analysis

### Lens 1: Repetition Frequency
[Findings with counts. What's repeated most = what they care about most.]

### Lens 2: Order & Emphasis
[Findings. What's listed first = highest priority.]

### Lens 3: Required vs. Nice-to-Have
[Findings. What's actually screening vs. differentiating.]

### Lens 4: Verb Choices
[Findings. Scope and autonomy signals.]

### Lens 5: Between the Lines
| Signal | Likely Meaning | Confidence | Verify |
|---|---|---|---|
| [euphemism] | [interpretation] | LOW/MEDIUM | [question to ask] |

### Lens 6: What's Missing
[Findings. What absence tells you — with alternative explanations.]

## Fit Assessment [if Profile exists]
- **Verdict**: [Strong Fit / Investable Stretch / Long-Shot Stretch / Weak Fit]
| Competency | Match | Evidence |
|---|---|---|
| [competency 1] | Match/Partial/Gap | [specific evidence or gap description] |
- **Frameable gaps** (narrative can bridge): [list with bridge strategy]
- **Structural gaps** (real limitations): [list — honest]

## Question Prediction Seeds
Based on top competencies and identified gaps:
- [Likely question 1 — from competency 1]
- [Likely question 2 — from competency 2]
- [Likely question 3 — from identified gap]

## Verify With Recruiter (priority order)
1. [Question — what you're verifying — how to ask naturally]
2. [Question]
3. [Question]

## Learn to Read This Yourself
- **Pattern spotted**: [teaching point from this specific JD]
- **Trap to watch for**: [common misread this JD exemplifies]
- **Next time, try**: [self-decode prompt for future JDs]

**Recommended next**: `prep [company]` for full interview preparation. **Alternatives**: `research [company]`, `decode` (batch triage with more JDs)
```

## Output Schema — Deep Decode

```markdown
## JD Deep Decode: [Company] — [Role]

[All Standard sections, expanded]

## Seniority Calibration
- JD states: [what level language the JD uses]
- JD signals: [what level the scope, verbs, and requirements actually target — with evidence]
- Assessment: [aligned / JD over-titles / JD under-titles] — [Confidence]
- Implication for candidate: [what this means for their application/positioning]

## Team Maturity Signals
[What the JD reveals about the team's stage: process maturity, tech stack age, org structure, growth rate — all with confidence labels. Multiple interpretations where ambiguous.]

## JD Structural Analysis
- Quality: [well-written / boilerplate / kitchen-sink / internally contradictory]
- What quality reveals: [a well-written JD suggests a thoughtful hiring process; a kitchen-sink JD may indicate unclear role definition]
- Red flags: [if any — internal contradictions, impossible combinations, unrealistic requirements]

## Challenge (Level 5 only)
- **Assumptions this decode rests on**: [2-3 assumptions with what would change if they're wrong]
- **Blind spots**: [what we fundamentally can't see from a JD alone]
- **Devil's advocate**: [strongest case that this decode is wrong]
- **Highest-leverage verification**: [the single question that would most change the analysis]

## Priority Moves (ordered)
1. [highest-impact action — verify, apply, research more, skip]
2. [second]
3. [third]

**Recommended next**: `prep [company]` for full interview preparation. **Alternatives**: `research [company]`, `practice` (targeted drills on gap competencies)
```

## Output Schema — Batch Triage (appended after individual decodes)

```markdown
## Batch Triage: [N] Roles

## Ranking
| Rank | Company | Role | Fit | Strongest Match | Biggest Gap | Recommendation |
|---|---|---|---|---|---|---|
| 1 | ... | ... | Strong | [competency] | [gap or none] | Pursue |
| 2 | ... | ... | Investable Stretch | [competency] | [gap] | Pursue with positioning |
| 3 | ... | ... | Long-Shot Stretch | [competency] | [gap] | Skip unless referral |

## Your Sweet Spot
[Competencies that appear across multiple JDs — this is what the market values in you. Ordered by frequency across JDs.]

## Divergence
[Requirements that pull in different directions — reveals a scope decision the candidate needs to make.]

## Allocation Recommendation
- **Pursue first**: [which roles, why — highest fit + highest priority]
- **Pursue with targeted prep**: [which roles, what specific gap to address]
- **Research more before deciding**: [which roles, what's missing]
- **Skip or deprioritize**: [which roles, why — honest about structural gaps]

## Your Market Profile
[What these JDs collectively reveal about what the market wants from someone like the candidate. This is career intelligence, not just job-search tactics.]

**Recommended next**: `research [top-ranked company]` or `prep [top-ranked company]`. **Alternatives**: `decode` with more JDs, `resume` (JD-targeted optimization for top target)
```

## State Write Targets

Save to coaching_state.md (one entry per JD — multiple can exist):

```markdown
## JD Analysis: [Company] — [Role]
- Date: [date]
- Depth: [Quick Scan / Standard / Deep Decode]
- Fit verdict: [Strong Fit / Investable Stretch / Long-Shot Stretch / Weak Fit]
- Top competencies: [top 3 in priority order]
- Frameable gaps: [list]
- Structural gaps: [list]
- Unverified assumptions: [count of LOW/UNKNOWN confidence items]
- Batch triage rank: [if part of batch — rank/total]
```

## Recommended Next

State-aware recommendation:
- If interview within 48 hours AND fit is Strong/Investable Stretch → `prep [company]`
- If interview within 48 hours AND fit is Long-Shot Stretch/Weak → consider alternatives, or `prep` if truly committed
- If fit is Strong Fit and no interview scheduled → `prep [company]` or `research [company]`
- If multiple JDs decoded → review batch triage ranking and decide allocation
- If top competency has storybank gap → `stories` to develop that competency
