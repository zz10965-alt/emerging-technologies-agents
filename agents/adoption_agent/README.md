# Adoption Agent — Phase 1 test preparation

Version: `0.1-phase1`. The reviewed specialist instructions are retained unchanged.
All three organizations are synthetic test scenarios. No independent model run,
observed behavioral result, or completed student judgment is recorded here.

## Independent ChatGPT execution

Use a separate fresh ChatGPT conversation for each file below. Upload the entire
`.txt` file (or paste its entire contents) and ask ChatGPT to execute it and return
only the required JSON. Do not supply another case's conversation or output.
Use the same model/settings and no browsing for all three runs. The supplied
evidence-only run constraint preserves comparability; do not add external claims.
Record actual model, run date, settings and any unavailable runtime details.

1. `prompts/primary_prompt.txt` — moderate mid-sized company.
2. `prompts/contrast_1_prompt.txt` — startup with stronger review, isolation and recovery capabilities.
3. `prompts/contrast_2_prompt.txt` — provider with unresolved data permission, weak isolation, scarce review and persistent downstream consequences.

Save returned JSON verbatim to new, unused filenames, for example
`responses/primary_v0.1_run1.json`, `responses/contrast_1_v0.1_run1.json` and
`responses/contrast_2_v0.1_run1.json`. Preserve malformed or weak outputs too;
do not repair them before review. No response files have been prepopulated.

From the repository root, validate each returned file using:

```sh
python tools/validate_response.py agents/adoption_agent/responses/primary_v0.1_run1.json
python tools/validate_response.py agents/adoption_agent/responses/contrast_1_v0.1_run1.json
python tools/validate_response.py agents/adoption_agent/responses/contrast_2_v0.1_run1.json
python tools/check_frozen_core.py
```

The original response validator checks only part of the frozen contract. A full
JSON Schema check and manual analytical review are still needed after execution.
Neither prompt construction nor a schema pass establishes behavioral quality.
Review evidence attribution, stability of general findings, context-to-action
reasoning, contradictions, scope, and actionable learning/change conditions.
Do not force different categories; record if a common constraint dominates.

## Inputs and evidence

`agent_metadata.json` supplies the common metadata object. `cases/*.json` use
only the original common intake fields. Each `additional_context` embeds the
same `evidence/shared_evidence.txt` verbatim so packets are self-contained.
The frozen builder includes common instructions, metadata, reviewed specialist
instructions, the entire case and the unchanged output schema.

The evidence includes exact excerpts from two original GitHub product-documentation
pages, with pinned source commit, retrieval date, retained Markdown snapshots and
SHA-256 hashes in `evidence/source_manifest.json`. Both are vendor sources;
they are not independent corroboration, empirical productivity results, a market
diffusion study, or local intervention evidence. Publication dates are unknown.
Unexpanded documentation templates and linked pages are not treated as checked.
No current price, contract term, model version, legal finding or numerical benefit
is asserted. This deliberately limited evidence supports tests of uncertainty
handling; it does not establish production readiness or actual net advantage.

Technology, application, business need, alternatives, decision question, horizon,
and source evidence stay constant. Context varies in review staffing, test/security
coverage, data segregation and permission, resources, failure exposure, recovery
and persistence of harm. All numbers and approvals in cases are labeled scenario
assumptions, not facts about actual organizations or measured test outcomes.

## Rebuild

Run from the repository root, preserving exact independent responses:

```sh
python tools/build_prompt.py --agent agents/adoption_agent --case agents/adoption_agent/cases/primary.json --out agents/adoption_agent/prompts/primary_prompt.txt
python tools/build_prompt.py --agent agents/adoption_agent --case agents/adoption_agent/cases/contrast_1.json --out agents/adoption_agent/prompts/contrast_1_prompt.txt
python tools/build_prompt.py --agent agents/adoption_agent --case agents/adoption_agent/cases/contrast_2.json --out agents/adoption_agent/prompts/contrast_2_prompt.txt
```

Do not overwrite retained packet versions after execution; version changes first.
See `records/phase1_preflight.json` for structural checks of these exact files.
Final Agent Record, independent report, actual failure/revision record and output
report remain pending independent execution and the student's professional review.
