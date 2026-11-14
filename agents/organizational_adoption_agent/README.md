# Assignment 7 — Organizational Adoption Agent / SubAgent 6
Selected final specialist: **v0.2-context-sequencing**. Three genuine original v0.1 outputs and three genuine v0.2 retests are preserved unchanged. All six passed the official frozen validator and full frozen schema. Actual before/after review shows improved capacity-first sequencing and intermediate event checkpoints, with documented residual limits.

## Current workflow
From repository/package root:
```
python tools/check_frozen_core.py
python agents/organizational_adoption_agent/tests/check_final.py
```
Add --portable to check_final.py in the standalone final package, which intentionally omits earlier assignment agents. Prior work remains unchanged in the original repository. Historical checks check_preparation.py and check_review.py reflect earlier stages and intentionally assert their historical pending states; use check_final.py for current validation.

Current submission documents are under deliverables/: Agent_Record, Primary_Output_Report, Independent_Professional_Judgment, AI_Verification_Note, Craft_Gained and Team_Handoff (Word plus Markdown), with Submission_Checklist.md and Validation_Summary.md. The actual primary report uses responses/primary_v0.2_run1.json. Original instructions/patch and both packet versions remain under revisions/, records/ and prompts/. Superseded draft documents/handoffs are historical evidence, not final submission files.

Only specialist_instructions.md changed among runnable v0.1 inputs for v0.2. Cases and metadata file remain unchanged. The specialist explicitly overrides response agent.version to 0.2-context-sequencing while preserving the name/specialty; complete frozen schemas remain unchanged. No API key or replacement architecture is needed. Original tools use Python standard library; supplemental full-schema checks use jsonschema already installed here.

Known limits: synthetic classroom profiles, unverified permission/capacity/performance, single original/retest per case, governance-awareness framing and small-case permission/protocol wording. See records/v0.2_before_after_review.md. Model/settings/run times/chat references were not supplied; no runtime metadata invented.

Student must enter identity/team in Agent Record, endorse/revise the independent judgment and confirm genuine Craft Gained learning before submission. GitHub final push/verification is recorded in the delivery package's BUILD_PROVENANCE.json, rather than assumed from local commits. Brightspace upload is the student's action.
