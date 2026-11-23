# Assignment 8 internal Agent Record

- Agent and version — Emerging Technology Landscape Agent, v0.2. Version 0.1 was prepared and v0.2 revised for source currency and attribution on 2026-11-22.
- Repository — `zz10965-alt/emerging-technologies-agents`. Repository branch: `assignment8-landscape`. Tested v0.2 prompt commit: `80d9f753652b451cbfaa8f0e10094f18aea67f39`. Archived test evidence and source review commit: `0369014c62f0a5e87c9e88d125987959e04cd887`. Historical v0.1 prompt checkpoint: `23dd283b6d8ebfff106e0f9b70de02825731e37d`.
- Scaffold — `MASY1800_ET_Agent_Scaffold_v1_0`.
- Governing question — Where does this emerging technology and application sit in the current technology landscape, and what signals should this organization monitor next?
- Primary decision — A hypothetical mid-sized cross-border consulting firm, a cautious fast follower, is considering a controlled three-month pilot for research synthesis and human-reviewed client report drafting. The key risks are weak or outdated sources, geographic and language gaps, confidentiality, and inaccurate client advice.

## Historical pre-run evaluation hypotheses

These hypotheses were recorded before testing. The completed observations and verification results appear below.

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
| Prompt reconstruction | Passed | Rebuilt all three v0.2 packets with the packaged scaffold and all three v0.1 packets with the historical v0.1 specialist inputs. All six matched byte for byte. |
| ChatGPT primary and contrasts | Completed for v0.1 and v0.2 | Three original responses per round, with execution metadata retained. |
| Response structure | Passed for both rounds | The frozen `tools/validate_response.py` passed all six original files. Full output schema validation also passed for all six. |
| Context comparison and bounded revision | Completed | v0.2 added release checks, more precise claim locators and scopes, and distinct evidence entries. The three cases were reused unchanged. The observed effects and residual weaknesses appear below. |
| Final technical package | Prepared | Includes the original responses and the verified findings below. Use the verified figures for downstream summaries. |

## Source and evidence log

