# jobs — Daily Job Discovery

Surface 3 job listings per session that match the candidate's criteria. Use feedback to iteratively refine criteria over time. Builds picture of what candidate actually responds to vs. what they say they want.

## Input Requirements

- **From candidate**: Initial Job Search Criteria (if first time running `jobs`), OR feedback on previously surfaced roles (interested / not interested / why)
- **From coaching_state.md**: Job Search Criteria (target roles, location, company size, must-haves, exclusions, refinement history)

## State Files Needed

- `coaching_state.md` → Job Search Criteria (all filtering parameters)
- `coaching_state.md` → Job Discovery Log (to cross-reference previously surfaced roles)
- `coaching_state.md` → Interview Loops (to avoid surfacing companies already active in pipeline)
- `coaching_state.md` → Application Tracker (to avoid duplicate applications)

## Workflow

1. **Check trigger**:
   - **Auto-trigger at session start**: If Job Search Criteria exists AND Daily search enabled AND Last searched is not today → run silently, announce results at greeting
   - **Manual trigger**: User types `jobs`
   - **First-time setup**: If no Job Search Criteria section exists or criteria empty → run brief setup before searching

2. **First-time setup** (if needed — one question at a time):
   1. Target role keywords (pre-fill from Profile, confirm)
   2. Location / remote preference (pre-fill from stored criteria if available)
   3. Company size preference (startup / scale-up / mid-market / enterprise, or mix)
   4. Any hard exclusions (industries, company types, known companies to avoid)
   - Save to Job Search Criteria
   - Then proceed to search

3. **Read Job Search Criteria** from coaching_state.md:
   - Target roles + seniority
   - Location preference
   - Company size/stage preference
   - Must-have signals
   - Exclusions
   - Refined-from-feedback history (use to avoid re-surfacing similar companies to ones already rejected)

4. **Search for 3 current job listings** using Source Priority Order (see below):
   - Start with Tier 1 sources (PM-specific boards — strongest signal-to-noise)
   - Move to next tier if current tier yields fewer than 3 verified matches
   - Tier 6 (LinkedIn) only as last resort

5. **Validate each posting** (mandatory before presenting):
   - Go to company's careers page directly (careers.company.com or company.com/careers)
   - Confirm role exists — search by title or requisition ID
   - Check posting date — flag if older than 3 weeks as potentially stale
   - If role cannot be verified on company careers page → drop it and find replacement

6. **Pre-screen filter** (before any decode):
   - Role type match: Is this actually a PM role (not VC partner, GTM, consultant, etc.)?
   - Title band match: Does seniority (IC5 vs. Director vs. VP) match target band? If off by 2+ levels → skip
   - Posting verified: Did it pass company careers page check?
   - Only roles passing all 3 filters get full presentation

7. **Cross-reference active loops** (before presenting):
   - Check Interview Loops in coaching_state.md
   - Don't surface companies already active (candidate applied or interviewing)
   - If match appears for active company → skip and find replacement

8. **Present 3 roles** using schema below

9. **Feedback processing** (for each role candidate passes on):
   - Push for specifics: "Too big / too small? Wrong product area? Company you've heard things about? Seniority misaligned? Industry you want to avoid?"
   - Use feedback to update Job Search Criteria in real time
   - Log each refinement with date and reason
   - Candidate's rejection patterns reveal actual preferences

10. **For roles candidate is interested in**:
    - Offer: "Want me to decode the JD for fit assessment, or go straight to logging an application?"

11. **Update state**:
    - Log all 3 jobs to Job Discovery Log (date, company, role, URL, fit signal, interest, notes)
    - Update Last searched to today
    - Update Job Search Criteria if refinements made
    - Increment Refined from feedback count for each criteria change

## Source Priority Order (strict ordering)

Work through sources in order. Move to next tier if current yields fewer than 3 verified matches.

**Tier 1 — PM-specific boards** (strongest signal-to-noise):
- Mind the Product: https://lnkd.in/eBz7bB97
- Product Manager Job Board: https://lnkd.in/eyWijeuP
- ProductHired: https://lnkd.in/eBc_BRdH

**Tier 2 — VC portfolio boards** (startup/scale-up roles):
- a16z Speedrun portfolio jobs: https://lnkd.in/e3pm7frN
- Sequoia Capital portfolio jobs: https://lnkd.in/e32E-G_t
- Index Ventures startup jobs: https://lnkd.in/eENscJUP

**Tier 3 — Broader job boards**:
- Wellfound (AngelList): wellfound.com/jobs
- Builtin Chicago: builtinchicago.org/jobs
- Welcome to the Jungle: welcometothejungle.com/en/jobs

