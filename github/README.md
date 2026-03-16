# GitHub Setup Guide for Interview Coach

This guide walks you through creating a private GitHub repository to store your Interview Coach state, prompts, and configuration files. All automation workflows (Make.com, Apple Shortcuts) will read from and write to this repo.

## Overview

- **Repository name**: `interview-coach` (private)
- **Purpose**: Single source of truth for all coaching state, prompts, and workflow data
- **Access**: You + API authentication (GitHub token, Make.com integration)
- **Commit frequency**: Automated writes from workflows + manual commits during development

---

## Step 1: Create the Private Repository

1. Go to **github.com** and sign in to your account
2. Click the **+** icon (top right) → **New repository**
3. Fill in:
   - **Repository name**: `interview-coach`
   - **Description**: "Interview coaching system with automated workflows and state management"
   - **Visibility**: **Private**
   - **Initialize with README?** No (we'll add our own)
   - **Add .gitignore?** Yes, select **Node.js** as a starting point (we'll customize it)
   - **License**: MIT (optional)
4. Click **Create repository**

You now have an empty private repo.

---

## Step 2: Create and Configure .gitignore

Clone the repo locally (or use GitHub's web editor):

```bash
git clone https://github.com/YOUR_USERNAME/interview-coach.git
cd interview-coach
```

Replace the auto-generated `.gitignore` with this content:

```gitignore
# OS files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Backup and archived state (pre-rebuild, rollback artifacts)
_backup_pre_rebuild/
state_ARCHIVED/
coaching_state_ARCHIVED.md
coaching_state_backup_*.md

# Sensitive data (never commit)
.env
.env.local
*.key
*.pem
api-key.txt
api_key.txt

# Local development artifacts
*.log
.vscode/
.idea/
*.swp
*.swo
*~

# Workflow temp files (Make.com runner artifacts — usually not committed)
*.tmp
_temp/

# Editor state
.DS_Store
*.iml

# Optional npm/yarn cruft
node_modules/
```

Save and commit:

```bash
git add .gitignore
git commit -m "Configure .gitignore for Interview Coach"
git push origin main
```

---

## Step 3: Commit the Full Project Structure

Copy the entire Interview Coach directory structure into your local clone. The full structure should be:

```
interview-coach/
├── .gitignore
├── CLAUDE.md                      # Pointer file (~87 lines)
├── prompts/
│   ├── registry.md               # Command → file routing table
│   ├── layer1-identity/
│   │   └── identity.md           # Coaching identity + voice
│   ├── layer2-protocol/
│   │   ├── session-protocol.md   # Session start/end, mode detection, loading rules
│   │   └── state-schema.md       # Schema definitions for all state files
│   ├── layer3-commands/
│   │   ├── kickoff.md            # (27 command files total)
│   │   ├── research.md
│   │   ├── prep.md
│   │   ├── analyze.md
│   │   ├── debrief.md
│   │   ├── practice.md
│   │   ├── mock.md
│   │   ├── stories.md
│   │   ├── concerns.md
│   │   ├── questions.md
│   │   ├── linkedin.md
│   │   ├── resume.md
│   │   ├── pitch.md
│   │   ├── outreach.md
│   │   ├── decode.md
│   │   ├── present.md
│   │   ├── salary.md
│   │   ├── hype.md
│   │   ├── thankyou.md
│   │   ├── progress.md
│   │   ├── negotiate.md
│   │   ├── reflect.md
│   │   ├── feedback.md
│   │   ├── jobs.md
│   │   ├── track.md
│   │   ├── write.md
│   │   ├── help.md
│   │   └── rubrics/
│   │       └── rubrics-full.md
│   ├── layer4-orchestration/
│   │   ├── day.md                # Daily trigger logic
│   │   └── week.md               # Weekly report logic
│   └── shared/
│       ├── calibration-engine.md
│       ├── challenge-protocol.md
│       ├── cross-cutting.md
│       ├── differentiation.md
│       ├── examples.md
│       ├── role-drills.md
│       ├── story-mapping-engine.md
│       ├── storybank-guide.md
│       ├── transcript-formats.md
│       └── transcript-processing.md
├── state/
│   ├── state_index.md            # Tier 1 — always loaded
│   ├── state_profile.md          # Tier 2 — profile, resume, coaching notes
│   ├── state_stories.md          # Tier 2 — storybank + STAR details
│   ├── state_scores.md           # Tier 2 — score history + drill progression
│   ├── state_intel.md            # Tier 3 — interview intelligence + calibration
│   ├── state_tracking.md         # Tier 3 — apps, jobs, analytics, session log
│   └── loops/
│       ├── _index.md             # Tier 1 — loop registry + signals
│       ├── active/
│       │   └── [company].md      # Tier 3 — per-company loop detail
│       └── inactive/
│           └── [company].md      # Closed/withdrawn/offered loops
├── eval/
│   ├── golden/
│   │   └── my-references.md      # 3 reference answers for drift detection
│   └── results/
│       ├── baseline.md           # Scoring baseline (populated after first run)
│       └── [date]-run.md         # Monthly eval results
├── references/                   # Kept for backward compatibility
│   ├── commands/                 # Original command reference files
│   └── [shared reference files]
├── github/
│   └── README.md                 # This file
├── make-workflows/
│   ├── README.md                 # Workflow overview + cost breakdown
│   ├── daily-jobs.md
│   ├── follow-up-reminders.md
│   ├── weekly-report.md
│   └── monthly-eval.md
└── shortcuts/
    └── interview-morning.md      # Apple Shortcut + Make Workflow 5
```

**To commit this structure:**

```bash
# Copy all files from your local Interview Coach directory into the cloned repo
# (This assumes you have the source files ready)

# Stage everything
git add .

# Commit with the initial message
git commit -m "Initial rebuild — v2 architecture"

# Push to GitHub
git push origin main
```

---

## Step 4: Verification Checklist

After your initial commit, verify the repo is set up correctly:

- [ ] Repository is private (check **Settings → Visibility**)
- [ ] All files are committed (run `git status` — should show "nothing to commit")
- [ ] `.gitignore` is in place and includes patterns for `.DS_Store`, `_backup_pre_rebuild/`, `state_ARCHIVED/`, `coaching_state_ARCHIVED.md`, `.env`, `*.key`
- [ ] No sensitive files (API keys, tokens) are in the repo (search commits: `git log -p | grep -i "api\|key\|token"` — should be empty)
- [ ] Directory structure matches the tree above (run `find . -type d | head -30`)
- [ ] Main files present:
  - [ ] `CLAUDE.md` (core system)
  - [ ] `prompts/registry.md` (prompt index)
  - [ ] `state/state_index.md` (coaching index)
  - [ ] `eval/golden/my-references.md` (calibration data)
  - [ ] `make-workflows/daily-jobs.md` (workflow docs)
  - [ ] `shortcuts/interview-morning.md` (shortcut docs)

---

## Step 5: Generate Your GitHub Token

Workflows will authenticate using a Personal Access Token (PAT). To create one:

1. Go to **github.com → Settings → Developer settings → Personal access tokens → Tokens (classic)**
2. Click **Generate new token (classic)**
3. Fill in:
   - **Token name**: `interview-coach-automation`
   - **Expiration**: 90 days (or "No expiration" if preferred)
   - **Scopes**: Select:
     - `repo` (full control of private repos)
     - `workflow` (update GitHub workflows)
4. Click **Generate token**
5. **Copy the token immediately** — you won't see it again. Store it safely (we'll use it in Make.com setup).

---

## Step 6: Configure GitHub Repository Settings (Optional but Recommended)

### Branch Protection

1. Go to **Settings → Branches**
2. Add rule for `main`:
   - **Require pull request reviews before merging**: OFF (for automation speed)
   - **Require status checks to pass before merging**: OFF (no CI/CD pipeline yet)
   - **Restrict who can push to matching branches**: OFF (allow Make.com automation)

### Automated Commits

Make.com workflows will commit automatically. To keep things clean:

1. In **Settings → Actions → General**:
   - Allow **Actions** (should already be enabled)
   - **Fork pull request workflows from outside collaborators**: OFF

---

## Step 7: Update Your Local .gitconfig (Optional)

When Make.com commits to your repo, you can customize the commit author. Set a local config:

```bash
git config user.name "Interview Coach Automation"
git config user.email "automation@interview-coach.local"
```

Or globally (if you want all repos to use this):

```bash
git config --global user.name "Interview Coach Automation"
git config --global user.email "automation@interview-coach.local"
```

---

## Next Steps

1. **Keep your GitHub token secure**: Store it in a password manager or secure note. Do not commit it to the repo.
2. **Proceed to Make.com setup**: Use `/make-workflows/daily-jobs.md` to configure the first automation workflow.
3. **Test the integration**: After setting up the first Make workflow, run it manually to verify GitHub commits work.
4. **Monitor commits**: Check your repo's commit history to see state updates from automation.

---

## Troubleshooting

### "Cannot authenticate with GitHub"
- Verify your token is valid and hasn't expired
- Confirm the token has `repo` scope
- Check that the token is correctly entered in Make.com

### "File not found in repo"
- Verify the file path in your Make workflow matches the exact case and location in GitHub
- Remember: GitHub paths are case-sensitive on Linux-style repos

### "Commit shows '[bot]' author"
- This is normal when using API tokens. You can customize the commit author in Make.com's GitHub module settings.

### "Too many commits cluttering the repo"
- Consider batching state updates: instead of committing every hour, batch to once daily with a summary commit

---

## Summary

You now have:
- ✅ Private GitHub repository for Interview Coach
- ✅ Configured `.gitignore` (no sensitive data exposed)
- ✅ Full project structure committed
- ✅ Personal Access Token ready for Make.com authentication

**Next**: Proceed to `/make-workflows/daily-jobs.md` to set up your first automated workflow.
