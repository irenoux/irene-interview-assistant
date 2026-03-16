# Golden Reference Answers

## Purpose
These are calibration answers used to detect scoring drift.
Run monthly via Make workflow (Batch API).
Each answer is scored 5 times — mean and SD compared to baseline.

## Scoring Instructions
When scoring these answers, use the full rubric from /prompts/layer3-commands/rubrics/rubrics-full.md.
Score each dimension 1-5: Substance, Structure, Relevance, Credibility, Differentiation.
Apply the seniority calibration band noted for each answer.

---

## Reference Answer 1: Behavioral — Leadership
**Question**: Tell me about a time you led a team through a difficult situation.
**Seniority band**: Senior (8-15y)
**Target scores**: Substance: 4, Structure: 4, Relevance: 4, Credibility: 4, Differentiation: 3

**Answer**:
At my previous company, we were midway through a critical platform migration when our lead architect unexpectedly left. The team of eight engineers was demoralized — we'd already missed one deadline, and leadership was questioning whether to pause the project entirely.

I took three steps. First, I ran a two-day technical audit with the remaining senior engineers to identify which architectural decisions were already locked in versus still open. This gave us a concrete map of what we actually needed help with versus what the team could own. Second, I restructured the work into three parallel workstreams so that no single person was a bottleneck — this meant some engineers had to stretch beyond their comfort zone, but I paired each stretch assignment with a weekly check-in so problems surfaced early. Third, I went to leadership with an honest revised timeline — not padding, but an evidence-based schedule showing exactly where the risk lived and what we'd de-risked.

We delivered two weeks late from the revised timeline, which was still three weeks ahead of leadership's worst-case expectation. More importantly, two engineers who'd been considered mid-level stepped into technical leadership roles during the project and were promoted within six months. The lesson I took away was that losing a key person isn't primarily a knowledge problem — it's a confidence problem. The team had the skills; they needed someone to restructure the work so they could see that they had the skills.

---

## Reference Answer 2: Behavioral — Failure
**Question**: Tell me about a time you failed.
**Seniority band**: Mid (4-8y)
**Target scores**: Substance: 3, Structure: 3, Relevance: 3, Credibility: 3, Differentiation: 2

**Answer**:
I was leading the launch of a new reporting feature that our sales team had been requesting for months. I was so focused on shipping quickly that I skipped the usual user research phase — I figured the sales team had told us exactly what they needed, so we should just build it.

We launched on time, and initial adoption was strong — the sales team was excited. But within three weeks, usage dropped significantly. When I finally did the user research I should have done upfront, I found that what sales had asked for was a dashboard showing deal velocity, but what they actually needed was alerts when deals were stalling. They'd described the solution they imagined, not the problem they were solving.

We rebuilt the feature as a notification system with configurable triggers, and that version stuck. The whole detour cost us about six weeks. I learned that even when stakeholders are specific and confident about what they want, you still need to validate the underlying problem. Confidence in a solution isn't evidence that it's the right one. I now build a lightweight problem validation step into every project, even when the request seems clear-cut.

---

## Reference Answer 3: Behavioral — Impact
**Question**: What's your biggest professional achievement?
**Seniority band**: Senior (8-15y)
**Target scores**: Substance: 5, Structure: 4, Relevance: 4, Credibility: 5, Differentiation: 4

**Answer**:
I built the first entity-resolution quality measurement system at a data analytics company — something the industry had talked about but nobody had actually quantified. The company's core product resolved entities across massive datasets, but there was no way to measure how well it was working. Teams were using proxy metrics — counting parser changes as a stand-in for quality improvement — because the real thing wasn't measurable.

What made this hard wasn't the technical challenge — it was the organizational one. I had no authority over any of the teams I needed. Data science needed to build detection models. Delivery needed to codify tribal knowledge. Engineering needed to prioritize work that wasn't on their roadmap. I had two part-time engineers and no budget. Everything was built through persuasion and borrowed capacity.

I started by proving the problem was real: I categorized every incoming feature request and showed that over half were solving the wrong problem — teams were tweaking upstream data quality as a proxy for entity-resolution accuracy. That data was the credibility I needed. I established a cross-functional working group, defined a three-pillar roadmap — education, codified best practices, measurable metrics — and we built the company's first quantifiable quality benchmark, validated against live customer data.

The result: feature requests dropped 45%, we created the company's first standardized best-practice guidance adopted globally, and the working group became a standing governance body influencing the innovation roadmap. But the real achievement was proving that the most dangerous product feedback is specific, confident, and wrong — and building the measurement infrastructure that made that visible. That insight changed how the entire product organization evaluated requests.
