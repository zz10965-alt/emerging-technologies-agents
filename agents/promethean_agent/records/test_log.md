# Test plan and execution log

Status: NOT EXECUTED. No model responses, response-validation results or analytical pass/fail outcomes exist in Phase 2. Prompt-building and scaffold-integrity checks are technical preparation only.

| Test | Exact input | Intended analytical review |
|---|---|---|
| A | cases/primary.json | Three levels, justified gate/classification reasoning and bounded software-development implication. |
| B | cases/contrast_1.json | Same general technology/evidence; defensible clinical-application and organizational differences, with documentation separated from decision support. |
| C | cases/contrast_2.json | Same software-development functionality; changed posture/resources must not inflate general significance. Context can change action without requiring a particular decision. |
| D | cases/hype_probe.json | Only unsupported hype claim added to A; explicit rejection of investment/excitement as proof, no evidence-free classification upgrade. |
| E | To be selected from actual weakness | Preserve raw failing/weak response; revise instructions, keep case/evidence fixed, rerun and compare honestly. |

## Required record for each future actual run

Record actual case/path, exact packet, agent version/commit, evidence snapshot, runtime model/settings/date, raw response path, source access, original validator command/exit status/stdout/stderr, supplemental schema review, analytical findings and reviewer. Never prefill a passing result. Preserve invalid responses and separately identify any rerun or correction.

## Supplemental contract checklist (the original validator is incomplete)

- Input: all 11 required fields present as strings; additional_context is a string when present; input represents the intended case.
- Output: one JSON object; exactly the common allowed top-level properties; all 13 required properties; agent name/specialty/version match metadata.
- All declared string fields are strings; evidence is an array of objects with the five required string properties.
- contrary_evidence_or_limitations, change_monitoring_triggers and abstention_or_more_information_needed contain strings, not nested objects or numbers.
- Do not silently fix the response to make it validate. Record validation defects and reruns distinctly.

## Analytical checklist

- System/component boundary, honest barrier statement, suppression counterfactual and multiple tiers evaluated in order.
- Reduction, unresolved dissolution and confirmed present dissolution not conflated; downstream gate stops honored.
- Six criteria individually supported/qualified or explicitly not reached; ratios and baselines valid; no fabricated weighted score.
- Prospective/retrospective mode declared; no Confirmed Promethean for emerging LLM systems; course calibration acknowledged with agreement/departure explained.
- Strongest supporting/opposing evidence traceable; fact/inference/hypothesis/unsupported claim distinct; present evidence separated from predictions.
- General finding evidence-consistent across A/B/C; application/organization implications change only for defensible reasons. Identify one appropriately stable and one appropriately changed conclusion, or document an exposed weakness.
- D explicitly rejects the hype inference; confidence/classification do not increase on that basis alone.
- Recommendation bounded, controls context-sensitive, missing information and reconsideration triggers explicit.
- A validator pass alone does not establish analytical success. No expected label or recommendation is hardcoded into the review.

## Evidence-preparation update v0.2

Seven original sources/reports inspected with methodological and date qualifications. All four case contexts now share evidence/shared_snapshot_v0.2.txt; hype adds only its unsupported claim. Four v0.2 packets prepared by the unchanged builder; old v0.1 packets retained. No actual model execution or response validation has occurred. Execute using manual_execution.md, then record actual observations. Empirical source verification does not mean source experiments were replicated or all evidence gaps resolved.
