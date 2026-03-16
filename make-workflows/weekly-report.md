# Make.com Workflow 3: Weekly Report (Batch API)

**Workflow name**: `Interview Coach — Weekly Report`
**Trigger**: Schedule — Sunday 7:00 PM (your local timezone)
**Purpose**: Generate a comprehensive weekly summary of your interview progress, job search activity, and coaching signals using Claude's Batch API (50% cheaper than synchronous calls)
**Duration**: ~2 minutes (real-time) + ~5 minutes (batch processing, runs asynchronously)

---

## Pre-Requisites

- [ ] GitHub repo and token configured in Make.com
- [ ] Anthropic API key with **Batch API** access enabled
- [ ] `/state/state_index.md`, `/state/state_intel.md`, `/state/state_tracking.md` populated
- [ ] Make.com account with Batch Request support (standard on all plans)

---

## Why Use the Batch API?

- **Cost**: ~50% cheaper than standard API calls
- **Latency**: Results come back in 5-60 minutes (asynchronous)
- **Use case**: Weekly/monthly reports that don't need immediate results
- **Limit**: Supports up to 10,000 requests per batch job

For this workflow, we submit 1 large request (your full coaching state → Claude analysis) and poll for results in ~5 minutes.

---

## Workflow Architecture

```
[Sunday 7:00 PM Trigger]
        ↓
[GitHub: Read state_index.md]
        ↓
[GitHub: Read state_intel.md]
        ↓
[GitHub: Read state_tracking.md]
        ↓
[HTTP: Submit Batch Request to Anthropic]
        ↓ (returns batch_id)
        ↓
[Sleep: 60 seconds]
        ↓
[HTTP: Poll Batch Status]
        ↓
[Router: If batch complete, get results]
        ↓     (else loop back to sleep)
        ↓
[HTTP: Get Batch Results]
        ↓
[GitHub: Create weekly report file]
        ↓
[Email: Send report summary]
```

---

## Step-by-Step Setup in Make.com

### 1. Create a New Scenario

1. Go to **make.com** → **Create a new scenario**
2. **Scenario name**: `Interview Coach — Weekly Report`
3. Click **Create**

### 2. Add Schedule Trigger

1. Click **+** to add the first module
2. Search for **Schedule** → **Schedule - Trigger an event at a specified time**
3. Configure:
   - **Frequency**: Weekly
   - **Day of week**: Sunday
   - **Time**: 19:00 (7:00 PM)
   - **Timezone**: Your local timezone
4. Click **OK**
5. **Label**: `Schedule: Sunday 7 PM`

### 3. Add GitHub Module 1: Read state_index.md

1. Click **+** to add a module
2. Search for **GitHub** → **Get file content**
3. Configure:
   - **Connection**: `Interview Coach GitHub`
   - **Repository owner**: Your GitHub username
   - **Repository name**: `interview-coach`
   - **File path**: `state/state_index.md`
4. Click **OK**
5. **Label**: `GitHub 1: Read state_index.md`

### 4. Add GitHub Module 2: Read state_intel.md

1. Click **+** to add a module
2. Search for **GitHub** → **Get file content**
3. Configure:
   - **Connection**: `Interview Coach GitHub`
   - **Repository owner**: Your GitHub username
   - **Repository name**: `interview-coach`
   - **File path**: `state/state_intel.md`
4. Click **OK**
5. **Label**: `GitHub 2: Read state_intel.md`

### 5. Add GitHub Module 3: Read state_tracking.md

1. Click **+** to add a module
2. Search for **GitHub** → **Get file content**
3. Configure:
   - **Connection**: `Interview Coach GitHub`
   - **Repository owner**: Your GitHub username
   - **Repository name**: `interview-coach`
   - **File path**: `state/state_tracking.md`
4. Click **OK**
5. **Label**: `GitHub 3: Read state_tracking.md`

### 6. Add HTTP Module: Submit Batch Request

1. Click **+** to add a module
2. Search for **HTTP** → **Make a request**
3. Configure:
   - **URL**: `https://api.anthropic.com/v1/messages/batches`
   - **Method**: POST
   - **Headers**: Add three headers:
     - `x-api-key`: `[your-anthropic-api-key]`
     - `anthropic-version`: `2023-06-01`
     - `content-type`: `application/json`

   - **Body** (raw JSON): Copy the full template below:

