# Make.com Workflow 4: Monthly Eval (Batch API with Calibration)

**Workflow name**: `Interview Coach — Monthly Eval`
**Trigger**: Schedule — 1st of every month, 8:00 AM
**Purpose**: Re-calibrate your coaching system by scoring 5 reference answers (3 rubric dimensions each, 15 requests total in one batch) to detect scoring drift and ensure reliability
**Duration**: ~5 minutes (real-time) + ~5-10 minutes (batch processing)

---

## Pre-Requisites

- [ ] GitHub repo and token configured in Make.com
- [ ] Anthropic API key with Batch API access
- [ ] `/eval/golden/my-references.md` exists with 5 reference answers (pre-scored)
- [ ] `/eval/results/baseline.md` exists with baseline calibration data
- [ ] `/prompts/layer3-commands/rubrics/rubrics-full.md` exists with detailed rubric

---

## Why Monthly Calibration?

Coaching quality depends on consistent, reliable scoring. Over time, a coach's scoring can "drift" — becoming more generous, stricter, or inconsistent. This workflow:

1. **Re-scores your 5 reference answers** using the official rubric
2. **Compares to your baseline** (established in your first session)
3. **Flags drift**: If any dimension's standard deviation > 0.3 or mean shift > 0.3, it triggers an alert
4. **Updates your coaching state** to flag recalibration needed

This is especially important for Interview Coach because calibration affects all downstream coaching (practice scores, mock scores, analysis feedback).

---

## Workflow Architecture

```
[1st of month, 8:00 AM Trigger]
        ↓
[GitHub: Read my-references.md (5 reference answers)]
        ↓
[GitHub: Read baseline.md (your baseline scores)]
        ↓
[GitHub: Read rubrics-full.md (scoring instructions)]
        ↓
[HTTP: Submit Batch with 15 scoring requests]
        ↓ (5 answers × 3 dimensions each)
        ↓
[Sleep + Poll (same as weekly report)]
        ↓
[HTTP: Get Batch Results (15 scores)]
        ↓
[Calculate: Mean + SD per dimension per answer]
        ↓
[Compare to Baseline]
        ↓
[Router: If drift detected, flag as ALERT]
        ↓
[GitHub: Create eval results file]
        ↓
[GitHub: Update state_index.md with alert (if drift)]
        ↓
[Email: Send results (alert if needed)]
```

---

## Step-by-Step Setup in Make.com

### 1. Create a New Scenario

1. Go to **make.com** → **Create a new scenario**
2. **Scenario name**: `Interview Coach — Monthly Eval`
3. Click **Create**

### 2. Add Schedule Trigger

1. Click **+** to add the first module
2. Search for **Schedule** → **Schedule - Trigger an event at a specified time**
3. Configure:
   - **Frequency**: Monthly
   - **Day of month**: 1
   - **Time**: 08:00 (8:00 AM)
   - **Timezone**: Your local timezone
4. Click **OK**
5. **Label**: `Schedule: 1st of month, 8 AM`

### 3. Add GitHub Module 1: Read my-references.md

1. Click **+** to add a module
2. Search for **GitHub** → **Get file content**
3. Configure:
   - **Connection**: `Interview Coach GitHub`
   - **Repository owner**: Your GitHub username
   - **Repository name**: `interview-coach`
   - **File path**: `eval/golden/my-references.md`
4. Click **OK**
5. **Label**: `GitHub 1: Read my-references.md`

**Expected format** in my-references.md:
```markdown
# Reference Answers (Golden Calibration Set)

## Answer 1: [Title]
[Full candidate answer here]

## Answer 2: [Title]
[Full candidate answer here]

[... 3 more answers ...]
```

### 4. Add GitHub Module 2: Read baseline.md

1. Click **+** to add a module
2. Search for **GitHub** → **Get file content**
3. Configure:
   - **Connection**: `Interview Coach GitHub`
   - **File path**: `eval/results/baseline.md`
4. Click **OK**
5. **Label**: `GitHub 2: Read baseline.md`

