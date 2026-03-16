# write — Cover Letter and Direct Message Generator

Generate tailored cover letters and direct outreach messages using job spec, resume, storybank, and positioning statement. Output should sound like the candidate wrote it — voice preservation is as important as content quality.

## Input Requirements

- **For cover letters**: Job description, resume version to base on (if multiple), tone preference, anything specific to address
- **For DMs**: Recipient name/role/company, goal (learn about company / express interest / get on radar / ask for intro), recipient context (optional but high-value), job spec (if relevant)
- **From coaching_state.md**: Positioning Statement (core hook), Storybank (Story Details for evidence anchoring), Resume Analysis (positioning strengths as fallback if no Positioning Statement)

## State Files Needed

- `coaching_state.md` → Positioning Statement (if exists, for core hook)
- `coaching_state.md` → Resume Analysis (positioning strengths, as fallback)
- `coaching_state.md` → Storybank (Story Details for evidence selection)

## Sub-Commands

| Sub-command | What it does |
|---|---|
| `write cover-letter [company]` | Generate a cover letter for a specific role |
| `write dm [person / company]` | Generate a direct message (LinkedIn DM, cold email, warm intro, recruiter reply) |

---

## Pre-Flight Check (both sub-commands)

Before generating, verify source material availability:

1. **Positioning Statement** from coaching_state.md — the core hook. If absent, use Resume Analysis positioning strengths as fallback and note: "Your positioning statement hasn't been built yet. This will be strong but not as sharp as it could be — run `pitch` to fix that."

2. **Storybank** (read Story Details from coaching_state.md) — select 1-2 stories relevant to role/company for evidence anchoring

3. **Job spec or recipient details** — provided by candidate in this session. If not provided, ask before generating.

---

## write cover-letter — Cover Letter Generation

### Inputs (collect before generating)

1. **Job spec**: "Paste the job description or key requirements." Required.
2. **Resume version to base this on**: Ask which version — Exec / Platform/Infra / Regulated/Fintech / General/SaaS / VC/Startup. This affects which experience is foregrounded.
3. **Anything specific you want to address**: Optional — e.g., "I want to address the short Capital One tenure" or "They specifically mentioned entity resolution — lean into that."
4. **Tone**: Infer from company type (startup → conversational; regulated enterprise → professional). Confirm if ambiguous.

### Structure

**Paragraph 1 — Opening hook (2-3 sentences)**

Lead with earned secret, specific observation about the company's challenge, or counterintuitive take on the role's core problem. **NOT**: "I am excited to apply for the [Role] position at [Company]." That sentence should never appear.

Goal: Make them read paragraph 2.

Examples of strong openers:
- Earned secret lead: "I've learned that the hardest part of building data products isn't the data — it's getting 9 teams to agree on what 'correct' means. That's the problem I've been solving for 8 years."
- Company-challenge lead: "The most interesting thing about [Company]'s approach to [specific thing in JD] is [observation]. That's the kind of problem I've built my career on."
- Spiky take: "Most AI product work fails at the measurement layer, not the model layer. That's the gap I've spent the last 3 years closing."

**Paragraph 2 — Why you, specifically (3-4 sentences)**

Ground the match in real evidence. Reference 1-2 specific experiences from storybank. Don't restate resume — add interpretation layer:
- "My work at Quantexa on [specific thing] taught me that [earned secret], which maps directly to [specific requirement from JD]."
- Name the impact number + the insight behind it, not just the number.

**Paragraph 3 — Why them, specifically (2-3 sentences)**

Must be specific to this company. Draw from JD, what's known about product/mission, or specific signal in posting. Generic company praise ("I've long admired [Company]") is worse than nothing.

If nothing specific available: "I don't have enough to write a genuine 'why them' paragraph without risking a generic take. Tell me: what specifically drew you to this company? One real reason is enough."

**Paragraph 4 — Bridge + close (1-2 sentences)**

Connect trajectory to where they're going. End clean. "I'd welcome the conversation" > "I look forward to hopefully hearing from you."

### Length and Format

- 3-4 paragraphs
- 250-350 words. Never over 400.
- No bullet points — prose only
- No bold headers inside letter body
- Should paste directly into email or application portal

### What to Avoid

- "I am excited/thrilled/passionate to apply..."
- Restating resume bullets in prose form
- Generic company praise without evidence
- Passive voice throughout
- Apologetic close ("I hope to hear from you")
- "Please find attached my resume" as opener

### After Generating

Run voice check:
- "Does this sound like you? Read it aloud — any sentence that feels like someone else wrote it?"
- Watch for: overly formal structure, hedging phrases, corporate buzzwords, excessive qualifications
- Candidate should be able to deliver this naturally in verbal pitch without sounding scripted

