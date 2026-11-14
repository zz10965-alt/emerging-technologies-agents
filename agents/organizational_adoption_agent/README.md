# Assignment 7 — Organizational Adoption Agent / SubAgent 6
Version 0.1-initial-unexecuted. **Development package; not submission-ready.**

Built with original tools/new_agent.py from the byte-verified canonical template. Existing earlier assignments and frozen core are preserved. No API key or package installation is needed for the original tools. Supplemental full-schema checks use already-installed jsonschema; document generation uses already-installed python-docx. The student-facing specialist remains a prompt specialist within the original scaffold.

Start with deliverables/CHATGPT_RUN_INSTRUCTIONS.md. Three standalone packets are in prompts/. Genuine model execution, comparison, weakness/revision/retest and output report remain pending. Documents are drafts and distinguish case-based proposed judgment from unexecuted agent findings.

From repository root:
```
python tools/check_frozen_core.py
python agents/organizational_adoption_agent/tests/check_preparation.py
```
In the portable ZIP, add `--portable` to the preparation check: prior assignments are intentionally excluded; their preservation is checked in the original checkout. The preparation baseline check intentionally stops once response JSON files exist, at which point use the actual-response validation workflow.

For each returned result run original tools/validate_response.py and the full-schema command in the handoff instructions. Schema validity cannot establish analytical quality. Preserve all original responses and use the rubric in records/test_plan.md.

The canonical ZIP and supplied course materials are unchanged under sources/. Earlier work is excluded from this assignment's portable package but is retained in Git. No final submission, external publication, remote push, or model execution is implied by a local commit.
