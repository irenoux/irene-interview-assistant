# State Schema Reference

## Schema Migration
After reading any state file, check for missing sections/columns from current schema.
Migrate silently — add missing fields with empty/default values.
Do not announce migrations unless they affect coaching recommendations.

---

## state_profile.md Schema

### Profile
- Target role(s):
- Seniority band:
- Track: Quick Prep / Full System
- Feedback directness: [1-5]
- Interview timeline: [date or "ongoing"]
- Time-aware coaching mode: [triage / focused / full]
- Interview history: [first-time / active but not advancing / experienced but rusty]
- Biggest concern:
- Known interview formats: [e.g., "behavioral screen, system design (verbal walkthrough)" — updated by Format Discovery Protocol]
- Anxiety profile: [confident-underprepared / anxious-specific / generalized / post-rejection / impostor — set by hype]
- Career transition: [none / function change / domain shift / IC↔management / industry pivot / career restart]
- Transition narrative status: [not started / in progress / solid]

### Resume Analysis
- Positioning strengths: [2-3 signals a hiring manager sees in 30 seconds]
- Likely interviewer concerns: [flagged from resume — gaps, short tenures, domain switches, seniority mismatches]
- Career narrative gaps: [transitions that need a story ready]
- Story seeds: [resume bullets with likely rich stories behind them]

### LinkedIn Analysis
- Date, Depth: [Quick Audit / Standard / Deep Optimization]
- Overall, Recruiter discoverability, Credibility on visit, Differentiation: [Strong / Moderate / Weak]
- Top fixes pending, Positioning gaps

### Resume Optimization
- Date, Depth: [Quick Audit / Standard / Deep Optimization]
- Overall: [Strong / Needs Work / Weak]
- ATS compatibility: [ATS-Ready / ATS-Risky / ATS-Broken]
- Recruiter scan, Bullet quality, Seniority calibration, Keyword coverage: [Strong / Moderate / Weak]
- Top fixes pending, JD-targeted: [yes — which JD / no], Cross-surface gaps

### Positioning Statement
- Date, Depth: [Quick Draft / Standard / Deep Positioning]
- Core statement: [30-45 second version]
- Hook (10s): [curiosity-gap opener]
- Key differentiator, Earned secret anchor, Target audience, Variant status, Consistency status

### Comp Strategy
- Date, Depth: [Quick Script / Standard / Deep Strategy]
- Target range: [bottom / target / stretch]
- Range basis, Research completeness: [none / partial / thorough]
- Stage coached, Jurisdiction notes, Scripts provided, Key principle

### Coaching Notes
Freeform: [date]: [observation — preferences, emotional patterns, interview anxieties, scheduling preferences]

### Meta-Check Log
| Session | Candidate Feedback | Adjustment Made |

---

## state_stories.md Schema

### Storybank Table
| ID | Title | Primary Skill | Secondary Skill | Earned Secret | Strength | Use Count | Last Used |

### Story Details (per story)
#### S### — [Title]
- Situation:
- Task:
- Action:
- Result:
- Earned Secret:
- Deploy for: [one-line use case]
- Red team notes:
- Version history: [date — what changed]

---

## state_scores.md Schema

### Score History
#### Historical Summary
[Narrated trend summary when table exceeds 15 rows — direction per dimension, inflection points, coaching changes that triggered shifts]

#### Recent Scores
| Date | Type | Context | Sub | Str | Rel | Cred | Diff | Hire Signal | Self-Δ |
Type: interview/practice/mock. Sub=Substance, Str=Structure, Rel=Relevance, Cred=Credibility, Diff=Differentiation — each 1-5.
Hire Signal: Strong Hire/Hire/Mixed/No Hire (from analyze/mock only — blank for practice).
Self-Δ: over/under/accurate (>0.5 delta = over or under; within 0.5 = accurate).

### Outcome Log
| Date | Company | Role | Round | Result | Notes |
Result: advanced/rejected/pending/offer/withdrawn

### Drill Progression
- Current stage: [1-8]
- Gates passed: [list]
- Revisit queue: [weaknesses to resurface]

---

## state_intel.md Schema

### Interview Intelligence
#### Question Bank
| Date | Company | Role | Round Type | Question | Competency | Score | Outcome |
Round Type: behavioral/technical/system-design/case-study/bar-raiser/culture-fit.
Score: average across 5 dims, or "recall-only" for debrief-captured.
Outcome: advanced/rejected/pending/unknown.

