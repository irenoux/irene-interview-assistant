# Make.com Workflow 1: Daily Job Discovery

**Workflow name**: `Interview Coach — Daily Jobs`
**Trigger**: Schedule — 8:00 AM (your local timezone) daily
**Purpose**: Automatically surface 3 matching job roles each morning based on your search criteria, then update your coaching state with new discoveries
**Duration**: ~2 minutes

---

## Pre-Requisites

- [ ] GitHub private repo created (`interview-coach`)
- [ ] GitHub Personal Access Token generated and stored safely
- [ ] Make.com account (free tier supports up to 1,000 ops/month)
- [ ] Anthropic API key (for Claude calls)
- [ ] `/state/state_tracking.md` has `Job Search Criteria` section populated with:
  - Target roles (e.g., "Product Manager", "Senior PM")
  - Must-have signals (e.g., "B2B SaaS", "Series A-C")
  - Seniority range
  - Location preference
  - Company size/stage exclusions

---

## Workflow Architecture

```
[8:00 AM Trigger]
        ↓
[GitHub: Read state_index.md]
        ↓
[GitHub: Read state_tracking.md]
        ↓
[Anthropic API: Run jobs.md prompt]
        ↓
[Text Parser: Extract job entries]
        ↓
[GitHub: Update state_tracking.md with new jobs]
        ↓
[Notification: Email summary (optional)]
```

---

## Step-by-Step Setup in Make.com

### 1. Create a New Scenario

1. Go to **make.com** → click **Create a new scenario**
2. **Scenario name**: `Interview Coach — Daily Jobs`
3. Click **Create**

You'll see the blank scenario editor.

### 2. Add Schedule Trigger

1. Click the **+** icon in the center to add your first module
2. Search for **Schedule** module
3. Select **Schedule - Trigger an event at a specified time**
4. Configure:
   - **Frequency**: Daily
   - **Time**: 08:00 (8:00 AM)
   - **Repeat every**: 1 day
   - **Timezone**: Your local timezone
5. Click **OK**

### 3. Add GitHub Module 1: Read state_index.md

1. Click **+** to add a new module (to the right of Schedule)
2. Search for **GitHub**
3. Select **GitHub - Get file content**
4. **Connection**: Click **Add** to authenticate:
   - Choose **Personal Access Token** auth
   - **Token**: Paste your GitHub Personal Access Token
   - **Connection name**: `Interview Coach GitHub`
   - Click **Save**
5. Configure the module:
   - **Connection**: `Interview Coach GitHub`
   - **Repository owner**: Your GitHub username
   - **Repository name**: `interview-coach`
   - **File path**: `state/state_index.md`
6. Click **OK**
7. **Label this module**: `GitHub 1: Read state_index.md` (for clarity)

### 4. Add GitHub Module 2: Read state_tracking.md

1. Click **+** to add another module (to the right of Module 3)
2. Search for **GitHub**
3. Select **GitHub - Get file content**
4. Configure:
   - **Connection**: `Interview Coach GitHub` (reuse from step 3)
   - **Repository owner**: Your GitHub username
   - **Repository name**: `interview-coach`
   - **File path**: `state/state_tracking.md`
5. Click **OK**
6. **Label this module**: `GitHub 2: Read state_tracking.md`

### 5. Add HTTP Module: Call Anthropic API

1. Click **+** to add a new module (to the right of Module 4)
2. Search for **HTTP**
3. Select **HTTP - Make a request**
4. Configure:
   - **URL**: `https://api.anthropic.com/v1/messages`
   - **Method**: POST
   - **Headers**: Click **Add a header**:
     - Header 1: `x-api-key` = `[your-anthropic-api-key]`
     - Header 2: `anthropic-version` = `2023-06-01`
     - Header 3: `content-type` = `application/json`

   - **Body** (raw JSON): Copy the template below and customize:

```json
{
  "model": "claude-sonnet-4-20250514",
  "max_tokens": 2000,
  "system": "You are the Interview Coach job discovery engine. Your role is to surface 3 matching job roles that align with the candidate's search criteria. For each role, you must:\n\n1. Verify it matches ALL must-have signals\n2. Flag any nice-to-haves it includes\n3. Note any exclusions that disqualify it\n4. Provide a one-line fit assessment\n\nOutput format:\n## Job 1: [Role Title] at [Company]\n- **URL**: [job-posting-url]\n- **Fit Signal**: [why it matches]\n- **Interest**: Candidate to assess\n- **Notes**: [relevance notes]\n\n## Job 2: [Role Title] at [Company]\n[same format]\n\n## Job 3: [Role Title] at [Company]\n[same format]",
  "messages": [
    {
      "role": "user",
      "content": "# Active Job Search Criteria\n\nFrom state_index.md:\n{{ 1.data }}\n\n# Current Discovery Log & Criteria Details\n\nFrom state_tracking.md:\n{{ 2.data }}\n\n# Task\nRun daily job discovery. Find 3 NEW roles (not already in the discovery log) that match the criteria above. Return roles in the format specified in the system prompt."
    }
  ]
}
```

**Important**: Replace `{{ 1.data }}` and `{{ 2.data }}` with the Make.com variable references:
- `{{ 1.data }}` = output from GitHub Module 1 (state_index.md content)
- `{{ 2.data }}` = output from GitHub Module 2 (state_tracking.md content)

To insert variables:
1. Click in the Body field
2. Click **Add a variable** (top right of the field)
3. Select the correct module output

5. Click **OK**
6. **Label**: `Anthropic API: Run jobs.md`

