# jobs — Daily Job Discovery

## Purpose

Surface 3 job listings per session that match the candidate's criteria. Use feedback (interested / not interested / why) to iteratively refine criteria over time. Over multiple sessions, this command builds a picture of what the candidate actually responds to — not just what they say they want.

---

## Trigger Logic

**Auto-trigger at session start** (when Job Search Criteria exists and Daily search is enabled):
- Read `Job Search Criteria` from `coaching_state.md`
- Check `Last searched` date. If not today → run `jobs` automatically as part of session start
- Announce: "Found 3 new roles matching your criteria. Take a look and let me know what's interesting."
- If `Last searched` is already today → skip auto-trigger silently

**Manual trigger**: User types `jobs`

**First-time setup** (no Job Search Criteria section exists yet or criteria are empty):
- Run brief setup before searching. Collect minimum viable criteria using the one-question-at-a-time rule:
  1. Target role keywords (pre-fill from Profile, confirm)
  2. Location / remote preference (pre-fill from stored criteria if available)
  3. Company size preference (pre-fill from stored criteria if available)
  4. Any hard exclusions (industries, company types, known companies to avoid)
- Save to Job Search Criteria. Then run the search.

---

## Step 1: Read Criteria

Before searching, read from `coaching_state.md → Job Search Criteria`:
- Target roles + seniority
- Location preference
- Company size/stage preference
- Must-have signals
- Exclusions
- Refined-from-feedback history (use this to avoid surfacing similar companies to ones already rejected)

---

## Step 2: Search

Use WebSearch to find 3 current job listings. Follow the source priority order strictly.

---

### Source Priority Order

Work through sources in this order. Move to the next source tier if current tier yields fewer than 3 verified matches.

**Tier 1 — PM-specific boards (strong signal-to-noise):**
- Mind the Product: https://lnkd.in/eBz7bB97
- Product Manager Job Board: https://lnkd.in/eyWijeuP
- ProductHired: https://lnkd.in/eBc_BRdH

**Tier 2 — VC portfolio boards (startup/scale-up roles):**
- a16z Speedrun portfolio jobs: https://lnkd.in/e3pm7frN
- Sequoia Capital portfolio jobs: https://lnkd.in/e32E-G_t
- Index Ventures startup jobs: https://lnkd.in/eENscJUP

**Tier 3 — Broader job boards:**
- Wellfound (AngelList): wellfound.com/jobs
- Builtin Chicago: builtinchicago.org/jobs
- Welcome to the Jungle: welcometothejungle.com/en/jobs

**Tier 4 — Remote-specific boards (if remote roles are in scope):**
- We Work Remotely: https://lnkd.in/eyXAxjm6
- Remotivate: https://lnkd.in/eqTjY4zJ
- Working Nomads: https://lnkd.in/epNVZDJ5
- RemoteOK: https://lnkd.in/e4sPQEDe

**Tier 5 — Chicago/Midwest startup ecosystems:**
- Midwest Startups: https://lnkd.in/gp4YRrSq
- Jump Capital portfolio jobs: https://lnkd.in/gzDWK7DN
- Hyde Park Venture Partners: https://lnkd.in/gxe2PxQK
- OCA Ventures: https://lnkd.in/giuSa5KM
- 1871 job board: https://1871.com/jobs/

**Tier 6 — LinkedIn (last resort only):**
- Use only if tiers 1–5 yield fewer than 3 valid matches
- Flag to the candidate: "This came from LinkedIn — worth verifying the posting is still live before investing time"

---

### Posting Validation (mandatory for every role before presenting)

After finding a candidate role, validate it before surfacing:
1. **Go to the company's careers page directly** (careers.company.com or company.com/careers)
2. **Confirm the exact role exists** — search by title or requisition ID
3. **Check posting date** — flag anything older than 3 weeks as potentially stale
4. If the role cannot be verified on the company careers page → **drop it and find a replacement**. Never surface an unverified role.

**Pre-screen filter (run before any decode):**
Before presenting a role or running a decode, check:
1. **Role type match**: Is this actually a PM role (not VC partner, GTM advisor, consultant, etc.)? If not → 2-line skip, no decode
2. **Title band match**: Does the seniority level (IC5 vs Director vs VP) match the candidate's target band? If mismatched by 2+ levels → 2-line skip
3. **Posting verified**: Did it pass the company careers page check above?

