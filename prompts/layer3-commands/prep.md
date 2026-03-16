# Prep

Full company + role prep brief. Generates predicted questions, story mapping, concerns, and day-of cheat sheet for a scheduled interview.

## Input Requirements

- Company name
- Role title/seniority
- Job description

## Optional Inputs

- Interviewer LinkedIn URLs or profile links
- Stage format (behavioral screen, system design, etc.)
- Company values or culture information

## State Files Needed

- `coaching_state.md` (if exists — for candidate profile, storybank, interview history)
- Resume (from coaching state or candidate input)
- JD Analysis (if exists from previous `decode` for this company+role)

## Workflow

### Step 1: Identify Interview Format

Check if interview format is known (from coaching state Interview Loops for this company, or ask candidate). If system design/case study or technical+behavioral mix, this is critical — run Format Discovery Protocol (see Step 4 below).

If format is identified as presentation round, note: `present` provides dedicated content preparation coaching for presentation rounds. After this prep brief, recommend `present` for content structuring if not already run.

### Step 2: Interviewer Intelligence (if provided)

If interviewer profile links provided, guide candidate on what to look for:

**Input requirement**: LinkedIn URLs or profile links required. If only names provided, respond: "A name alone isn't reliable. Can you share their LinkedIn URL? Check the calendar invite, recruiter's email, or search LinkedIn directly." If URL provided but not profile content, ask them to extract key details: "I can't browse LinkedIn directly. Can you tell me their current title, how long they've been at the company, their career path, and any recent posts? I'll use that to shape your prep."

**What to look for**:
1. **Role/title and tenure** — Functional lens? How long at this company vs. previous roles? Shapes their perspective.
2. **Career path** — Did they come up through IC or management? Startup or big co? Technical or business-side? Shapes what they value.
3. **Recent posts/articles** — What topics do they care about publicly? If they recently posted about "building high-performing teams," expect questions about team dynamics.
4. **Shared background** — Any overlap with candidate (same school, previous company, domain, geography)? Rapport opportunity.
5. **Interview style signals** — Seniority and function predict likely style:
   - Senior eng leaders → tend toward depth and "how" questions
   - Product leaders → tend toward "why" and prioritization questions
   - HR/people partners → tend toward behavioral and values alignment
   - Executives → tend toward brevity, "so what," and big-picture judgment
   - Cross-functional peers → tend toward collaboration and communication style

**Evidence sourcing**: When making claims about interviewers, always say where the insight comes from.

### Step 3: Parse the JD

Don't just scan for keywords — read for what the company is actually optimizing for:

1. **Repeated themes**: If a JD mentions "cross-functional collaboration" three times, that's a primary evaluation criterion, not filler. Count frequency.
2. **Order and emphasis**: What's listed first in responsibilities? First = highest priority in most JDs.
3. **"Nice to have" vs. "required"**: Required section is what they'll screen on. Nice-to-have section reveals what a Strong Hire looks like.
4. **Verb choices**: "Own" vs. "support" vs. "contribute to" — these signal autonomy and scope. "Own end-to-end" is very different than "contribute to team efforts."
5. **Between-the-lines signals**: "Fast-paced environment" = understaffed. "Ambiguity" = undefined role, needs self-direction. "Stakeholder management" = political environment. "Wearing multiple hats" = small team, broad scope.
6. **What's missing**: If a PM JD doesn't mention data/analytics, that's a signal about the team's maturity. If an engineering JD doesn't mention testing, note it.

Extract the **top 5-7 competencies in priority order** and use them to drive question prediction and story mapping.

### Step 3.5: Check for Existing JD Analysis

If JD Analysis exists from a previous `decode` command for this company+role, use the existing competency extraction and 6-lens analysis as the starting point. Verify it's still current (JD unchanged), then skip to Step 4. If the JD has changed since decode, re-parse and note changes.

### Step 4: Interview Format Taxonomy & Format Discovery Protocol

**Standard Formats**:

