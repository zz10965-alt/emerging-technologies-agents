# v0.2 independent ChatGPT test instructions

Three original independent v0.2 run1 outputs have been supplied and reviewed. See records/performance_review_v0.2_run1.md relative to the agent root. The procedure below is the retained original v0.2 protocol; do not rerun all cases just for the valid six-month duration. Targeted v0.3 Primary/Hospital retest instructions are in revisions/v0.3/README.md relative to the agent root. No v0.3 retest has been run. Use only the three *_v0.2_prompt.txt packets. v0.1 packets and a complete original candidate archive are retained for comparison; do not mix versions.

1. Open three separate NEW ChatGPT conversations, using the same model/reasoning settings. Disable browsing for this closed-snapshot comparison. Upload or paste one complete packet per chat, without truncation or other test outputs.
2. Say: “Execute this complete packet for its included case. Use only the supplied evidence and return the complete required JSON object.” Each packet contains full common instructions, specialist instructions, version/provenance metadata, one complete case, identical shared evidence and the frozen output schema. No external files are required.
3. Record actual run date/time, model/settings, browsing status, chat/export reference if available and the packet hash from records/packet_manifest.json. Actual run time is separate from preparation/publication/observation dates.
4. Save complete, unedited actual responses to responses/primary_v0.2_run1.json, responses/contrast_1_v0.2_run1.json and responses/contrast_2_v0.2_run1.json. Do not overwrite existing files. Preserve any malformed prose/fenced result separately before documented extraction; never silently repair an answer.
5. From the repository root run:

```sh
python tools/validate_response.py agents/diffusion_agent/responses/primary_v0.2_run1.json
python tools/validate_response.py agents/diffusion_agent/responses/contrast_1_v0.2_run1.json
python tools/validate_response.py agents/diffusion_agent/responses/contrast_2_v0.2_run1.json
python agents/diffusion_agent/tests/check_development.py --responses
python tools/check_frozen_core.py
```

The original validator covers the basic contract; the supplemental checker enforces the frozen output schema's declared shape and metadata. Neither proves analytical adequacy. See tests/test_plan.json for semantic review.

6. Compare the general findings first, then application/peer interpretations and timing. Preserve one appropriately stable and one changed conclusion. Check all five factors, adopter-category uncertainty, E1/E4 denominator accuracy, broad-AI versus LLM scope, historical versus current observations, E2/E4 dependence, individual use versus company deployment, and the unsupported hospital claim. Do not fail a responsible abstention merely because it lacks a market label.
7. Preserve at least one actual meaningful output weakness with an exact quote/file reference, diagnosis, revision/control and new retest. A preparation weakness or missing-source log is not an actual model-output failure. If no weakness is identified, report that honestly and plan an appropriate stress test.
8. Return the three actual outputs for review before final Agent Record, independent judgment/report, reflection, submission packaging or any commit/push approval.

Preparation checks: `python agents/diffusion_agent/tests/check_development.py --full-repository`. This checks protected original repository files and the complete v0.1 baseline; for a portable ZIP without earlier assignments omit --full-repository. No API key or pip installation is needed.