Only roles that pass all 3 filters get a full presentation or decode.

---

**Query construction**: Combine target role + seniority + key skill area + location filter.
- Vary query structure across the 3 results — don't surface 3 identical roles
- Mix company sizes when no strong preference: 1 startup/scale-up, 1 mid-size, 1 larger company (or adjust based on stated preference)

**Quality filters**:
- Recency: prefer postings from the last 2 weeks. Flag if older.
- Relevance: verify the role matches the candidate's target (don't surface "Data PM" when the target is "AI Product Manager" unless they explicitly overlap)
- No duplicate companies from the same session

**If fewer than 3 strong verified matches found**: Surface what's available and be honest — "I only found 2 verified matches today. Holding the third rather than surfacing an unverified role."

---

## Step 3: Present

For each role, use this format:

```
**[N]. [Company] — [Role Title]**
- Seniority: [level from posting]
- Location: [remote / hybrid / onsite — city if relevant]
- Company: [size/stage, one line on what they do]
- Why it matches: [1-2 lines on specific fit signals — tie to the candidate's criteria and storybank strengths, not generic]
- Quick take: [one honest line — "Strong fit on data platform", "Stretch on seniority — JD reads more Director", "Worth decoding — ambiguous title"]
- URL: [direct link]
```

After all 3: "Which of these are interesting? And for any you're passing on — what didn't land?"

---

## Step 4: Feedback Processing

For each role the candidate passes on, push for specifics. Don't accept "not interested" alone:
- "Too big / too small?"
- "Wrong product area within data/AI?"
- "Company you've heard things about?"
- "Seniority misaligned?"
- "Industry you want to avoid?"

Use the feedback to update Job Search Criteria in real time. Each refinement narrows the criteria and is logged with date and reason. Over time this log becomes the candidate's actual preference profile — often more specific than their initial self-description.

**Feedback routing**:
- "Too enterprise / too slow" → add to Exclusions or size preferences
- "Not enough AI — too generic" → tighten Must-have signals
- "I've heard bad things about [Company]" → add to Exclusions
- "Interesting but seniority is off" → adjust seniority range filter
- "Not the right kind of data work" → refine role keyword strategy

For each role the candidate is interested in, offer: "Want me to decode the JD for a fit assessment, or go straight to logging an application?"

---

## Step 5: Cross-Reference with Active Loops

Before presenting results, check `Interview Loops` in coaching_state.md. Don't surface companies that are already active in the pipeline (the candidate has applied or is interviewing). If a match appears for a company already in the pipeline, skip it and find a replacement.

---

## Step 6: Update State

After running `jobs`:
- Log all 3 jobs to `Job Discovery Log` (date, company, role, URL, fit signal, interest, notes)
- Update `Last searched` date to today
- Update `Job Search Criteria` if any refinements were made
- Increment `Refined from feedback` count for each criteria change

---

## Output Schema

```markdown
## Today's Job Matches — [date]

**1. [Company] — [Role Title]**
- Seniority: [level]
- Location: [remote/hybrid/onsite]
- Company: [size/stage, one line]
- Why it matches: [fit signal]
- Quick take: [honest 1-line assessment]
- URL: [link]

**2. [Company] — [Role Title]**
[same format]

**3. [Company] — [Role Title]**
[same format]

---
Which of these are interesting? For any you're passing on — what didn't land?

**Recommended next**: `decode [company]` — full JD fit assessment before deciding to apply. **Alternatives**: `track log`, `prep [company]`, `jobs` (run again for a fresh batch)
```

---

## Criteria Refinement Log Format

Each refinement entry in Job Search Criteria:
`[date]: [what changed] — [reason from candidate feedback]`

Example:
- `2026-03-05: Added exclusion — fintech-only roles. Candidate wants to move away from FS-heavy product work.`
- `2026-03-07: Tightened must-have: AI/ML must be core product, not just 'uses data'. Generic data PM roles not matching intent.`
- `2026-03-10: Removed pure enterprise. Candidate finds the org complexity unattractive at this stage.`

This log is the long-term record of what the candidate actually wants.
