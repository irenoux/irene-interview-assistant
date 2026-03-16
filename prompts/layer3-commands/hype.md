# hype — Pre-Interview Boost Workflow

Build data-driven pre-interview confidence. 60-second hype reel, pre-mortem (Level 5 only), 3x3 plan (concerns + counters, questions to ask), format-specific warmup routine, recovery guidance.

## Purpose

Generate a personalized, data-grounded pre-interview confidence boost + tactical 3x3 plan + recovery guidance.

## Input Requirements

- Optional: Company name or interview context (pulled from coaching_state.md if available)
- Optionally: what format interview is (if not in coaching_state)

## State Files Needed

- `coaching_state.md` — Load Score History (for recent practice high points), Storybank (top-scoring stories), Interview Loops (for company-specific round context, prepared questions), Prep Brief (if `prep` was run — evaluation criteria, culture, interviewer intel), Coaching Notes (anxiety profile, patterns), Outcome Log (recent rejections), Active Coaching Strategy (bottleneck for failure mode prediction)

## Workflow

### Data-Driven Hype Construction

The hype reel should be built from real coaching data, not generic encouragement:
- **Pull from practice high points**: Reference the candidate's best practice moments — "In your last practice session, you nailed the prioritization question with a 4 on Structure. That's the level you're bringing today."
- **Reference strongest stories**: Name the 2-3 stories that scored highest in the storybank and are mapped to this interview.
- **Use real score trajectory**: If scores have been improving, name it — "Your Structure scores went from 2s to consistent 4s over the last three sessions. That's not luck."
- **If no coaching data exists yet** (first session): Build from resume strengths and kickoff profile. Be explicit: "I don't have practice scores or storybank data to draw from yet — this hype reel is built from your resume and what you've told me. It'll be more powerful once we've done some practice rounds together."

### Anxiety-Profile Personalization

Candidates experience pre-interview anxiety differently. During `kickoff` (or the first time `hype` is run), identify the candidate's anxiety profile from their stated concern and interview history:

| Profile | Signals | Hype Adjustment |
|---|---|---|
| **Confident but underprepared** | "I'm fine with interviews, just haven't prepped" | Skip emotional boost — focus on tactical 3x3 and cheat sheet. Be direct about gaps. |
| **Anxious about specific failure** | "I always freeze on behavioral questions" or "I can't think of stories" | Address the specific fear head-on with evidence. "You have 8 stories in your storybank, 5 rated 4+. You've practiced retrieving them under pressure. You're not going to freeze." |
| **Generalized anxiety** | "I'm just really nervous" or "I always feel like I'll mess up" | Lead with the physiological warmup (breathing, physical reset). Provide the reframe early: "This is a conversation, not a test." Keep the hype short and grounded. |
| **Post-rejection anxiety** | Recent rejection in Outcome Log, or candidate mentions a bad experience | Acknowledge it directly: "Your last interview at [Company] didn't go the way you wanted. That's done. This is a different company, different interviewers, fresh start." Reference what changed since then. |
| **Impostor syndrome** | "I don't think I'm qualified" or fit verdict was Investable Stretch | Ground in evidence: specific resume achievements, practice scores, storybank strengths. "The data says you belong in this interview. Let's look at why you were invited." |

Save the identified profile to coaching_state.md Profile as `Anxiety profile: [type]` so subsequent `hype` sessions don't re-diagnose — they adapt immediately.

### Interview-Specific Tailoring

If a `prep` brief exists for the upcoming interview, the hype should reference it directly:
- "You're about to talk to [Interviewer Name], who based on their background will likely focus on [area]. Your [Story Title] is perfect for this."
- "This is a [format] interview. Remember: [format-specific key advice from prep]."
- "Their top concern about you is probably [from concerns]. Your counter: [one sentence]."

If no prep exists, say so and suggest running `prep` first if time allows.

### No-Data Fallback

When `coaching_state.md` is empty or has no scores, don't output a hollow version of the data-driven hype. Instead, shift to a different mode:
- Lead with resume-grounded strengths (from kickoff resume analysis)
- Focus the warmup routine on calming techniques rather than score references
- Use the candidate's stated biggest concern (from kickoff) as the basis for the 3x3
- Be honest: "Once you've done some practice rounds, this hype reel will reference your specific high points and score trajectory. For now, here's what's genuinely strong about your profile."

## Output Schema

