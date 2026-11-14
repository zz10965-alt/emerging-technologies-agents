# Required ChatGPT runs — exact handoff
**Current state:** 3 standalone packets prepared; 0 specialist model runs. Assignment not submission-ready.

## 1. Run three original packets
Open three separate NEW normal ChatGPT conversations. Use the same available model and reasoning settings for each; disable browsing for this supplied-evidence comparison. Upload or paste ONE full packet in each conversation. Do not share another output between chats:
- prompts/primary_v0.1_prompt.txt
- prompts/contrast_1_v0.1_prompt.txt
- prompts/contrast_2_v0.1_prompt.txt

Exact accompanying message:
> Execute the attached complete specialist prompt packet for its included case. Use only the supplied evidence and hypothetical assumptions. Return one complete JSON object conforming to the included frozen output schema, with no Markdown wrapper or surrounding prose. Do not invent evidence or claim controls, benefits, or tests have occurred.

Keep the full packet intact. Record actual date/time and timezone, model/settings, browsing state and conversation/export reference if available in records/execution_manifest.json. Save exact outputs as:
- responses/primary_v0.1_run1.json
- responses/contrast_1_v0.1_run1.json
- responses/contrast_2_v0.1_run1.json

If the response is not pure JSON, preserve exact original as .txt; do not silently fix it. Return the originals to Codex, including errors or weak outputs and run metadata. Do not run unrelated previous-assignment prompts.

## 2. Validate actual responses locally (or return them here for validation)
From /workspace/emerging-technologies-agents, or the root of the portable package:
```sh
python tools/check_frozen_core.py
python tools/validate_response.py agents/organizational_adoption_agent/responses/primary_v0.1_run1.json
python tools/validate_response.py agents/organizational_adoption_agent/responses/contrast_1_v0.1_run1.json
python tools/validate_response.py agents/organizational_adoption_agent/responses/contrast_2_v0.1_run1.json
```
Supplement with the full frozen schema (jsonschema is installed in this cloud environment):
```sh
python - <<'PYCODE'
from pathlib import Path
import json
from jsonschema import Draft202012Validator
root = Path.cwd()
schema = json.loads((root/'core/output_schema.json').read_text())
validator = Draft202012Validator(schema)
agent = root/'agents/organizational_adoption_agent'
metadata = json.loads((agent/'agent_metadata.json').read_text())
for case in ['primary', 'contrast_1', 'contrast_2']:
    path = agent/'responses'/f'{case}_v0.1_run1.json'
    data = json.loads(path.read_text())
    validator.validate(data)
    assert data['agent'] == metadata, f'Metadata mismatch: {path}'
    print('FULL SCHEMA AND METADATA PASSED:', path)
PYCODE
```
A missing file, JSON/schema error or metadata mismatch must remain a failure in the log until diagnosed. Never claim a pass for absent data. Record command, actual exit code and output. The original validator is a basic contract check, not a complete schema checker. Neither check proves substantive correctness.

## 3. Inspect and revise using genuine evidence
Apply records/test_plan.md to the actual outputs. Quote one appropriately stable general/application finding and one defensibly changed organizational finding; reference exact files/fields. Do not copy the expected directions as observed results.

Preserve an actual weak output and diagnosis. If all initial runs look sound, run prompts/diagnostic_followup.txt as directed and inspect the result. A responsible uncertainty statement is not automatically a weakness. If none is found, honestly report that the mandatory failure evidence remains unresolved rather than inventing it.

Once an actual weakness is found, preserve initial instructions (already saved), edit only the specialist, increment its version to 0.2 with a reason, rebuild NEW prompt packets using the original builder and unchanged relevant case(s), run a fresh ChatGPT retest, and save exact outputs separately. Revalidate and compare before/after quotations; record residual limitations. Do not generate v0.2 results before a targeted revision exists.

## 4. Finalize documents and packaging
Derive the primary report from the actual selected validated response, complete pending Agent Record C–E/test fields, update AI note, review the proposed independent judgment, replace Craft Gained with the student's genuine reflection, and enter student/team identity. Preserve the template A–E structure and word/length limits. Update team handoff, logs, execution metadata and remaining-limits record. Recheck frozen core and all prior work; commit real changes on the Assignment 7 branch. Rebuild a ZIP clearly labeled final only after mandatory evidence exists.

## 5. GitHub and Brightspace
A local Assignment 7 branch and real commits exist; no remote push is claimed. After reviewing finished work, push with `git push -u origin assignment7-organizational-adoption` if authorized and accessible. Verify the remote commit after pushing. This package and the current commit are preparation evidence, not a completed tested submission. Brightspace submission must include the finalized working package and Agent Record, actual primary output report, endorsed independent judgment, AI note and genuine <=100-word Craft Gained reflection. Check the course site for due date and upload instructions; none were inferred here.
