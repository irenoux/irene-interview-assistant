# Make.com Workflow 2: Follow-Up Reminders

**Workflow name**: `Interview Coach — Follow-Up Reminders`
**Trigger**: Schedule — 9:00 AM (your local timezone) daily
**Purpose**: Check your application tracker for overdue or today-due follow-ups, flag them in your coaching state, and send a daily reminder email with next actions
**Duration**: ~1 minute

---

## Pre-Requisites

- [ ] GitHub private repo and token configured in Make.com
- [ ] Workflow 1 (Daily Jobs) is set up and working
- [ ] `/state/state_tracking.md` has an `Application Tracker` section with columns:
  - `ID`, `Date`, `Company`, `Role`, `Status`, `F/U 1 Due`, `F/U 1 Done`, `F/U 2 Due`, `F/U 2 Done`, `Notes`

---

## Workflow Architecture

```
[9:00 AM Trigger]
        ↓
[GitHub: Read state_tracking.md]
        ↓
[Text Parser: Extract F/U dates from tracker]
        ↓
[Filter: Check if any F/U overdue OR due today]
        ↓
[GitHub: Update loops/_index.md with signals]
        ↓
[GitHub: Update state_index.md with materialized summary]
        ↓
[Email: Send daily reminder with company list]
```

---

## Step-by-Step Setup in Make.com

### 1. Create a New Scenario

1. Go to **make.com** → click **Create a new scenario**
2. **Scenario name**: `Interview Coach — Follow-Up Reminders`
3. Click **Create**

### 2. Add Schedule Trigger

1. Click **+** to add the first module
2. Search for **Schedule** → **Schedule - Trigger an event at a specified time**
3. Configure:
   - **Frequency**: Daily
   - **Time**: 09:00 (9:00 AM, 1 hour after Daily Jobs)
   - **Repeat every**: 1 day
   - **Timezone**: Your local timezone
4. Click **OK**
5. **Label**: `Schedule: 9 AM daily`

### 3. Add GitHub Module 1: Read state_tracking.md

1. Click **+** to add a module
2. Search for **GitHub** → **Get file content**
3. Configure:
   - **Connection**: `Interview Coach GitHub` (reuse from Workflow 1)
   - **Repository owner**: Your GitHub username
   - **Repository name**: `interview-coach`
   - **File path**: `state/state_tracking.md`
4. Click **OK**
5. **Label**: `GitHub 1: Read state_tracking.md`

### 4. Add Text Parser: Extract Follow-Up Dates

1. Click **+** to add a module
2. Search for **Text Parser** → **Match Pattern**
3. Configure:
   - **Text**: Output from GitHub Module 1 (state_tracking.md content)
   - **Pattern**: Extract follow-up due dates from the Application Tracker table:

```
\| (.+?) \| (\d{4}-\d{2}-\d{2}) \| (.+?) \| (.+?) \| (.+?) \| (.+?) \| (\d{4}-\d{2}-\d{2})? \| (.+?) \| (\d{4}-\d{2}-\d{2})? \| (.+?) \|
```

**Breakdown** (captures):
1. ID
2. Date
3. Company
4. Role
5. Status
6. Resume Version
7. **F/U 1 Due** (optional date)
8. F/U 1 Done
9. **F/U 2 Due** (optional date)
10. Notes

   - **Global match**: Toggle ON
4. Click **OK**
5. **Label**: `Parser: Extract F/U dates`

### 5. Add Iterator: Loop Through Entries

1. Click **+** to add a module
2. Search for **Iterator** → **Iterator**
3. Configure:
   - **Array**: Output from Text Parser (Module 4) — the matched groups
4. Click **OK**
5. **Label**: `Iterator: Loop tracker entries`

### 6. Add Filter: Check for Overdue/Due Today