**Expected format** in baseline.md:
```markdown
# Calibration Baseline

| Answer | Substance | Structure | Relevance | Credibility | Differentiation | Mean |
|--------|-----------|-----------|-----------|-------------|-----------------|------|
| A1 | 4.0 | 3.8 | 4.2 | 4.1 | 3.9 | 4.0 |
| A2 | 3.5 | 3.7 | 3.6 | 3.8 | 3.4 | 3.6 |
| ... | ... | ... | ... | ... | ... | ... |
```

### 5. Add GitHub Module 3: Read rubrics-full.md

1. Click **+** to add a module
2. Search for **GitHub** → **Get file content**
3. Configure:
   - **File path**: `prompts/layer3-commands/rubrics/rubrics-full.md`
4. Click **OK**
5. **Label**: `GitHub 3: Read rubrics-full.md`

### 6. Add HTTP Module: Submit Batch (15 Scoring Requests)

1. Click **+** to add a module
2. Search for **HTTP** → **Make a request**
3. Configure:
   - **URL**: `https://api.anthropic.com/v1/messages/batches`
   - **Method**: POST
   - **Headers**:
     - `x-api-key`: `[your-anthropic-api-key]`
     - `anthropic-version`: `2023-06-01`
     - `content-type`: `application/json`

   - **Body** (raw JSON): Copy the full template below:

