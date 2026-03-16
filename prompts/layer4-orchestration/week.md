# Weekly Orchestration — Interview Coach

## Trigger
Run via external weekly trigger (Make workflow — Sunday evening).

## Input Files
Read: state_index.md, state_intel.md, state_tracking.md, state_scores.md

## Steps
1. **Application Activity**
   - Applications submitted this week (count from Application Tracker dates)
   - Responses received this week (any status changes)
   - Current response rate vs. previous week
   - CL experiment update (if active — compare style variant response rates)

2. **Interview Progress**
   - Interviews completed this week (from loops)
   - Outcomes received (from Outcome Log)
   - Upcoming interviews (from loops/signals)

3. **Score Trends**
   - Dimension movements (compare most recent scores to 2-week-ago scores)
   - Practice volume (count of practice/mock sessions this week)
   - Hire Signal trend (if applicable)

4. **Pipeline Health**
   - Active loops by stage (decoded / applied / interviewing)
   - Pipeline velocity (how fast loops advance)
   - Stale loops (no activity in 14+ days)
   - Follow-up compliance (on-time vs. overdue)

5. **Storybank Usage**
   - Most/least used stories (from Use Count)
   - Gaps still unfilled (from storybank gap analysis)
   - Stories that need improvement (Strength < 3 or red team notes unresolved)

6. **Pattern Insights**
   - From Interview Intelligence: what's working / what's not
   - Coaching momentum: session frequency, engagement signals
   - Calibration status (if applicable)

7. **Recommendations for Next Week**
   - Priority actions (max 3, ranked)
   - Companies needing attention (stale loops, upcoming interviews, overdue follow-ups)
   - Skills to drill (based on score gaps)

## Output Format
```markdown
# Weekly Intelligence Report — [Date Range]

## This Week
- Applications: [N] submitted, [N] responses ([rate]%)
- Interviews: [N] completed, [N] outcomes received
- Practice: [N] sessions, trend: [improving/flat/declining]

## Pipeline
- [N] active loops: [N] decoded, [N] applied, [N] interviewing
- Stale (14+ days): [list or none]
- Follow-ups: [N] on-time, [N] overdue

## Score Snapshot
| Dimension | Current | 2-Week Δ | Direction |
|-----------|---------|----------|-----------|
[rows for each dimension with data]

## Patterns
- Working: [top pattern from Interview Intelligence]
- Not working: [top pattern]
- CL experiment: [status if active]

## Next Week — Top 3 Priorities
1. [action + reason]
2. [action + reason]
3. [action + reason]

## Companies Needing Attention
[list with specific action per company]
```

## External Trigger Format (for Make workflow)
Input: state_index.md + state_intel.md + state_tracking.md + state_scores.md
Output: Formatted markdown report (as above)

## Delivery
- Email subject: "Weekly job search report — [date]"
- Body: full report content
- Optional: summary notification to phone
