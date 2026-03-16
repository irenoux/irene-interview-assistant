# Apple Shortcuts: Interview Day Hype Brief

**Shortcut name**: `Interview Day`
**Trigger**: Calendar automation — when event title contains "interview", fire 2 hours before
**Purpose**: Automatically generate a personalized hype brief 2 hours before your interview, with company-specific prep, hot stories, and last-minute confidence boosts
**Duration**: ~1 minute (shortcut execution)

---

## Pre-Requisites

- [ ] Apple Shortcuts app installed (iOS/Mac)
- [ ] Calendar with interview events (title must contain word "interview", e.g., "Interview: Google PM")
- [ ] Make.com account with a webhook-triggered workflow set up (Workflow 5)
- [ ] `/state/loops/active/[company].md` exists with interview context
- [ ] `/state/state_stories.md` exists with storybank

---

## Architecture

```
[Calendar event: "Interview: [Company]" scheduled]
        ↓
[2 hours before → Trigger Shortcut]
        ↓
[Shortcut: Extract company name from event]
        ↓
[Shortcut: Call Make.com webhook with company + time]
        ↓
[Make Workflow 5: Triggered]
        ├─ GitHub: Read /state/loops/active/[company].md
        ├─ GitHub: Read /state/state_stories.md
        └─ Anthropic API: Generate hype brief
        ↓
[Make: Email/push hype brief]
        ↓
[Shortcut: Show notification "Hype brief ready"]
```

---

## Part A: Create the Apple Shortcut

### Step 1: Open Shortcuts App

1. Open the **Shortcuts** app (iOS/macOS)
2. Click the **+** button (top right) to create a new shortcut
3. **Name**: `Interview Day`
4. Click **Add**

### Step 2: Add Calendar Automation Trigger

You'll build the trigger inside the shortcut itself.

1. In the empty shortcut, add the first action:
   - Search for **Ask for [Calendar Event]**
   - Or use **Get Calendar Events** to access scheduled events

**Alternative (Recommended)**: Use calendar automation directly:
1. Go to **Shortcuts → Automation** (bottom tab)
2. Click **Create Personal Automation** (or **+**)
3. Configure:
   - **Trigger**: Time of Day? **No**
   - **Trigger**: Calendar Event? **Yes**
   - **Calendar**: All Calendars
   - **Event Title**: Contains "interview"
   - **Notify before**: 2 hours
4. Click **Add Action**

You're now building the automation's action sequence.

### Step 3: Extract Company Name

Add an action to extract the company name from the calendar event title.

