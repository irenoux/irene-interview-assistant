# Make.com Workflows — Interview Coach Automation Suite

This directory contains setup guides for 5 automated workflows that power the Interview Coach system. Together, they create a complete interview prep and job search automation loop.

---

## Workflow Overview

| # | Name | Trigger | Purpose | Cost/Month | Status |
|---|------|---------|---------|-----------|--------|
| 1 | **Daily Jobs** | 8:00 AM daily | Surface 3 matching roles based on your criteria | ~$0.01 | `/daily-jobs.md` |
| 2 | **Follow-Up Reminders** | 9:00 AM daily | Flag overdue/due-today follow-ups | ~$0.01 | `/follow-up-reminders.md` |
| 3 | **Weekly Report** | Sunday 7:00 PM | Generate comprehensive weekly summary (Batch API) | ~$0.005 | `/weekly-report.md` |
| 4 | **Monthly Eval** | 1st of month, 8:00 AM | Re-calibrate scoring with 15 reference evals (Batch API) | ~$0.01 | `/monthly-eval.md` |
| 5 | **Hype Brief** | On-demand + Calendar | Generate 2-hour-before interview brief | ~$0.02 per use | `/interview-morning.md` (Shortcuts) |

**Total monthly cost**: ~$0.05 on Make.com free tier (1,000 ops/month) + Anthropic API usage (~$0.02-0.05 depending on usage).

---

## Prerequisites (All Workflows)

Before setting up any workflow, ensure:

- [ ] GitHub private repo created (`interview-coach`)
- [ ] GitHub Personal Access Token generated (scope: `repo`)
- [ ] Anthropic API key obtained (from console.anthropic.com)
- [ ] Make.com account (free tier supports 1,000 ops/month)
- [ ] State files populated (`/state/` directory)

---

## Setup Sequence

1. **Start with GitHub** → `/github/README.md`
   - Create private repo
   - Configure `.gitignore`
   - Commit project structure
   - Generate Personal Access Token

2. **Workflow 1: Daily Jobs** → `/daily-jobs.md`
   - Reads your job search criteria
   - Calls Claude to find 3 matching roles
   - Updates your discovery log
   - Sends email notification
   - **Foundational**: Other workflows depend on this

3. **Workflow 2: Follow-Up Reminders** → `/follow-up-reminders.md`
   - Checks application tracker for due follow-ups
   - Updates coaching signals
   - Sends daily reminder
   - **Light-weight**: Depends on state_tracking.md from Workflow 1

4. **Workflow 3: Weekly Report** → `/weekly-report.md`
   - Synthesizes coaching state
   - Uses Batch API (~50% cost savings)
   - Generates comprehensive summary
   - **Batch-first pattern**: Model for complex reports

5. **Workflow 4: Monthly Eval** → `/monthly-eval.md`
   - Scores 5 reference answers
   - Detects calibration drift
   - Flags alerts if needed
   - **Calibration check**: Essential for coaching reliability

6. **Workflow 5: Hype Brief (Shortcuts)** → `/interview-morning.md`
   - Apple Shortcuts automation
   - Triggered by calendar events
   - Uses Make.com webhook
   - **Real-time engagement**: Event-driven

---

## Architecture Diagram

```
GitHub Repo (Single Source of Truth)
├── /state/state_index.md
├── /state/state_tracking.md
├── /state/state_stories.md
├── /state/state_intel.md
└── /state/active/[company].md

                ↑
    [All workflows read/write here]
                ↑

┌─────────────────────────────────────────────────────────┐
│         Make.com Automation Suite                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Daily Jobs (8:00 AM)                                  │
│  └─ Read: state_index, state_tracking                  │
│  └─ Write: state_tracking (new jobs)                   │
│                                                         │
│  Follow-Up Reminders (9:00 AM)                         │
│  └─ Read: state_tracking                               │
│  └─ Write: state_index (signals), loops/_index.md      │
│                                                         │
│  Weekly Report (Sunday 7:00 PM)                        │
│  └─ Read: state_index, state_intel, state_tracking    │
│  └─ Write: /reports/[date]-week.md                     │
│                                                         │
│  Monthly Eval (1st, 8:00 AM)                           │
│  └─ Read: /eval/golden/my-references.md                │
│  └─ Write: /eval/results/[date]-run.md                 │
│                                                         │
│  Hype Brief (Webhook + Calendar)                       │
│  └─ Read: state/active/[company], state_stories        │
│  └─ No writes (read-only)                              │
│                                                         │
└─────────────────────────────────────────────────────────┘

                ↓
    [Notifications via Email/Slack/Push]
                ↓
            You (Candidate)
```

---

## Workflow Dependencies