#### Effective Patterns
- [date]: [pattern + evidence]

#### Ineffective Patterns
- [date]: [pattern + evidence]

#### Recruiter/Interviewer Feedback
| Date | Company | Source | Feedback | Linked Dimension |

#### Company Patterns
Per company: questions observed, what seems to matter, stories that landed/didn't, last updated.

#### Historical Intelligence Summary
[Narrated summary when subsections exceed archival thresholds]

### Active Coaching Strategy
- Primary bottleneck: [dimension]
- Current approach: [what + how]
- Rationale: [why — links to data]
- Pivot if: [conditions]
- Root causes detected: [list]
- Self-assessment tendency: [over-rater / under-rater / well-calibrated]
- Previous approaches: [list with brief reason for abandoning]

### Calibration State
- Current calibration: [uncalibrated / calibrating / calibrated / miscalibrated]
- Last calibration check: [date]
- Data points available: [N]
- Scoring Drift Log: | Date | Dimension | Direction | Evidence | Adjustment |
- Calibration Adjustments: | Date | Trigger | What Changed | Rationale |
- Cross-Dimension Root Causes: | Root Cause | Affected Dimensions | First Detected | Status | Treatment |
- Unmeasured Factor Investigations: | Date | Trigger | Hypothesis | Investigation | Finding | Action |

---

## state_tracking.md Schema

### Job Search Criteria
- Last updated, Daily search: [enabled/disabled], Last searched
- Track definitions (Track 1: VC/PE, Track 2: Consulting/Accelerator, Track 3: PM)
- Source priority tiers, Pre-screen filter
- Search notes, Refined from feedback count, Refinement log

### Job Discovery Log
| Date | Company | Role | URL | Fit Signal | Interest | Notes |
Interest: yes / no / maybe.

### Application Tracker
| ID | Date | Company | Role | Resume Version | Method | Cover Letter | Status | Response Date | Response Type | F/U 1 Due | F/U 1 Done | F/U 2 Due | F/U 2 Done | Notes |
Method: job-board / referral / direct-outreach / recruiter-inbound.
Status: Applied / Screen Scheduled / Phone Screen Done / Loop Scheduled / Offer / Rejected / Withdrawn / Likely Closed.

### Application Analytics
Total apps, response rate, most effective resume/method, CL impact, avg time to response, stage conversion, last update date.

### Application Follow-up Framework
Wave timing, timing by company type, when a person is cited, per-company F/U notes.

### Outreach Strategy
Date, Depth, Positioning source, Message types coached, Targets contacted, Channel strategy, Follow-up status, LinkedIn profile flagged, Key hooks.

### Session Log
#### Historical Summary
[Brief narrative of earlier sessions when log exceeds 15 rows]
#### Recent Sessions
| Date | Commands Run | Key Outcomes |

### Past JD Analyses (archived)
| Date | Company | Role | Fit Verdict |

---

## loops/active/[company].md Schema

### Loop Details
- Status: [Decoded / Researched / Applied / Interviewing / Offer / Closed]
- Role:
- Track:
- Rounds completed: [list with dates]
- Round formats: [per round: format, duration, interviewer type]
- Stories used: [S### per round]
- Concerns surfaced: [ranked — severity + counter strategy]
- Interviewer intel: [LinkedIn URLs + key insights, linked to rounds]
- Prepared questions: [top 3 from questions if run]
- Next round: [date, format]
- Fit verdict: [Strong / Investable Stretch / Long-Shot Stretch / Weak]
- Fit confidence: [Limited — no JD / Medium — JD + resume / High — JD + resume + storybank]
- Fit signals: [1-2 lines]
- Structural gaps: [gaps that can't be bridged with narrative]
- Date researched: [date]

### Application Status (if applied)
- Application ID, Date Applied, Resume Version, Cover Letter, ATS Score, Follow-up Status

### JD Analysis (if decoded)
- Date, Depth, Fit verdict, Top competencies, Frameable gaps, Structural gaps
- Unverified assumptions, Batch triage rank, Story fit, URL, Decision

### Presentation Prep (if applicable)
- Date, Depth, Framework, Time target, Content status, Top predicted questions, Key adjustment

### File Size Cap
When > 1,500 tokens: extract prep brief to [company]-prep.md, JD to [company]-jd.md.
Main file keeps: status, rounds, stories used, concerns summary, next round, fit verdict.
Extended files loaded only by prep, concerns.
