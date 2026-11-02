# v0.3-provenance-fix — targeted retest candidate

Parent v0.2 inputs, original packets, evidence and three uploaded outputs remain unchanged. This folder is an isolated authoring revision, not a new Git branch. It adds one short provenance-control paragraph plus version/provenance metadata. No evidence or case narrative was changed. Both case files are byte-identical to v0.2, including the final six-month duration.

Observed weaknesses, with exact original quotes and severity, are in ../../records/performance_review_v0.2_run1.json and its Markdown companion. The six-month horizon is valid; this revision addresses unsupported execution-date inference and overcategorical unknown-sampling wording, not a horizon-duration failure.

## Retest only the affected cases

Open separate fresh ChatGPT conversations for prompts/primary_v0.3_prompt.txt and prompts/contrast_2_v0.3_prompt.txt. Use the full packet with the same closed evidence and comparable settings, without pasting prior outputs or desired answers. If exact current execution metadata is not supplied, the expected handling is “unknown,” not an inferred date. Record actual model/settings, timestamps and chat reference externally when known. Preserve all actual returned bytes with new filenames; do not overwrite original v0.2 outputs.

Save future actual responses to ../../responses/primary_v0.3_run1.json and ../../responses/contrast_2_v0.3_run1.json. No responses exist yet. From repository root validate with the original tools/validate_response.py and frozen output schema; compare W1/W2 handling, six-month duration, source denominators and unchanged substantive conclusions against v0.2. Startup regression is optional for these particular weaknesses. No all-three rerun is required merely because an earlier unexecuted design mentioned twelve months.

No retest pass is claimed. Do not promote/finalize the agent, Agent Record or submission before real retest review and user approval.