```
Daily Jobs (1)
    ↓ (writes state_tracking.md)
    ↓
Follow-Up Reminders (2)
    ↓ (reads & writes state_index.md)
    ↓
Weekly Report (3)
    ↓ (synthesizes all state)
    ↓
Monthly Eval (4)
    ↓ (standalone calibration check)

Calendar Events
    ↓
Hype Brief (5)
    ↓ (real-time, independent)
```

**Independence**: Workflow 5 (Hype Brief) is independent and can run at any time.

---

## API Keys & Credentials Needed

### GitHub Token
- **Where to store**: Make.com connection (steps in each workflow)
- **Scope**: `repo` (full control of private repos)
- **Expiration**: 90 days (renew quarterly) or no expiration

### Anthropic API Key
- **Where to store**: Make.com HTTP headers
- **Usage**: All HTTP → Anthropic API modules
- **Cost**: ~$3 per 1M input tokens, ~$12 per 1M output tokens
- **Estimate**: ~1,000 tokens per daily job discovery = ~$0.003/day

### Make.com Webhook URL
- **Generated by**: Workflow 5 (Hype Brief)
- **Used by**: Apple Shortcut
- **Format**: `https://hook.make.com/[webhook-id]`
- **Security**: Webhook is scoped — requires exact URL match

---

## Cost Breakdown

| Workflow | Operations/Month | API Calls/Month | Est. Cost |
|----------|------------------|-----------------|-----------|
| Daily Jobs | 300 (10 ops × 30 days) | 30 Claude calls | $0.01 |
| Follow-Up Reminders | 300 (10 ops × 30 days) | 0 (no API calls) | $0.00 |
| Weekly Report | 4 (batch per week) | 4 Claude calls | $0.005 |
| Monthly Eval | 1 (15 reqs in batch) | 15 Claude calls | $0.01 |
| Hype Brief | ~10 per month (on demand) | 10 Claude calls | $0.02 |

**Total Make.com**: Free tier (1,000 ops/month easily covers ~614 ops)
**Total Anthropic**: ~$0.055/month (under free tier limits if not at 100% usage)

---

## Monitoring & Observability

### Make.com Execution History
- Go to each scenario → **Execution history** tab
- View logs for every run
- Errors surface here first

### GitHub Activity
- Monitor commits in your repo's commit log
- Each workflow auto-commits state updates
- Verify file updates match expected changes

### Notifications
- Check email/Slack for workflow outputs
- Non-arrival of expected notification = workflow failed
- Review Make.com execution history for error details

### State File Changes
- Pull latest `/state/` files from GitHub
- Compare Last updated timestamps
- Ensure workflows are writing successfully

---

## Troubleshooting Guide

### "All modules succeed but no GitHub update"
1. Check Make.com HTTP module response
2. Verify GitHub token hasn't expired (GitHub → Settings → Developer settings)
3. Confirm file path is correct (case-sensitive)
4. Regenerate GitHub token if older than 90 days

### "Anthropic API returns 401 Unauthorized"
1. Verify API key is correct (copy from console.anthropic.com)
2. Check that key hasn't been revoked
3. Ensure headers are: `x-api-key: [key]`, `anthropic-version: 2023-06-01`, `content-type: application/json`

### "Workflow triggers but produces empty results"
1. Verify GitHub file content is valid markdown/JSON
2. Check that Claude's response format matches expected parsing pattern
3. Test Claude directly in the Anthropic console with same prompt

### "Email notifications not arriving"
1. Check spam folder (Gmail, Outlook, etc.)
2. Verify email connection is still authorized in Make.com
3. Test with a simple text email first (no variables) to isolate

### "Batch API job stays 'processing' for >10 minutes"
- Normal: Batch API can take 5-60 minutes. Increase poll sleep duration (step 8 in each batch workflow) to 5 minutes
- Add a max-retry counter to prevent infinite loops (optional)

---

## Customization Examples

### Run Jobs Discovery at Different Times
- **Default**: 8:00 AM daily
- **Alternative**: 3x per week (Mon/Wed/Fri)
- **Alternative**: 2x daily (8:00 AM + 5:00 PM)

Edit: Workflow 1 → Schedule module → change frequency

### Extend Follow-Up Reminders to 3rd Follow-Up
- **Current**: F/U 1 and F/U 2
- **Extended**: Add F/U 3 and F/U 4
- **How**: Duplicate Filter logic in Workflow 2 for additional F/U columns

### Change Report Cadence
- **Default**: Weekly (Sunday 7:00 PM)
- **Alternative**: Every 2 weeks or biweekly
- **How**: Edit Schedule in Workflow 3