| Source or evidence | Status and relevance |
| --- | --- |
| Assignment 8 memo V3 and common course documents | Read during preparation. Establish scope, evidence policy, testing and handoff requirements. They supply no dated market observations. |
| Uploaded original scaffold ZIP | Archive integrity and byte comparisons verified. Establishes the common contracts and reference toolchain. |
| Three Assignment 8 cases | Newly written hypothetical inputs. Test priorities are inferences from their assumptions. Local performance, permission, and applicable requirements remain undetermined. |
| OWASP official project source | Retrieved the [issuer's GitHub project source](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/index.md). It identifies the 2025 edition as historical and dates the 2026 release to August 4, 2026, before the case cutoff. This verifies the version issue. It does not establish any incident rate or a product's safety. |
| Stanford HAI 2026 AI Index | The user-supplied report PDF was checked against the raw outputs. Figure 4.3.1 does not support their 70% figure. See the verified findings below. |
| NIST AI 600-1 | The user-supplied issuer PDF confirms the July 2024 edition and relevant risk sections. The exact website publication day and later updates were outside the completed verification. |
| EU AI Act | The primary output cites the Commission timeline and a consolidated EUR-Lex text dated 2026-07-27. Independent requests to both were blocked by proxy HTTP 403. The output qualifies applicability, which remains undetermined for the hypothetical firm. |
| Vendor and local performance | No provider contract, pricing, representative task benchmark, or measured local outcome was supplied. Claimed transfer of broad results remains a hypothesis. |

## Actual v0.1 comparison and diagnosis

All three outputs used byte-identical general finding text. The general finding was stable across these cases. At the application and organization levels, the primary favored a comparison of analyst-led research with retrieval-supported drafting on authorized multilingual sources, gated on lineage and data permissions. The hospital retained templates and interpreters, allowing only an offline synthetic benchmark pending language fidelity, reviewer capacity and approvals. Ecommerce proposed a four-week SKU sandbox against templates, gated on factual attributes, editing effort and rollback. The comparisons and monitoring priorities changed in the expected direction. The three outputs describe hypothetical decisions, with no observed deployment benefit.

A shared weakness was the unqualified use of OWASP 2025 as the supporting edition in all three outputs despite a newer release before the cutoff. This does not invalidate the general security concern. Ecommerce also cited OWASP twice for essentially the same warning, and the hospital repeated NIST. The fragile claims were plausible examples of invalid transfer, but often lacked a dated original assertion attributable to anyone. v0.2 adds release history checks, precise support and survey scope, evidence deduplication, and explicit labeling for hypothetical transfer. The original replies are preserved. The v0.2 results assess the revision on the three cases.

Team handoff: For the consultancy, source-to-claim traceability and reuse rights are the priority signals, and analyst-led research is the baseline. Carry forward human approval and the limits of the survey evidence. Local benefit, provider fit, and regulatory applicability remain undetermined.

## v0.2 retest and packaging assessment

Both rounds retained a consistent general finding across cases and changed their recommendations, alternatives, and monitoring criteria to reflect the application and organization.

| Revision target | v0.1 → v0.2 observed result |
| --- | --- |
| Citation currency | Resolved for OWASP in all three cases. The [official 2026 release README](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/blob/main/2026/README.md) independently returned HTTP 200 and identifies the published edition, August 4, 2026 release date, and the dated prompt-injection entry. NIST 2024 is now explicitly a historical baseline. Its currency was not independently established. |
| Citation specificity | Improved, still incomplete. Stanford now has an Economy chapter locator and separates GenAI use from general AI adoption, but its 70% claim was unsupported by the subsequently checked figure. The primary adds an Article 4 locator, but the exact consolidation and its contents were not independently verified. NIST identifies the exact report and date, without a supporting section locator. |
| Duplication | Resolved in this sample. The hospital combined its repeated NIST entries and ecommerce removed its repeated OWASP entries. Each v0.2 response has one entry per cited source (primary 4, hospital and ecommerce 3 each). |
| Fragile claims | Primary attributes a dated survey inference and disallows using it for vendor selection. Hospital and ecommerce now explicitly label candidate vendor/benchmark claims unverified. The primary has a refresh condition in its limitations, but no dedicated survey-refresh item in its monitoring array, as the specialist requested. |
| Context sensitivity | Retained. Primary compares authorized retrieval and analyst workflows with a citation and source-rights gate. Hospital defers patient-facing use, comparing templates and interpreters on synthetic language cases with a critical semantic-error stop condition. Ecommerce compares platform, standalone and deterministic templates in a four-week sandbox with editing-effort, attribute and rollback gates. Local performance and provider choices remain unmeasured. |

### Execution metadata

The preserved metadata reports GPT-6 with browsing on 2026-11-22 for both rounds. Each round produced a fresh response for each of the three case prompts within one conversation. Shared context limits conclusions about isolated repeatability.

## Verified findings and source limits

- **Stanford AI Index 2026, Economy chapter, §4.3, p. 193, Figure 4.3.1.** The chapter attributes the figure to the 2025 McKinsey & Company survey. In 2025, **79% of respondents** reported regular generative AI use in at least one business function at their organization, compared with **71% in 2024**. The separate all-AI figure was **88% in 2025**. The exact 70% figure in all three v0.2 replies is not supported by this figure. These are self-reported, directional results, not a census, an industry-specific estimate, or a measure of workflow benefit. The original JSON is preserved as test evidence. Use the corrected figures only with these qualifications. [Stanford report](https://hai.stanford.edu/ai-index/2026-ai-index-report/economy)
- **NIST AI 600-1.** The supplied issuer PDF confirms the title, DOI and July 2024 edition. Sections 2.2, 2.4 and 2.8 discuss confabulation, data privacy and information integrity. This verifies the cited risk-management scope. The PDF alone does not establish the exact webpage publication day or whether later guidance exists. [NIST report](https://doi.org/10.6028/NIST.AI.600-1)
- **EUR-Lex.** The exact 2026-07-27 consolidation and Article 4 citation remained inaccessible through the proxy. The package retains the original citation for audit but does not rely on it for a legal or pilot conclusion. The primary pilot gate remains a request for determination by accountable legal and security reviewers once actual jurisdictions, actors and data flows are known.
- **Disposition.** The three cases and both test rounds are complete for the technical package. Shared conversation context, the outstanding legal citation, and the missed primary survey-refresh trigger are documented limitations. No new model output or prompt revision is represented here.