```json
{
  "requests": [
    {
      "custom_id": "eval-a1-substance",
      "params": {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 500,
        "system": "You are a rigorous interview coaching evaluator. Your role is to score a candidate's answer on a single dimension using a provided rubric.\n\nDimension: Substance\nDefinition: Evidence quality and depth — are claims backed by specific examples? Is there enough detail to understand the situation, choices, and impact?\n\nScore 1-5 using the anchors provided. Return ONLY a JSON object with: {\"dimension\": \"Substance\", \"score\": N, \"reasoning\": \"brief explanation\"}\n\nRubric anchors:\n{{ 3.data | extractSection('## Substance') }}",
        "messages": [
          {
            "role": "user",
            "content": "Score this answer on the Substance dimension:\n\n{{ extractAnswerN(1.data, 1) }}"
          }
        ]
      }
    },
    {
      "custom_id": "eval-a1-structure",
      "params": {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 500,
        "system": "You are a rigorous interview coaching evaluator. Your role is to score a candidate's answer on a single dimension using a provided rubric.\n\nDimension: Structure\nDefinition: Narrative clarity and flow — is the story told in a logical order? Can the listener follow the arc?\n\nScore 1-5 using the anchors provided. Return ONLY a JSON object with: {\"dimension\": \"Structure\", \"score\": N, \"reasoning\": \"brief explanation\"}\n\nRubric anchors:\n{{ 3.data | extractSection('## Structure') }}",
        "messages": [
          {
            "role": "user",
            "content": "Score this answer on the Structure dimension:\n\n{{ extractAnswerN(1.data, 1) }}"
          }
        ]
      }
    },
    {
      "custom_id": "eval-a1-relevance",
      "params": {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 500,
        "system": "You are a rigorous interview coaching evaluator. Your role is to score a candidate's answer on a single dimension using a provided rubric.\n\nDimension: Relevance\nDefinition: Question fit and focus — does this answer address what was asked? Is the response focused or wandering?\n\nScore 1-5 using the anchors provided. Return ONLY a JSON object with: {\"dimension\": \"Relevance\", \"score\": N, \"reasoning\": \"brief explanation\"}\n\nRubric anchors:\n{{ 3.data | extractSection('## Relevance') }}",
        "messages": [
          {
            "role": "user",
            "content": "Score this answer on the Relevance dimension:\n\n{{ extractAnswerN(1.data, 1) }}"
          }
        ]
      }
    },
    {
      "custom_id": "eval-a2-substance",
      "params": {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 500,
        "system": "You are a rigorous interview coaching evaluator. Your role is to score a candidate's answer on a single dimension using a provided rubric.\n\nDimension: Substance\n\nScore 1-5 using the anchors provided. Return ONLY a JSON object with: {\"dimension\": \"Substance\", \"score\": N, \"reasoning\": \"brief explanation\"}\n\nRubric anchors:\n{{ 3.data | extractSection('## Substance') }}",
        "messages": [
          {
            "role": "user",
            "content": "Score this answer on the Substance dimension:\n\n{{ extractAnswerN(1.data, 2) }}"
          }
        ]
      }
    },
    {
      "custom_id": "eval-a2-structure",
      "params": {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 500,
        "system": "You are a rigorous interview coaching evaluator.\n\nDimension: Structure\n\nScore 1-5. Return JSON: {\"dimension\": \"Structure\", \"score\": N, \"reasoning\": \"...\"}\n\nRubric:\n{{ 3.data | extractSection('## Structure') }}",
        "messages": [
          {
            "role": "user",
            "content": "Score this answer on the Structure dimension:\n\n{{ extractAnswerN(1.data, 2) }}"
          }
        ]
      }
    },
    {
      "custom_id": "eval-a2-relevance",
      "params": {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 500,
        "system": "You are a rigorous interview coaching evaluator.\n\nDimension: Relevance\n\nScore 1-5. Return JSON: {\"dimension\": \"Relevance\", \"score\": N, \"reasoning\": \"...\"}\n\nRubric:\n{{ 3.data | extractSection('## Relevance') }}",
        "messages": [
          {
            "role": "user",
            "content": "Score this answer on the Relevance dimension:\n\n{{ extractAnswerN(1.data, 2) }}"
          }
        ]
      }
    },
    {
      "custom_id": "eval-a3-substance",
      "params": {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 500,
        "system": "Evaluate on Substance. Return JSON: {\"dimension\": \"Substance\", \"score\": N, \"reasoning\": \"...\"}\n\n{{ 3.data | extractSection('## Substance') }}",
        "messages": [
          {
            "role": "user",
            "content": "{{ extractAnswerN(1.data, 3) }}"
          }
        ]
      }
    },
    {
      "custom_id": "eval-a3-structure",
      "params": {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 500,
        "system": "Evaluate on Structure. Return JSON: {\"dimension\": \"Structure\", \"score\": N, \"reasoning\": \"...\"}\n\n{{ 3.data | extractSection('## Structure') }}",
        "messages": [
          {
            "role": "user",
            "content": "{{ extractAnswerN(1.data, 3) }}"
          }
        ]
      }
    },
    {
      "custom_id": "eval-a3-relevance",
      "params": {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 500,
        "system": "Evaluate on Relevance. Return JSON: {\"dimension\": \"Relevance\", \"score\": N, \"reasoning\": \"...\"}\n\n{{ 3.data | extractSection('## Relevance') }}",
        "messages": [
          {
            "role": "user",
            "content": "{{ extractAnswerN(1.data, 3) }}"
          }
        ]
      }
    },
    {
      "custom_id": "eval-a4-substance",
      "params": {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 500,
        "system": "Evaluate on Substance. Return JSON: {\"dimension\": \"Substance\", \"score\": N, \"reasoning\": \"...\"}\n\n{{ 3.data | extractSection('## Substance') }}",
        "messages": [
          {
            "role": "user",
            "content": "{{ extractAnswerN(1.data, 4) }}"
          }
        ]
      }
    },
    {
      "custom_id": "eval-a4-structure",
      "params": {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 500,
        "system": "Evaluate on Structure. Return JSON: {\"dimension\": \"Structure\", \"score\": N, \"reasoning\": \"...\"}\n\n{{ 3.data | extractSection('## Structure') }}",
        "messages": [
          {
            "role": "user",
            "content": "{{ extractAnswerN(1.data, 4) }}"
          }
        ]
      }
    },
    {
      "custom_id": "eval-a4-relevance",
      "params": {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 500,
        "system": "Evaluate on Relevance. Return JSON: {\"dimension\": \"Relevance\", \"score\": N, \"reasoning\": \"...\"}\n\n{{ 3.data | extractSection('## Relevance') }}",
        "messages": [
          {
            "role": "user",
            "content": "{{ extractAnswerN(1.data, 4) }}"
          }
        ]
      }
    },
    {
      "custom_id": "eval-a5-substance",
      "params": {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 500,
        "system": "Evaluate on Substance. Return JSON: {\"dimension\": \"Substance\", \"score\": N, \"reasoning\": \"...\"}\n\n{{ 3.data | extractSection('## Substance') }}",
        "messages": [
          {
            "role": "user",
            "content": "{{ extractAnswerN(1.data, 5) }}"
          }
        ]
      }
    },
    {
      "custom_id": "eval-a5-structure",
      "params": {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 500,
        "system": "Evaluate on Structure. Return JSON: {\"dimension\": \"Structure\", \"score\": N, \"reasoning\": \"...\"}\n\n{{ 3.data | extractSection('## Structure') }}",
        "messages": [
          {
            "role": "user",
            "content": "{{ extractAnswerN(1.data, 5) }}"
          }
        ]
      }
    },
    {
      "custom_id": "eval-a5-relevance",
      "params": {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 500,
        "system": "Evaluate on Relevance. Return JSON: {\"dimension\": \"Relevance\", \"score\": N, \"reasoning\": \"...\"}\n\n{{ 3.data | extractSection('## Relevance') }}",
        "messages": [
          {
            "role": "user",
            "content": "{{ extractAnswerN(1.data, 5) }}"
          }
        ]
      }
    }
  ]
}
```

