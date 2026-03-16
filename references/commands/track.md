# track — Application Tracker

## Purpose

Log applications, track status, manage follow-up sequences, and surface analytics on what's working across the search. The tracker is the source of truth for the candidate's pipeline and the data engine for understanding what's converting.

---

## Sub-Commands

| Sub-command | What it does |
|---|---|
| `track log` | Log a new application |
| `track update [company]` | Update status or log a response for an existing application |
| `track pipeline` | View the full tracker with follow-up queue |
| `track analytics` | Surface patterns from application data (requires 5+ applications) |
| `track followup` | Show all overdue or due-today follow-ups |

---

## track log — Logging a New Application

Collect in sequence (one question at a time):

1. **Company name** and **role title**
2. **Date applied** — default today if not specified
3. **Resume version used** — present the candidate's folder structure and ask which was used:
   - Exec / Broad Platform Leader
   - Platform / Engineering / Infra
   - Regulated / Fintech / Financial Data
   - Senior PM — General, SaaS, Ops
   - VC / Startup / Investor
   - Or: "custom version — describe"
4. **Application method**:
   - Job board (which one: LinkedIn / Indeed / company site / other)
   - Referral (note who)
   - Direct outreach (cold apply, DM, email)
   - Recruiter inbound (they contacted me)
5. **Cover letter**: Yes / No. If yes: which version or brief description (e.g., "tailored for their data platform focus" or "used write-generated CL from [date]")
6. **Notes** (optional): anything worth remembering — referral name, specific angle used, key requirement you addressed

**Assign Application ID**: A001, A002, etc. in order of logging.

**Auto-set follow-up dates**:
- Follow-up 1: 5 business days after application date
- Follow-up 2: 10 business days after application date (only if no response to F/U 1)
- After F/U 2 with no response: status automatically moves to "Likely closed" unless updated

**Confirm on logging**:
"Logged — A[###]. Follow-up 1 is due [date]. I'll remind you at session start."

**Cross-reference**: After logging, check if a `decode` has been run for this company. If not, offer: "No JD decode on file for [Company]. Want to run `decode` while you're here?" If a decode exists, cross-link to JD Analysis section.

---

## track update — Updating Status

When the candidate reports a response or status change:

**Status progression**:
Applied → Screen Scheduled → Phone Screen Done → Loop Scheduled → Offer → Closed/Rejected/Withdrawn

**Response types to log**:
- Recruiter screen scheduled
- Hiring manager screen scheduled
- Rejection (with or without feedback)
- No response / Ghosted
- Offer
- Withdrawn (candidate withdrew)

**On rejection**: "Want to log any feedback? Even a standard rejection template sometimes contains signals." If feedback exists, route to `Recruiter/Interviewer Feedback` in Interview Intelligence.

**On advancing**: "Want to run `prep [company]` to get ready for the next round? I'll cross-link this to your Interview Loop." Create or update Interview Loop entry for the company.

**On offer**: Route to `negotiate` command and log in Outcome Log with Result: offer.

---

## track pipeline — Full Pipeline View

Display the complete tracker organized by status:

```markdown
## Application Pipeline — [date]

### Active
| ID | Company | Role | Applied | Resume | Method | Cover Letter | Status | Follow-up Due |
[rows — active applications]

### Pending Follow-up
[applications where follow-up is due or overdue — highlighted]

### Closed
| ID | Company | Role | Applied | Status | Response Type | Notes |
[rows — rejected, withdrawn, ghosted]
```

Flag overdue follow-ups prominently: "⚠️ Follow-up overdue: A[###] [Company] — due [date]. Want a draft?"

Offer follow-up drafts inline for any overdue items.

---

## track analytics — Pattern Analysis

**Minimum threshold**: 5 applications. Before 5: "Analytics needs at least 5 applications to surface patterns. You have [N]. Keep logging."

**Analyses to run** (only include where N is sufficient for the comparison):

1. **Overall response rate**: (applications with any response / total) × 100
2. **Response rate by resume version**: which version is getting traction
3. **Response rate by application method**: referral vs. direct outreach vs. job board vs. recruiter inbound
4. **Cover letter impact**: response rate for applications with CL vs. without
5. **Time to first response**: average business days from application to first contact
6. **Stage conversion**: % reaching screen → % reaching loop → % receiving offer
7. **Company size pattern**: is startup/scale-up responding differently than enterprise?

**Framing**: Always state N. "With [N] applications, this is directional, not definitive. Here's what the data suggests so far..."

**Connect findings to action**:
- Resume version underperforming → flag for `resume` audit
- Direct outreach outperforming job boards → recommend shifting strategy, flag for `outreach`
- No cover letter pattern → surface explicitly: "Applications with cover letters have a [X]% response rate vs. [Y]% without. Worth factoring in your approach."
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

For each overdue / due-today item, offer a draft follow-up using the templates below.

---

## Follow-up Message Templates

Personalize based on application notes (referral, tailored angle, etc.).

**Follow-up 1 (5 business days) — tone: light, professional:**
> Hi [Name / Hiring Team], I wanted to follow up on my application for [Role] submitted on [date]. I'm genuinely excited about [specific thing — 1 phrase from company/role, not generic]. Please let me know if there's anything additional I can share. Best, Irene Zhang

**Follow-up 2 (10 business days) — tone: closing the loop, graceful:**
> Hi [Name / Hiring Team], I'm following up once more on my [Role] application. I understand hiring timelines vary — if the timing isn't right or the role has moved in a different direction, that's completely fine. I remain interested and happy to reconnect if circumstances change. Best, Irene Zhang

**Referral variant**: If applied via referral, mention it in F/U 1: "I was referred by [Name], who thought this could be a strong mutual fit..."

**Recruiter-inbound variant**: If they reached out first: "You reached out to me about [Role] on [date] — I wanted to follow up and confirm my interest..."

---

## State Updates

- `track log` → Add row to Application Tracker; set follow-up dates; cross-link to Job Discovery Log if job was surfaced via `jobs`
- `track update` → Update existing Application Tracker row; update Outcome Log if rejection/offer; create/update Interview Loop if advancing
- `track analytics` → Update Application Analytics section
- At session start → Check for overdue follow-ups and surface them in greeting: "You have [N] follow-ups due or overdue. Want to see the list?"

---

## Output Schema

**After `track log`:**
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

**After `track update`:**
```markdown
## Updated: A[###] — [Company] — [Role]
- Previous status: [status]
- New status: [status]
- Response logged: [details]
- [If advancing]: Interview Loop updated. Run `prep [company]` when ready.
- [If rejected]: Outcome logged. Run `feedback` to capture any notes.
```