**Tier 4 — Remote-specific boards** (if remote roles in scope):
- We Work Remotely: https://lnkd.in/eyXAxjm6
- Remotivate: https://lnkd.in/eqTjY4zJ
- Working Nomads: https://lnkd.in/epNVZDJ5
- RemoteOK: https://lnkd.in/e4sPQEDe

**Tier 5 — Chicago/Midwest startup ecosystems**:
- Midwest Startups: https://lnkd.in/gp4YRrSq
- Jump Capital portfolio jobs: https://lnkd.in/gzDWK7DN
- Hyde Park Venture Partners: https://lnkd.in/gxe2PxQK
- OCA Ventures: https://lnkd.in/giuSa5KM
- 1871 job board: https://1871.com/jobs/

**Tier 6 — LinkedIn** (last resort only):
- Use only if tiers 1–5 yield fewer than 3 valid matches
- Flag to candidate: "This came from LinkedIn — worth verifying posting is still live before investing time"

## Query Construction

- Combine target role + seniority + key skill area + location filter
- Vary query structure across 3 results — don't surface 3 identical roles
- Mix company sizes when no strong preference: 1 startup/scale-up, 1 mid-size, 1 larger company (or adjust based on stated preference)

## Quality Filters

- Recency: prefer postings from last 2 weeks. Flag if older.
- Relevance: verify role matches candidate's target (don't surface "Data PM" when target is "AI Product Manager" unless explicit overlap)
- No duplicate companies from same session
- If fewer than 3 strong verified matches: Surface what's available and be honest — "I only found 2 verified matches today. Holding the third rather than surfacing an unverified role."

## Output Schema

```markdown
## Today's Job Matches — [date]

**1. [Company] — [Role Title]**
- Seniority: [level from posting]
- Location: [remote / hybrid / onsite — city if relevant]
- Company: [size/stage, one line on what they do]
- Why it matches: [1-2 lines on specific fit signals — tie to criteria and storybank strengths, not generic]
- Quick take: [one honest line — "Strong fit on data platform", "Stretch on seniority — reads more Director", "Worth decoding — ambiguous title"]
- URL: [direct link]

**2. [Company] — [Role Title]**
[same format]

**3. [Company] — [Role Title]**
[same format]

---

Which of these are interesting? For any you're passing on — what didn't land?

**Recommended next**: `decode [company]` — full JD fit assessment before deciding to apply. **Alternatives**: `track log`, `prep [company]`, `jobs` (run again for fresh batch)
```

## Feedback Routing (Criteria Refinement)

For each role candidate passes on, push for specifics:
- "Too enterprise / too small?"
- "Wrong product area within your domain?"
- "Company you've heard things about?"
- "Seniority misaligned?"
- "Industry you want to avoid?"

Use feedback to update Job Search Criteria in real time:
- "Too enterprise / too slow" → add to Exclusions or adjust size preferences
- "Not enough AI — too generic" → tighten Must-have signals
- "I've heard bad things about [Company]" → add to Exclusions
- "Interesting but seniority is off" → adjust seniority range filter
- "Not the right kind of data work" → refine role keyword strategy

**Criteria Refinement Log Format**:
Each refinement entry: `[date]: [what changed] — [reason from candidate feedback]`

Example:
- `2026-03-05: Added exclusion — fintech-only roles. Candidate wants to move away from FS-heavy product work.`
- `2026-03-07: Tightened must-have: AI/ML must be core product, not just 'uses data'. Generic data PM roles not matching intent.`
- `2026-03-10: Removed pure enterprise. Candidate finds org complexity unattractive at this stage.`

This log is the long-term record of what candidate actually wants.

## State Write Targets

- **Job Discovery Log**: Add row for each of 3 roles (date, company, role, URL, fit signal, interest, notes)
- **Job Search Criteria → Last searched**: Update to today
- **Job Search Criteria → Target roles / Location / Company size / Must-haves / Exclusions**: Update if refinements made
- **Job Search Criteria → Refinement log**: Add entry for each refinement with date and reason
- **Job Search Criteria → Refined from feedback**: Increment count for each criteria change

## Recommended Next

**State-aware sequence**:
- For roles candidate is interested in → `decode [company]` (full JD fit assessment) or `track log` (log application immediately)
- For roles candidate wants to research → `prep [company]` (if they advance)
- For fresh batch → `jobs` again next session (if Daily search enabled)

**Alternatives**: `decode [company]`, `track log`, `write cover-letter [company]`, `jobs` (run again for fresh batch)

## Auto-Trigger at Session Start

When Job Search Criteria exists, Daily search is enabled, and Last searched is not today:
- Run `jobs` silently
- Announce at greeting: "Found 3 new roles matching your criteria. Take a look, then we'll pick up where we left off."
- If Last searched is already today → skip silently, don't mention