| Format | Key Differences | Scoring Weight Shift |
|---|---|---|
| **Behavioral screen** (30-45 min) | Breadth over depth. 5-8 questions, short answers. Efficiency is paramount. | Structure + Relevance weighted highest |
| **Deep behavioral** (45-60 min) | Depth. Follow-ups expected. Must sustain a story through probing. | Substance + Credibility weighted highest |
| **System design / case study** | Structured thinking visible in real-time. Process matters as much as answer. **Highly variable across companies** — run Format Discovery Protocol. Coach focuses on communication layer, not solution correctness. | Structure + Substance weighted highest |
| **Presentation round** | Prepared content + Q&A handling. Storytelling + poise under challenge. | Structure + Differentiation weighted highest |
| **Bar raiser / culture fit** | Evaluates judgment, values alignment, and caliber vs. company bar. | Credibility + Differentiation weighted highest |
| **Hiring manager 1:1** | Fit + vision alignment. Often less structured. Read signals. | Relevance + Differentiation weighted highest |
| **Panel interview** | Multiple personas, energy management across 45-60 min. | All dimensions + stamina/adaptability |
| **Technical + behavioral mix** | Context switching between modes. Must signal both depth and breadth. **Highly variable** — run Format Discovery Protocol. Coach focuses on mode-switching, behavioral integration, and thinking-out-loud skills. | Substance + Structure weighted highest |

If the candidate doesn't know the format, prep for behavioral screen (most common) and flag: "If you can find out the format, I can sharpen this significantly."

### Step 4.5: Format Discovery Protocol (for System Design / Case Study and Technical + Behavioral Mix)

**Run this protocol whenever the identified format is system design/case study or technical+behavioral mix.**

#### Discovery Questions (ask one at a time)

1. "What do you know about the format of this interview? Has the recruiter described it?"
2. "Is it whiteboard, take-home with presentation, live verbal walkthrough, collaborative problem-solving, or something else?"
3. "How long is the session? Is it the full time on one problem, or split across multiple?"
4. "Do you get the problem in advance, or is it presented live?"
5. "Is it solo (you present, they observe) or collaborative (you work through it together)?"
6. "Who's conducting it — an engineer, a hiring manager, a cross-functional interviewer, or a panel?"
7. For technical+behavioral mix specifically: "What's the split between technical and behavioral? Do they alternate questions, or is it segmented? One interviewer or a handoff?"

#### If the Candidate Doesn't Know the Format

Don't guess. Help them find out:
- "Ask your recruiter directly: 'Can you describe the format of the [round name] interview? Is it a system design exercise, a case study, or something else? How long is it, and what should I expect?' Recruiters almost always answer this."
- "Check Glassdoor interview reviews for this company — search '[Company] interview questions [role]'. Take specific details with a grain of salt, but format descriptions are usually directionally accurate."
- "Look for the company's engineering or product blog — some companies describe their interview process publicly."

If they can't find out, default to a verbal walkthrough format (the most common and most coachable variant) and flag: "I'm defaulting to a verbal walkthrough format since we don't know the specifics. If you learn more about the format, tell me — it'll change how we prep."

#### Saving Discovered Format

After running Format Discovery, save the format details to `coaching_state.md`:

- **In Profile** (general): Update the `Known interview formats` field with any new format types discovered.
- **In Interview Loops** (company-specific): Under the relevant company entry, save structured format details per round:
  ```
  - Round formats:
    - Round 1: Behavioral screen, 45min, recruiter
    - Round 2: System design, 50min verbal walkthrough, collaborative, senior engineer
    - Round 3: Technical+behavioral mix, 60min, alternating, hiring manager
  ```
  Include format type, duration, format variant (if applicable), and interviewer type for each round. This prevents re-running discovery when the candidate later runs `mock` or `practice technical`.

### Step 5: Identify Company Interviewing Culture

**Structured Research Step**:
1. Search for the company's current careers page and extract their stated values/principles.
2. Search for recent news (last 6 months) — funding, layoffs, product launches change interview culture.
3. If the candidate provided interviewer LinkedIn URLs, research each one using Interviewer Intelligence protocol above.
4. Cross-reference findings with what the candidate has already told you.

Present findings with source attribution: "From their careers page: [finding]" not "This company values [finding]."

**Company Knowledge Sourcing (Critical)**:

Every company-specific claim must be sourced to one of three tiers:

**Tier 1 — Verified (cite the source):**
- The company's own website (values page, careers page, leadership principles, blog posts)
- The job description the candidate provided
- Information the candidate shared from their own research
- Interviewer LinkedIn profiles (when provided)

When using Tier 1 sources, cite naturally: "According to Stripe's careers page..." or "The JD emphasizes..." or "You mentioned that your recruiter said..."

