# Irene's Interview Assistant

A personal AI-powered job search operating system built on Claude Code.
Started from [Noam Segal's interview coaching skill](https://github.com/noamseg/interview-coach-skill)
and rebuilt into a full job search OS with a new architecture, automation
layer, and experiment-driven application engine.

---

## Origin

This project began with Noam Segal's interview coaching skill — a well-designed
Claude Code system for interview prep, storybank management, and transcript
analysis. That foundation is excellent. What I built on top of it is a complete
rearchitecture and significant extension.

---

## What I Changed and Why

### Problem with the original
The original system is a single monolithic file (~54KB CLAUDE.md +
~100KB coaching_state.md). Every command loads everything, every turn.
At scale this becomes slow, expensive, and increasingly noisy as coaching
state grows.

### Architectural Rebuild

**Layered prompt architecture** — CLAUDE.md trimmed to ~80 lines.
All instructions distributed across a four-layer /prompts/ directory:
- Layer 1: Identity and guardrails (immutable)
- Layer 2: Session protocol and state schema
- Layer 3: Per-command workflows + shared tools (rubric, calibration engine)
- Layer 4: Orchestration (daily and weekly workflows)

**Tiered context loading** — State split from one 100KB file into five
purpose-scoped files loaded on demand:
- state_index.md (~300 tokens, always loaded)
- state_profile.md (Tier 2 — most sessions)
- state_stories.md (Tier 2 — most sessions)
- state_scores.md (Tier 2 — most sessions)
- state_intel.md (Tier 3 — per command)
- state_tracking.md (Tier 3 — per command)

**Per-company loop files** — Each active company gets its own file in
/state/loops/active/. The loop index carries only names and status.
Architecture scales cleanly from 2 to 20+ active applications.

**Prompt caching** — Static files marked with cache_control. Session
baseline drops from ~50,000+ tokens per turn to ~2,000 tokens.

### New Capabilities Added

**Job search engine** — Application tracker, experiment registry,
job discovery, follow-up scheduling, weekly intelligence reports.
The system tracks what's working across cover letter styles, resume
versions, and outreach approaches with proper A/B experiment framing.

**Experiment registry** — Every application tagged to an active
experiment. Cover letter opener style (earned-secret vs traditional),
resume version performance, outreach approach. Auto-conclusion logic
flags when minimum sample is reached.

**Daily orchestration (`day` command)** — Assembles the full daily
workflow: pipeline status, overdue follow-ups, job discovery,
practice drill, apply workflow. One HITL checkpoint before execution.

**Weekly intelligence (`week` command)** — Automated weekly report
covering search funnel, experiment outcomes, interview performance
trends, energy tracking, and three specific changes for next week
backed by evidence.

**Evaluation framework** — Personal golden dataset for scoring drift
detection. Monthly consistency checks. Outcome correlation tracking
(do practice scores predict real interview outcomes?).

**Make.com automation** — Four scheduled workflows running in the
background: daily job discovery, follow-up reminders, weekly report
(Batch API), monthly eval run (Batch API). Apple Shortcuts integration
for interview-morning hype brief triggered by calendar events.

### Design Principles Applied

The rebuild was used as a learning vehicle for AI platform concepts:
- Tiered context architecture (hot/cold data, principle of least privilege)
- Prompt management with layered governance and version pinning
- Orchestration design (intent classification, planning, HITL checkpoints,
  replanning thresholds)
- Caching strategy (assembly order, write-through, invalidation rules)
- Reliability design (graceful degradation, fallback registry, observability)
- Evaluation framework (ground truth definition, consistency testing,
  drift detection, outcome correlation)

---

## Architecture
```
/
├── CLAUDE.md                    # ~80 lines — pointer file only
├── /prompts/
│   ├── registry.md              # Command routing table
│   ├── /layer1-identity/        # Guardrails — immutable
│   ├── /layer2-protocol/        # Session protocol + state schema
│   ├── /layer3-commands/        # Per-command workflows + rubrics
│   ├── /layer4-orchestration/   # day.md + week.md
│   └── /shared/                 # Cross-cutting modules
├── /state/
│   ├── state_index.md           # Tier 1 — always loaded
│   ├── state_profile.md         # Tier 2
│   ├── state_stories.md         # Tier 2
│   ├── state_scores.md          # Tier 2
│   ├── state_intel.md           # Tier 3
│   ├── state_tracking.md        # Tier 3
│   └── /loops/
│       ├── _index.md            # Loop names + status only
│       └── /active/             # One file per active company
├── /eval/                       # Scoring calibration framework
├── /make-workflows/             # Make.com workflow configs
├── /shortcuts/                  # Apple Shortcuts setup
├── /scripts/                    # Python utilities
│   ├── ats_score.py             # ATS keyword scorer
│   ├── follow_up_queue.py       # Follow-up due date checker
│   ├── sync_tracker.py          # Google Sheets → state sync
│   └── weekly_insights.py       # Application analytics
└── /github/                     # Repo setup documentation
```

---

## Token Budget

| Layer | When Loaded | Budget |
|-------|-------------|--------|
| CLAUDE.md | Always | ~80 tokens |
| Layer 1–2 prompts | Always | ~1,200 tokens |
| state_index.md | Always | ~300 tokens |
| Session baseline | | **~2,000 tokens** |
| Per-command files | On demand | ~300–800 tokens |
| State detail files | On demand | Variable |

Previous architecture: ~50,000–70,000 tokens per turn.

---

## Setup

This repo contains the architecture and prompt files.
State files (personal coaching data) are excluded from the public repo.

To use it yourself:
1. Clone the repo
2. Rename CLAUDE.md if needed for your environment
3. Run `kickoff` in Claude Code to initialise your own coaching state
4. Follow /github/README.md to set up your private repo for state files
5. Follow /make-workflows/ to set up automation

Requires a paid Claude plan and Claude Code.

---

## Credits

Original interview coaching skill by
[Noam Segal](https://github.com/noamseg/interview-coach-skill) — MIT License.
The coaching logic, command structure, scoring rubric, and storybank system
are his work. This repo extends that foundation with a new architecture,
automation layer, and job search engine.

Extended and rebuilt by Irene Zhang, March 2026.