### 6. Add Text Parser: Extract Job Entries

1. Click **+** to add a new module (to the right of Module 5)
2. Search for **Text Parser**
3. Select **Text Parser - Match Pattern**
4. Configure:
   - **Text**: Select output from HTTP module (Module 5)
   - Click **Add a variable** → select HTTP response body

   - **Pattern**: Copy this regex to extract job entries:
```
## Job \d+:(.+?)\n- \*\*URL\*\*: (.+?)\n- \*\*Fit Signal\*\*: (.+?)\n- \*\*Interest\*\*: (.+?)\n- \*\*Notes\*\*: (.+?)(?=## Job \d+:|$)
```

   - **Global match**: Toggle ON (to get all 3 jobs)

5. Click **OK**
6. **Label**: `Parser: Extract jobs`

### 7. Add Iterator: Loop Through Jobs

1. Click **+** to add a new module
2. Search for **Iterator**
3. Select **Iterator**
4. Configure:
   - **Array**: Select the output from Text Parser (Module 6) — the matched groups
5. Click **OK**
6. **Label**: `Iterator: Loop jobs`

### 8. Add GitHub Module 3: Update state_tracking.md

1. Click **+** inside the Iterator (to create a nested module)
2. Search for **GitHub**
3. Select **GitHub - Update file content**
4. Configure:
   - **Connection**: `Interview Coach GitHub`
   - **Repository owner**: Your GitHub username
   - **Repository name**: `interview-coach`
   - **File path**: `state/state_tracking.md`

   - **File content** (the new file body):
     - Fetch current content from Module 2 (state_tracking.md)
     - Append a new row to the `Job Discovery Log` table:
```
| {{ now | formatDate("YYYY-MM-DD") }} | [Company from iterator] | [Role from iterator] | [URL from iterator] | [Fit Signal from iterator] | maybe | [Notes] |
```

To construct this dynamically:
- Use Make.com's **map** function to extract job data from the iterator
- Append to the existing file content before the blank lines at the end
- Update `Last searched` date to today

**Tip**: Use a **Text** module before this to construct the new file content (concatenate old + new rows).

5. Click **OK**
6. **Label**: `GitHub 3: Update state_tracking.md`

### 9. (Optional) Add Email Notification

1. Click **+** outside the Iterator
2. Search for **Email**
3. Select **Email - Send an email**
4. Configure:
   - **Connection**: Click **Add** to connect your email (Gmail, Outlook, etc.)
   - **To**: Your email address
   - **Subject**: `Interview Coach: 3 new roles discovered`
   - **Body**:
```
Good morning! Here are 3 roles that match your search criteria:

{{ 6[].data }}

Check your coaching state for the full discovery log: /state/state_tracking.md

Happy hunting!
```

5. Click **OK**

---

## Testing the Workflow

1. **Save** the scenario (top-right corner)
2. Click **Run once** (bottom-left) to test immediately
3. **Check the execution**:
   - All modules should turn green (success)
   - Go to your GitHub repo and verify `state/state_tracking.md` was updated with new job rows
   - Check your email for the notification

### Troubleshooting Test Failures

**GitHub authentication fails**:
- Re-verify your Personal Access Token in Make.com
- Confirm the token has `repo` scope

**Anthropic API returns 401**:
- Verify your API key is correct
- Check it hasn't been revoked in the Anthropic console

**Parser extracts no matches**:
- Claude's response format may not match the expected regex
- Adjust the pattern to match Claude's actual output, or simplify the parse logic

**File update succeeds but no change in repo**:
- Verify the file path is correct (case-sensitive)
- Confirm the new file content includes the old content + appended rows

---

## Activating the Daily Schedule

Once testing passes:

1. **Save** the scenario
2. Click **Schedule** (left sidebar) to see the trigger
3. Toggle **Enabled** ON
4. The workflow will now run at 8:00 AM every day

---

## Monthly Cost Estimate

- **Operations**: ~10 ops per run (2 GitHub reads, 1 API call, 1 parse, 1 update)
- **Frequency**: Daily = 300 ops/month
- **Cost**: Free on the Make.com starter plan (1,000 ops/month included)

---

## Workflow Customization

### Change Discovery Frequency
- **Edit Schedule**: Change "Daily" to "3 times a week" (e.g., Mon/Wed/Fri)

### Add Multiple Slack Notifications
- Instead of email, add **Slack - Send a message** module
- Post to a dedicated `#job-search` channel

### Filter Jobs by Keywords
- Add a **Filter** module between Parser and Iterator:
  - **Condition**: Text from Parser contains "AI" OR "Machine Learning" (customize to your interests)

### Adjust API Model
- In the HTTP Body, change `claude-sonnet-4-20250514` to `claude-opus-4-1-20250805` for more in-depth analysis (costs more)

---

## Integration with Other Workflows

This workflow populates `/state/state_tracking.md`, which feeds into:
- **Follow-up Reminders** workflow (checks discovery log for stale entries)
- **Weekly Report** workflow (summarizes new jobs discovered)

Keep `Job Search Criteria` updated in `/state/state_tracking.md` to refine future discoveries.

---

## Summary

You've built a daily job discovery bot that:
- ✅ Reads your search criteria and discovery history
- ✅ Calls Claude to surface 3 matching roles
- ✅ Updates your coaching state with new job entries
- ✅ Notifies you by email (optional)
- ✅ Runs automatically every morning at 8:00 AM

**Next**: Proceed to `/make-workflows/follow-up-reminders.md` to set up the second workflow.