```markdown
## 60-Second Hype Reel

- **Line 1**: [grounded in real coaching data or resume strengths]
- **Line 2**: [specific evidence of capability]
- **Line 3**: [reference to best story or practice moment]
- **Line 4**: [what makes you different from other candidates]

## Pre-Mortem (Level 5 only)

The honest counterweight. Based on your patterns, the 2-3 most likely ways this interview doesn't go well:
1. [failure mode] — Prevention: [one-line cue]
2. [failure mode] — Prevention: [one-line cue]
3. [failure mode] — Prevention: [one-line cue]

You know these risks. Now set them aside and go execute.

## Pre-Call 3x3

### 3 Likely Concerns + Counters
1. [Concern from Interview Loops or inferred from JD/profile] — Counter: [brief one-liner]
2. [Concern] — Counter: [one-liner]
3. [Concern] — Counter: [one-liner]

### 3 Questions To Ask
[Pull from Interview Loops if `questions` was previously run for this company — top 3]
[If no saved questions: generate 3 tailored to the company/round]
1. [Question — one-liner]
2. [Question — one-liner]
3. [Question — one-liner]

## Focus Cue

- One thing to remember in the room: [single sentence — the most important tactical or mindset shift for this interview]

## 10-Minute Warmup Routine

[Check Interview Loops for saved format data from `prep` or Format Discovery. If the format is a presentation round and `present` was run, pull the key structural decisions and timing calibration from Presentation Prep for the warmup. Tailor the warmup to the format: a presentation round warmup focuses on opening delivery. A system design warmup focuses on scoping out loud. A behavioral screen warmup focuses on story retrieval speed. Panel → mentally rehearse switching between interviewer styles.]

1. Read this hype reel out loud once.
2. [Format-specific drill]:
   - Behavioral → pick your weakest story and deliver the 60-second version out loud.
   - Presentation → deliver your opening 30 seconds out loud.
   - System design → practice scoping a simple problem out loud for 60 seconds.
   - Panel → mentally rehearse switching between interviewer styles.
3. Review the 3x3 above — don't memorize, just refresh.
4. Physical reset: [walk, stretch, breathe — whatever routine works for you].
5. Reframe: "This is a conversation to see if there's mutual fit. I'm also interviewing them."

## If You Bomb an Answer Mid-Interview

[Inlined recovery guidance — acknowledge, pivot, and re-engage]

Key approach:
- Acknowledge briefly: "I didn't explain that as clearly as I'd like. Let me try again."
- Pivot: Reframe or ask a clarifying question: "What would be most helpful to know about [topic]?"
- Re-engage: Show you're present and adaptable, not derailed.

## If You Get a Question You Have No Story For

[Inlined gap-handling guidance — adjacent bridge technique]

Key approach:
- Don't freeze or say "I don't have a story for that."
- Name the adjacent skill/experience: "I haven't done exactly that, but I did [adjacent experience]..."
- Bridge: Explain why the adjacent experience is relevant: "...which required the same [key skill]. Here's what happened..."
- Land: Full STAR on the adjacent story.

## If You Have Back-to-Back Interviews

- Between interviews: 5-minute reset. Don't review notes — your brain needs a break, not more input.
- Physical reset: stand up, walk, get water, stretch. Change your physical state.
- Mental reset: "That interview is done. I can't change it. This next one starts fresh."
- Don't carry energy from the previous interview — good or bad. Each interviewer is meeting you for the first time.
- If you bombed the last one: "That conversation is over. This interviewer doesn't know about it and doesn't care."
- Quick re-read: glance at the Day-Of Cheat Sheet for the next interviewer (if different from the last).

**Recommended next**: `practice ladder` — one final drill to lock in your best answer. **Alternatives**: `questions`, `mock [format]`, `debrief`
```

## Step-by-Step Workflow

### Step 1: Load Coaching Data

Pull from coaching_state.md:
- Score History (for recent practice high points)
- Storybank (top-scoring stories)
- Interview Loops (for company-specific round context, prepared questions)
- Prep Brief (if exists)
- Coaching Notes (anxiety profile, patterns)
- Outcome Log (recent rejections)
- Active Coaching Strategy (bottleneck)

### Step 2: Anxiety Profile Detection

Check Coaching Notes for saved anxiety profile. If not saved (first hype session), diagnose from:
- Candidate's stated biggest concern (from kickoff)
- Interview history (first-time / active but not advancing / experienced but rusty)
- Recent outcomes (rejections, acceptances, pending)

Save the profile for future sessions.

### Step 3: 60-Second Hype Reel Construction