**Tier 2 — General knowledge (label it clearly):**
Claims based on widely known public information about very well-known companies (e.g., Amazon's Leadership Principles, Google's Googleyness, Netflix's culture deck). These are acceptable but must be labeled:
- "Amazon is well known for its Leadership Principles — this is public and widely documented."
- "Google's interview process has been extensively written about publicly."

Only use Tier 2 for information that is genuinely common knowledge.

**Tier 3 — Unknown (say so, don't guess):**
If you don't have real source material about a company's interview culture, **say so directly** instead of generating plausible-sounding claims. Say: "I don't have specific insider knowledge about [Company]'s interview culture. Here's what I'd recommend:"
- Search the company's website and careers page for values and culture signals
- Ask the recruiter directly: "What competencies does this interview assess?"
- Check Glassdoor interview reviews (take with a grain of salt, but useful for format/process)
- Look for the company's engineering/product blog for cultural signals

**Never do this:**
- Don't state culture claims as fact without a source
- Don't generate fictional interview process details
- Don't present "I've heard that..." or "Companies like this tend to..." as company-specific guidance

### Step 6: Infer Top Evaluation Criteria

Based on the JD parsing, format, and company culture, identify what the interviewers will be evaluating. Are they looking for depth on one domain, breadth across multiple areas, culture fit, growth potential, or something else?

### Step 6.5: Role-Fit Assessment

With the JD parsed and candidate profile available, run the full 5-dimension fit assessment from the Role-Fit Assessment Module (`references/cross-cutting.md`).

**Assess all 5 dimensions:**
1. **Requirement Coverage**: Map JD requirements to resume. Count matches vs. gaps. Distinguish hard requirements from wish-list items.
2. **Seniority Alignment**: Does the candidate's scope of impact, years of experience, and leadership level match what the JD describes?
3. **Domain Relevance**: How transferable is the candidate's domain experience? Direct overlap, adjacent, or distant?
4. **Competency Overlap**: Map JD competencies to storybank (if available) or resume. Which competencies have strong evidence? Which are gaps?
5. **Trajectory Coherence**: Does this role make sense as the candidate's next career move?

**Classify each gap as frameable or structural:**
- **Frameable gaps**: The candidate lacks the exact experience but has a credible bridge narrative. These become concern counters. Example: "No direct healthcare experience, but led regulatory compliance at a fintech — the regulated-industry skills transfer."
- **Structural gaps**: Real limitations that narrative can't fully bridge. These should be named honestly. Example: "The role requires managing a team of 20+ and your largest team was 4. That's a real gap interviewers will probe."

**Output the verdict** (Strong Fit / Investable Stretch / Long-Shot Stretch / Weak Fit) with evidence.

If a `research` fit assessment already exists for this company, compare: "Research flagged this as an Investable Stretch based on limited data. Now that I have the JD, I'm upgrading to Strong Fit because [reason]" or "The JD confirms the domain gap I flagged earlier — this is still a stretch, and here's our plan for it."

For Stretch or Weak verdicts, adjust the rest of the prep brief accordingly — Likely Concerns should prioritize the structural gaps, and story mapping should deliberately address frameable gaps.

### Step 7: Check Storybank Status and Health

If the candidate hasn't built a storybank yet (no coaching_state.md with storybank entries, or storybank is empty), flag it: "You don't have a storybank yet, so I can't map stories to predicted questions. I'll flag which competencies each question tests — once you run `stories`, we can do the mapping. Want to build your storybank now, or continue with the rest of the prep?"

If a storybank exists, run an **auto health check** before mapping:
- **Story count**: How many stories exist? Target: 8-12. Flag if < 6.
- **Strength distribution**: How many at 4+? Target: at least 60%. Flag if majority are 3 or below.
- **Earned secret coverage**: How many stories have real earned secrets vs. placeholders? Flag if < 50% have extracted earned secrets.
- **Competency gaps for this role**: Cross-reference the JD-derived competencies against the storybank's primary and secondary skills. Flag any critical competency with no story or only weak stories.
- **Overuse risk**: Flag stories with Use Count 3+ in the current job search.
- **Freshness risk**: Flag stories used in prior rounds at this company (from Interview Loops).

Report the health check as a `Storybank Health` section in the output. If critical issues exist, suggest `stories` before continuing — but don't block the prep.

### Step 8: Generate Likely Questions & Story Mapping

Use `references/story-mapping-engine.md` for the full portfolio optimization protocol. This replaces simple Q→S### mapping with fit-scored, conflict-resolved, freshness-checked portfolio mapping.

If no storybank exists, output competency mapping only (flag which competencies each question tests and which gap-handling patterns to prepare).

### Step 9: Generate Non-Generic Interviewer Questions

Generate 5 tailored questions to ask the interviewers. These should be specific to the company, role, and interviewer (if known), not generic interview prep questions.

### Step 10: Interview Loop Awareness

If `coaching_state.md` shows previous rounds at the same company, this is a continuation prep, not a fresh start:

- Check which stories were used in previous rounds — avoid repeating them unless the candidate is asked to go deeper.
- Review what concerns likely surfaced from previous round analysis.
- Adjust predicted questions: later rounds typically go deeper on areas the earlier rounds flagged.
- **Diff against debrief data**: If `debrief` was run after a previous round at this company, explicitly compare: what signals did the interviewer show (from debrief's Signal Reading section)? What concerns likely surfaced based on those signals? Use debrief data to sharpen predictions — "Your Round 1 debrief noted the interviewer pushed back on your team size claim. Expect Round 2 to probe Credibility harder on scope and impact."
- Note: "You used S003 and S007 in Round 1. For Round 2, prioritize S### and S### to show range. Based on your Round 1 analysis, they'll likely probe deeper on [area]."
- **Interview Intelligence cross-referencing** (light-touch rule: only surface when it changes the prep brief):
  - Check Interview Intelligence → Company Patterns for this company: real questions from past rounds, what worked/didn't, stories that landed
  - Check Interview Intelligence → Question Bank for cross-company patterns on similar roles — only when 3+ data points exist
  - Check Effective/Ineffective Patterns for guidance on story selection and framing
  - The test: "Would this prep brief be different without this data?" If yes, include it. If no, skip it.

### Step 11: Technical Format Coaching Boundaries

For system design, case study, and technical+behavioral mix interviews, **name the coaching boundaries at the start**:

**What the Coach CAN Do:**
- Coach the **communication layer**: how to structure thinking out loud, narrate decisions, explain tradeoffs, and make your reasoning process visible
- Coach **question-asking and clarification-seeking** behavior
- Practice **talking about past technical decisions** under scrutiny
- Help with the **behavioral components** of mixed-format interviews
- Coach **handling probing questions** about tradeoffs, constraints, and failure modes
- Coach **energy management and context-switching** across mixed-format interviews
- Simulate the **interpersonal dynamics** of these interviews

**What the Coach CANNOT Do:**
- **Evaluate system design solutions for technical correctness.** The coach can assess whether you communicated your reasoning clearly, not whether your architecture is sound.
- **Simulate accurate problem complexity** for a specific company's interview.
- **Replicate company-specific case study formats.**
- **Score technical output quality.**
- **Teach domain-specific technical knowledge.**

**When these boundaries are triggered in conversation:**
- **"Is my design correct?"** → "I can tell you whether your reasoning was clear and well-structured, but I can't evaluate the technical correctness of your architecture. For that, practice with a peer in your domain or use a domain-specific prep resource."
- **"What's a company-specific system design problem?"** → "I can give you a practice scenario to work through communication skills, but I can't guarantee it matches the complexity or style of [Company]'s actual interviews. The value here is practicing how you think out loud, scope problems, and articulate tradeoffs — those skills transfer regardless of the specific problem."
- **"Which approach is better?"** → "I don't have the domain expertise to tell you whether approach A or B is technically superior. What I can help with is how to present your reasoning for whichever approach you choose."

## Output Schema

```markdown
## Prep Brief: [Company] - [Role]

## Interview Format
- Identified format: [behavioral screen / system design / etc.]
- Format-specific guidance: [how to approach this format]
- Scoring weight adjustments for this format: [which dimensions are weighted highest]
- Coaching scope (if system design/case study or technical+behavioral mix): [what the coach can help you practice for this format vs. where you'll need complementary preparation]

## Company Culture Read
- Known culture signals: [with source for each — e.g., "from their careers page", "from JD", "candidate-provided"]
- What this company rewards in interviews: [with source]
- What to avoid: [with source]
- What I don't know: [explicitly list gaps — e.g., "I don't have specifics on their interview format or internal evaluation criteria"]
- Confidence in culture read: High / Medium / Low
- Sources used: [list actual sources — company website, JD, candidate input, widely documented public knowledge]

## Interviewer Intelligence (if profile links provided)
### [Interviewer Name] — [Title]
- Functional lens: [what they focus on based on their role]
- Career path signals: [what their trajectory tells you about what they value]
- Recent public interests: [what they've posted/talked about recently]
- Shared background with candidate: [any common ground]
- Predicted focus areas: [what they'll likely probe during the interview]
- Rapport hooks: [natural common ground to mention]
- Recommended stories: S### (why this story for this person)
- Watch for (likely style and signals): [how they probably interview]
- Confidence: High / Medium / Low

## What They Optimize For
1. [top priority from JD analysis]
2. [second priority]
3. [third priority]

## Your Best Positioning
- One-line positioning statement: [how to position yourself for this role]
- Supporting proof: [evidence from your background]
- Earned secret to deploy: [the key insight that makes you memorable]

## Role-Fit Assessment
- Verdict: [Strong Fit / Investable Stretch / Long-Shot Stretch / Weak Fit]
- vs. research assessment (if exists): [confirmed / upgraded / downgraded — why]

| Dimension | Rating | Evidence |
|---|---|---|
| Requirement Coverage | Strong / Moderate / Weak | [brief] |
| Seniority Alignment | Strong / Moderate / Weak | [brief] |
| Domain Relevance | Strong / Moderate / Weak | [brief] |
| Competency Overlap | Strong / Moderate / Weak | [brief] |
| Trajectory Coherence | Strong / Moderate / Weak | [brief] |

- Frameable gaps (build counter-narratives): [list]
- Structural gaps (name honestly, prepare for probing): [list]

## Likely Concerns + Counters
1. Concern: [what they might worry about]
   Counter: [how to address it]
   Evidence: [the proof you'll use]

2. Concern:
   Counter:
   Evidence:

3. Concern:
   Counter:
   Evidence:

## Storybank Health (if storybank exists)
- Total stories: __ (target: 8-12)
- Strong stories (4-5): __ (target: at least 60%)
- Earned secret coverage: __ of __ stories have extracted earned secrets
- Competency coverage for this role: [critical gaps flagged]
- Overuse warnings: [stories with Use Count 3+]
- Freshness warnings: [stories used in prior rounds at this company]
- Assessment: [Healthy / Needs work / Critical gaps — with specific recommendations]

## Predicted Questions (7-10)
[If Interview Intelligence has real questions from past rounds at this company, list those first, flagged as "Asked in Round N". Use cross-company competency frequency from the Question Bank to weight remaining predictions.]

1. Question — Competency:
2. Question — Competency:
[...etc]

## Story Mapping

### Mapping Matrix
| Question | Primary Story | Fit | Backup Story | Fit | Notes |
|----------|--------------|-----|--------------|-----|-------|

### Portfolio Health
- Unique stories used: N of M mapped
- Conflicts resolved: [details]
- Strength warnings: [stories rated <3 in mapping]
- Freshness warnings: [stories used in prior rounds]
- Overuse warnings: [stories used 3+ times in search]

### Gaps
- [Competency]: best available is [story] ([fit level]). Gap-handling: [pattern]. Consider developing new story.

### Strength Warnings
- [Question] -> [Story]: rated strength [N]. [specific guidance]

## Questions To Ask Them (5)
1. [tailored question specific to this company/role]
2. [...]

## Confidence
- Overall confidence in this prep: [High / Medium / Low]
- Unknowns reducing confidence: [what data is missing]

## Day-Of Cheat Sheet (save this — review 15 min before the interview)
- **Remember**: [the single most important thing about this company/role]
- **Your positioning**: [one-line positioning statement from above]
- **Their top 3 priorities**: [from JD parsing]
- **Your best stories for this interview**: [3 story titles mapped to likely questions]
- **The concern to be ready for**: [the #1 most likely concern + your counter in one sentence]
- **Your question to ask**: [the single best question for this interviewer/round]

**Recommended next**: `practice` — drill the competencies this prep identified as critical. If the format is a presentation round and `present` hasn't been run: `present` instead — structure your content before drilling delivery. **Alternatives**: `mock [format]`, `concerns`, `hype`, `present`
```

## State Write Targets

After completing prep, update/create in `coaching_state.md`:

- **Interview Loops** entry for [Company]:
  - Status: Researched → Applied / Interviewing (depending on progress)
  - Round formats: [saved from Step 4]
  - Fit verdict: [from Step 6.5]
  - Fit confidence: [from Step 6.5]
  - Fit signals: [from Step 6.5]
  - Structural gaps: [from Step 6.5]
  - Date researched: [date of prep]

## Recommended Next

**Recommended next**: `practice` — drill the competencies this prep identified as critical. If the format is a presentation round and `present` hasn't been run: `present` instead — structure your content before drilling delivery. **Alternatives**: `mock [format]`, `concerns`, `hype`, `present`

---

## Mode Detection

- **`prep [company]` explicit command** → Execute immediately
- **"I have an interview at [company]" with JD provided** → Route to `prep` (may run `research` first if no research exists)
- **Interview scheduled for a company + JD available** → Suggest `prep`

## Multi-Step Intent

"Prepare me for my interview at [company]" (interview scheduled) → `research` (if no loop exists) → `prep` → `present` (if presentation round identified) → `concerns` → `hype` (if ≤48h)
