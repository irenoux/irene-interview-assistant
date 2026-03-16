# Coaching State — Irene Zhang
Last updated: 2026-03-03

## Profile
- Target role(s): Senior PM / Lead PM — Data & AI products (industry-agnostic)
- Seniority band: Senior / Lead
- Track: Full System
- Feedback directness: 5
- Interview timeline: Exploring; one pending recruiter screen outcome
- Time-aware coaching mode: full
- Interview history: active but not advancing (first Senior/Lead attempts; previously mostly PM-level interviews)
- Biggest concern: Finding the right role; ATS/AI screening; product case structuring + pace management under pressure; story coverage and spinning anchor stories
- Known interview formats: [pending — will be updated during prep/mock]
- Anxiety profile: imposter syndrome (candidate-flagged); calibrate Level 5 challenge to push without eroding confidence
- Career transition: domain shift (financial services → industry-agnostic; maintaining data/AI focus)
- Transition narrative status: not started

## Resume Analysis
- Positioning strengths:
  1. Clear data/AI PM through-line — Capital One (data platform modernization), Quantexa (entity resolution + ML), Morningstar (data distribution) — rare depth in building platform data products in regulated environments
  2. 0-to-1 + scale credibility — led full SaaS pivot at Quantexa from ideation to GTM, including challenging the initial direction and preserving ~80% of prior investment
  3. Quantified business impact — 72% rework reduction, 33% delivery velocity improvement, £250k savings, 12% TAM expansion — numbers speak the Senior PM language
- Likely interviewer concerns:
  1. Title gap — actual titles (Data PM, PM, Product Owner) don't uniformly signal "Senior PM"; scope is senior but labels may not hold up under scrutiny at some companies
  2. Capital One short tenure (13 months, Nov 2024–Dec 2025) — needs a tight, preemptive story; will be flagged
  3. UK-heavy career trajectory — Capital One is the only US role; US market fluency may be probed at some companies
  4. Product case performance — known weakness (Uber HM interview); structure under pressure is a specific, documented gap
  5. Lead-level readiness — cross-functional leadership is visible but "lead" signals (org direction-setting, PM mentorship, headcount ownership) aren't always explicit in resume framing
- Career narrative gaps:
  1. Capital One short tenure needs a clear "why I left" narrative — absence of explanation invites speculation
  2. UK-to-US career trajectory — should be addressed proactively in pitch, not left for interviewers to raise
  3. Financial services → industry-agnostic transition — data/AI skills transfer, but stories over-indexed on fintech context need reframing for non-FS audiences
- Story seeds:
  1. Quantexa 0-to-1 SaaS pivot — challenged direction, preserved ~80% of investment, expanded TAM 12% — rich strategic decision-making story
  2. Capital One "logic drift" root cause discovery — multi-year systemic problem solved via cross-functional investigation — strong Substance/Credibility story
  3. Morningstar £250k data architecture consolidation (40 plants → 1 cloud database) — clear business impact, strong Relevance for data platform roles
  4. Quantexa AI/ML product improvements — 7% accuracy gain, democratized for non-expert users — good AI/ML product story
  5. Sthaler biometric auth — user friction −34%, retention +40% — 0-to-1 / user-centric story with fintech context

## Storybank
| ID | Title | Primary Skill | Secondary Skill | Earned Secret | Strength | Use Count | Last Used |
|----|-------|---------------|-----------------|---------------|----------|-----------|-----------|
| S001 | SaaS ER Pivot | Strategic thinking | Ambiguity navigation | When a hyperscaler enters your market, their entry validates the market while their structural constraints define the whitespace. Design dual value paths to eliminate all-or-nothing risk. | 4 | 0 | — |
| S002 | Entity Quality Working Group | Problem-solving | Influence without authority | The most dangerous product feedback is specific, confident, and wrong. When teams flood you with feature requests, investigate the underlying problem they can't measure. | 4 | 0 | — |
| S003 | Logic Drift | Problem-solving | Leadership | The most expensive bugs in data systems aren't in the code — they're in the language. Reframe recurring rework as definition drift, not defect drift. | 4 | 0 | — |
| S004 | Capital One Recoveries Dataset | Cross-functional leadership | Execution/delivery | When everyone owns something, nobody does. Make lineage visible first; accountability becomes concrete when each team sees exactly where their handoff is. | 3 | 0 | — |

### Story Details

#### S001 — SaaS ER Pivot (Quantexa)
- **Situation**: Leading development of a no-code data-model configuration tool for business analysts to configure entity-resolution (ER) models without writing Scala. Midway through development, Amazon and Google released ER-only products, validating a market Quantexa had previously dismissed and introducing competitive risk. A second opportunity was also visible: Quantexa had 9–18 month lead-to-value timelines and 2–3 month single data-source onboarding. The tool could serve as a delivery accelerator even if external ER market traction proved slow. Leadership decided to pivot and compete directly in the ER-only space.
- **Task**: Validate and challenge the strategy; reposition the product for differentiation; enable the pivot without derailing the roadmap; ensure the product would still generate internal value even if external traction was slow.
- **Action**: (1) Challenged the pivot: conducted competitive research across Amazon, Google, and the only other ER-only vendor. Found all competitors were black-box tools — unusable for regulated industries where transparency and auditability are non-negotiable. (2) Identified differentiator: positioned product as configurable, transparent, and explainable — aligned with Quantexa's regulated-industry customer base. (3) Proposed dual value path: reframed the product to also solve Quantexa's internal delivery problem — compress data-source onboarding from months to weeks. Aligned with delivery teams to ensure the tool eliminated repetitive engineering work. (4) Led minimal, high-impact engineering pivot: added ER execution to the no-code interface; reused ~80% of existing roadmap; prioritized explainability, rule transparency, and auditability. (5) Enabled Sales & GTM: created competitive battlecards, redesigned demo flows, enabled "bring your own data" demos — customers could see results on their own data within days rather than months.
- **Result**: Preserved ~80% of prior investment. TAM expanded by 12%. License-to-service ratio improved 21%. Delivery onboarding timelines compressed from months to weeks. Stronger, more credible sales demos. Product entered a newly validated market while maintaining regulated-industry differentiation.
- **Earned Secret**: "When a hyperscaler enters your market, the instinct is to race them. I've learned the opposite: their entry validates the market while their structural constraints — opacity, inflexibility, regulatory blind spots — define the whitespace that actually matters. The companies that survive that moment are the ones who ran toward what big players fundamentally can't do. And if you can design dual value paths into the product, you eliminate the all-or-nothing risk of an early market bet."
- **Deploy for**: Strategic thinking under competitive pressure; 0-to-1 product decisions; challenging leadership; AI/ML product development; regulated market differentiation; influence without authority (getting leadership alignment on a non-obvious path)
- **Red team notes** (2026-03-02): Add one sentence acknowledging leadership's legitimate concern (investor signaling) before the counter-proposal. Clarify whether TAM/license numbers are actuals or projections. Be ready for: "What would have happened if leadership had overruled you?"
- **Version history**: 2026-03-02 — Initial capture from STAR experience.docx (updated STAR version)

#### S002 — Entity Quality Working Group (Quantexa)
- **Situation**: Took over Parsers product at Quantexa — a foundational component of the entity-resolution platform. Noticed unusually high volume of small feature requests and configuration changes from delivery teams. Hypothesized the requests weren't about missing features but reflected issues with ER outcomes. Analysis revealed two root causes: (1) best practices were siloed among senior delivery experts, (2) ER quality wasn't measurable — no consistent way to quantify accuracy, leading teams to focus on upstream data quality via parsers as a proxy.
- **Task**: Unite cross-functional experts across Delivery, Data Science, Engineering, and Product to establish shared approaches to ER quality education, best practices, and measurement — strengthening how Quantexa defined and delivered entity-resolution quality to customers. Hard constraint: no authority over any team involved, and my own team's capacity was committed to the parser roadmap — two engineers contributed part-time as domain experts. Everything had to be built through persuasion and borrowed capacity.
- **Action**: (1) Validated root cause: categorized all incoming parser requests — over half stemmed from misinterpreted ER outcomes, not missing parser capabilities. (2) Made the call not to build more parser features in response to the requests. The correct investment was measurement infrastructure — but that meant convincing Data Science to prototype detection models, Delivery to codify tribal knowledge, and Engineering to prioritize work that didn't appear on any of their roadmaps. All without authority, budget, or formal mandate. (3) Established the Entity Quality Working Group: brought together cross-functional experts from Delivery, Data Science, Engineering, and Product. (4) Defined roadmap around three pillars: education/communication, codified best practices, measurable quality metrics. (5) Codified expertise: documented and standardized parser-configuration best practices with data examples. (6) Developed quality measurement models: partnered with Data Science to prototype detection models that quantified ER quality — the company's first internal benchmark — validated against live customer data and deployments.
- **Result**: Parser-related feature requests reduced by 45%. Created Quantexa's first standardized best-practice guidance for parser configuration, adopted globally. Detection models established company's first quantifiable ER quality measure — validated on live customer data and deployments. EQWG became a standing governance and innovation body influencing the Innovation Roadmap.
- **Earned Secret**: "The most dangerous product feedback is specific, confident, and wrong. 45+ parser feature requests were technically precise but solving the wrong problem — teams were using parser changes as a proxy for ER quality improvement because ER quality wasn't measurable. I've learned that when you're flooded with narrow, confident feature requests, the right response is almost never to build them — it's to find what problem they're actually trying to solve. Fix the underlying measurement problem, and the feature requests evaporate."
- **Deploy for**: Influence without authority; data-driven decision making; cross-functional alignment; "tell me about a time you identified a systemic problem"; working with data science and engineering teams; building internal tooling with product judgment
- **Red team notes** (2026-03-02 → resolved 2026-03-03): Authority constraint now explicit in Task. Blog outcome removed from Result. Decision moment restructured in Action (investment call framing, not capacity redirect — my team continued parser roadmap; two engineers part-time was all I had). | **Be ready for "Did the models ship to customers?"**: "When I left, the models were running on live customer data and real deployments internally — we were still iterating. I've since heard they've been shared externally, but that happened after I left." Honest, shows real stakes, doesn't overclaim.
- **Version history**: 2026-03-02 — Initial capture from STAR experience.docx | 2026-03-03 — Improved to Strength 4: authority constraint made explicit in Task (two part-time engineers, no budget, no mandate), decision moment reframed in Action (investment call, not capacity redirect), blog outcome removed from Result, live customer data validation added, be-ready-for answer documented.

