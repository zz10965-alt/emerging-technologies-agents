# Manual execution of verified-evidence packets v0.2

No callable interactive ChatGPT model-execution tool is available in this environment. The Python course tools build/validate files; they do not invoke ChatGPT. No model responses have been created. These packets are ready to test reasoning with the bounded verified evidence supplied, including qualification/abstention for remaining gaps; they do not promise a high classification or local deployment readiness.

## Exact next action

Run these four exact files, each in a separate fresh ChatGPT conversation, using the same model/settings and source-access conditions:

1. prompts/primary_v0.2_prompt.txt
2. prompts/contrast_1_v0.2_prompt.txt
3. prompts/contrast_2_v0.2_prompt.txt
4. prompts/hype_probe_v0.2_prompt.txt

Paste or attach the entire file and ask: "Execute this prompt packet and return the required JSON only." Do not add instructions steering the conclusion. Use the supplied source snapshot without browsing for the matched baseline comparison, so general evidence stays constant. A browsing-enabled exploratory run is possible later, but new retrieved evidence and settings must be preserved and consistently reflected in matched tests before comparing them. Do not confuse lack of browsing with a prohibition on stating evidence gaps.

## Save raw responses without edits

Save the complete returned response exactly as generated, including any extra prose or Markdown fences. Do not repair JSON, numbers, citations, omissions or conclusions. Use these paths relative to agents/promethean_agent/:

- responses/primary_v0.2_run01_raw.txt
- responses/contrast_1_v0.2_run01_raw.txt
- responses/contrast_2_v0.2_run01_raw.txt
- responses/hype_probe_v0.2_run01_raw.txt

A raw .txt preserves even a nonconforming response. Do not extract JSON or replace it with corrected prose before handing it back; derived files must later be labeled separately and the raw response retained. Export/download when possible; if copying text, preserve all content exactly and disclose the capture method. Never overwrite a prior run. Return/upload all four raw files here, or place them at those paths and tell Codex they are available.

For each run provide actual date/time/timezone, displayed model name, settings/tools/browsing state, packet filename, capture method and any truncation/error. Packet hashes, agent version, source snapshot and working version are in preparation_v0.2_manifest.json plus the Git commit reported by Codex. Unknown runtime details must be recorded as unknown, not inferred.

## What Codex will do after receiving the real responses

Run the original tools/validate_response.py on each unedited raw response (it parses file contents irrespective of extension), record actual exit status/output, apply supplemental common-schema checks and the analytical checklist, and compare A/B/C/D. Invalid JSON is an observed result, not permission to silently fix it. Any later correction or rerun must preserve its own packet/response/provenance. Only an observed weakness can support a revision/retest record. No output, validation pass, failure, revision effect or final report is claimed now.

## Boundaries

S1/S2/S6 support capability investigation; S3/S7 limit simplistic usefulness/reliability claims; S4/S5 qualify historical negativity with newer but uncertain evidence. General classification is not prescribed. Clinical simulation is not a clinical-documentation trial, safety authorization or generic-LLM equivalence. No verified society-wide 10x or long-run irreversibility finding is supplied. Those limits are intentional analytical test conditions and must remain visible.