```json
{
  "requests": [
    {
      "custom_id": "weekly-report-1",
      "params": {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 4000,
        "system": "You are the Interview Coach analysis engine. Your role is to generate a comprehensive weekly report for a candidate currently in their job search and interview preparation.\n\nThe report should include:\n\n1. **Progress Summary**: Key metrics from the week (interviews completed, roles applied, outcomes)\n2. **Interview Performance**: Trends in scoring dimensions (Substance, Structure, Relevance, Credibility, Differentiation)\n3. **Job Search Activity**: New roles discovered, applications sent, follow-ups due\n4. **Coaching Signals**: Active concerns, patterns detected, recommended focus areas\n5. **Next Week Priorities**: Top 3 action items for maximum impact\n\nBe concise, data-driven, and actionable. Lead with signals and recommendations.",
        "messages": [
          {
            "role": "user",
            "content": "# Weekly Report Request\n\nToday's date: {{ now | formatDate(\"YYYY-MM-DD\") }}\n\n## Coaching State Summary\n\n### state_index.md\n{{ 1.data }}\n\n### state_intel.md\n{{ 2.data }}\n\n### state_tracking.md\n{{ 3.data }}\n\n---\n\nGenerate a comprehensive weekly report based on the coaching state above. Focus on:\n- Progress this week (new interviews, applications, outcomes)\n- Performance trends (are scores improving?)\n- Job search momentum (roles found, applications sent)\n- Coaching signals (what should the candidate focus on next?)\n- Top 3 priorities for next week\n\nFormat as markdown with clear sections. Be actionable."
          }
        ]
      }
    }
  ]
}
```

**Key points**:
- Replace `{{ 1.data }}`, `{{ 2.data }}`, `{{ 3.data }}` with Make.com variables from the three GitHub modules
- Replace `[your-anthropic-api-key]` with your actual API key
- The batch request format wraps one large analysis request

4. Click **OK**
5. **Label**: `HTTP: Submit Batch Request`

**After submitting, Make.com will capture the response**, which contains:
```json
{
  "id": "msgbatch_...",
  "type": "message_batch",
  "processing_status": "processing",
  "request_counts": {...},
  ...
}
```

### 7. Add Text Module: Extract Batch ID

1. Click **+** to add a module
2. Search for **Text** → **Extract** (or **Compose**)
3. Configure:
   - Extract the `id` field from the HTTP response
   - Pattern: `"id":"([^"]+)"`
4. Click **OK**
5. **Label**: `Text: Extract batch_id`

**Alternative** (simpler): Use the module output mapping in Make.com to directly reference `{{ 6.body.id }}` later.

### 8. Add Sleep Module

1. Click **+** to add a module
2. Search for **Sleep**
3. Select **Sleep**
4. Configure:
   - **Delay**: 60 seconds
5. Click **OK**
6. **Label**: `Sleep: Wait for batch`

### 9. Add HTTP Module: Poll Batch Status

1. Click **+** to add a module
2. Search for **HTTP** → **Make a request**
3. Configure:
   - **URL**: `https://api.anthropic.com/v1/messages/batches/{{ 6.body.id }}` (use the batch_id from step 6)
   - **Method**: GET
   - **Headers**:
     - `x-api-key`: `[your-anthropic-api-key]`
     - `anthropic-version`: `2023-06-01`
4. Click **OK**
5. **Label**: `HTTP: Poll batch status`

This returns:
```json
{
  "id": "msgbatch_...",
  "processing_status": "processing" | "succeeded" | "failed",
  "result_counts": {
    "succeeded": N,
    "errored": N,
    "expired": N
  },
  ...
}
```

### 10. Add Router: Check Batch Status

1. Click **+** to add a module
2. Search for **Router**
3. Select **Router** (flow control)
4. Configure routes:
   - **Route 1 (succeeded)**: `{{ 9.body.processing_status }} == "succeeded"`
     - Continue to step 11 (get results)
   - **Route 2 (still processing)**: `{{ 9.body.processing_status }} == "processing"`
     - Loop back to step 8 (sleep another 60s)
   - **Route 3 (failed)**: `{{ 9.body.processing_status }} == "failed"`
     - Send error email and stop

5. Click **OK**
6. **Label**: `Router: Check batch status`

**To loop back to sleep**:
- In Route 2, add a **Go to** module pointing back to step 8
- Or use **Repeat** to retry

### 11. Add HTTP Module: Get Batch Results

1. Click **+** in the "succeeded" route (from Router)
2. Search for **HTTP** → **Make a request**
3. Configure:
   - **URL**: `https://api.anthropic.com/v1/messages/batches/{{ 6.body.id }}/results`
   - **Method**: GET
   - **Headers**:
     - `x-api-key`: `[your-anthropic-api-key]`
     - `anthropic-version`: `2023-06-01`
4. Click **OK**
5. **Label**: `HTTP: Get batch results`

This returns an array of results:
```json
{
  "results": [
    {
      "custom_id": "weekly-report-1",
      "result": {
        "type": "succeeded",
        "message": {
          "content": [
            {
              "type": "text",
              "text": "[Claude's analysis here]"
            }
          ]
        }
      }
    }
  ]
}
```

### 12. Add Text Module: Extract Report Content

1. Click **+** after step 11
2. Search for **Text** → **Compose**
3. Configure:
   - Extract the text content from the batch result
   - Pattern or manual extraction: `{{ 11.body.results[0].result.message.content[0].text }}`
4. Click **OK**
5. **Label**: `Text: Extract report content`