**Setup note**:
- This batch contains 15 requests (5 answers × 3 dimensions)
- Each request includes the relevant rubric section (via extractSection helper)
- Make.com will merge the variables from modules 1 and 3

4. Click **OK**
5. **Label**: `HTTP: Submit batch (15 evals)`

### 7. Add Sleep Module (60 seconds)

1. Click **+** to add a module
2. Search for **Sleep**
3. Configure: **Delay**: 60 seconds
4. Click **OK**
5. **Label**: `Sleep: Wait for batch`

### 8. Add HTTP Module: Poll Batch Status

1. Click **+** to add a module
2. Search for **HTTP** → **Make a request**
3. Configure:
   - **URL**: `https://api.anthropic.com/v1/messages/batches/{{ 6.body.id }}`
   - **Method**: GET
   - **Headers**:
     - `x-api-key`: `[your-anthropic-api-key]`
     - `anthropic-version`: `2023-06-01`
4. Click **OK**
5. **Label**: `HTTP: Poll batch status`

### 9. Add Router: Check Status

1. Click **+** to add a module
2. Search for **Router**
3. Configure routes:
   - **Route 1 (succeeded)**: `{{ 8.body.processing_status }} == "succeeded"`
   - **Route 2 (processing)**: `{{ 8.body.processing_status }} == "processing"` → loop back to step 7
   - **Route 3 (failed)**: `{{ 8.body.processing_status }} == "failed"` → send error email
4. Click **OK**
5. **Label**: `Router: Check status`

### 10. Add HTTP Module: Get Batch Results

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

### 11. Add Code Module: Calculate Mean + SD

1. Click **+** after step 10
2. Search for **Code** → **Execute JavaScript**
3. Configure JavaScript to:
   - Parse the 15 batch results
   - Extract scores from each result's JSON response
   - Group by answer and dimension
   - Calculate mean and standard deviation per dimension per answer

**Sample JavaScript**:
```javascript
const results = {{ 10.body.results }};
const scores = {};

results.forEach(r => {
  const custom_id = r.custom_id; // e.g., "eval-a1-substance"
  const match = custom_id.match(/eval-a(\d+)-(\w+)/);
  if (match) {
    const answer = 'A' + match[1];
    const dimension = match[2];
    const score = JSON.parse(r.result.message.content[0].text).score;

    if (!scores[answer]) scores[answer] = {};
    if (!scores[answer][dimension]) scores[answer][dimension] = [];
    scores[answer][dimension].push(score);
  }
});

const summary = {};
Object.keys(scores).forEach(answer => {
  summary[answer] = {};
  Object.keys(scores[answer]).forEach(dim => {
    const vals = scores[answer][dim];
    const mean = vals.reduce((a, b) => a + b, 0) / vals.length;
    const sd = Math.sqrt(
      vals.reduce((sq, n) => sq + Math.pow(n - mean, 2), 0) / vals.length
    );
    summary[answer][dim] = { mean: mean.toFixed(2), sd: sd.toFixed(2) };
  });
});

return summary;
```