If coaching data exists:
- **Line 1**: Grounded in recent Score History. "Your Substance scores jumped from 2.5 to 4 in the last three sessions."
- **Line 2**: Specific evidence. "You nailed the [story title] story with a 5 on Differentiation in your last practice."
- **Line 3**: Reference strongest storybank stories. "You have [Story Title] and [Story Title] — both rated 4+. You've practiced deploying them under pressure."
- **Line 4**: Differentiator. "What makes you different: [from Active Coaching Strategy or positioning statement]."

If no coaching data:
- **Line 1**: Resume strength. "Your background shows consistent growth in [domain]."
- **Line 2**: Specific achievement. "[Concrete accomplishment from resume or kickoff]."
- **Line 3**: Candidate's best story candidate from kickoff. "In our initial conversation, you highlighted [topic]. That's a strong example of [competency]."
- **Line 4**: Differentiator. "What makes you different: [from positioning or resume analysis]."

### Step 4: Pre-Mortem Construction (Level 5 only)

Source failure modes from real coaching data — don't generate generic risks:
- **Active Coaching Strategy bottleneck**: If the primary bottleneck is Differentiation, "Your answers sound competent but don't stand out" is a concrete failure mode.
- **Storybank gaps for this company**: If predicted questions map to gaps, those are failure modes.
- **Self-assessment calibration tendency**: An over-rater may not self-correct in the moment.
- **Avoidance patterns from Coaching Notes**: Whatever the candidate has been avoiding is likely what will trip them up.
- **Previous rejection feedback**: Feedback from similar companies predicts what this company may also flag.

End with the release cue: "You know these risks. Now set them aside and go execute."

At Levels 1-4: Skip the Pre-Mortem entirely. Hype stays pure boost.

### Step 5: 3x3 Plan Construction

**3 Likely Concerns + Counters**:
- Pull from Interview Loops if company-specific concerns were saved during `prep` or `concerns` command
- Infer from JD Analysis if concerns were documented
- Draw from Outcome Log if recent rejection feedback applies to this company type
- For each concern: provide a one-liner counter (not a full story — just the positioning shift)

**3 Questions To Ask**:
- If `questions` was previously run for this company, pull the top 3 from Interview Loops (saved under "Prepared questions")
- Don't regenerate — consistency matters
- If no saved questions, generate 3 tailored to the company/round (or suggest running `questions` if time allows)

### Step 6: Format-Specific Warmup

Check Interview Loops for the next round's format. If Presentation round detected and `present` was run, pull structural data. Tailor the warmup to the format:

- **Behavioral Screen**: Warmup focuses on story retrieval speed. Pick your weakest story and deliver the 60-second version out loud.
- **Presentation Round**: Warmup focuses on opening delivery. Deliver your opening 30 seconds out loud.
- **System Design**: Warmup focuses on scoping. Practice scoping a simple problem out loud for 60 seconds.
- **Panel Interview**: Warmup focuses on style switching. Mentally rehearse switching between interviewer styles.
- **Hybrid/Unknown**: Standard physical reset + story/question review.

### Step 7: Recovery Guidance Inlining

Include two recovery sections:

**If You Bomb an Answer Mid-Interview**:
Inline key guidance from Psychological Readiness Module (Mid-Interview Recovery):
- Acknowledge briefly: "I didn't explain that as clearly as I'd like. Let me try again."
- Pivot: Reframe or ask a clarifying question.
- Re-engage: Show you're present and adaptable.

**If You Get a Question You Have No Story For**:
Inline key guidance from Gap-Handling Module (Pattern 1: Adjacent Bridge):
- Don't freeze.
- Name the adjacent skill/experience: "I haven't done exactly that, but I did [adjacent experience]..."
- Bridge: Explain why adjacent experience is relevant.
- Land: Full STAR on the adjacent story.

## State Write Targets

Hype does not update coaching_state.md — it READS from it. The only state update is anxiety profile (if first-time hype), saved to Profile.

If this is the first `hype` run for the candidate:
- Identify and save anxiety profile: `Anxiety profile: [type]`

Otherwise: No state write.

## Recommended Next

After hype is complete:
- If interview is within 2-4 hours → encourage the warmup routine, then go interview
- If interview is later today (4+ hours) → suggest `practice ladder` (one final drill)
- Post-interview → `debrief` (same day or next day)
- Default → go interview

Format in closing: `**Recommended next**: `practice ladder` — one final drill to lock in your best answer. **Alternatives**: `questions`, `mock [format]`, `debrief`
