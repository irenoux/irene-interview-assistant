# Command Registry

## Routing Table
| Command | Prompt File | Shared Files | State Files Needed |
|---------|------------|--------------|-------------------|
| kickoff | layer3-commands/kickoff.md | — | state_profile (write) |
| research | layer3-commands/research.md | cross-cutting.md | loops/_index, loops/active/[co] (write) |
| prep | layer3-commands/prep.md | story-mapping-engine.md | state_profile, state_stories, loops/active/[co] |
| analyze | layer3-commands/analyze.md | transcript-processing.md, transcript-formats.md, rubrics-full.md, calibration-engine.md, differentiation.md | state_scores, state_stories, state_intel, loops/active/[co] |
| debrief | layer3-commands/debrief.md | — | state_stories, loops/active/[co], state_scores |
| practice | layer3-commands/practice.md | role-drills.md, calibration-engine.md | state_scores, state_stories |
| mock | layer3-commands/mock.md | calibration-engine.md | state_scores, state_stories, loops/active/[co] |
| stories | layer3-commands/stories.md | storybank-guide.md, differentiation.md | state_stories |
| concerns | layer3-commands/concerns.md | — | state_profile, loops/active/[co] |
| questions | layer3-commands/questions.md | — | loops/active/[co] |
| linkedin | layer3-commands/linkedin.md | differentiation.md, storybank-guide.md | state_profile |
| resume | layer3-commands/resume.md | differentiation.md, storybank-guide.md | state_profile |
| pitch | layer3-commands/pitch.md | differentiation.md, storybank-guide.md | state_profile, state_stories |
| outreach | layer3-commands/outreach.md | differentiation.md, storybank-guide.md | state_profile, state_tracking |
| decode | layer3-commands/decode.md | cross-cutting.md | state_profile, loops/_index |
| present | layer3-commands/present.md | storybank-guide.md | state_stories, loops/active/[co] |
| salary | layer3-commands/salary.md | — | state_profile, loops/active/[co] |
| hype | layer3-commands/hype.md | — | state_profile, state_stories, loops/active/[co] |
| thankyou | layer3-commands/thankyou.md | — | loops/active/[co] |
| progress | layer3-commands/progress.md | calibration-engine.md | state_scores, state_intel, state_stories, loops/_index |
| negotiate | layer3-commands/negotiate.md | — | state_profile, loops/active/[co], state_tracking |
| reflect | layer3-commands/reflect.md | — | ALL state files |
| feedback | layer3-commands/feedback.md | — | state_scores, state_intel, loops/active/[co] |
| jobs | layer3-commands/jobs.md | — | state_tracking, state_profile |
| track | layer3-commands/track.md | — | state_tracking, loops/_index |
| write | layer3-commands/write.md | differentiation.md, storybank-guide.md | state_profile, state_stories, state_tracking |
| help | layer3-commands/help.md | — | — |
| day | layer4-orchestration/day.md | — | state_index, loops/_index, state_tracking |
| week | layer4-orchestration/week.md | — | state_index, state_intel, state_tracking, state_scores |

## Loading Protocol
1. Always loaded: CLAUDE.md → identity.md → session-protocol.md → state-schema.md → state_index.md
2. Per command: Read registry row → load prompt file + shared files + state files
3. Orchestration: day.md (daily trigger) or week.md (weekly trigger)
4. Orchestration commands: day → load day.md; week → load week.md. These can be triggered by user OR external automation.

## Shared Files Location
All shared files are in /prompts/shared/:
- cross-cutting.md
- differentiation.md
- storybank-guide.md
- story-mapping-engine.md
- calibration-engine.md
- transcript-processing.md
- transcript-formats.md
- challenge-protocol.md
- examples.md
- role-drills.md

## Rubrics Location
/prompts/layer3-commands/rubrics/rubrics-full.md

## Level 5 Additional Loading
At Directness Level 5: also load /prompts/shared/challenge-protocol.md for any command.