4. Click **OK**
5. **Label**: `Code: Calculate stats`

### 12. Add Code Module: Compare to Baseline

1. Click **+** after step 11
2. Search for **Code** → **Execute JavaScript**
3. Configure to compare current scores to baseline (from Module 2):
   - Flag if any dimension: `|current_mean - baseline_mean| > 0.3` OR `sd > 0.3`
   - Return drift alert status

**Sample JavaScript**:
```javascript
const current = {{ 11.output }};
const baseline = {{ 2.data }}; // Parsed as table

const drift = [];
Object.keys(current).forEach(answer => {
  Object.keys(current[answer]).forEach(dim => {
    const curr_mean = parseFloat(current[answer][dim].mean);
    const curr_sd = parseFloat(current[answer][dim].sd);
    const baseline_score = parseFloat(baseline[answer][dim]); // From table

    const shift = Math.abs(curr_mean - baseline_score);
    if (shift > 0.3 || curr_sd > 0.3) {
      drift.push({
        answer,
        dimension: dim,
        current_mean: curr_mean,
        baseline_score,
        shift,
        sd: curr_sd,
        flagged: true
      });
    }
  });
});

return {
  drift_detected: drift.length > 0,
  drift_items: drift,
  drift_count: drift.length
};
```

4. Click **OK**
5. **Label**: `Code: Detect drift`

### 13. Add Text Module: Build Report

1. Click **+** after step 12
2. Search for **Text** → **Compose**
3. Configure to build the eval report:

```
# Calibration Eval — {{ now | formatDate("YYYY-MM-DD") }}

## Summary

Total Requests: 15 (5 answers × 3 dimensions)
Drift Detected: {{ 12.output.drift_detected }}
Drift Count: {{ 12.output.drift_count }}

## Current Scores

{{ 11.output | formatAsTable }}

## Comparison to Baseline

{{ 12.output.drift_items | formatAsTable }}

{{ if 12.output.drift_detected }}
### ALERT: Calibration Drift Detected

You have {{ 12.output.drift_count }} dimension(s) showing significant drift from baseline. Review flagged items above.

Recommendation: Run a coaching recalibration session. Check which dimensions are drifting and why.
{{ endif }}

---
Report generated {{ now | formatDate("dddd, MMMM D, YYYY [at] h:mm A") }}
```

4. Click **OK**
5. **Label**: `Text: Build report`

### 14. Add GitHub Module: Create eval results file

1. Click **+** after step 13
2. Search for **GitHub** → **Create a file**
3. Configure:
   - **Connection**: `Interview Coach GitHub`
   - **Repository owner**: Your GitHub username
   - **Repository name**: `interview-coach`
   - **File path**: `eval/results/{{ now | formatDate("YYYY-MM-DD") }}-run.md`
   - **File content**: {{ 13.output }}
4. Click **OK**
5. **Label**: `GitHub: Create eval results`

### 15. Add Router: Check for Drift Alert

1. Click **+** after step 14
2. Search for **Router**
3. Configure routes:
   - **Route 1 (drift found)**: `{{ 12.output.drift_detected }} == true`
   - **Route 2 (no drift)**: `{{ 12.output.drift_detected }} == false`
4. Click **OK**
5. **Label**: `Router: Drift detected?`

### 16. (Route 1: Drift) Add GitHub Module: Update state_index.md

1. Click **+** in the "drift found" route
2. Search for **GitHub** → **Get file content** first to fetch current state_index.md
3. Then **Update file content**:
   - **File path**: `state/state_index.md`
   - **File content** (append alert):
```
## ⚠️ ALERT: Calibration Drift Detected

Run date: {{ now | formatDate("YYYY-MM-DD") }}
Drift items: {{ 12.output.drift_count }}

Details in: /eval/results/{{ now | formatDate("YYYY-MM-DD") }}-run.md

Action: Review evaluation results and recalibrate if drift exceeds acceptable threshold.
```

4. Click **OK**
5. **Label**: `GitHub: Update state_index (alert)`

### 17. (Route 1: Drift) Add Email: Send Alert

