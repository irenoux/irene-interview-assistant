# track — Application Tracker and Pipeline Management

Log applications, track status, manage follow-up sequences, and surface analytics on what's converting across the search.

## Input Requirements

- **From candidate**: Application details (company, role, date applied, resume version, method, cover letter), status updates, follow-up responses
- **From coaching_state.md**: Application Tracker (existing applications), Job Discovery Log (for cross-referencing), Interview Loops (to cross-link advancing interviews)

## State Files Needed

- `coaching_state.md` → Application Tracker (source of truth for all applications)
- `coaching_state.md` → Job Discovery Log (to cross-reference if job was surfaced via `jobs`)
- `coaching_state.md` → Interview Loops (to cross-link when advancing)
- `coaching_state.md` → Outcome Log (for rejections/offers)
- `coaching_state.md` → Application Analytics (for pattern analysis)

## Sub-Commands

| Sub-command | What it does |
|---|---|
| `track log` | Log a new application |
| `track update [company]` | Update status or log a response |
| `track pipeline` | View full tracker with follow-up queue |
| `track analytics` | Surface patterns from application data (requires 5+ applications) |
| `track followup` | Show all overdue or due-today follow-ups |

---

## track log — Logging a New Application

Collect in sequence (one question at a time):

1. **Company name** and **role title**

2. **Date applied** (default: today if not specified)