State assumptions made: "I assumed [X]. If that's wrong, tell me and I'll adjust."

At Level 5: Be direct about weakest section. "The opening is the weakest part here — it's specific but not surprising. If you want to sharpen it, tell me one thing about this company's approach that you find genuinely interesting."

---

## write dm — Direct Message Generation

### Inputs (collect before generating)

1. **Message type**: LinkedIn DM / Cold email / Reply to recruiter inbound / Warm intro via mutual connection

2. **Recipient**: Name, role, company — required

3. **Goal**: Learn about company / Express interest in role / Get on their radar / Ask for intro / Other

4. **Recipient context** (optional but high-value): Anything specific about their work, background, posts, articles, projects. What you found when you looked at their profile. Any shared connection or context.

5. **Job spec or role** (if outreach is about specific role): optional

### DM Structure

**LinkedIn DM / Short cold message (5-7 sentences max)**:

1. **Opener** — Something specific about *them*. Not "I came across your profile on LinkedIn." Look for: a post they wrote, a company they built, a role transition they made, a product they shipped, something from their About section. If no specific context provided, ask: "What did you notice about their profile that made you want to reach out?"

2. **Credibility hook** — One sentence on who you are and why the connection is relevant. Use earned secret framing — not job title. "I've spent the last 8 years building data products in regulated environments" > "I'm a Senior PM with 8 years of experience."

3. **The ask** — Specific, low-friction, easy to say yes to. "15 minutes" not "a call sometime." Named topic, not vague conversation.

4. **Close** — One sentence. No sorry-to-bother. No paragraph of gratitude.

**Cold email (8-10 sentences)**:
Same structure with slightly more room to establish credibility and context. Still under 150 words.

**Recruiter-inbound reply**:
They reached out → lead with genuine interest signal → add one proof point specific to the role → ask a clarifying question to qualify before committing to call. Goal: show you're serious, not just politely engaging.
- "Thanks for reaching out about [Role] — the [specific thing in their message/role] caught my attention. I've been [specific experience that maps to the role]. Before we schedule time, could you share [specific qualifying question — e.g., 'whether the role involves more platform strategy or feature execution']?"

**Warm intro via mutual connection**:
Reference the connection in sentence 1. This is your credibility proxy — use it. "I was introduced by [Name], who thought our work on [shared area] might be worth a conversation."

### Voice Preservation

After generating: "Does this sound like you? Read it out loud. Any line that feels like you wouldn't say it?"
- Remove corporate-speak, hedging, excessive qualifications
- Keep it conversational — these messages should read like a smart professional wrote them, not a template

### What to Avoid

- Opening with your own credentials before establishing why you're reaching out to *them*
- "I hope this message finds you well"
- "I would love to pick your brain"
- Overly long messages — every additional sentence reduces response rate
- Asking for too much in first message (referral + call + advice = too many asks)

---

## Story Selection for write

When grounding a message in storybank evidence:

1. Read Story Details from coaching_state.md
2. Match story to JD requirements or company focus — don't use same story for every message
3. Extract earned secret or one specific detail (number, decision, counterintuitive outcome) — use as hook, not full STAR story
4. For cover letters: 1-2 stories max. For DMs: at most 1 story reference, only the hook.

---

## Output Schema

```markdown
## [Cover Letter / LinkedIn DM / Cold Email]: [Company or Recipient] — [Role if applicable]

---

[Full message text — clean, no headers inside letter body]

---

**Voice check**: [What's strongest. Where the AI-voice risk is highest. One sentence each.]

**Assumptions made**: [Any inferences the candidate should verify before sending]

**Storybank used**: [Which story/stories were drawn from, and how]

**Recommended next**: `track log` — log this application or outreach. **Alternatives**: `decode [company]`, `prep [company]`
```

## State Write Targets

- **Application Tracker** (if entry exists for this company): Update Cover Letter field to "Yes — generated [date]"
- **Application Tracker notes** (if new outreach): Note message type and date
- **Coaching Notes** (if consistent positioning pattern emerges): "earned secret about dual-value-path design landing consistently as opening hook"

## Recommended Next

**State-aware sequence**:

- After `write cover-letter` → `track log` (log application) or `send` (if candidate ready to send directly)
- After `write dm` to recruiter/hiring manager → `track log` (log outreach as application if applicable) or `send` (if candidate ready)

**Alternatives**: `decode [company]`, `prep [company]`, `jobs` (for more role ideas), `pitch` (if positioning needs work)
