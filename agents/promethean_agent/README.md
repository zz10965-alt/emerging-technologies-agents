# Promethean Technology Classification Agent — Phase 2

Version: 0.1-phase2. Created with the original tools/new_agent.py. No original scaffold files are modified. No dependencies beyond the scaffold's standard-library Python workflow are added. All paths below are relative to the repository root.

## Current status

Implementation and four preparation packets only. No model tests, response validations, revision/retests, final Agent Record or final reports have been completed. responses/ intentionally contains only the inherited .gitkeep. Evidence is currently course-only: contemporary empirical verification remains a prerequisite for evidence-complete execution. The agent must qualify/abstain when evidence is insufficient; prepared packets must not be mistaken for completed tests.

## Rebuild a packet using the unchanged course builder

```sh
python tools/build_prompt.py --agent agents/promethean_agent --case agents/promethean_agent/cases/primary.json --out agents/promethean_agent/prompts/primary_v0.1_prompt.txt
```

Repeat for contrast_1, contrast_2 and hype_probe with matching output names. The explicit --out keeps all assignment artifacts here rather than the ignored work/ directory. Do not overwrite an executed packet: preserve it and use a new version/run filename.

## Later execution — requires the next phase

1. Verify contemporary evidence, update the shared snapshot consistently and regenerate affected packets. Review course-only qualifications if evidence remains unavailable.
2. Submit one exact packet per fresh ChatGPT conversation with the same model/settings/evidence conditions where possible. Request JSON only. Record actual runtime model/version, date, agent commit, evidence snapshot and any browsing/source access. No API account is needed. A fresh conversation avoids cross-case contamination.
3. Save the actual returned response unchanged under responses/<case>_<agent-version>_<run>.json. Preserve invalid JSON as returned too; any correction is a separately recorded run/artifact, never a silent rewrite.
4. Run the original validator on the saved response:
   `python tools/validate_response.py agents/promethean_agent/responses/<actual-response>.json`
   Capture actual exit status/output in records/test_log.md. The validator is basic; additionally inspect all common-schema constraints and analytical requirements using that checklist.
5. Preserve an actual weakness, revise only this agent folder, version the specialist, rebuild the affected packet and rerun the same case/evidence. Record differences and limitations without manufacturing a failure or improvement.
6. Run `python tools/check_frozen_core.py` after edits. Compare every original file byte-for-byte to the original archive; never edit manifests to conceal changes.

## Team boundary

This specialist classifies significance; it does not authorize adoption, clinical practice or legal compliance. General classification must remain evidence-consistent across contexts. Keep application value, organization readiness and management action distinct. Potential Promethean status is never automatic near-term adoption advocacy.

## Version control

Repository: zz10965-alt/emerging-technologies-agents. Baseline is the unchanged course archive, including its originally ignored toy prompt. Assignment branch: assignment4-promethean. Record actual commits in the working records. Local commits and a successful GitHub push are separate facts; do not claim a push without verifying it. Preserve the canonical uploaded ZIP unchanged. Budget work within the course's 60–90 minutes and record unresolved issues at the limit.