3. **Resume version used** (present the candidate's available versions):
   - Exec / Broad Platform Leader
   - Platform / Engineering / Infra
   - Regulated / Fintech / Financial Data
   - Senior PM — General, SaaS, Ops
   - VC / Startup / Investor
   - Or: "custom version — describe"

4. **Application method**:
   - Job board (specify: LinkedIn / Indeed / company site / other)
   - Referral (note who)
   - Direct outreach (cold apply, DM, email)
   - Recruiter inbound (they contacted me)

5. **Cover letter**: Yes / No. If yes: which version or brief description (e.g., "tailored for their data platform focus" or "used write-generated CL from [date]")

6. **Notes** (optional): Anything worth remembering — referral name, specific angle used, key requirement you addressed

**Auto-set follow-up dates**:
- Follow-up 1: 5 business days after application date
- Follow-up 2: 10 business days after application date (only if no response to F/U 1)
- After F/U 2 with no response: status automatically moves to "Likely closed" unless updated

**Assign Application ID**: A001, A002, etc. in order of logging.

**Confirm on logging**:
"Logged — A[###]. Follow-up 1 is due [date]. I'll remind you at session start."

**Cross-reference check**: After logging, check if a `decode` has been run for this company. If not, offer: "No JD decode on file for [Company]. Want to run `decode` while you're here?" If decode exists, cross-link to JD Analysis section.

**Output**:
```markdown
## Application Logged: A[###] — [Company] — [Role]
- Date applied: [date]
- Resume version: [version]
- Method: [method]
- Cover letter: [yes/no — description if yes]
- Follow-up 1 due: [date]
- Follow-up 2 due: [date]
- Notes: [if any]

**Recommended next**: `decode [company]` — JD fit assessment if not done. **Alternatives**: `write cover-letter [company]`, `prep [company]`
```

---

## track update — Updating Status

When candidate reports a response or status change:

**Status progression**:
Applied → Screen Scheduled → Phone Screen Done → Loop Scheduled → Offer → Closed/Rejected/Withdrawn

**Response types to log**:
- Recruiter screen scheduled
- Hiring manager screen scheduled
- Rejection (with or without feedback)
- No response / Ghosted
- Offer
- Withdrawn (candidate withdrew)

**On rejection**: "Want to log any feedback? Even a standard rejection template sometimes contains signals." If feedback exists, route to Interview Intelligence → Recruiter/Interviewer Feedback table via `feedback` command.

**On advancing**: "Want to run `prep [company]` to get ready for the next round? I'll cross-link this to your Interview Loop."
- Create or update Interview Loop entry for the company
- Update Interview Loops → Status and Rounds completed

**On offer**: Route to `negotiate` command and log in Outcome Log with Result: offer.

**Output**:
```markdown
## Updated: A[###] — [Company] — [Role]
- Previous status: [status]
- New status: [status]
- Response logged: [details]
- [If advancing]: Interview Loop updated. Run `prep [company]` when ready.
- [If rejected]: Outcome logged. Run `feedback` to capture any notes.
```

---

## track pipeline — Full Pipeline View

Display complete tracker organized by status:

```markdown
## Application Pipeline — [date]

### Active (Awaiting Response)
| ID | Company | Role | Applied | Resume | Method | Cover Letter | Status | Follow-up Due |
[rows — active applications]

### Pending Follow-up
[applications where follow-up is due or overdue — highlighted with ⚠️]

### Closed
| ID | Company | Role | Applied | Status | Response Type | Notes |
[rows — rejected, withdrawn, ghosted]
```

Flag overdue follow-ups prominently:
"⚠️ Follow-up overdue: A[###] [Company] — due [date]. Want a draft?"

Offer follow-up drafts inline for any overdue items using Follow-up Message Templates (see below).

---

## track analytics — Pattern Analysis

**Minimum threshold**: 5 applications. Before 5: "Analytics needs at least 5 applications to surface patterns. You have [N]. Keep logging."

**Analyses to run** (only include where N is sufficient for comparison):

1. **Overall response rate**: (applications with any response / total) × 100
2. **Response rate by resume version**: which version is getting traction
3. **Response rate by application method**: referral vs. direct outreach vs. job board vs. recruiter inbound
4. **Cover letter impact**: response rate with CL vs. without
5. **Time to first response**: average business days from application to first contact
6. **Stage conversion**: % reaching screen → % reaching loop → % receiving offer
7. **Company size pattern**: does startup/scale-up respond differently than enterprise?

**Framing**: Always state N. "With [N] applications, this is directional, not definitive. Here's what the data suggests so far..."

**Connect findings to action**:
- Resume version underperforming → flag for `resume` audit
- Direct outreach outperforming job boards → recommend shifting strategy, flag for `outreach`
- No cover letter pattern → surface explicitly: "Applications with cover letters have [X]% response rate vs. [Y]% without. Worth factoring into your approach."
- Low overall response rate after 10+ applications → raise with candidate: "10+ applications with [X]% response rate. Let's look at whether the targeting is right before adding more volume."

---

## track followup — Follow-up Queue

Show all follow-ups due today or overdue:

```markdown
## Follow-up Queue — [date]

### Overdue
- A[###] [Company] — [Role] — was due [date] ([N] days ago)
- A[###] [Company] — [Role] — was due [date] ([N] days ago)

### Due Today
- A[###] [Company] — [Role] — Follow-up [1 or 2]

### Due This Week
- A[###] [Company] — [Role] — due [date]
```

For each overdue / due-today item, offer a draft follow-up using templates below.

---

## Follow-up Message Templates

Personalize based on application notes (referral, tailored angle, etc.).

**Follow-up 1 (5 business days) — tone: light, professional**:
```
Hi [Name / Hiring Team], I wanted to follow up on my application for [Role] submitted on [date]. I'm genuinely excited about [specific thing — 1 phrase from company/role, not generic]. Please let me know if there's anything additional I can share. Best, [Candidate Name]
```

**Follow-up 2 (10 business days) — tone: closing the loop, graceful**:
```
Hi [Name / Hiring Team], I'm following up once more on my [Role] application. I understand hiring timelines vary — if the timing isn't right or the role has moved in a different direction, that's completely fine. I remain interested and happy to reconnect if circumstances change. Best, [Candidate Name]
```

**Referral variant** (if applied via referral, mention in F/U 1):
```
Hi [Name / Hiring Team], I wanted to follow up on my application for [Role] submitted on [date]. I was referred by [Referral Name], who thought this could be a strong mutual fit. I'm genuinely excited about [specific thing from company/role]. Please let me know if there's anything additional I can share. Best, [Candidate Name]
```

**Recruiter-inbound variant** (if they reached out first):
```
Hi [Name], You reached out to me about [Role] on [date] — I wanted to follow up and confirm my strong interest in this opportunity. [Optional: add specific note about what attracted you]. Looking forward to learning more. Best, [Candidate Name]
```

---

## State Write Targets

- **Application Tracker**: Add row for each new application; update existing rows on status changes
- **Job Discovery Log**: Cross-reference if job was surfaced via `jobs` command
- **Interview Loops**: Create or update entry if application advances to interview
- **Outcome Log**: Log rejection or offer outcomes
- **Application Analytics**: Update when `track analytics` run

## Recommended Next

**State-aware sequence**:

- After `track log` → `decode [company]` (JD fit assessment) or `write cover-letter [company]` (generate CL if needed)
- After `track update` (advancing) → `prep [company]` (interview prep for next round)
- After `track update` (rejected) → `feedback` (capture any feedback provided)
- After `track update` (offer) → `negotiate` (negotiation coaching)
- After `track analytics` → focus on highest-converting method/resume version going forward

**Alternatives**: `decode [company]`, `write cover-letter [company]`, `prep [company]`, `feedback`, `negotiate`

## Follow-up Reminder at Session Start

At each session start, check for overdue or due-today follow-ups:
- If overdue: "You have [N] follow-ups overdue from [dates]. Want to see the list?"
- If due today: "You have [N] follow-ups due today. Want to knock them out?"
