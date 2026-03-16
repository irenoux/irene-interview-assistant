# Daily Orchestration — Interview Coach

## Trigger
Run at session start OR via external daily trigger (Make workflow).

## Steps
1. Read state_index.md
2. Check signals:
   - Interview within 48h? → Load loops/active/[co].md → Generate hype brief
   - Follow-ups overdue? → Load state_tracking.md → List overdue items
   - Daily job search enabled + not searched today? → Run jobs workflow
3. Output: Brief signal summary for candidate greeting
4. Write: Update state_index.md signals, state_tracking.md Last searched date

## Signal Priority Order
1. Interview within 48h (highest urgency — time-sensitive prep)
2. Follow-ups overdue (relationship damage compounds daily)
3. Pending outcomes to ask about (keeps pipeline accurate)
4. Daily job discovery (routine — lowest urgency of triggered signals)

## Session Greeting Format
When signals are present, lead with them before the standard coaching recommendation:

**If interview within 48h:**
"You have an interview at [company] on [date]. Let's make sure you're ready. [hype brief or prep check]"

**If follow-ups overdue:**
"You have [N] follow-ups overdue: [company list]. Want to draft those now, or should we focus on [coaching recommendation] first?"

**If jobs found:**
"Found [N] new roles for you. Take a look, then we'll pick up where we left off."

**If no signals:**
Standard prescriptive recommendation from session-protocol.md.

## External Trigger Format (for Make workflow)
Input: state_index.md content + state_tracking.md content
Output: JSON with fields:
```json
{
  "jobs_found": [
    {"company": "", "role": "", "url": "", "fit_signal": ""}
  ],
  "follow_ups_due": [
    {"company": "", "days_overdue": 0}
  ],
  "hype_needed": "company_name or null",
  "tracking_updates": "string to append to state_tracking.md"
}
```

## State Updates
- state_index.md: refresh Signals section
- state_tracking.md: update Last searched date (if jobs ran)
- Job Discovery Log: append new entries (if jobs ran)
