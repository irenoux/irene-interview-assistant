# Scoring Baseline

## Purpose
Baseline scores for drift detection. Established by running 5x scoring on each reference answer.
Drift threshold: SD > 0.3 OR mean shift > 0.3 from baseline.

## How to Use
1. Run the monthly eval workflow (Make Workflow 4 — Batch API)
2. Each reference answer is scored 5 times independently
3. Calculate mean and SD per dimension per answer
4. Compare to baseline values below
5. Flag if SD > 0.3 OR mean shift > 0.3 from baseline

## Baseline (to be populated after first eval run)

### Reference Answer 1 — Leadership (Senior band)
| Dimension | Target | Mean | SD |
|-----------|--------|------|----|
| Substance | 4 | — | — |
| Structure | 4 | — | — |
| Relevance | 4 | — | — |
| Credibility | 4 | — | — |
| Differentiation | 3 | — | — |

### Reference Answer 2 — Failure (Mid band)
| Dimension | Target | Mean | SD |
|-----------|--------|------|----|
| Substance | 3 | — | — |
| Structure | 3 | — | — |
| Relevance | 3 | — | — |
| Credibility | 3 | — | — |
| Differentiation | 2 | — | — |

### Reference Answer 3 — Impact (Senior band)
| Dimension | Target | Mean | SD |
|-----------|--------|------|----|
| Substance | 5 | — | — |
| Structure | 4 | — | — |
| Relevance | 4 | — | — |
| Credibility | 5 | — | — |
| Differentiation | 4 | — | — |

## Run History
| Date | Status | Drift Detected | Notes |
|------|--------|---------------|-------|

## Alert Thresholds
- **Yellow**: Any single dimension SD > 0.3 → investigate but don't block
- **Red**: Any single dimension mean shift > 0.3 from baseline → review rubric interpretation before trusting new scores
- **Critical**: 2+ dimensions drifting in same direction → systemic calibration issue, pause scoring until resolved