#### S003 — Logic Drift (Capital One)
- **Situation**: Capital One's Credit Card Technology org — its largest business unit — was deep in a multi-year migration from mainframe to cloud. A recurring defect known as "logic drift" had plagued multiple streaming data pipelines for over two years. Despite several attempted fixes, delivery delays, costly rework, and declining leadership confidence persisted. Assigned to diagnose root causes and design a sustainable solution.
- **Task**: Identify underlying causes of logic drift across transformation pipelines; implement immediate remediation; design scalable process and ownership model to prevent recurrence.
- **Action**: (1) Diagnosed end-to-end: interviewed 13 stakeholders across Modeling, Engineering, Program, and Product. Discovered four systemic gaps: ambiguous requirements, misaligned pseudo-code interpretation, inconsistent implementation, and lack of validation. Built an end-to-end pipeline map to trace where divergence actually appeared in data — used this as the tiebreaker when stakeholder diagnoses conflicted. (2) Reframed for leadership: positioned "logic drift" as a governance and collaboration breakdown, not a coding defect — shifting focus from reactive bug-fixing to structural prevention. (3) Redesigned cross-team process: introduced Definitions of Ready and Done; established shared validation cadence across 3 job functions; designed lightweight ownership/sign-off framework; refactored transformation library eliminating 23% redundant logic. (4) Secured alignment from Senior Director and VP stakeholders. (5) Defined long-term roadmap for validation automation.
- **Result**: Rework reduced 72%; coordination overhead reduced 68%. Delivery velocity improved 33%. Restored leadership confidence in the transformation program. Framework became a template for Recoveries Modernization and Discovery Integration programs.
- **Earned Secret**: "The most expensive bugs in data systems aren't in the code — they're in the language. 'Logic drift' was really 'definition drift': no shared meaning of 'correct' across teams contributing to the same pipeline. I've learned that when you see repeated rework in a complex data system, the first diagnostic shouldn't be 'bad code' — it should be 'whose definition of correct are we building to?' Fixing the code without fixing the shared language just regenerates the same drift six months later."
- **Deploy for**: Complex ambiguous problem diagnosis; organizational change; executive alignment; data systems / platform quality; "tell me about a time you drove systemic improvement"; governance and process design; reframing problems for leadership
- **Red team notes** (2026-03-02): Add one sentence showing synthesis of conflicting stakeholder diagnoses (the pipeline map was the tiebreaker — use that). Acknowledge what teams were doing right before you arrived to avoid "savior" framing. Be ready for: "How exactly was the 72% measured? Who validated it?"
- **Version history**: 2026-03-02 — Initial capture from STAR experience.docx (fuller version with 13 stakeholders, specific numbers)

#### S004 — Capital One Recoveries: First Standardized Batch Dataset
- **Situation**: Capital One's Credit Card org was migrating the Recoveries domain from a siloed legacy platform to a modern enterprise ledger. Recoveries handles customers who have fallen behind on payments — and the domain's isolation meant that customers who repaid their debt couldn't easily resume banking with Capital One without opening a new account. Recoveries was chosen as a lower-risk pilot to migrate first. Deep misalignment blocked progress: modeling team's schema conflicted with platform constraints; downstream consumers flagged missing values; no single team owned reconciling these perspectives.
- **Task**: Unblock delivery by aligning all stakeholders — from upstream data producers to downstream consumers — around a single feasible, business-fit data model. Deliver the first standardized batch dataset for Recoveries on the new ledger system.
- **Action**: (1) Coordinated 9 stakeholder groups: Modeling, Enterprise Platform, Configuration, Batch Data Engineering, Data Products, Enterprise Governance, Data Stewards, Architecture, and Consumer teams. (2) Built shared visibility of data lineage: consolidated data definitions and mappings from legacy system; partnered with data analysts to do field-by-field validation. (3) Mapped end-to-end data flow: traced full data journey from charge-off events on legacy to standardized outputs on new system — identifying gaps, dependencies, redundancies. (4) Bridged business logic and system design: led collaborative sessions between modeling and platform engineers to integrate system requirements into the modeling process. (5) Embedded validation into delivery cadence: introduced schema review checkpoints and alignment rhythms for future migrations.
- **Result**: Delivered Capital One's first standardized batch dataset on the modern enterprise ledger — a key modernization milestone. Identified 38 new attributes required for completeness; remodeled 28. Modeling velocity improved 12%. Modeled attributes meet consumer needs with <2% re-modeling required. Enabled seamless customer re-entry: repaid customers can resume banking without opening a new account. Process and learnings adopted for subsequent digital-transformation programs.
- **Earned Secret**: "When everyone owns something, nobody does. With 9 stakeholder groups contributing to one data product, the risk wasn't technical complexity — it was diffused accountability. I've learned that the way to convert abstract ownership into concrete action in large cross-functional programs is to make the lineage visible first. When each team can see exactly where their output ends and the next team's begins, the conversation shifts from 'who's responsible?' to 'what does quality mean at my specific handoff point?' That's when accountability becomes real."
- **Deploy for**: Complex stakeholder alignment; cross-functional delivery; data quality/standards at scale; "tell me about a time you drove delivery with no clear ownership"; creating reusable frameworks; customer impact from technical work
- **Red team notes** (2026-03-02): RESTRUCTURE — open with the customer impact (repaid customers blocked from re-banking), then pull back to technical context. Add the specific conflict moment: name the teams with irreconcilable constraints and how you broke the tie. "I coordinated 9 teams" is not a story — the friction is the story.
- **Version history**: 2026-03-02 — Initial capture from STAR experience.docx

## Score History
### Historical Summary
[none yet]

### Recent Scores
| Date | Type | Context | Sub | Str | Rel | Cred | Diff | Hire Signal | Self-Δ |
|------|------|---------|-----|-----|-----|------|------|-------------|--------|
| 2026-03-03 | practice | Zillow HM roleplay — data platform roadmap prioritization (R1: baseline) | 3 | 2 | 3 | 2 | 2 | Mixed | — |
| 2026-03-03 | practice | Zillow HM roleplay — data platform roadmap prioritization (R2: after coaching) | 4 | 3 | 4 | 4 | 4 | Hire | — |

## Outcome Log
| Date | Company | Role | Round | Result | Notes |
|------|---------|------|-------|--------|-------|
| 2026-02-~16 | Uber | Senior PM | HM Interview | rejected | Product case structure broke down under pressure; stream-of-consciousness delivery — confirmed primary gap |


## Interview Intelligence

### Question Bank
| Date | Company | Role | Round Type | Question | Competency | Score | Outcome |
|------|---------|------|------------|----------|------------|-------|---------|

### Effective Patterns (what works for this candidate)
[none yet — will be populated by analyze, debrief, and feedback]

### Ineffective Patterns (what keeps not working)
- 2026-03-02 (self-reported): Structure under pressure in product cases — reverts to stream-of-consciousness delivery. Evidenced by Uber HM interview. Address in practice and mock.

### Recruiter/Interviewer Feedback
| Date | Company | Source | Feedback | Linked Dimension |
|------|---------|--------|----------|-----------------|

### Company Patterns (learned from real experience)
[none yet]

### Historical Intelligence Summary
[none yet]

## Drill Progression
- Current stage: 1
- Gates passed: []
- Revisit queue: [product case structure — known gap from Uber]

## Interview Loops (active)
### Uber
- Status: Closed — Rejected
- Rounds completed: HM Interview (~2026-02-16)
- Round formats:
  - Round 1: HM Interview — included product case component
- Stories used: [unknown — pre-coaching]
- Concerns surfaced: [Product case structure under pressure — confirmed as rejection factor]
- Interviewer intel: []
- Prepared questions: []
- Next round: N/A — rejected
- Fit verdict: N/A
- Fit confidence: N/A
- Fit signals: []
- Structural gaps: [product case structure under pressure — confirmed gap]
- Date researched:

### Google
- Status: Waiting — assessment passed, no recruiter contact yet
- Track: Track 3 — Major Tech Brand
- Rounds completed: Online assessment (2026-02-04, passed for 1 role; rejected from 2 other roles)
- Round formats:
  - Pre-screen: Google online assessment — passed
  - Round 1: Recruiter phone screen — not yet scheduled (~4 weeks since assessment)
- Stories used: []
- Concerns surfaced: []
- Interviewer intel: []
- Prepared questions: []
- Next round: Awaiting recruiter outreach — no action needed; Google pipeline is slow and opaque. If no contact by 2026-03-17 (6 weeks post-assessment), treat as likely ghosted.
- Fit verdict: unknown — specific role unknown; clarify when/if recruiter contacts
- Fit confidence: Limited — no JD matched to loop yet
- Fit signals: []
- Structural gaps: []
- Date researched:

### Alvarez and Marsal
- Status: Phone Screen Done
- Track: Track 2 — Consulting/Accelerator/Incubator
- Role: Director
- Rounds completed: Recruiter screen (2026-02-04)
- Round formats:
  - Round 1: Recruiter screen — complete
  - Round 2: unknown — awaiting confirmation of next steps
- Stories used: []
- Concerns surfaced: [Director-level title may require more explicit leadership evidence than current storybank shows; consulting format likely case-heavy — different from PM interviews]
- Interviewer intel: []
- Prepared questions: []
- Next round: TBD — waiting to hear back
- Fit verdict: unknown — no JD decoded yet; Director at A&M is a significant title signal worth researching
- Fit confidence: Limited
- Fit signals: [A&M fits Track 2 well — consulting format, exposure to multiple sectors/companies, PE and corporate finance practice relevant to eventual investing goals]
- Structural gaps: [consulting case interviews are a different format from PM behavioral — may need format-specific prep if advanced]
- Date researched:

### Zillow
- Status: Decoded
- Track: Track 3 — Major Tech Brand / Data Platform
- Role: Senior PM, Data Platform
- Rounds completed: []
- Round formats: []
- Stories used: []
- Concerns surfaced: [lateral title; comp top-of-range achievability; eventing domain vocabulary gap]
- Interviewer intel: []
- Prepared questions: []
- Next round: Not yet applied
- Fit verdict: Strong Fit
- Fit confidence: Medium — JD + resume
- Fit signals: [Near-perfect data platform alignment; Capital One governance work + Morningstar streaming feeds directly relevant; eventing/developer experience framing needed]
- Structural gaps: [none — all gaps frameable]
- Date researched: 2026-03-02

