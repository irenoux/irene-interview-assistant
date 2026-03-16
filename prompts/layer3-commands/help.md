# Help
Show available commands and their purposes.

## Input Requirements
None.

## State Files Needed
None.

## Workflow
Display the command table. If state exists, highlight which commands are most relevant based on current coaching stage.

## Output Schema

```
# Interview Coach — Commands

| Command | What It Does |
|---------|-------------|
| kickoff | Initialize your coaching profile from resume + goals |
| research [company] | Lightweight company research + fit assessment |
| prep [company] | Full interview prep brief for a specific company |
| analyze | Score and analyze an interview transcript |
| debrief | Post-interview rapid capture (same day) |
| practice | Practice drill menu — behavioral, product case, role-specific |
| mock [format] | Full simulated interview (4-6 questions) |
| stories | Build, improve, or review your storybank |
| concerns | Generate likely interviewer concerns + counters |
| questions | Generate tailored questions to ask your interviewers |
| linkedin | LinkedIn profile optimization |
| resume | Resume optimization + ATS scoring |
| pitch | Core positioning statement + context variants |
| outreach | Networking and outreach message coaching |
| decode | JD analysis + batch triage for multiple roles |
| present | Presentation round coaching |
| salary | Early/mid-process compensation coaching |
| hype | Pre-interview confidence boost + 3x3 plan |
| thankyou | Post-interview thank-you note drafts |
| progress | Trend review, self-calibration, pattern analysis |
| negotiate | Post-offer negotiation coaching |
| reflect | Post-search retrospective + archive |
| feedback | Capture recruiter feedback, report outcomes, add context |
| jobs | Daily job discovery — surface matching roles |
| track | Log applications, update status, manage follow-ups |
| write | Generate cover letters and outreach messages |
| help | Show this command list |
```

## State Write Targets
None.

## Recommended Next
Based on current state signals — direct to the highest-leverage command.
