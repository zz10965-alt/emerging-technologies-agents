# Assignment 7 — Organizational Adoption Agent / SubAgent 6
**Current state: genuine v0.1 evaluated; v0.2-context-sequencing prepared; final submission blocked on genuine retests.**

Start at deliverables/V0.2_RETEST_INSTRUCTIONS.md. Three original user-supplied v0.1 responses passed original validator and full frozen schema checks. Their exact bytes, source ZIP and packet hashes are preserved. records/v0.1_comparison.md contains actual stable/changed findings and quoted weaknesses. v0.2 changes only specialist instructions among runnable inputs; cases and metadata file remain unchanged. The specialist explicitly overrides response version to 0.2-context-sequencing.

Run current local checks from repository root:
```
python tools/check_frozen_core.py
python agents/organizational_adoption_agent/tests/check_review.py
```
Add --portable in the standalone ZIP, which intentionally omits earlier assignments. All prior work remains unchanged in the original repository. The old check_preparation.py and preparation_validation.log are historical initial-stage evidence, not current output-validation instructions.

Current outputs/documents: Primary_Output_Report_v0.1.docx derives from the actual primary; Agent_Record_DRAFT.docx has v0.1 evidence and real revision with final retest pending; first-person judgment/reflection drafts need student endorsement. v0.2 output validation and improvement are NOT RUN. Superseded primary-report placeholders are retained under revisions/pre_execution_placeholders/ and are not submission deliverables.

Original standard-library tools and frozen architecture are preserved; no API key is needed. Supplemental local full-schema checks use already-installed jsonschema, and document generation uses already-installed python-docx. Canonical ZIP/course sources are unchanged under sources/. No prior-assignment responses are used as this specialist's tests. No remote push or Brightspace submission is implied by local commits.