### Upstart
- Status: Decoded
- Track: Track 3 — Title/Comp Progression (with domain caveat)
- Role: Principal PM, Capital Platform
- Rounds completed: []
- Round formats: []
- Stories used: []
- Concerns surfaced: [domain trap — keeps candidate in financial services; "capital platform" vocabulary absent from resume]
- Interviewer intel: []
- Prepared questions: []
- Next round: Not yet applied
- Fit verdict: Strong Fit (skills/comp/title) with domain preference concern
- Fit confidence: Medium — JD + resume
- Fit signals: [Highest skills match of the 5 roles; regulated fintech, enterprise B2B platform, 0-to-1 all directly present in background]
- Structural gaps: [no direct lending product experience; domain mismatch with candidate's stated goal to leave FS]
- Date researched: 2026-03-02

### Inspiren
- Status: Applied
- Track: Track 3 — Title/Comp Progression + Cool Product
- Role: Principal PM, Strategic Expansion
- Rounds completed: []
- Round formats: []
- Stories used: []
- Concerns surfaced: [hardware-enabled systems requirement is explicit — now frameable via Sthaler finger vein reader; healthcare domain new]
- Interviewer intel: []
- Prepared questions: []
- Next round: Awaiting response — applied 2026-03-02
- Fit verdict: Investable Stretch
- Fit confidence: Medium — JD + resume
- Fit signals: [0-to-1 expansion work maps directly to S001; comp ($240k-$280k) and title (Principal) both hit targets; AI product is genuinely interesting]
- Structural gaps: [hardware-enabled/sensor systems in production — was flagged as unbridgeable; Sthaler finger vein reader (v5.1 edit) provides honest frameable experience]
- Date researched: 2026-03-02

### Pinterest
- Status: Applied
- Track: Track 3 — Major Tech Brand
- Role: Sr. PM, Content Quality Signals
- Rounds completed: []
- Round formats: []
- Stories used: []
- Concerns surfaced: [content quality/safety domain entirely new; B2C consumer experience absent; ranking/personalization gap unaddressed; ATS ceiling ~85% — structural domain keywords can't be added honestly]
- ATS: ~85% (general_saas_v4.3, 17/20); OKR edit added 2026-03-02
- Cover letter: drafted Yes — 2026-03-02 (EQWG quality signal bridge, S002; gap acknowledged; candidate-written, coach-cleaned)
- Stories used: [S002 — EQWG quality signal methodology]
- Interviewer intel: []
- Prepared questions: []
- Next round: Not yet applied
- Fit verdict: Investable Stretch
- Fit confidence: Medium — JD + resume
- Fit signals: [Major tech brand; ML partnership experience at Quantexa is real; S002 (EQWG proxy metric) maps well to content quality signal design challenge]
- Structural gaps: [no safety/integrity/content quality domain experience; no B2C/consumer PM experience]
- Date researched: 2026-03-02

### Zen Educate
- Status: Applied
- Track: Track 3 (borderline — Principal title + Chicago hybrid; comp unknown)
- Role: Principal PM (IC)
- Rounds completed: []
- Round formats: []
- Stories used: []
- Concerns surfaced: [not data/AI core; comp likely below $220k target; not major brand; doesn't fit Track 1, 2, or 3 clearly]
- Interviewer intel: []
- Prepared questions: []
- Next round: Candidate to confirm intent before applying
- Fit verdict: Weak Fit
- Fit confidence: Limited — JD not available; company context only
- Fit signals: [UK-origin company — candidate's UK background may be an advantage; startup/Principal title; SaaS expansion work present]
- Structural gaps: [not data/AI core; comp likely below target; no track alignment]
- Date researched: 2026-03-02

### Webflow
- Status: Decoded
- Track: Track 3 — Recognized Brand / AI Platform
- Role: Principal PM, AI
- Rounds completed: []
- Round formats: []
- Stories used: []
- Concerns surfaced: [Zone-dependent comp ($200–340k) — verify Illinois zone before applying; YOE 10+ requirement is essentially met (~9 years product work since 2017 Product Owner start)]
- Interviewer intel: []
- Prepared questions: []
- Next round: Not yet applied
- Fit verdict: Investable Stretch
- Fit confidence: Medium — JD summary + resume
- Fit signals: [Strong AI/ML product alignment (Quantexa AI democratization + EQWG detection models); Principal title = Track 3 criteria met; CPO-reporting role is high visibility; user-facing AI for non-technical users maps directly to Quantexa AI usability work]
- Structural gaps: [None — ~9 years product work since 2017 Product Owner start essentially meets the 10-year requirement; zone-dependent comp is the main unknown]
- Date researched: 2026-03-03

### Upwork
- Status: Decoded
- Track: Track 3 — Title/Comp Progression + AI Platform
- Role: Principal PM, AI Search
- Rounds completed: []
- Round formats: []
- Stories used: []
- Concerns surfaced: [Older posting — verify active before applying; B2C/marketplace experience gap; two-sided marketplace model differs from B2B enterprise background]
- Interviewer intel: []
- Prepared questions: []
- Next round: Not yet applied — verify posting active first
- Fit verdict: Investable Stretch
- Fit confidence: Medium — JD summary + resume
- Fit signals: [Strong comp ($229.5–344.5k total) hits Track 3 target; AI/ML search + data-driven background alignment; Principal title = title progression; 7+ years requirement achievable]
- Structural gaps: [No two-sided marketplace PM experience; no direct search/recommendations product background — transferable but requires framing]
- Date researched: 2026-03-03

### Braze
- Status: Decoded
- Track: Track 3 — Recognized B2B SaaS Brand + Applied ML
- Role: Senior PM, Applied ML
- Rounds completed: []
- Round formats: []
- Stories used: []
- Concerns surfaced: [Wide comp range ($112–258k OTE) — verify achievable comp for Senior PM before investing; Senior PM title is lateral (not progression); marketing automation domain is different from data platform]
- Interviewer intel: []
- Prepared questions: []
- Next round: Not yet applied — verify comp band first
- Fit verdict: Investable Stretch
- Fit confidence: Medium — JD summary + resume
- Fit signals: [B2B enterprise platform = strongest background alignment; ML/DS partnership experience (S002 EQWG) directly matches "DS background preferred"; Chicago remote option = location positive; Braze is a recognized public SaaS company]
- Structural gaps: [Marketing automation/decisioning domain is different from data platform; comp ceiling uncertainty at Senior PM level]
- Date researched: 2026-03-03

## Active Coaching Strategy
- Primary bottleneck: [to be confirmed after first analyze or practice — likely Structure under pressure based on Uber evidence]
- Current approach: Full system build — storybank foundation first, then product case structure drills, then differentiation
- Rationale: Active but not advancing at Senior level; known product case weakness; full timeline available; 4 existing anchor stories need spinning and extension
- Pivot if: Recruiter screen outcomes reveal different bottleneck; or analyze/practice surfaces a different primary dimension gap
- Root causes detected: Structure under pressure (product case); possible imposter syndrome impact on real interview performance
- Self-assessment tendency: unknown
- Previous approaches: []

## Calibration State

### Calibration Status
- Current calibration: uncalibrated
- Last calibration check: never
- Data points available: 0 real interviews with scored outcomes

### Scoring Drift Log
| Date | Dimension | Direction | Evidence | Adjustment |
|------|-----------|-----------|----------|------------|

### Calibration Adjustments
| Date | Trigger | What Changed | Rationale |
|------|---------|--------------|-----------|

### Cross-Dimension Root Causes (active)
| Root Cause | Affected Dimensions | First Detected | Status | Treatment |
|------------|---------------------|----------------|--------|-----------|

### Unmeasured Factor Investigations
| Date | Trigger | Hypothesis | Investigation | Finding | Action |
|------|---------|------------|---------------|---------|--------|

## LinkedIn Analysis
- Date:
- Depth:
- Overall:
- Recruiter discoverability:
- Credibility on visit:
- Differentiation:
- Top fixes pending:
- Positioning gaps:

## Resume Optimization
- Date:
- Depth:
- Overall:
- ATS compatibility:
- Recruiter scan:
- Bullet quality:
- Seniority calibration:
- Keyword coverage:
- Top fixes pending:
- JD-targeted:
- Cross-surface gaps:

## Positioning Statement
- Date:
- Depth:
- Core statement:
- Hook (10s):
- Key differentiator:
- Earned secret anchor:
- Target audience:
- Variant status:
- Consistency status:

## Application Follow-up Framework
Last updated: 2026-03-02

### Wave Timing
| Wave | Trigger | Channel | Length | Content rule |
|------|---------|---------|--------|--------------|
| F/U 1 | 5 BD after apply (default) | LinkedIn DM preferred | 2–3 sentences | Confirm application + 1 specific sentence showing you read the role closely. No ask. |
| F/U 2 | 12 BD after apply | Same channel | 1–2 sentences | Only if F/U 1 got no response. Hook on something new: product news, recent launch, thought since applying. Still no ask. |
| F/U 3 | 21 BD after apply | Email | 1–2 sentences | Optional final. "Keeping the door open." If nothing by this point, let it go. |

### Timing by Company Type
| Company type | F/U 1 timing | Tone | Channel | Key rule |
|---|---|---|---|---|
| Seed/early startup (<30 people) | 2–3 BD | Warm, direct, peer-level | LinkedIn DM or email | Founder often reads everything. Show genuine interest in the problem, not the process. |
| Scale-up (30–200 people) | 3–4 BD | Personal, specific | LinkedIn DM | Name the specific team/product area. Generic is invisible. |
| Mid-size (200–1000 people) | 5 BD | Professional, specific | LinkedIn DM or email | Personal follow-up still moves applications. |
| Enterprise / FAANG | 5–7 BD | Professional | LinkedIn DM (recruiter only) | ATS dominates. DM to recruiter is OK but low-conversion. Focus energy on ATS score first. |
| VC/PE firms | 1–2 BD | Relationship-first, thesis-aware | Email | Almost no ATS. Everything is relationship-based. Mention your thesis, not just credentials. |
| Consulting (A&M, BCG etc.) | 1–2 BD | Confident, client-facing | Email preferred | Reaching out promptly IS part of the screen. Silence reads as low interest. |

### When a Person Is Cited on the Application
| Scenario | Who | Action |
|----------|-----|--------|
| Referral — someone inside the company vouched for you | Internal advocate | Update them the day you apply: "Submitted — wanted to keep you posted. Happy to loop you in on anything that helps." Then let them work internally. Your external F/U timeline is unchanged. |
| Named hiring contact on job post | Recruiter or HM with implied permission | Reach out 1–2 BD after applying. Short note: confirm you applied + one sentence on why this role specifically. Highest-leverage F/U scenario. |
| Named HM/manager you found on LinkedIn (cited in CL) | Person who'll review your file | Reach out within 3 BD. LinkedIn DM — 3 sentences max. Don't reference that you name-dropped them in the CL; just introduce yourself and reference the role. |
| External connector — mutual contact outside the company | Your network contact | Tell them you applied. Ask: "Would you be comfortable making a warm intro to anyone on their team?" Let them decide whether to amplify. Don't pressure. |

### Per-Company F/U 1 Notes (batch 2026-03-02)
| Company | Type | F/U 1 Date | Hook |
|---------|------|-----------|------|
| Zillow | Mid-size/enterprise | 2026-03-09 | Eventing + real-time data background (Morningstar streaming → Zillow data platform) |
| Upstart | Scale-up | 2026-03-09 | Capital platform data infrastructure; Capital One regulated data work |
| Inspiren | Small startup | **2026-03-07** | 0-to-1 expansion judgment (S001); DM to CPO/VP Product directly |
| Zen Educate | Small startup | **2026-03-07** | Chicago hybrid + UK background natural fit; DM to UK-based hiring contact |
| Pinterest | Enterprise | 2026-03-09 | EQWG signal bridge → content quality signal design; DM to PM manager (low-conversion but worth doing) |

## Outreach Strategy
- Date:
- Depth:
- Positioning source:
- Message types coached:
- Targets contacted:
- Channel strategy:
- Follow-up status:
- LinkedIn profile flagged:
- Key hooks identified:

## Comp Strategy
- Date:
- Depth:
- Target range:
- Range basis:
- Research completeness:
- Stage coached:
- Jurisdiction notes:
- Scripts provided:
- Key principle:

## Job Search Criteria
- Last updated: 2026-03-02
- Daily search: enabled
- Last searched: 2026-03-03
- Location preference: remote OR hybrid Chicago-area — AND willing to relocate to SF, NY, LA, Seattle, Chicago for the right role (confirmed 2026-03-03)

### Track 1: VC / PE / Investment
- Long-term goal: build own investment fund focused on myology-based companies; need VC/PE experience as foundation
- Target roles: VC Associate, Venture Associate, Investor-in-Residence, Investment Analyst (operator background), Operator-to-Investor programs, PE portfolio operations roles
- Target firms: early-stage VC (seed–Series B focus), health/biotech-adjacent investors, PE firms with tech portfolio, venture studios with investment component
- Must-have: firm invests in life sciences, health, biotech, or AI/tech broadly (myology adjacency a plus); operator track valued
- Nice-to-have: thesis-driven firms; emerging fund managers; firms with explicit operator-to-investor programs
- Exclusions: purely financial engineering PE (no value in building toward fund); firms where PM background is irrelevant

### Track 2: Consulting / Accelerator / Incubator
- Goal: project-based work, broad startup exposure, portfolio-style experience — builds the operating breadth useful for investing
- Target types: management/strategy consulting (A&M, BCG Digital, McKinsey Digital, etc.), startup accelerators, venture studios, incubators, EIR programs
- Target roles: Consultant/Senior Consultant, Venture Builder, EIR, Accelerator PM/Operator, Startup Studio product/operator roles
- Must-have: meaningful exposure to different companies/sectors within the role; not a single-company deployment
- Nice-to-have: fintech/health/data adjacent portfolio; roles where investment thesis is part of the work

### Track 3: Traditional PM
- Criteria: must meet at least ONE of the following — all else equal, preference by this rank order:
  1. Major recognizable tech brand (FAANG or equivalent — for resume signal and market credibility)
  2. $220k+ total comp
  3. Meaningful title progression: Senior PM → Lead / Director / Principal / Founding PM
  4. Founding PM at a well-funded, high-signal startup (seed+ with strong investors)
- Product criteria (soft filters — don't reject a great role on these alone):
  - Data/AI core to product (not peripheral)
  - Ideally 0-to-1 or platform-scale work
  - "Cool product" threshold: technology with genuine novelty or intellectual depth (e.g. entity resolution/Quantexa, wildfire AI detection/Pano AI, Notion-style collaborative tools) — refining further as roles are reviewed; not a hard veto, a preference signal
  - "Amazing culture" filter: removed — not a decision criterion
- Seniority range: Senior PM / Lead PM / Principal PM / Director of Product / Founding PM
- Company size/stage: flexible — enterprise OK for brand signal; startup OK for title/comp progression; mid-size OK for both
- Industry: any (data/AI skills transfer); financial services not preferred unless the other criteria strongly warrant it
- Exclusions: pure analytics/BI tooling re-labeled as PM; roles with no path to the comp target; companies with known culture issues (add to exclusions as they emerge)

### Source Priority (updated 2026-03-03)
Work through tiers in order. Every role must be verified on company careers page before surfacing. LinkedIn is last resort only.

**Tier 1 — PM-specific boards:** Mind the Product (lnkd.in/eBz7bB97), Product Manager Job Board (lnkd.in/eyWijeuP), ProductHired (lnkd.in/eBc_BRdH)
**Tier 2 — VC portfolio boards:** a16z Speedrun (lnkd.in/e3pm7frN), Sequoia (lnkd.in/e32E-G_t), Index Ventures (lnkd.in/eENscJUP)
**Tier 3 — Broader boards:** Wellfound, Builtin Chicago, Welcome to the Jungle
**Tier 4 — Remote boards (if remote in scope):** We Work Remotely, Remotivate, Working Nomads, RemoteOK
**Tier 5 — Chicago/Midwest ecosystems:** Midwest Startups (lnkd.in/gp4YRrSq), Jump Capital (lnkd.in/gzDWK7DN), Hyde Park VP (lnkd.in/gxe2PxQK), OCA Ventures (lnkd.in/giuSa5KM), 1871 (1871.com/jobs)
**Tier 6 — LinkedIn (last resort):** Flag to candidate when used

### Pre-Screen Filter (run before any decode or full presentation)
1. Correct role type? (PM, not VC partner / GTM advisor / consultant) → if not: 2-line skip
2. Title band match? (no more than 1 level off) → if 2+ levels off: 2-line skip
3. Posting verified on company careers page? → if not verified: drop and replace

### Search Notes
- Refined from feedback: 1 refinement (2026-03-03: source priority list added based on candidate feedback)
- Refinement log:
  - 2026-03-03: Added tiered source priority list (Midwest/VC ecosystem boards first, LinkedIn last resort); added company careers page verification requirement; added pre-screen filter for role type + title band
- Note: ~8 applications to non-PM roles in pre-tracker data were intentional Track 1/2 applications — not role targeting scatter

## Job Discovery Log
| Date | Company | Role | URL | Fit Signal | Interest | Notes |
|------|---------|------|-----|------------|---------|-------|
| 2026-03-02 | Zen Educate | Principal PM (IC) | https://jobs.lever.co/zeneducate/4c74de74-1d10-415e-8981-3cb93d0ced6e | SaaS + startup expansion | Candidate-selected | Weak Fit — not data/AI core, comp likely below $220k target, doesn't meet Track 3 criteria; awaiting candidate clarification |
| 2026-03-02 | Inspiren | Principal PM, Strategic Expansion | https://job-boards.greenhouse.io/inspiren/jobs/5065042007 | 0-to-1 expansion, AI product, comp $240k-$280k, Principal title | Candidate-selected | Investable Stretch — hardware requirement is structural gap; strong comp/title upside |
| 2026-03-02 | Pinterest | Sr. PM, Content Quality Signals | https://www.pinterestcareers.com/jobs/7158642/sr-product-manager-content-quality-signals/ | Major tech brand, ML partnership, remote | Candidate-selected | Investable Stretch — major brand, but content safety/B2C domain is a meaningful stretch |
| 2026-03-02 | Zillow | Senior PM, Data Platform | https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External/job/Remote-USA/Senior-Product-Manager--Data-Platform_P749415-1 | Near-perfect data platform fit, recognizable brand, remote | Candidate-selected | Strong Fit (role content) — title is lateral; top of comp range ($232k) borderline hits target |
| 2026-03-02 | Upstart | Principal PM, Capital Platform | https://careers.upstart.com/jobs/principal-product-manager-capital-platform-a8813358-dc80-4a50-911d-0a3384a38866 | Principal title, $188k-$260k, regulated fintech expertise | Candidate-selected | Strong Fit (skills) — domain trap: keeps her in financial services; candidate should confirm intent before applying |
| 2026-03-03 | Energize Capital | Unknown VC role | — | Track 1 VC/PE | no | Salary too low — rejected by candidate |
| 2026-03-03 | UChicago Polsky | Sr Manager, Venture Development | already applied (A041) | Track 2 — venture development, university ecosystem | yes | Track 2 confirmed — already applied 2026-02-06; low salary accepted for venture path exposure |
| 2026-03-03 | Webflow | Principal PM, AI | webflow.com/careers | AI platform + Principal title + $200–340k comp | yes | Investable Stretch — strong AI/ML alignment; ~9 years product work since 2017 meets 10-year requirement; verify Illinois comp zone |
| 2026-03-03 | Upwork | Principal PM, AI Search | upwork.com/careers | AI/ML search, Principal title, $230–345k comp | yes | Investable Stretch — verify posting still active; marketplace gap; strong comp |
| 2026-03-03 | Braze | Senior PM, Applied ML | braze.com/careers | B2B + ML + DS partnership match; Chicago option | yes | Investable Stretch — verify comp band; title lateral; B2B fit strong |
| 2026-03-03 | BetterHelp | Senior PM, International | https://job-boards.greenhouse.io/betterhelpcom/jobs/5127442008 | B2C marketplace, international focus | no | Weak Fit — comp $170–200k below target; three-way domain mismatch (international + B2C + healthcare) |
| 2026-03-03 | Halcyon | Senior PM | https://job-boards.greenhouse.io/halcyon/jobs/5808978004 | B2B SaaS, cybersecurity | maybe | Long-Shot Stretch — B2B experience fits; cybersecurity domain is structural gap; pursue only with referral |
| 2026-03-03 | TollBit | PM | https://job-boards.greenhouse.io/tollbit/jobs/5114600008 | AI infrastructure, developer experience | maybe | Research First — verify comp + title regression before committing |
| 2026-03-03 | Owner | Director of Product | a16z article (Owner.com) | Restaurant tech, Director title | maybe | Investable Stretch conditional on comp — verify $200k+ before applying; domain gap is restaurant tech |
| 2026-03-03 | EliseAI | Growth PM, Future Platforms | already applied (A022) | AI company, growth PM function | — | Already applied 2026-02-04; Long-Shot Stretch — Growth PM function mismatch vs. data platform background |
| 2026-03-03 | Decagon | Product Manager (Founding PM) | https://jobs.ashbyhq.com/decagon/d790a2a2-958d-4f49-96ed-adbd68d2e6ce | AI platform (agent builder, testing, analytics, enterprise controls); founding PM; $200–285k | yes | Strong Fit — top pick of batch; comp hits target; platform PM scope maps directly to background; SF in-office (viable) |
| 2026-03-03 | Rippling | Product Lead, Platform, Reporting & Analytics | https://ats.rippling.com/rippling/jobs/388848ed-3f89-4f5e-9698-3adf8a25ae4c | Reporting/BI/unified data platform; Product Lead title; $159–278k; SF hybrid | yes | Strong Fit — data platform scope maps directly; Product Lead is title progression; recognized brand; verify comp range in recruiter screen |
| 2026-03-03 | Sayari | Senior PM, AI Platform | https://job-boards.greenhouse.io/sayari/jobs/4140623009 | Knowledge graph + risk intelligence AI platform; $185–200k base + bonus + equity; US remote | yes | Strong Fit — knowledge graph = Quantexa's exact technology; strongest domain skills alignment of any role; confirm total comp $220k+ |
| 2026-03-03 | Pylon | Product Manager (First PM hire) | https://jobs.ashbyhq.com/pylon-labs/6fabb5e9-7bc8-4098-826f-d4793c43b2b5 | B2B post-sales SaaS; first PM hire; Series B $51M; SF in-office; comp undisclosed | maybe | Investable Stretch — B2B 0-to-1 ✓; not data/AI core; pursue only if comp negotiates to $220k+ |
| 2026-03-03 | Ambient.ai | Senior PM | https://jobs.ashbyhq.com/ambient.ai/6a15cf0a-6e35-452a-92ba-5e4072a2a6d5 | Physical security AI; one of first PMs; $180–205k base + equity; Redwood City hybrid | maybe | Investable Stretch — enterprise B2B ✓; physical security domain stretch; pursue if problem is genuinely interesting |
| 2026-03-03 | Flint | Founding PM | https://jobs.ashbyhq.com/flint/d314ccb6-6884-4a3c-9a1f-bb9359c0ffde | Autonomous websites AI; seed ($5M); SF onsite; CS degree REQUIRED; comp undisclosed | no | Skip — CS degree hard requirement; seed-stage comp likely below target; weakest domain relevance |
| 2026-03-03 | Magic School | Senior PM, Student Experiences | https://jobs.ashbyhq.com/magicschool/560fbe30-777e-44a3-bf64-34f647b26def | K-12 edtech AI; consumer product; $160–200k; US remote | no | Skip — comp ceiling below target; consumer edtech double domain mismatch; priority deadline March 8 |
| 2026-03-03 | Decagon | Senior Agent PM (NYC — bonus find) | https://jobs.ashbyhq.com/decagon/dcf9b561-f2fb-422b-88a9-33ce76e96608 | Customer-facing enterprise AI agent implementation; $200–285k; NYC in-office | maybe | Investable Stretch — comp hits target; NY viable; customer-facing track (different from SF platform role); Quantexa delivery context relevant |

## Application Tracker
| ID | Date | Company | Role | Resume Version | Method | Cover Letter | Status | Response Date | Response Type | F/U 1 Due | F/U 1 Done | F/U 2 Due | F/U 2 Done | Notes |
|----|------|---------|------|----------------|--------|-------------|--------|--------------|--------------|-----------|-----------|-----------|-----------|-------|
| A001 | 2026-02-~16 | Uber | Senior PM | unknown | unknown | unknown | Screen Done | — | HM interview | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | HM interview done; pending outcome on next round |
| A002 | 2026-03-02 | Unknown | Senior PM | unknown | unknown | unknown | Screen Scheduled | — | — | N/A | — | N/A | — | Recruiter screen pending outcome — update company name when known |
| A003 | 2026-02-10 | Qumis | Founding PM | unknown | company-website | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A004 | 2025-12-09 | Future Sight | Product Lead, Venture studio core team | unknown | company-website | Yes | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A005 | 2025-12-04 | Nabis | Technical PM | unknown | other | No | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A006 | 2025-12-09 | Decile / VC labs | PM | unknown | company-website | Yes | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A007 | 2025-12-10 | AirGarage | Senior PM | unknown | company-website | Yes | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A008 | 2025-12-10 | Pano AI | Senior PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A009 | 2025-12-10 | Jobgether | Senior PM, Dedicated | unknown | company-website | No | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A010 | 2025-12-12 | Houlihan Lokey | DSG Senior PM - VP | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | Messaged contact 2026-02-10 |
| A011 | 2026-02-02 | Whatnot | Product Manager | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A012 | 2026-02-02 | Oportun | Principal PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A013 | 2026-02-02 | datatruck | Senior PM | unknown | linkedin | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A014 | 2026-02-02 | Adyen | Senior PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A015 | 2026-02-03 | Alumni Venture | Senior Associate | unknown | company-website | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | Non-PM role |
| A016 | 2026-02-03 | Monzo | Lead PM | unknown | company-website | Yes | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A017 | 2026-02-04 | JP Morgan | PM Fusion Data | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A018 | 2026-02-04 | Google | Various | unknown | company-website | No | Loop Scheduled | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | Online assessment passed (2026-02-04); awaiting recruiter phone screen scheduling |
| A019 | 2026-02-04 | Koyfin | Senior PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A020 | 2026-02-04 | Alvarez and Marsal | Director | unknown | company-website | No | Loop Scheduled | — | Recruiter screen | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | Recruiter screen complete; waiting to hear about next steps |
| A021 | 2026-02-04 | Nexus 3 capital | Director | unknown | company-website | No | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A022 | 2026-02-04 | Elise AI | Growth PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A023 | 2026-02-04 | Weights & Biases (CoreWeave) | Staff PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A024 | 2026-02-04 | Persuit | PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A025 | 2026-02-04 | Tilt | Senior PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A026 | 2026-02-04 | Transcarent | Senior PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A027 | 2026-02-05 | Acorns | PM, Core Experience | unknown | company-website | No | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A028 | 2026-02-05 | Chainguard | Senior PM | unknown | company-website | No | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A029 | 2026-02-05 | Signifyd | Senior PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A030 | 2025-02-05 | Varo Bank | Senior PM, Data | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | Date may be 2026-02-05 — verify |
| A031 | 2026-02-05 | Vercel | PM Accounts | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A032 | 2026-02-05 | Recharge | PM | unknown | company-website | No | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A033 | 2026-02-05 | Codal | PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A034 | 2026-02-05 | Benchling | PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A035 | 2026-02-06 | Netflix | Various | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A036 | 2026-02-06 | Glia | Senior PM | unknown | company-website | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A037 | 2026-02-06 | mHub | Venture Associate | unknown | other | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | Non-PM role |
| A038 | 2026-02-06 | Primary | Associate, Fintech Incubation | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | Non-PM role |
| A039 | 2026-02-06 | Shaper Capital | Venture Builder in Residence | unknown | company-website | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | Non-PM role |
| A040 | 2026-02-06 | Anfa | VC Investor | unknown | linkedin | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | Non-PM role |
| A041 | 2026-02-06 | University of Chicago | Senior Manager, Venture Development | unknown | company-website | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | Non-PM role |
| A042 | 2026-02-06 | Canoe Intelligence | Senior PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A043 | 2026-02-06 | Blackstone | PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A044 | 2026-02-06 | Juniper Square | Senior PM | unknown | company-website | No | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A045 | 2026-02-06 | Fin | PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A046 | 2026-02-06 | Addition Wealth | Senior PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A047 | 2026-02-12 | Apple | Various | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A048 | 2026-02-12 | Producto | First PM | unknown | other | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A049 | 2026-02-12 | Human Ventures | PM | unknown | linkedin | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A050 | 2026-02-12 | 84.51° | Lead PM, Core Services | unknown | company-website | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A051 | 2026-02-12 | Avant | Gen AI PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A052 | 2026-02-12 | Plaid | PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A053 | 2026-02-12 | Makai Labs | PM | unknown | company-website | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A054 | 2026-02-12 | Rinsed | PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A055 | 2026-02-12 | Amethyst Partners | Senior PM | unknown | linkedin | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A056 | 2026-02-12 | Primactic | Senior PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A057 | 2026-02-12 | Robinhood | PM | unknown | company-website | No | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A058 | 2026-02-13 | Stripe | Various | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | ⭐ Top-ranked (13/15) |
| A059 | 2026-02-13 | Figma | PM Creation Engine | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | ⭐ Top-ranked (12/15) |
| A060 | 2026-02-18 | Perplexity | PM Comet Mobile | unknown | company-website | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | ⭐ Top-ranked (12/15) |
| A061 | 2026-02-18 | Grindr | Technical PM | unknown | company-website | No | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A062 | 2026-02-18 | Rally UXR | Senior PM | unknown | company-website | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A063 | 2026-02-18 | Valon | Senior PM, Data | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A064 | 2026-02-18 | Employ | PM Incubation | unknown | company-website | No | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A065 | 2026-02-18 | Playbook | PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A066 | 2026-02-18 | Caribou | Principal PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A067 | 2026-02-18 | Vanilla | Senior PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A068 | 2026-02-18 | Backstage / Cast and Crew | Senior PM | unknown | linkedin | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A069 | 2026-02-18 | Weave | Senior PM AI/ML | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A070 | 2026-02-18 | Sumsub | Data Intelligence Global PM | unknown | company-website | Yes | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A071 | 2026-02-18 | Mindbody | Senior PM | unknown | linkedin | No | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A072 | 2026-02-18 | Retool | PM Automation | unknown | y-combinator | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | Also applied on website 2026-02-23 |
| A073 | 2026-02-19 | Certara | Senior PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A074 | 2026-02-19 | Confido | Senior PM | unknown | y-combinator | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A075 | 2026-02-19 | Fieldguide | Lead PM | unknown | y-combinator | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A076 | 2026-02-19 | Juicebox | Founding PM | unknown | y-combinator | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A077 | 2026-02-19 | Sully.ai | Senior PM | unknown | y-combinator | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A078 | 2026-02-19 | Ophelia | Senior PM | unknown | company-website | Yes | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A079 | 2026-02-19 | Candid Health | Senior PM | unknown | company-website | Yes | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A080 | 2026-02-20 | Nextdoor | PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A081 | 2026-02-20 | Anthropic | Compute Platform PM | unknown | company-website | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A082 | 2026-02-23 | Handshake | Senior PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A083 | 2026-02-23 | Klaviyo | Senior PM | unknown | jungle | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A084 | 2026-02-23 | Afresh | Senior PM | unknown | jungle | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A085 | 2026-02-23 | Dataiku | Product Evangelist | unknown | jungle | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | Not strictly PM role |
| A086 | 2026-02-23 | Common Room | Senior PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A087 | 2026-02-25 | Nuro | Senior PM | unknown | company-website | Yes | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A088 | 2026-02-26 | Rentable / ApartmentIQ | Senior PM | unknown | company-website | No | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A089 | 2026-02-26 | Block | Platform Monetization PM | unknown | company-website | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A090 | 2026-02-26 | World Labs | PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A091 | 2026-02-26 | Abby | Senior PM | unknown | jungle | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A092 | 2026-02-26 | Mercury | Senior PM | unknown | jungle | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A093 | 2026-02-27 | Cambio | Senior PM | unknown | company-website | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A094 | 2026-02-27 | Permit Flow | PM | unknown | wellfound | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A095 | 2026-02-27 | Reach Security | Senior PM | unknown | wellfound | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A096 | 2026-02-27 | Human Agency | Lead PM | unknown | wellfound | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A097 | 2026-02-27 | Affinity | Staff PM | unknown | company-website | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A098 | 2026-03-02 | Whatznew.ai | PM, AI | unknown | wellfound | Yes | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A099 | 2026-03-02 | Freed | PM, Growth | unknown | wellfound | No | Rejected | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A100 | 2026-03-02 | Noyo | Senior PM | unknown | wellfound | No | Applied | — | — | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | N/A (pre-tracker) | — |
| A101 | 2026-03-02 | Upstart | Principal PM, Capital Platform | regulated_v3.5 | company-website | Yes — generated, no edits | Applied | — | — | 2026-03-09 | — | 2026-03-16 | — | CL Style A (Earned Insight: Logic Drift governance); Source: company-website; F/U 1 at 5BD post-apply |
| A102 | 2026-03-02 | Inspiren | Principal PM, Strategic Expansion | vc_startup_v5.1 | company-website | Yes — hardware field (not CL), generated, no edits | Applied | — | — | 2026-03-07 | — | 2026-03-16 | — | CL N/A — form field only (Sthaler finger vein sensor, 4 sentences); Source: company-website; F/U 1 at 3BD (startup) — DM CPO/VP Product directly |
| A103 | 2026-03-02 | Zen Educate | Senior PM | general_saas_v4.3 | company-website | Yes — free text box, 2 paragraphs, Logic Drift proof, UK-to-US hook, iterated with candidate | Applied | — | — | 2026-03-07 | — | 2026-03-16 | — | CL Style B (Mirror: Logic Drift as direct proof + UK-to-US background mirror); Source: company-website; ATS ~95% (19/20); F/U 1 at 3BD (startup) — Chicago + UK background hook |
| A104 | 2026-03-02 | Pinterest | Sr. PM, Content Quality Signals | general_saas_v4.3 | company-website | Yes — 3 paragraphs, EQWG quality signal bridge (S002), gap acknowledged honestly | Applied | — | — | 2026-03-09 | — | 2026-03-16 | — | CL Style A (Earned Insight: EQWG signal bridge, candidate-written); Source: company-website; ATS ~85% (17/20); F/U 1 at 5BD |
| A105 | 2026-03-02 | Zillow | Senior PM, Data Platform | platform_v2.3_zillow_20260302 | company-website | No | Applied | — | — | 2026-03-09 | — | 2026-03-18 | — | Resume-only; no CL; F/U 1 at 5BD |
| A106 | 2026-03-03 | Webflow | Principal PM, AI | platform_v2.5 (desktop v2.5.docx) | company-website | Yes — CL + Why Webflow answer (vibe coding two-gap framing: dev gap vs design expertise gap) | Applied | — | — | 2026-03-10 | — | 2026-03-19 | — | CL Style C (Problem Statement: two-gap framing); ATS ~81% (platform_v2.5); F/U 1 at 5BD |
| A107 | 2026-03-03 | Halcyon | Senior PM | general_saas_v4.4 (desktop v4.4.docx) | company-website | Yes — CL (RAI course guest speaker hook; domain gap addressed directly) | Applied | — | — | 2026-03-06 | — | 2026-03-16 | — | CL Style A (Earned Insight: Responsible AI Leadership course cybersecurity guest speaker); ATS ~87%; F/U 1 at 3BD (startup) |
| A108 | 2026-03-03 | TollBit | PM | vc_startup_v5.1_tollbit_20260303 (desktop v5.2.docx edits) | company-website | Yes — CL (API monetization problem statement) | Applied | — | — | 2026-03-06 | — | 2026-03-16 | — | CL Style C (Problem Statement: commercial layer for AI content access); ATS ~82%; F/U 1 at 3BD (startup) |
| A109 | 2026-03-04 | Sayari | Senior PM, AI Platform | regulated_v3.6_sayari_20260303 | company-website | Yes — generated 2026-03-04; ground truth/evaluation framework hook; S002 EQWG primary evidence | Applied | — | — | 2026-03-11 | — | 2026-03-18 | — | ATS ~53%; JD Analysis on file; F/U 1 at 5BD |
| A110 | 2026-03-04 | Rippling | Product Lead, Payments Risk | regulated_v3.7 | company-website | Yes — generated 2026-03-04; data layer/bad data hook; S003 Logic Drift + S002 EQWG evidence | Applied | — | — | 2026-03-11 | — | 2026-03-18 | — | ATS ~63%; JD Analysis on file; F/U 1 at 5BD |

## Application Analytics
- Total applications: 110 (98 from spreadsheet + A001 Uber + A002 unknown recruiter screen + A101 Upstart + A102 Inspiren + A103 Zen Educate + A104 Pinterest + A105 Zillow + A106 Webflow + A107 Halcyon + A108 TollBit + A109 Sayari + A110 Rippling)
- Overall response rate (any response / spreadsheet total): 21/98 = 21% — includes 19 rejections + 2 interview invites
- Interview conversion rate: 2/98 = 2% (Google, Alvarez and Marsal) — plus Uber HM (pre-tracker)
- Most effective resume version: unknown — resume version not tracked pre-coaching; start tracking from A101+ onwards
- Most effective method: company-website dominates (73/98 = 74%) — insufficient contrast data to draw conclusions; Wellfound, YC, Jungle, LinkedIn each <7 applications
- Cover letter impact: With CL: 29 apps, 7 rejections (24%), 0 interviews. Without CL: 69 apps, 12 rejections (17%), 2 interviews. CL is not correlating with better outcomes — but this may reflect role targeting rather than CL quality. CL experiment tracking active from 2026-03-02 with style variants (A=Earned Insight, B=Mirror, C=Problem Statement, D=No CL)
- Average time to first response: insufficient tracking data (response dates not recorded pre-tracker)
- Stage conversion: applied → any response 21%; applied → interview 2%
- Role targeting note: ~8 applications to non-PM roles (VC, venture associate, product evangelist) — these should be filtered or tracked separately
- Last analytics update: 2026-03-02

### CL Experiment Tracker (started 2026-03-02)
| Style | Label | Apps | Responses | Response Rate | Notes |
|-------|-------|------|-----------|---------------|-------|
| A | Earned Insight | 3 (A101, A104, A107) | pending | — | Upstart (Logic Drift insight), Pinterest (EQWG signal bridge), Halcyon (RAI course cybersecurity guest speaker) |
| B | Mirror | 1 (A103) | pending | — | Zen Educate (Logic Drift proof + UK-to-US) |
| C | Problem Statement | 2 (A106, A108) | pending | — | Webflow (two-gap design/dev framing), TollBit (API monetization commercial layer) |
| D | No CL (control) | 1 (A105) | pending | — | Zillow (resume-only); Pre-tracker data: 69 apps → 17% rejection, 2 interviews |

## JD Analysis: Zillow — Senior PM, Data Platform
- Date: 2026-03-02
- Depth: Standard
- Fit verdict: Strong Fit
- Top competencies: (1) Data platform strategy + governance adoption, (2) Cross-functional engineering partnership, (3) Developer experience / platform rollout
- Frameable gaps: Event-driven/eventing architecture vocabulary (adjacent to streaming feeds work at Morningstar; frameable); lateral title (Senior→Senior, not progression)
- Structural gaps: None that can't be addressed in resume + CL
- Unverified assumptions: 2 (whether comp top-of-range is achievable at offer; exact scope of "eventing" — Kafka/stream processing vs. broader event bus)
- Batch triage rank: 1/5
- ATS estimate: 68% base → 76% with targeted additions (add: "eventing", "event-driven", "developer experience", "platform enablement")
- Resume version: General/SaaS v4.1 (Platform/Infra v4.2 preferred but failed to load)
- CL drafted: Yes — 2026-03-02, earned secret: governance trust → platform adoption
- Follow-up: F/U 1 at 5BD post-apply; LinkedIn DM to Zillow data PM/recruiter after apply

## JD Analysis: Upstart — Principal PM, Capital Platform
- Date: 2026-03-02
- Depth: Standard
- Fit verdict: Strong Fit (with domain caveat)
- Top competencies: (1) Regulated/fintech data platform, (2) Enterprise B2B partner integrations, (3) 0-to-1 platform development
- Frameable gaps: "Capital platform" vocabulary (reframe Capital One as capital data infrastructure); white-label framing (Quantexa SaaS is analogous)
- Structural gaps: No direct lending/loan product experience; staying in financial services (candidate's stated intent is to move away from FS)
- Unverified assumptions: 1 (whether domain concern is a dealbreaker for candidate or a preference to be overridden by comp/title)
- Batch triage rank: 2/5
- ATS estimate: 65% base → 73% with targeted additions (add: "capital platform", "white-label", "partner integrations", "lender workflows")
- Resume version: Regulated/Fintech v3.4
- CL drafted: Yes — 2026-03-02, earned secret: logic drift / definitional governance in capital data systems
- Follow-up: F/U 1 at 5BD post-apply; LinkedIn DM to Capital Platform PM lead at Upstart

## JD Analysis: Inspiren — Principal PM, Strategic Expansion
- Date: 2026-03-02
- Depth: Standard
- Fit verdict: Investable Stretch
- Top competencies: (1) Strategic expansion / new market entry, (2) 0-to-1 product development, (3) Cross-functional leadership across hardware/software/AI
- Frameable gaps: Healthcare domain (PM principles transfer; domain expertise builds fast); no explicit "expansion portfolio" language (Quantexa pivot is the reframe)
- Structural gaps: "Experience with hardware-enabled or sensor-based systems in production" — was flagged as hard requirement. Resolved: Sthaler used a proprietary finger vein sensor as the core of its biometric payment platform; this is frameable and honest. v5.1 resume updated to reflect this.
- Unverified assumptions: 2 (how strictly the hardware requirement is screened; whether the expansion focus is geographic or segment-based)
- Batch triage rank: 3/5
- ATS estimate: 55% base → 62% with targeted additions (hardware gap cannot be fixed); startup size increases probability of human review over ATS filtering
- Resume version: VC/Startup v5.0 with "strategic market expansion" reframe on Quantexa pivot bullet
- CL drafted: Yes — 2026-03-02, earned secret: expansion judgment (preserve vs. rebuild) from S001
- Follow-up: F/U 1 at 5BD; LinkedIn DM to CPO/VP Product after apply (small company — direct outreach is high signal)

## JD Analysis: Pinterest — Sr. PM, Content Quality Signals
- Date: 2026-03-02
- Depth: Standard
- Fit verdict: Investable Stretch
- Top competencies: (1) ML-driven signal design and measurement, (2) Cross-functional strategy in ambiguous environments, (3) Major tech platform experience
- Frameable gaps: ML quality measurement experience (EQWG proxy signal story directly maps); cross-functional leadership at scale
- Structural gaps: No content quality/safety/integrity domain experience; no consumer/B2C experience (all B2B/enterprise); "content signals" vocabulary entirely absent from resume
- Unverified assumptions: 3 (how much weight Pinterest places on safety domain experience vs. transferable ML measurement skills; actual comp offered at Sr PM band; whether "fast-growing companies" requirement disfavors enterprise background)
- Batch triage rank: 4/5
- ATS estimate: 48% base → 55% with targeted additions; human review is the primary path given domain vocabulary gap
- Resume version: General/SaaS v4.1 with "quality signals" and "proxy-based measurement" reframe on EQWG bullet
- CL drafted: Yes — 2026-03-02, earned secret: ML measurement proxy (S002 EQWG) maps to content quality signals design
- Follow-up: F/U 1 at 5BD; Pinterest has large recruiting operation — LinkedIn DM to PM manager has low but nonzero success rate

## JD Analysis: Zen Educate — Principal PM (IC)
- Date: 2026-03-02
- Depth: Standard (full JD retrieved from candidate)
- Fit verdict: Investable Stretch
- Top competencies: (1) End-to-end discovery + delivery in ambiguous environments, (2) Data-driven product decision-making, (3) Cross-functional alignment across ops/eng/design
- Frameable gaps: Marketplace domain new (but JD emphasises general PM rigour over domain expertise); EdTech new; ~9 years product work since 2017 essentially meets any 10-year requirement
- Structural gaps: No marketplace business experience (explicit JD requirement); comp unstated (likely below $220k target for EdTech startup); not a major tech brand; not data/AI core
- Unverified assumptions: 2 (actual salary range; how strictly "marketplace" is screened vs. general PM skills)
- Batch triage rank: 4/5 (upgraded from 5 — full JD shows strong general PM skills match; Chicago hybrid is a significant location positive)
- ATS estimate: ~95% (general_saas_v4.3, 19/20)
- Resume version: general_saas_v4.3
- CL drafted: Yes — free text box, 2 paragraphs, 2026-03-02
- Location note: Chicago hybrid (3 days in office) — directly matches candidate's location; rare advantage
- Follow-up: TBD

## JD Analysis: Webflow — Principal PM, AI
- Date: 2026-03-03
- Depth: Quick Scan
- Fit verdict: Investable Stretch
- Top competencies: (1) AI/ML product roadmap ownership, (2) Cross-functional leadership at platform scale, (3) Gen AI/LLM product delivery for non-technical users
- Frameable gaps: Gen AI/LLM-specific experience (AI/ML product context is real; LLM-specific depth uncertain); zone-dependent comp (verify Illinois zone)
- Structural gaps: None — ~9 years product work since 2017 Product Owner start meets the 10-year requirement; YOE is not a screening risk
- Unverified assumptions: 2 (exact comp zone for Illinois; scope of "AI roadmap" — platform-wide vs. specific product area)
- Batch triage rank: 1/9 (2026-03-03 batch)
- Story fit: S001 (AI platform strategy + competitive positioning), S002 (ML product + cross-functional alignment)

## JD Analysis: Upwork — Principal PM, AI Search
- Date: 2026-03-03
- Depth: Quick Scan
- Fit verdict: Investable Stretch
- Top competencies: (1) AI/ML product for search & recommendations, (2) Two-sided marketplace product, (3) Data-driven decision making at scale
- Frameable gaps: Marketplace experience (reframe entity resolution as a matching/ranking system — structural parallel); search/recommendations background (data/ML experience is real, search-specific is not)
- Structural gaps: No direct two-sided marketplace PM experience — real gap, bridgeable with narrative
- Unverified assumptions: 2 (posting still active — verify first; whether marketplace experience is hard-screened or preferential)
- Batch triage rank: 2/9 (2026-03-03 batch)
- Story fit: S002 (measurement-first approach, ML product), S003 (data systems + analytics-driven root cause)

## JD Analysis: Braze — Senior PM, Applied ML
- Date: 2026-03-03
- Depth: Quick Scan
- Fit verdict: Investable Stretch
- Top competencies: (1) ML product development with embedded data science collaboration, (2) B2B enterprise platform product, (3) Decisioning/recommendation systems
- Frameable gaps: Marketing automation domain (reframe as "ML decisioning infrastructure" — EQWG is the bridge: built ML that makes quality decisions on behalf of teams); title lateral not progression
- Structural gaps: No marketing automation / customer engagement platform domain experience
- Unverified assumptions: 2 (actual comp band for Senior PM at Braze — verify $200k+ OTE achievable; whether "ML/DS background preferred" is differentiating or partially screening)
- Batch triage rank: 3/9 (2026-03-03 batch)
- Story fit: S002 (primary — DS partnership + measurement + influence without authority maps directly), S003 (data systems quality)

## JD Analysis: Owner — Director of Product
- Date: 2026-03-03
- Depth: Quick Scan (partial — full JD not retrieved)
- Fit verdict: Investable Stretch (conditional on comp verification)
- Top competencies: (1) Director-level product leadership + strategy, (2) SaaS platform product, (3) 0-to-1 or expansion product work
- Frameable gaps: Restaurant tech domain (SaaS platform principles transfer; no hospitality experience is a real gap but may not be hard-screened at Director level)
- Structural gaps: None confirmed — need full JD to assess
- Unverified assumptions: 3 (comp range — critical before investing; full JD requirements; whether domain expertise is required vs. preferred at Director level)
- Batch triage rank: 4/9 (conditional — contingent on comp verification)
- Story fit: S001 (0-to-1 + strategic expansion), S004 (cross-functional delivery at scale)

## JD Analysis: Halcyon — Senior PM
- Date: 2026-03-03
- Depth: Quick Scan
- Fit verdict: Long-Shot Stretch
- Top competencies: (1) B2B enterprise SaaS product, (2) Cybersecurity/security domain knowledge, (3) Cross-functional alignment in technical product
- Frameable gaps: B2B enterprise SaaS model (Quantexa maps well)
- Structural gaps: No cybersecurity domain experience — CISO/SOC buyer language, threat models, incident response workflows are expected context at a security startup; this is visible from the resume
- Unverified assumptions: 2 (how strictly cybersecurity domain is screened vs. general enterprise SaaS PM; whether equity brings total comp to $220k+)
- Batch triage rank: 5/9 (2026-03-03 batch)
- Story fit: S001 (B2B enterprise platform context), S003 (platform quality + governance)

## JD Analysis: TollBit — PM
- Date: 2026-03-03
- Depth: Quick Scan
- Fit verdict: Research First (Weak Fit without comp data)
- Top competencies: (1) Developer experience product (API/SDK/docs), (2) AI infrastructure product for novel use cases, (3) Early-stage execution under ambiguity
- Frameable gaps: AI infrastructure context (data platform work is adjacent in philosophy)
- Structural gaps: Title "PM" not "Senior PM" — title regression from current trajectory; comp unknown (high uncertainty for early-stage)
- Unverified assumptions: 3 (comp range — critical; equity structure at current valuation; whether "PM" title represents actual Senior PM scope)
- Batch triage rank: 6/9 (2026-03-03 batch)
- Story fit: S002 (influence without authority + measurement first), S001 (AI product strategy)

## JD Analysis: BetterHelp — Senior PM, International
- Date: 2026-03-03
- Depth: Quick Scan
- Fit verdict: Weak Fit
- Top competencies: (1) International product management (localization, compliance, multi-market), (2) B2C subscription/marketplace, (3) Healthcare/mental health domain
- Frameable gaps: None worth investing in — three-way domain mismatch
- Structural gaps: No international product experience; no B2C/consumer PM background; comp $170–200k base below $220k target; healthcare domain is new; Teladoc subsidiary = corporate structure / slower career progression
- Unverified assumptions: 0 — weak fit is clear from available data
- Batch triage rank: 9/9 (2026-03-03 batch) — Skip; do not apply
- Story fit: None with strong relevance

## JD Analysis: PayPal — Senior PM, SMB Risk
- Date: 2026-03-03
- Depth: Quick Scan
- Fit verdict: Investable Stretch (comp ceiling risk)
- Top competencies: (1) Data-driven product decisions + metrics, (2) AI/ML product integration, (3) End-to-end cross-functional execution
- Frameable gaps: Risk/fraud domain — Capital One financial data platform is adjacent; downstream decision accuracy framing bridges it
- Structural gaps: Chicago band tops at $193,600 — below $220k target; no payments/risk product background
- Unverified assumptions: 2 (whether Chicago band is flexible for strong candidates; whether risk domain is a hard screen)
- Batch triage rank: 1/3 (2026-03-03 new batch) — recruiter inbound via personalised link (vanramirez@paypal.com)
- Decision: Skipped for now — comp ceiling risk; revisit if recruiter re-engages

## JD Analysis: a16z Speedrun — Partner, Product Growth
- Date: 2026-03-03
- Depth: Quick Scan
- Fit verdict: Weak Fit
- Top competencies: (1) PLG strategy (freemium/bottoms-up/community), (2) Founder advisory / $0→$10M ARR track record, (3) VC ecosystem credibility + public profile
- Frameable gaps: Quantexa L:S ratio + no-code tooling is product-led delivery, not product-led growth (acquisition loops) — insufficient bridge
- Structural gaps: Not a PM role; no PLG/growth marketing track record; no founder experience; SF in-person required; VC ecosystem credibility gap
- Unverified assumptions: 0 — weak fit is clear from available data
- Batch triage rank: 3/3 (2026-03-03 new batch)
- Decision: Skip

## JD Analysis: Decagon — Product Manager (Founding PM)
- Date: 2026-03-03
- Depth: Quick Scan
- Fit verdict: Strong Fit
- Top competencies: (1) AI platform product ownership (agent builder, testing, analytics, integrations, enterprise controls), (2) Technical depth — APIs, data models, architecture, (3) Founding 0-to-1 platform product
- Frameable gaps: CS degree preferred (not required — "or equivalent technical experience"); AI agents domain is adjacent not identical to data platform
- Structural gaps: None — strong technical acumen + 0-to-1 + enterprise customer base all present; degree preference is non-blocking
- Unverified assumptions: 1 (whether comp $200–285k is base-only or base+equity-attributed)
- Batch triage rank: 1/7 (2026-03-03 Ashby+expanded batch)
- Story fit: S001 (founding 0-to-1 + self-serve configuration = Quantexa no-code tool), S002 (analytics + measurement infrastructure), S004 (cross-functional alignment at enterprise scale)
- URL: https://jobs.ashbyhq.com/decagon/d790a2a2-958d-4f49-96ed-adbd68d2e6ce
- Decision: Pursue — top pick of the batch

## JD Analysis: Rippling — Product Lead, Platform, Reporting & Analytics
- Date: 2026-03-03
- Depth: Quick Scan
- Fit verdict: Strong Fit
- Top competencies: (1) Reporting/BI/analytics platform product ownership, (2) Unified data platform + data federation across sources, (3) Complexity-to-simplicity UX for enterprise users
- Frameable gaps: HR/IT/Finance domain (not FS, and platform principles transfer completely); wide comp range — verify achievable band
- Structural gaps: None — data federation, unified data platform, and BI/analytics scope directly match Capital One + Morningstar + Quantexa background
- Unverified assumptions: 2 (where in $159k–$278k range Irene would land; whether Rippling would consider Chicago-based for nominally SF role — need to confirm in recruiter screen)
- Batch triage rank: 2/7 (2026-03-03 Ashby+expanded batch)
- Story fit: S003 (data systems clarity + pipeline quality), S004 (unified data model + cross-functional alignment), S002 (analytics measurement infrastructure)
- URL: https://ats.rippling.com/rippling/jobs/388848ed-3f89-4f5e-9698-3adf8a25ae4c
- Decision: Pursue — Product Lead title is progression; recognized brand; data platform scope maps directly

## JD Analysis: Sayari — Senior PM, AI Platform
- Date: 2026-03-03
- Depth: Quick Scan
- Fit verdict: Strong Fit
- Top competencies: (1) AI/ML backend platform product (model orchestration, evaluation, prompt management), (2) Knowledge graph + risk intelligence domain, (3) Agentic workflow product strategy
- Frameable gaps: Agentic workflows (adjacent — entity resolution pipelines have similar automation logic); title is lateral (Senior→Senior)
- Structural gaps: None — knowledge graph domain is Quantexa's core technology; risk/financial investigation data directly present in background; AI/ML model lifecycle work at Quantexa maps to requirements
- Unverified assumptions: 2 (bonus structure — need to confirm total comp crosses $220k; whether FS-adjacency of risk intelligence domain feels like staying in FS or moving beyond it)
- Batch triage rank: 3/7 (2026-03-03 Ashby+expanded batch)
- Story fit: S001 (AI product strategy + competitive differentiation), S002 (ML product + measurement infrastructure), S003 (data pipeline quality + root cause)
- URL: https://job-boards.greenhouse.io/sayari/jobs/4140623009
- Decision: Pursue — strongest domain skills alignment of any role reviewed; confirm bonus/equity makes total $220k+

## JD Analysis: Pylon — Product Manager (First PM hire)
- Date: 2026-03-03
- Depth: Quick Scan
- Fit verdict: Investable Stretch
- Top competencies: (1) B2B 0-to-1 product ownership with ARR accountability, (2) Customer-obsessed conviction-led product decisions, (3) GTM collaboration (sales + marketing partnership)
- Frameable gaps: No explicit seniority on title (negotiate to Senior PM); comp undisclosed (negotiate early)
- Structural gaps: No data/AI core product (customer support/success SaaS); no ARR/commercial framing in resume currently — stories need reframing toward revenue signals
- Unverified assumptions: 2 (comp — must reach $220k+; whether B2B SaaS without data/AI core is acceptable given strong 0-to-1 fit)
- Batch triage rank: 4/7 (2026-03-03 Ashby+expanded batch)
- Story fit: S001 (primary — B2B 0-to-1 + arguing the strategy + preserving investment), S002 (customer insight → investment call without authority)
- URL: https://jobs.ashbyhq.com/pylon-labs/6fabb5e9-7bc8-4098-826f-d4793c43b2b5
- Decision: Investable Stretch — pursue only if comp negotiation reaches $220k+; role is not data/AI core

## JD Analysis: Ambient.ai — Senior PM
- Date: 2026-03-03
- Depth: Quick Scan
- Fit verdict: Investable Stretch
- Top competencies: (1) Enterprise B2B product ownership (large customer base), (2) Cross-functional coordination across sales/engineering/leadership, (3) One of first PMs — high ownership founding context
- Frameable gaps: Physical security / computer vision domain (enterprise B2B principles transfer; AI product context is real even if application is different)
- Structural gaps: Physical security domain is meaningfully different from data/AI platform; base comp $180–205k is borderline ($220k+ needs equity to bridge)
- Unverified assumptions: 2 (equity value at Series B — does total comp cross $220k?; whether a16z/YC backing signals strong growth trajectory that justifies lower base)
- Batch triage rank: 5/7 (2026-03-03 Ashby+expanded batch)
- Story fit: S001 (founding 0-to-1 context), S004 (enterprise cross-functional delivery)
- URL: https://jobs.ashbyhq.com/ambient.ai/6a15cf0a-6e35-452a-92ba-5e4072a2a6d5
- Decision: Investable Stretch — pursue if physical security AI is genuinely interesting; domain stretch is real

## JD Analysis: Flint — Founding PM
- Date: 2026-03-03
- Depth: Quick Scan
- Fit verdict: Long-Shot Stretch
- Top competencies: (1) Customer discovery + sales engineering, (2) PLG systems + analytics infrastructure from scratch, (3) Founder-mode execution in ambiguity
- Frameable gaps: N/A — structural gaps dominate
- Structural gaps: CS/Engineering/Math degree HARD REQUIRED (listed as qualification, not preference); seed stage ($5M) — comp almost certainly below $220k target; "3+ years" requirement signals more junior role despite "founding" label; autonomous websites domain weakest data/AI relevance
- Unverified assumptions: 1 (Irene's degree — if CS/Engineering/Math, structural gap partially resolves; if not, hard blocker)
- Batch triage rank: 6/7 (2026-03-03 Ashby+expanded batch)
- Story fit: S001 (0-to-1 context only)
- URL: https://jobs.ashbyhq.com/flint/d314ccb6-6884-4a3c-9a1f-bb9359c0ffde
- Decision: Skip — unless Irene has CS/Engineering/Math degree AND is comfortable with seed-stage comp risk

## JD Analysis: Magic School — Senior PM, Student Experiences
- Date: 2026-03-03
- Depth: Quick Scan
- Fit verdict: Weak Fit
- Top competencies: (1) Consumer product for K-12 students (activation, retention, engagement), (2) Edtech / COPPA/FERPA compliance, (3) AI feature development for youth audiences
- Frameable gaps: None worth investing — domain and comp both misaligned
- Structural gaps: Comp ceiling $200k < $220k target; consumer K-12 edtech = double domain mismatch vs B2B data/AI platform; edtech experience explicitly required; consumer product motion entirely different from enterprise B2B work; priority deadline March 8 (2 days)
- Unverified assumptions: 0 — weak fit clear from available data
- Batch triage rank: 7/7 (2026-03-03 Ashby+expanded batch)
- Story fit: None with strong relevance
- URL: https://jobs.ashbyhq.com/magicschool/560fbe30-777e-44a3-bf64-34f647b26def
- Decision: Skip

## JD Analysis: Crosslake Technologies — PM Lead Consultant
- Date: 2026-03-03
- Depth: Quick Scan
- Fit verdict: Long-Shot Stretch (too early in career arc)
- Top competencies: (1) 15+ years at Director/VP/CPO level, (2) PE/investment due diligence, (3) AI/ML product strategy evaluation
- Frameable gaps: B2B SaaS + AI/ML product experience is a genuine match — but insufficient without the title history and PE context
- Structural gaps: 15+ years required (9+ actual); Director/VP/CPO title history required; no PE/consulting background
- Unverified assumptions: 0 — structural gaps are clear
- Batch triage rank: 2/3 (2026-03-03 new batch) — Skip now; revisit in 5–6 years as post-VP advisory path
- Decision: Skip

## Meta-Check Log
| Session | Candidate Feedback | Adjustment Made |
|---------|-------------------|-----------------|

## Session Log
### Historical Summary
[none]

### Recent Sessions
| Date | Commands Run | Key Outcomes |
|------|-------------|--------------|
| 2026-03-02 | kickoff | Profile initialized; resume analyzed (v3.4 Regulated/Fintech version); coaching plan set; imposter syndrome flagged |
| 2026-03-02 | stories | Indexed 4 anchor stories (S001–S004); earned secrets extracted; red-teamed all four; gap analysis completed |
| 2026-03-02 | system-expansion | Added jobs, track, write commands; job search criteria initialized; application tracker seeded with Uber + unknown company |
| 2026-03-02 | track import | Imported Job Tracking.xlsx — 98 applications (A003–A100) added; analytics computed: 21% response rate, 2% interview rate, CL not correlating with better outcomes |
| 2026-03-02 | jobs + decode + write | 3-track search strategy confirmed (VC/PE, consulting/accelerator, PM with criteria); 5 roles decoded (Zillow Strong Fit, Upstart Strong Fit/domain caveat, Inspiren Investable Stretch, Pinterest Investable Stretch, Zen Educate Weak Fit); ATS scores run; 4 CLs drafted; follow-up approach set |
| 2026-03-03 | stories (S002 improve), decode (9-role batch triage) | S002 improved to Strength 4: authority constraint explicit in Task (2 PT engineers, no budget/mandate), decision moment reframed in Action (investment call not capacity redirect), blog removed from Result, live data validation added, be-ready-for answer documented. Trigger map + 10s product case drop built for S002 deployment reflex. Batch decode: Webflow/Upwork/Braze = Investable Stretch (pursue); Owner = verify comp first; Halcyon = Long-Shot (low priority); TollBit = verify comp + title; BetterHelp = skip; UChicago Polsky + EliseAI = already applied, wait. |
| 2026-03-02 | write (5-role application workflow) | All 5 applications completed and logged (A100–A104); resumes customized + library updated (general_saas_v4.3 with OKR edit now canonical); CLs: Upstart ✅, Inspiren hardware field ✅, Zen Educate Logic Drift iterated with candidate ✅, Pinterest EQWG signal bridge candidate-written ✅; INDEX.md updated with 5 customized versions; Zillow applied resume-only |
| 2026-03-02 | system improvements | 6 system changes designed: (1) daily jobs auto-trigger confirmed; (2) follow-up framework defined (F/U 1 at 5BD, F/U 2 at 12BD, F/U 3 at 21BD — all 5 batch apps due 2026-03-09); (3) CL experiment launched (Style A/B/C/D, tracker added to Application Analytics); (4) daily practice warm-up confirmed (1 Stage 1 behavioral drill per session); (5) weekly insights format defined (Monday review: apps sent, responses, CL experiment, source breakdown, top tweak); (6) speed/friction plan: batch decode→ATS→resume→CL→log, skip ref re-reads in-session, monthly tracker archival |
| 2026-03-03 | write (Webflow, Halcyon, TollBit applications), decode (3-role triage: PayPal/a16z/Crosslake) | Webflow ✅ A106 (platform_v2.5 + CL Style C + Why Webflow answer); Halcyon ✅ A107 (v4.4 + CL Style A); TollBit ✅ A108 (v5.1 customised + CL Style C); Zillow A105 logged (resume-only, applied 2026-03-02); Quantexa block cleaned to 5 bullets for TollBit; 3-role triage: PayPal = Investable Stretch/skip for now (comp ceiling), a16z Speedrun = Weak Fit/skip, Crosslake = Long-Shot/skip; base divergence issue (v4.3.docx/v5.1.docx had wrong "8+" summaries) identified and corrected; platform_v2.5 established as new Platform track base |
| 2026-03-03 | jobs (expanded search + 7-role batch triage), location update | Location updated: willing to relocate to SF, NY, LA, Seattle, Chicago. Reevaluated 3 Ashby roles (previously skipped for SF location): Decagon Strong Fit ($200–285k, top pick), Pylon Investable Stretch (comp undisclosed), Flint Skip (CS degree hard requirement). New roles: Sayari Strong Fit (knowledge graph = Quantexa tech, remote), Rippling Product Lead R&A Strong Fit (data platform maps directly, title progression), Ambient.ai Investable Stretch (physical security domain stretch), Magic School Skip (comp ceiling + edtech mismatch). Bonus: Decagon NYC Senior Agent PM ($200–285k, NY viable, customer-facing track). Job Discovery Log updated +11 entries. |

## Coaching Notes
- 2026-03-02: Candidate has imposter syndrome — explicitly flagged. Level 5 directness applies, but frame gaps as specific fixable skills, not capability worth. Push on evidence and precision, not on whether she belongs.
- 2026-03-02: Actual job titles (Data PM, PM, Product Owner) don't uniformly signal "Senior PM" — she has the scope but not always the label. This will affect confidence as much as interviews. Coach her to own the scope language explicitly.
- 2026-03-02: Career based primarily in London (Quantexa, Morningstar, Sthaler, JumpWork Amsterdam) — Capital One was first US role and was short (13 months). US market fluency and "why did you leave Capital One" will be recurring interview questions.
- 2026-03-02: Already has 4 anchor stories; wants to learn to spin them and find stories she may have missed. Good self-awareness — don't rebuild from scratch, build on what exists.
- 2026-03-02: Uber HM interview — held up well until the product case, then lost structure. Classic pressure-triggered regression. Product case structuring is the acute gap to address in early practice sessions.
- 2026-03-02: Has multiple resume variants organized by target type (Exec, Platform/Infra, Regulated/Fintech, General SaaS/Ops, VC/Startup) — sophisticated approach to her search. Reference version map during resume session.
- 2026-03-02: Storybank has 4 stories — S001 (SaaS Pivot) is her strongest and most differentiated. S004 (Recoveries) needs restructuring before live use. Critical gaps: no prioritization story, no failure story, no user research story. She explicitly wants to spin existing stories — build spin awareness into practice sessions, not just story content.
- 2026-03-02: 3-track job search strategy confirmed — (1) VC/PE to build toward own myology investment fund long-term, (2) consulting/accelerator/incubator for project-based breadth, (3) traditional PM only if major brand, meaningful title/comp progression ($220k+), or Founding PM. Non-PM applications were intentional, not scatter. Revise job search framing accordingly.
- 2026-03-02: Myology (muscle physiology/biology) is the long-term investment thesis. This is a genuine differentiator — the "why I'm doing this" answer is far more interesting than "I want to grow as a PM." Embed this into pitch, cover letters, and VC/PE outreach. It's an earned secret in the making.
- 2026-03-02: "Cool product" and "amazing culture" are undefined PM role filters — coach her to operationalize these when they come up as decision factors, otherwise they become veto power without criteria.
- 2026-03-02: Alvarez and Marsal is at Director level — this is a significant title signal worth prepping for separately. Consulting interviews (A&M style) are case-heavy and structurally different from PM behavioral. Flag for format-specific prep if she advances.
- 2026-03-02: Google loop is active (assessment passed). Google's PM interview process is known for structured behavioral rounds, product sense, analytical thinking, and leadership questions. Will need format-specific prep when phone screen is scheduled.
- 2026-03-02: Session workflow updated — daily practice warm-up (1 Stage 1 behavioral drill) added to session start; daily jobs auto-trigger confirmed; weekly Monday insights review added; CL experiment active with Style A/B/C/D tagging; follow-up workflow: F/U 1 at 5BD, F/U 2 at 12BD, F/U 3 at 21BD.
- 2026-03-02: CL experiment hypothesis — existing data shows CL negatively correlated with outcomes (24% rejection vs 17%) but confounded by role targeting (harder roles got CLs). Run experiment by fit tier going forward. Style A=Earned Insight used for Investable Stretch domain-gap CLs; Style B=Mirror for Strong Fit proof CLs; Style C=Problem Statement not yet tested; Style D=No CL as control.
- 2026-03-02: coaching_state.md is now 70KB+ and growing. Schedule monthly archival of Application Tracker rows pre-2026-02 to keep session-start reads fast.