### Add Slack Notifications to All Workflows
- **Current**: Email only
- **Extended**: Add Slack modules after Email in each workflow
- **Cost**: Same (Slack is free within Make.com's ops count)

---

## Advanced Topics

### Batch API vs. Synchronous

| Aspect | Sync | Batch |
|--------|------|-------|
| **Speed** | 1-5 sec | 5-60 min |
| **Cost** | 100% | 50% |
| **Use case** | Real-time | Scheduled/reports |
| **Max requests** | 1 | 10,000 |

**Strategy**: Use Batch for weekly/monthly reports. Use Sync for daily/on-demand.

### Webhook Security

Webhooks are public URLs, but:
- Only `https://hook.make.com/[exact-id]` accepts requests
- Even with the URL, the Make workflow validates the payload schema
- Rate-limiting is implicit (Make.com limits concurrent executions)

### GitHub API Rate Limits

Make.com doesn't use GitHub API directly (uses file content endpoints), so rate limits are higher. No special handling needed unless you're committing 100+ times per day.

### Parallel vs. Sequential Execution

- **Workflows 1-2-3-4 are sequential** (each writes what the next reads)
- **Workflow 5 is parallel** (independent, can run anytime)
- **To run in parallel**: Make.com supports concurrent scenario executions — no conflicts expected

---

## Maintenance Checklist

### Weekly
- [ ] Check Make.com execution history for errors
- [ ] Verify GitHub commits are happening
- [ ] Spot-check state files for data freshness

### Monthly
- [ ] Review Calibration Eval results (Workflow 4)
- [ ] Check API usage in Anthropic console
- [ ] Rotate GitHub token (if expiration policy is <90 days)

### Quarterly
- [ ] Review cost breakdown
- [ ] Assess whether workflows are delivering value
- [ ] Update job search criteria if job market changed
- [ ] Archive old state files (backup to local)

---

## Integration with Claude Code

These workflows are **complementary** to Claude Code (the main coaching interface):

| Component | Role |
|-----------|------|
| **Claude Code** | Real-time coaching (you ask questions, Claude coaches) |
| **Workflows** | Automation (background operations, state management, scheduled reports) |

**Example session**:
1. You run `jobs` in Claude Code → manually review & add to Application Tracker
2. Workflow 2 (Follow-Up) runs daily → reminds you of due follow-ups
3. You run `practice` in Claude Code → Workflow 4 uses same rubric for calibration
4. Workflow 3 (Weekly Report) summarizes progress from all coaching sessions

---

## Summary

You now have:

✅ **5 automated workflows**:
- Daily job discovery
- Follow-up reminders
- Weekly progress report
- Monthly calibration check
- Real-time interview hype brief

✅ **GitHub as single source of truth**:
- All state centralized
- Version-controlled
- Backup & audit trail

✅ **Minimal cost**:
- ~$0.05/month on Make.com (free tier)
- ~$0.05/month on Anthropic API
- Total: ~$0.10/month

✅ **Extensible architecture**:
- Easy to add new workflows
- Can customize triggers, frequencies, notifications
- Batch API for cost efficiency on complex reports

---

## Next Steps

1. **Immediate**: Follow `/github/README.md` to set up GitHub
2. **Day 1-2**: Set up Workflow 1 (Daily Jobs) and test
3. **Day 2-3**: Add Workflow 2 (Follow-Up Reminders)
4. **Day 3-4**: Add Workflow 3 (Weekly Report)
5. **Day 4-5**: Add Workflow 4 (Monthly Eval)
6. **Day 5+**: Set up Workflow 5 (Hype Brief) and Apple Shortcuts

---

## Support & Troubleshooting

For each workflow, refer to the corresponding markdown file:
- **Daily Jobs**: `/daily-jobs.md` → section "Troubleshooting Test Failures"
- **Follow-Up Reminders**: `/follow-up-reminders.md` → section "Troubleshooting"
- **Weekly Report**: `/weekly-report.md` → section "Troubleshooting"
- **Monthly Eval**: `/monthly-eval.md` → section "Troubleshooting"
- **Hype Brief**: `/interview-morning.md` → section "Troubleshooting"

---

## FAQ

**Q: Can I run workflows without GitHub?**
A: No. GitHub is the single source of truth. Workflows read/write state files there.

**Q: Do I need all 5 workflows?**
A: No. Start with Daily Jobs + Follow-Up Reminders (most valuable). Add Weekly Report + Monthly Eval later.

**Q: What if I don't have an Anthropic API key?**
A: Use the `claude-opus` model in Claude Code instead. Workflows can use the Free/Pro tier via API key. Not recommended for long-term (API key gives you cost control).

**Q: Can I run these on schedule if my computer is off?**
A: Yes. Make.com runs in the cloud — doesn't depend on your computer being on.

**Q: What timezone are the schedules in?**
A: You configure it during setup. Usually your local timezone.

**Q: How do I disable a workflow?**
A: In Make.com, go to the scenario → toggle the Schedule module OFF. Scenario still exists, just won't execute.

---

**Happy automating!**