### 13. Add GitHub Module: Create Weekly Report File

1. Click **+** after step 12
2. Search for **GitHub** → **Create a file** (or **Update file content** if the file exists)
3. Configure:
   - **Connection**: `Interview Coach GitHub`
   - **Repository owner**: Your GitHub username
   - **Repository name**: `interview-coach`
   - **File path**: `reports/{{ now | formatDate("YYYY-MM-DD") }}-week.md` (e.g., `reports/2026-03-15-week.md`)
   - **File content**:
```
# Weekly Report — {{ now | formatDate("YYYY-MM-DD") }}

Generated by Interview Coach Automation

---

{{ 12.output }}

---

*Report generated on {{ now | formatDate("dddd, MMMM D, YYYY [at] h:mm A") }}*
```

4. Click **OK**
5. **Label**: `GitHub: Create weekly report`

### 14. Add Email Module: Send Report Summary

1. Click **+** after step 13
2. Search for **Email** → **Send an email**
3. Configure:
   - **To**: Your email address
   - **Subject**: `Interview Coach Weekly Report — {{ now | formatDate("YYYY-MM-DD") }}`
   - **Body**:
```
Your weekly report is ready!

{{ 12.output }}

Full report saved to:
/reports/{{ now | formatDate("YYYY-MM-DD") }}-week.md

Review your coaching state for more detail:
- /state/state_index.md (signals)
- /state/state_tracking.md (applications + jobs)
- /state/state_intel.md (questions + patterns)

See you next week!
```

4. Click **OK**
5. **Label**: `Email: Send weekly report`

---

## Testing the Workflow

1. **Save** the scenario
2. Click **Run once** to test immediately (don't wait for Sunday)
3. **Monitor the execution**:
   - Step 6 (HTTP Batch) succeeds → captures batch_id ✅
   - Step 8 (Sleep) waits 60 seconds ✅
   - Step 9 (Poll) checks status ✅
   - If status is "processing", Router loops back to step 8
   - When status is "succeeded", step 11 fetches results ✅
   - Step 13 creates `/reports/[date]-week.md` in GitHub ✅
   - Step 14 emails you the summary ✅

### Troubleshooting

**Batch status never changes to "succeeded"**:
- Batch API can take 5-60 minutes. Increase sleep duration (step 8) to 5 minutes
- Add a max-retries counter to prevent infinite loops

**Results are empty**:
- Check the batch result structure in the HTTP response
- Verify the extraction pattern in step 12

**Email doesn't contain report**:
- Verify the text extraction in step 12 is working
- Check email body template references correct module output

---

## Activating the Weekly Schedule

1. **Save** the scenario
2. Click **Schedule** (left sidebar)
3. Toggle **Enabled** ON
4. Workflow runs every Sunday at 7:00 PM

---

## Cost Comparison: Batch vs. Synchronous

| Metric | Synchronous API | Batch API | Savings |
|--------|-----------------|-----------|---------|
| Price per 1M input tokens | $3 | $1.50 | 50% |
| Price per 1M output tokens | $12 | $6 | 50% |
| Latency | 1-5 seconds | 5-60 minutes | N/A |
| Use case | Real-time | Batch/scheduled | — |

For a 3,000-token report request:
- **Synchronous**: ~$0.01 per week
- **Batch**: ~$0.005 per week

Savings over a year: ~$0.26 (or more if you scale to multiple reports).

---

## Customization

### Add Multiple Reports in One Batch

Modify step 6 to submit 2-3 requests in one batch:
```json
{
  "requests": [
    {
      "custom_id": "weekly-report-full",
      "params": { ... }
    },
    {
      "custom_id": "weekly-summary-short",
      "params": { ... }
    }
  ]
}
```

Then extract both results in step 11.

### Increase Polling Frequency

- Change step 8 (Sleep) from 60 to 10 seconds for faster turnaround
- Or change Router to retry after 5 minutes if still processing

### Add Slack Notification

- Replace Email (step 14) with **Slack - Send a message**
- Post to a #coaching-reports channel

### Generate Multiple Report Formats

- Add a second request in the batch to generate a short summary
- Create two files: `[date]-week.md` (full) and `[date]-week-summary.md` (short)

---

## Integration with Other Workflows

This workflow reads state files updated by:
- **Daily Jobs** (updates state_tracking.md with discoveries)
- **Follow-Up Reminders** (updates signals in state_index.md)

The weekly report synthesizes all activity into a single narrative.

---

## Summary

You've built a weekly analysis system that:
- ✅ Collects coaching state from GitHub
- ✅ Submits a batch request to Claude (50% cost savings)
- ✅ Polls asynchronously for results
- ✅ Creates a weekly report file in GitHub
- ✅ Emails you a summary
- ✅ Runs automatically every Sunday at 7:00 PM

**Next**: Proceed to `/make-workflows/monthly-eval.md` to set up the fourth workflow.