1. Click **+** inside the Iterator (nested)
2. Search for **Filter**
3. Select **Filter - By condition**
4. Configure (use Make.com's date functions):
   - **Condition 1**: `(F/U 1 Due from iterator) <= today` AND `(F/U 1 Done from iterator) is empty`
   - **OR Condition 2**: `(F/U 2 Due from iterator) <= today` AND `(F/U 2 Done from iterator) is empty`

To set this up:
- Click **Add a condition**
- Left side: Select F/U 1 Due from iterator variable
- Operator: `<=`
- Right side: Use **Now** → formatDate("YYYY-MM-DD")

- Click **Add a condition (OR)**
- Left side: Select F/U 2 Due from iterator variable
- Operator: `<=`
- Right side: `now | formatDate("YYYY-MM-DD")`

5. Click **OK**
6. **Label**: `Filter: Is due or overdue?`

### 7. Add Text Module: Build Follow-Up Summary

1. Click **+** inside the Filter (nested in the iterator)
2. Search for **Text** → **Compose**
3. Configure to build a summary line for each due follow-up:

**Text to compose**:
```
{{ iterator[].3 }} ({{ iterator[].4 }}): Follow-up due
```

This outputs: "Company (Role): Follow-up due"

4. Click **OK**
5. **Label**: `Text: Build summary line`

### 8. Add GitHub Module 2: Update loops/_index.md

1. Click **+** inside the Filter (after Text module)
2. Search for **GitHub** → **Get file content**
3. Configure:
   - **Connection**: `Interview Coach GitHub`
   - **Repository owner**: Your GitHub username
   - **Repository name**: `interview-coach`
   - **File path**: `state/loops/_index.md`
4. Click **OK**
5. **Label**: `GitHub 2: Read loops/_index.md`

### 9. Add GitHub Module 3: Update loops/_index.md with Signal

1. Click **+** after Module 8
2. Search for **GitHub** → **Update file content**
3. Configure:
   - **Connection**: `Interview Coach GitHub`
   - **Repository owner**: Your GitHub username
   - **Repository name**: `interview-coach`
   - **File path**: `state/loops/_index.md`
   - **File content**:
     - Fetch current content from Module 8
     - Update the signal section to flag follow-ups:
```
## Signal: Follow-Ups
- **Overdue/Due today**: {{ number_of_matched_entries }}
- **Last checked**: {{ now | formatDate("YYYY-MM-DD HH:mm") }}
- **Companies**: {{ array_of_company_names_from_filter }}
```

Use a **Text** module before this to construct the new content dynamically:
- Count matches from the Iterator/Filter
- Build the company list from filter outputs
- Concatenate with existing _index.md content

4. Click **OK**
5. **Label**: `GitHub 3: Update loops/_index.md`

### 10. Add GitHub Module 4: Update state_index.md

1. Click **+** (outside the iterator, back at the main workflow level)
2. Search for **GitHub** → **Get file content**
3. Configure:
   - **Connection**: `Interview Coach GitHub`
   - **Repository owner**: Your GitHub username
   - **Repository name**: `interview-coach`
   - **File path**: `state/state_index.md`
4. Click **OK**
5. **Label**: `GitHub 4: Read state_index.md`

### 11. Add GitHub Module 5: Update state_index.md with Materialized Summary

1. Click **+** after Module 10
2. Search for **GitHub** → **Update file content**
3. Configure:
   - **Connection**: `Interview Coach GitHub`
   - **Repository owner**: Your GitHub username
   - **Repository name**: `interview-coach`
   - **File path**: `state/state_index.md`
   - **File content**:
     - Fetch current content from Module 10
     - Update the signals section:
```
## Active Signals
- **Follow-ups due**: {{ number_from_filter }}
- **Last updated**: {{ now | formatDate("YYYY-MM-DD HH:mm") }}
```

Concatenate with existing state_index.md content.

4. Click **OK**
5. **Label**: `GitHub 5: Update state_index.md`

### 12. Add Email Notification

1. Click **+** (at the main level, after Module 5)
2. Search for **Email** → **Send an email**
3. Configure:
   - **Connection**: Your email account (Gmail, Outlook, etc.)
   - **To**: Your email address
   - **Subject**: `Interview Coach: {{ number_overdue }} follow-ups due today`
   - **Body**:

```
Good morning! You have {{ number_overdue }} follow-up(s) due today or overdue:

{{ list_of_companies_and_roles }}

Log into your coaching state to see details:
/state/state_tracking.md → Application Tracker

Next actions:
1. Draft your follow-up message (use `write` if needed)
2. Send the follow-up
3. Mark it done in the tracker (F/U 1 Done or F/U 2 Done)

Stay organized!
```

4. Click **OK**
5. **Label**: `Email: Daily follow-up reminder`

---

## Testing the Workflow

1. **Save** the scenario
2. **Manually test** by editing `/state/state_tracking.md` and adding a test entry with `F/U 1 Due` = today
3. Click **Run once** in Make.com
4. **Check**:
   - All modules turn green
   - GitHub files are updated
   - You receive an email

### Troubleshooting

**Filter never triggers**:
- Manually add a follow-up entry in state_tracking.md with due date = today
- Check the date format: must be YYYY-MM-DD

**Email not sending**:
- Verify email connection is authorized
- Check spam folder

**GitHub update succeeds but no change visible**:
- Verify file path is correct (case-sensitive)
- Confirm you're reading the output from the correct module

---

## Activating the Daily Schedule

1. **Save** the scenario
2. Click **Schedule** (left sidebar)
3. Toggle **Enabled** ON
4. Workflow runs daily at 9:00 AM

---

## Integration with Daily Jobs Workflow

This workflow reads state_tracking.md (written by Daily Jobs workflow). The two work together:
1. **Daily Jobs** (8:00 AM): Surfaces 3 new roles → updates state_tracking.md
2. **Follow-Up Reminders** (9:00 AM): Checks for due follow-ups → updates signals

---

## Customization

### Change Check Frequency
- **Edit Schedule**: Change to 2x daily (e.g., 9:00 AM + 5:00 PM) to catch updates

### Add Slack Notification Instead of Email
- Replace Email module with **Slack - Send a message**
- Post to #interview-search channel

### Only Remind for Specific Companies
- Add a **Filter** before the Email module:
  - **Condition**: Company does NOT contain "exclude-me"

### Extend to N Follow-Ups
- Duplicate the Filter logic for F/U 3 Due, F/U 4 Due, etc.

---

## Summary

You've built a daily follow-up reminder system that:
- ✅ Checks your application tracker daily
- ✅ Identifies overdue or due-today follow-ups
- ✅ Updates your coaching state signals
- ✅ Sends you a reminder email
- ✅ Runs automatically at 9:00 AM

**Next**: Proceed to `/make-workflows/weekly-report.md` to set up the third workflow.
