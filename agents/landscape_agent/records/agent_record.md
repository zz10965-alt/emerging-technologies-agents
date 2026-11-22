# Assignment 8 internal Agent Record

- Agent and version — Emerging Technology Landscape Agent, v0.1, prepared 2026-11-22.
- Repository — `zz10965-alt/emerging-technologies-agents`. Local branch — `assignment8-landscape`, based on verified Assignment 7 tip `a0862fd98f0f0c06a4ed189819c87b3752f1bd34`. This record accompanies the v0.1 prompt-preparation checkpoint. The final tested version commit is pending.
- Scaffold — `MASY1800_ET_Agent_Scaffold_v1_0`.
- Governing question — Where does this emerging technology and application sit in the current technology landscape, and what signals should this organization monitor next?
- Primary decision — A hypothetical mid-sized cross-border consulting firm, a cautious fast follower, is considering a controlled three-month pilot for research synthesis and human-reviewed client report drafting. The key risks are weak or outdated sources, geographic and language gaps, confidentiality, and inaccurate client advice.

## Pre-run expectations

These are evaluation hypotheses. The three-level findings, recommendation, and source-supported confidence are pending the actual runs.

| Level or case | Expected test of specialist behavior |
| --- | --- |
| General ET across all cases | The general position should remain consistent at comparable source scope and dates. In particular, general model or retrieval advances alone should leave task-specific performance and economics unresolved. Real differences in accessible evidence should be explained. |
| Primary application and organization | Compare retrieval-supported drafting against analyst-led research using licensed databases and editorial review. The pilot decision should emphasize traceability, current local-language coverage and reuse rights, plus client-data and provider terms before broader exposure. |
| Contrast 1 application and organization | Hospital appointment communications should elevate approved templates and interpreter services as alternatives or complements. Watch clinical meaning and language fidelity, qualified reviewer capacity, and approved messaging and data-handling pathways before patient-facing use. |
| Contrast 2 application and organization | Attribute-bound catalog drafting should elevate deterministic templates and platform-native features. Watch unsupported attributes, net editing effort, export or rollback, and cost before the next catalog update. A reversible sandbox with excluded customer data permits a different initial action. |

## Verification and test status

| Check | Status | Evidence |
| --- | --- | --- |
| Frozen core integrity | Passed | `python3 tools/check_frozen_core.py` returned `FROZEN CORE INTACT`. All core, tool, and template files matched canonical ZIP members byte for byte. |
| Case input contract | Passed | Used installed `jsonschema.validators.validator_for` with `core/input_schema.json` to check the schema and validate all three complete inputs. Confirmed identical technology and evidence boundaries. |
| Prompt packet construction | Passed | Ran `python3 tools/build_prompt.py --agent agents/landscape_agent --case agents/landscape_agent/cases/<case>.json --out agents/landscape_agent/prompts/assignment8_<case>_v0.1_prompt.txt` for three cases. Each packet contains its exact parsed case and the frozen output schema. |
| Primary packet reproduction | Passed | Rebuilt with the command in the README using a temporary output path. `cmp` confirmed an exact match. |
| ChatGPT primary and contrasts | Not run | Awaiting three original outputs. No earlier model outputs or test results were used. |
| Response structure, source accuracy, and analytical comparison | Not run | Awaiting original outputs. |
| Weakness, bounded revision, and retest | Not run | Diagnose from actual results. Keep originals and preserve unresolved limitations. |
| Staged package rebuild, extraction and manifest | Not run | Final packaging follows actual runs and review. |

## Source and evidence log

| Source or evidence | Status and relevance |
| --- | --- |
| Assignment 8 memo V3 and common course documents | Read during preparation. Establish scope, evidence policy, testing and handoff requirements. They supply no dated market observations. |
| Uploaded original scaffold ZIP | Archive integrity and byte comparisons verified. Establishes the common contracts and reference toolchain. |
| Three Assignment 8 cases | Newly written hypothetical inputs. Test priorities are inferences from their assumptions. Local performance, permission, and applicable requirements remain undetermined. |
| External landscape evidence | No external claim was verified during packet preparation. After runs, record original sources as actually accessed, dates and scopes, supported claims, vendor assertions, contrary evidence, and unresolved gaps. Recheck consequential claims against the original sources. |

Team handoff is provisional. Carry forward the three analytical levels, dated evidence provenance, refresh conditions, and human decision authority. The team's decision-relevant signal, strongest alternative, fragile claim, and limiting uncertainty remain pending observed outputs.