1. Search for **Text** → **Ask for Text**
   - **Prompt**: "Which company is this interview with?"
   - (This is a fallback if the shortcut can't parse the title)

**Or, to auto-extract**:
1. Search for **Text** → **Text**
   - Input: Calendar event title (e.g., "Interview: Google PM")
   - Use **Split Text** and **First item**:
   ```
   Split on: " - " or " at " or " with "
   Take: Last item (the company name)
   ```

2. Store in a variable: **Company** = extracted name

**Example flow**:
- Event title: `Interview: Google PM — Senior Product Manager`
- After split: ["Interview: Google PM", "Senior Product Manager"]
- Company = "Google PM" (or refine to just "Google")

### Step 4: Call Make.com Webhook

Add an HTTP request to trigger the Make workflow.

1. Search for **URL** → **Get contents of URL**
   - Or **Network** → **GET**
2. Configure:
   - **URL**: `https://hook.make.com/[your-webhook-id]` (you'll get this when setting up the Make workflow)
   - **Method**: POST
   - **Headers**:
     - `Content-Type`: `application/json`
   - **Request body** (JSON):
```json
{
  "company": "{{ Company }}",
  "time": "{{ Calendar event time }}",
  "timezone": "{{ Device timezone }}"
}
```

In Shortcuts, to insert variables:
- Click in the field and select the **Variable** icon (looks like a box with **x**)
- Choose **Company** (the variable you created in step 3)

3. Click **Request** (or **Add**)

### Step 5: Show Notification

Add a notification to confirm the hype brief is being generated.

1. Search for **Notification** → **Show Result**
   - Or **Show Notification** (iOS)
2. Configure:
   - **Title**: "Hype Brief Incoming"
   - **Message**: "Your brief for {{ Company }} is being prepared. Check your email in ~1 minute."
   - **Duration**: 5 seconds
3. Click **Add**

### Step 6: (Optional) Wait and Fetch Results

If you want the shortcut to wait for the Make workflow to complete and show the brief in-app:

1. Add **Wait** action
   - **Duration**: 90 seconds (to allow Make workflow time to complete)

2. Add another **Get contents of URL** action:
   - **URL**: A polling endpoint (would require a custom GitHub-based status API)
   - This is complex — usually better to just email the brief

For now, skip this step. The brief will come via email/push from Make.com.

---

## Part B: Create the Make.com Workflow (Workflow 5)

This is the backend that generates the actual hype brief.

### 1. Create a New Scenario in Make.com

1. Go to **make.com** → **Create a new scenario**
2. **Scenario name**: `Interview Coach — Hype Brief (Webhook)`
3. Click **Create**

### 2. Add Webhook Trigger

1. Click **+** to add the first module
2. Search for **Webhooks** → **Custom webhook**
3. Select **Webhooks - Trigger a scenario**
4. Configure:
   - **Webhook name**: `interview-hype-webhook`
5. Click **Save**
6. Make.com generates a webhook URL: `https://hook.make.com/[webhook-id]`
7. **Copy this URL** — you'll paste it into the Shortcut (step 4 above)

### 3. Add GitHub Module 1: Read Active Interview Context

1. Click **+** to add a module
2. Search for **GitHub** → **Get file content**
3. Configure:
   - **Connection**: `Interview Coach GitHub`
   - **Repository owner**: Your GitHub username
   - **Repository name**: `interview-coach`
   - **File path**: `state/loops/active/{{ company }}.md` (use the company variable from the webhook)
4. Click **OK**
5. **Label**: `GitHub 1: Read active interview`

The file should contain:
- Company name
- Role
- Round number
- Interviewer names (if known)
- Key questions (if any)
- Known concerns

### 4. Add GitHub Module 2: Read Storybank

1. Click **+** to add a module
2. Search for **GitHub** → **Get file content**
3. Configure:
   - **Connection**: `Interview Coach GitHub`
   - **File path**: `state/state_stories.md`
4. Click **OK**
5. **Label**: `GitHub 2: Read storybank`

### 5. Add HTTP Module: Call Anthropic API with Hype Prompt

1. Click **+** to add a module
2. Search for **HTTP** → **Make a request**
3. Configure:
   - **URL**: `https://api.anthropic.com/v1/messages`
   - **Method**: POST
   - **Headers**:
     - `x-api-key`: `[your-anthropic-api-key]`
     - `anthropic-version`: `2023-06-01`
     - `content-type`: `application/json`

   - **Body** (raw JSON):

```json
{
  "model": "claude-sonnet-4-20250514",
  "max_tokens": 2000,
  "system": "You are the Interview Coach hype brief generator. Your role is to deliver a focused, confidence-building brief 2 hours before an interview. The brief should:\n\n1. **Confidence Shot** (30 seconds): A personalized affirmation that reminds the candidate why they're strong for this role\n2. **Key Questions** (2 min): The top 3 questions likely to come up, with suggested frameworks\n3. **Hot Stories** (2 min): 2-3 of the candidate's strongest stories that are most relevant to this role\n4. **Interviewer Intel** (1 min): If known, what to expect from their interviewer(s)\n5. **Last-Minute Reminders** (1 min): Do's and don'ts from their coaching history\n\nTotal length: ~5-7 minutes to read.\n\nTone: Direct, energizing, zero fluff. Assume the candidate is calm and ready to go.",
  "messages": [
    {
      "role": "user",
      "content": "# Hype Brief Request\n\nInterview context:\n{{ 1.data }}\n\n## Available stories for this interview:\n{{ 2.data }}\n\n---\n\nGenerate a 5-7 minute hype brief for this interview. Use the format and guidelines from the system prompt. Lead with confidence, then tackle likely questions and top stories. Assume the candidate has {{ time }} before they need to be ready."
    }
  ]
}
```

4. Click **OK**
5. **Label**: `Anthropic API: Generate hype brief`

### 6. Add Email Module: Send Hype Brief

1. Click **+** to add a module
2. Search for **Email** → **Send an email**
3. Configure:
   - **Connection**: Your email account
   - **To**: Your email address
   - **Subject**: `🚀 Interview Hype Brief: {{ webhook_payload.company }}`
   - **Body**:

```
You have an interview with {{ webhook_payload.company }} in {{ webhook_payload.time }}. Here's your hype brief:

---

{{ 5.body.content[0].text }}

---

You've got this. Go crush it.

— Interview Coach
```

4. Click **OK**
5. **Label**: `Email: Send hype brief`

### 7. (Optional) Add Slack Notification

1. Click **+** after step 6
2. Search for **Slack** → **Send a message**
3. Configure:
   - **Workspace**: Your Slack workspace
   - **Channel**: Your personal DM or #interviews channel
   - **Message**:
```
🚀 Your interview with {{ webhook_payload.company }} is in {{ webhook_payload.time }}.

Hype brief sent to email. Ready? Let's go.
```

4. Click **OK**

---

## Testing the Shortcut

### Quick Test (Manual Trigger)

1. In the Shortcuts app, go to your `Interview Day` shortcut
2. Click the **▶** (play) button
3. The shortcut will:
   - Prompt you to enter company name (or auto-extract from clipboard)
   - Make the webhook call
   - Show a notification

4. Check your Make.com execution log to see if the workflow triggered
5. Check your email for the hype brief

### Full Test (Calendar Event)

1. Create a calendar event:
   - **Title**: "Interview: Google PM"
   - **Date/Time**: Tomorrow at 2:00 PM
2. The shortcut should trigger automatically at 12:00 PM (2 hours before)
3. Check:
   - Did the notification appear? ✅
   - Did the webhook trigger (check Make.com logs)? ✅
   - Did you receive the hype brief email? ✅

### Troubleshooting

**Shortcut doesn't trigger**:
- Verify calendar automation is enabled in Shortcuts settings
- Check that the event title contains "interview" (case-insensitive, but usually works)
- Manually test the shortcut with the play button

**Webhook doesn't trigger Make workflow**:
- Verify the webhook URL is correct (copy from Make.com step 2)
- Check the URL format: `https://hook.make.com/[webhook-id]`
- In Make.com, check the execution history for errors

**Hype brief doesn't arrive**:
- Check Make.com execution logs (step 5 HTTP request)
- Verify your Anthropic API key is valid
- Check spam folder for the email

**Company name not extracted**:
- Manually pass the company name in the shortcut
- Or refine the text-splitting logic in step 3

---

## Customization

### Change Trigger Time

Instead of 2 hours before, change to:
- **1 hour before**: Change "2 hours" to "1 hour" in the calendar automation
- **30 minutes before**: For a lightning-round brief
- **At event time**: For a final-minute confidence boost

### Add Interviewer-Specific Context

In GitHub Module 1 (step 3), check if the file includes interviewer LinkedIn profiles:
- If yes, pass them to the Anthropic prompt
- Claude can tailor the brief to known interviewer backgrounds

### Expand to Multiple Interview Rounds

Modify the shortcut to detect round number:
- Event title: "Interview: Google PM — Round 2 (System Design)"
- Pass round number to Make workflow
- Generate round-specific brief (e.g., system design focus)

### Add Slack-First Delivery

Instead of email, send the brief directly to Slack:
- Replace Email module (step 6) with Slack
- Include thread replies for follow-up messages

---

## Final Setup Checklist

- [ ] Apple Shortcut `Interview Day` created
- [ ] Calendar automation configured (contains "interview", 2 hours before)
- [ ] Make.com webhook URL copied and pasted into Shortcut step 4
- [ ] Make.com Workflow 5 created and saved
- [ ] GitHub connection configured in Make workflow
- [ ] Anthropic API key added to Make workflow
- [ ] Test calendar event created with "interview" in title
- [ ] Shortcut triggered automatically 2 hours before event
- [ ] Hype brief received via email
- [ ] Make.com execution log shows success

---

## Integration with Other Workflows

This shortcut feeds hype briefs in real-time, complementing:
- **Daily Jobs** (morning job discovery)
- **Follow-Up Reminders** (daily follow-up checks)
- **Weekly Report** (Sunday review)

Together, they create a complete automation loop:
- Morning: New job discovery + follow-up reminders
- Before interviews: Real-time hype briefs
- Weekly: Progress review
- Monthly: Calibration check

---

## Summary

You've built a real-time interview automation system that:
- ✅ Monitors your calendar for interview events
- ✅ Automatically triggers 2 hours before
- ✅ Pulls company context and your story bank
- ✅ Generates a personalized hype brief with Claude
- ✅ Delivers via email/Slack
- ✅ Shows a notification in your Shortcuts app

**Installation complete!**

You now have a fully automated Interview Coach ecosystem:
1. ✅ GitHub setup (`/github/README.md`)
2. ✅ Daily Jobs discovery (`/make-workflows/daily-jobs.md`)
3. ✅ Follow-Up Reminders (`/make-workflows/follow-up-reminders.md`)
4. ✅ Weekly Report (`/make-workflows/weekly-report.md`)
5. ✅ Monthly Eval (`/make-workflows/monthly-eval.md`)
6. ✅ Interview Day Shortcut (`/shortcuts/interview-morning.md`)

Next steps:
- Test each workflow in sequence
- Refine state files to match your coaching context
- Enable daily/weekly/monthly schedules
- Adjust notification preferences (email/Slack/push)
