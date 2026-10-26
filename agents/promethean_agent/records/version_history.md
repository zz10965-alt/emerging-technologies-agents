# Agent development version history — Phase 5A

| Version / stage | Actual history and artifact | Change and observed outcome |
|---|---|---|
| Original baseline | 7c6a4e0f47e22858623da4f6ffced9fbabc799c7 | Original 32-file course scaffold, including originally ignored toy prompt; unchanged. |
| 0.1-phase2 | 63f816a1791cb0f708348b41f6a779ada2e124db | Created specialist with original new_agent.py; four course-only preparation packets; no model execution then. |
| 0.2-evidence-prep | 96520a19a24e39b1ad371622c5287b8a2085e70c | Balanced seven-source dossier, shared evidence snapshot, four v0.2 packets. Four original run1 responses later supplied by user; schema passes, classification stability/context sensitivity and actual suppression-trigger defect documented in Phase 4A. |
| 0.3-suppression-fix | Phase 5A development commit containing current agent_metadata.json, specialist_instructions.md, records/phase4a_* and records/phase4b/ | Only Layer 2 step 3 revised. Original instruction/metadata copies and unified diff retained; same Primary case/evidence, new packet. One supplied Primary v0.3 run1 response passes schema checks and corrects targeted direction. No contrast/hype v0.3 tests. |

The v0.3 revision and actual evidence were prepared in the working tree between the v0.2 and Phase 5A commits, under explicit phase approvals. No historical commit is invented or backdated. Preparation manifests retain their truthful preparation-time status; later validation/diagnostic records document actual received results. No amended/rebased earlier history.

Resolve the exact Phase 5A candidate SHA after committing with:

```sh
git log -1 --format=%H -- agents/promethean_agent/records/version_history.md
```

A document cannot embed its own containing commit hash. The completed SHA and verified remote branch tip are reported to the user after the actual commit/push, rather than guessed here. Subsequent documentation-only commits, if any, must be distinguished from the tested-candidate instructions/packet hashes.

## Before and after

- Baseline response: responses/primary_v0.2_run1.json; /change_monitoring_triggers/2 reverses the suppression direction.
- Revision: records/phase4b/instruction_changes.diff; old instructions/metadata retained there. All three-level mappings, six criteria, evidence policy and common schema unchanged.
- Same case/evidence: Primary case SHA e74994e6b0601e9a994f12d720c6e1e510e730c8efa9b25ea392077c1575a365; snapshot SHA 8ee69cc52c778fc5b37c443a8b68261413ef85d648cc484ebe48698a9ad88e22.
- Retest: responses/primary_v0.3_run1.json; correctly separates feasible reversion/reduction, causally supported dependent collapse and unresolved substitution. Observed single-run improvement only. Classification stays qualified Breakthrough.
- Remaining limitation: "impossible in principle" may set a stronger standard than Chapter 11; preserved without further instruction revision. Other Phase 4A scope/label clarity issues remain documented, not quietly fixed.

## Preservation and provenance

Five raw outputs are original uploaded bytes, not edited to pass. Response hashes and baseline user-attested execution details appear in phase4a_validation_results.json; v0.3 hash/provenance limits in phase4b/primary_v0.3_validation.json. Source/packet/instruction hashes provide artifact traceability, not independently audited model telemetry. All final submission deliverables remain ungenerated.