1. Click **+** after step 16 (in drift route)
2. Search for **Email** → **Send an email**
3. Configure:
   - **To**: Your email address
   - **Subject**: `⚠️ Interview Coach: Calibration Drift Detected`
   - **Body**:
```
Your monthly calibration eval has detected significant scoring drift.

Drift items: {{ 12.output.drift_count }}

Details:
{{ 12.output.drift_items | formatAsTable }}

Full report: /eval/results/{{ now | formatDate("YYYY-MM-DD") }}-run.md

Recommendation: Run a coaching recalibration session to realign your scoring.

Next steps:
1. Review the flagged dimensions
2. Practice scoring on known answers
3. Reset baseline if needed
```

4. Click **OK**
5. **Label**: `Email: Drift alert`

### 18. (Route 2: No Drift) Add Email: Success

1. Click **+** in the "no drift" route
2. Search for **Email** → **Send an email**
3. Configure:
   - **To**: Your email address
   - **Subject**: `✅ Interview Coach: Calibration Stable`
   - **Body**:
```
Your monthly calibration eval shows no significant drift. Your scoring remains reliable.

Report: /eval/results/{{ now | formatDate("YYYY-MM-DD") }}-run.md

Keep coaching!
```

4. Click **OK**
5. **Label**: `Email: All clear`

---

## Testing the Workflow

1. **Prepare test data**:
   - Add 5 reference answers to `/eval/golden/my-references.md`
   - Create a baseline in `/eval/results/baseline.md` with initial scores
   - Ensure `/prompts/layer3-commands/rubrics/rubrics-full.md` exists

2. **Save** the scenario and run once

3. **Monitor**:
   - Batch submits (step 6) → captures batch_id ✅
   - Poll (step 8) waits for results
   - When complete, 15 scores extracted
   - Stats calculated (step 11)
   - Drift detection runs (step 12)
   - Report created (step 14)
   - Email sent (step 17 or 18) ✅

### Troubleshooting

**Batch takes >10 minutes to complete**:
- Increase sleep duration (step 7) to 5 minutes
- Batch API can take up to 60 minutes during peak load

**Scores parse as null**:
- Verify Claude's JSON response format
- Check extractSection helper in system prompt

**Drift always detected or never detected**:
- Verify threshold (0.3) in step 12 code
- Compare baseline values to actual results manually

---

## Activating the Monthly Schedule

1. **Save** the scenario
2. Click **Schedule** (left sidebar)
3. Toggle **Enabled** ON
4. Workflow runs on the 1st of every month at 8:00 AM

---

## Cost Estimate

- **15 scoring requests per month**: ~150 tokens input, 500 tokens output per request
- **Cost**: ~$0.01 per month on Batch API (vs. ~$0.02 on synchronous)
- **Annual**: ~$0.12

---

## Customization

### Add More Reference Answers

- Increase from 5 to 10 answers
- Change batch to 30 requests (10 × 3 dimensions)
- Update step 11-12 JavaScript to handle more answers

### Adjust Drift Thresholds

- Change 0.3 threshold to 0.5 (more lenient) or 0.2 (stricter) in step 12 code

### Score Additional Dimensions

- Add Credibility, Differentiation to the batch
- Change batch size to 25 requests (5 × 5 dimensions)

### Integrate with Progress Workflow

- If drift detected, automatically schedule a recalibration coaching session

---

## Integration with Other Workflows

This workflow ensures the calibration used by:
- **Practice** sessions (score calibration)
- **Mock** interviews (score calibration)
- **Analyze** (score calibration)

A drift alert signals that all downstream scoring may be unreliable.

---

## Summary

You've built a monthly calibration system that:
- ✅ Scores 5 reference answers on 3 dimensions (15 requests)
- ✅ Calculates mean and standard deviation per dimension
- ✅ Detects scoring drift from baseline
- ✅ Flags alerts and updates coaching state
- ✅ Emails you results
- ✅ Uses Batch API for cost savings (~50%)
- ✅ Runs automatically on the 1st of each month

**Next**: Proceed to `/shortcuts/interview-morning.md` to set up Apple Shortcuts automation.
