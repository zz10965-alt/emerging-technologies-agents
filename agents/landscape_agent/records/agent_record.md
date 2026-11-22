# Assignment 8 internal Agent Record

- Agent and version — Emerging Technology Landscape Agent, v0.1, prepared 2026-11-22. v0.2 revised on 2026-11-22 for source currency and claim attribution.
- Repository — `zz10965-alt/emerging-technologies-agents`. Local branch — `assignment8-landscape`, based on verified Assignment 7 tip `a0862fd98f0f0c06a4ed189819c87b3752f1bd34`. v0.1 prompt checkpoint: `23dd283b6d8ebfff106e0f9b70de02825731e37d`. v0.2 retest packets: `80d9f753652b451cbfaa8f0e10094f18aea67f39`. The final tested version commit is pending.
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
| ChatGPT primary and contrasts | Completed for v0.1 | Three original outputs supplied by the user and preserved byte for byte. The user reports GPT-6 with browsing on 2026-11-22, in one conversation. See the uploaded run metadata. |
| Response structure | Passed for v0.1 | `python3 tools/validate_response.py <response>` and the installed `jsonschema` validator against `core/output_schema.json` passed for all three files. |
| Source accuracy and analytical comparison | Partial for v0.1 | Context comparison completed. The OWASP version issue was independently confirmed. Other source checks were blocked by proxy errors. See below. |
| Weakness and bounded revision | Completed | v0.2 specifies release checks, precise claim locators and scopes, and distinct evidence entries. All three revised packets built with the unchanged cases. |
| v0.2 ChatGPT retests | Completed, shared conversation | Three original responses preserved and validated. Shared context is a limitation on claims of isolated repeatability. |
| Final technical package | Prepared | Includes the original responses and the verification addendum below. Use the verified figures in the addendum for any downstream summary. |

## Source and evidence log

| Source or evidence | Status and relevance |
| --- | --- |
| Assignment 8 memo V3 and common course documents | Read during preparation. Establish scope, evidence policy, testing and handoff requirements. They supply no dated market observations. |
| Uploaded original scaffold ZIP | Archive integrity and byte comparisons verified. Establishes the common contracts and reference toolchain. |
| Three Assignment 8 cases | Newly written hypothetical inputs. Test priorities are inferences from their assumptions. Local performance, permission, and applicable requirements remain undetermined. |
| OWASP official project source | Retrieved the [issuer's GitHub project source](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/index.md). It identifies the 2025 edition as historical and dates the 2026 release to August 4, 2026, before the case cutoff. This verifies the version issue. It does not establish any incident rate or a product's safety. |
| Stanford HAI 2026 AI Index | The outputs report accessing the original report. Our independent request to the cited report was blocked by proxy HTTP 403. The broad wording on GenAI adoption has no specific table or survey population in the outputs and remains independently unverified. |
| NIST AI 600-1 | The outputs report accessing the issuing-body publication dated 2024-07-26. Independent checks of the cited page, DOI and NIST PDF were blocked by proxy HTTP 403. |
| EU AI Act | The primary output cites the Commission timeline and a consolidated EUR-Lex text dated 2026-07-27. Independent requests to both were blocked by proxy HTTP 403. The output qualifies applicability, which remains undetermined for the hypothetical firm. |
| Vendor and local performance | No provider contract, pricing, representative task benchmark, or measured local outcome was supplied. Claimed transfer of broad results remains a hypothesis. |

## Actual v0.1 comparison and diagnosis

All three outputs used byte-identical general finding text. This keeps broad evidence stable, but shared conversation history can influence later outputs. It does not establish independent repeatability. At the application and organization levels, the primary favored a comparison of analyst-led research with retrieval-supported drafting on authorized multilingual sources, gated on lineage and data permissions. The hospital retained templates and interpreters, allowing only an offline synthetic benchmark pending language fidelity, reviewer capacity and approvals. Ecommerce proposed a four-week SKU sandbox against templates, gated on factual attributes, editing effort and rollback. The comparisons and monitoring priorities changed in the expected direction. The three outputs describe hypothetical decisions, with no observed deployment benefit.

A shared weakness was the unqualified use of OWASP 2025 as the supporting edition in all three outputs despite a newer release before the cutoff. This does not invalidate the general security concern. Ecommerce also cited OWASP twice for essentially the same warning, and the hospital repeated NIST. The fragile claims were plausible examples of invalid transfer, but often lacked a dated original assertion attributable to anyone. v0.2 adds release history checks, precise support and survey scope, evidence deduplication, and explicit labeling for hypothetical transfer. The original replies are preserved. The v0.2 results assess the revision on the three cases. Separate conversations would help measure carryover in a future replication study.

Team handoff is provisional. Carry forward the three analytical levels, dated evidence provenance, refresh conditions, and human decision authority. The team's decision-relevant signal, strongest alternative, fragile claim, and limiting uncertainty remain pending observed outputs.

## v0.2 retest and packaging assessment

The user supplied three GPT-6 outputs and execution metadata dated 2026-11-22, with browsing reported as available. The user confirmed that the three v0.2 prompts were run separately in one newly opened ChatGPT conversation, with fresh outputs for each case. The v0.1 metadata likewise reports one conversation for that round. Both rounds produced identical general findings within the round and different application and organizational findings. Shared conversation history limits claims about isolated repeatability. All three fresh case runs count toward the primary and contrast testing requirement. Separate conversations are optional for investigating carryover.

| Revision target | v0.1 → v0.2 observed result |
| --- | --- |
| Citation currency | Resolved for OWASP in all three cases. The [official 2026 release README](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/blob/main/2026/README.md) independently returned HTTP 200 and identifies the published edition, August 4, 2026 release date, and the dated prompt-injection entry. NIST 2024 is now explicitly a historical baseline. Its currency was not independently established. |
| Citation specificity | Improved, still incomplete. Stanford now has an Economy chapter locator and separates GenAI use from general AI adoption, but the 70% claim lacks the underlying table, population and field period. The primary adds an Article 4 locator, but the exact consolidation and its contents were not independently verified. NIST identifies the exact report and date, without a supporting section locator. |
| Duplication | Resolved in this sample. The hospital combined its repeated NIST entries and ecommerce removed its repeated OWASP entries. Each v0.2 response has one entry per cited source (primary 4, hospital and ecommerce 3 each). |
| Fragile claims | Primary attributes a dated survey inference and disallows using it for vendor selection. Hospital and ecommerce now explicitly label candidate vendor/benchmark claims unverified. The primary has a refresh condition in its limitations, but no dedicated survey-refresh item in its monitoring array, as the specialist requested. |
| Context sensitivity | Retained. Primary compares authorized retrieval and analyst workflows with a citation and source-rights gate. Hospital defers patient-facing use, comparing templates and interpreters on synthetic language cases with a critical semantic-error stop condition. Ecommerce compares platform, standalone and deterministic templates in a four-week sandbox with editing-effort, attribute and rollback gates. Local performance and provider choices remain unmeasured. |

### Independent source-check results

The outputs report original-source access. Independent `curl -LsS --max-time 15` requests to the exact Stanford Economy, NIST and consolidated EUR-Lex URLs each failed with proxy CONNECT HTTP 403. The alternate Crossref DOI metadata endpoint and EU official ELI link were also blocked. The OWASP canonical project README was accessible via raw.githubusercontent.com and independently confirms the edition and date. Before finalizing, verify the Stanford statistic against the original table and survey methodology, the NIST publication and any applicable updates, and the cited EUR-Lex consolidation and Article 4 text. Preserve source locators or original excerpts with access dates. Applicability to the hypothetical organization still requires actual jurisdiction, roles and accountable review.

### Technical checks

- Passed — `cmp` confirmed each v0.2 response and the execution metadata match the uploaded originals byte for byte. The v0.1 originals remain preserved.
- Passed — `python3 tools/validate_response.py <response>` passed for the three v0.2 originals. The installed JSON Schema validator passed all six original responses against the frozen output schema and all three cases against the frozen input schema.
- Passed — `python3 tools/check_frozen_core.py` returned `FROZEN CORE INTACT`.
- See the subsequent PDF verification addendum for the final evidence disposition.


## Verification addendum — original PDFs supplied by the user

- **Stanford AI Index 2026, Economy chapter, §4.3, p. 193, Figure 4.3.1.** The chapter attributes the figure to the 2025 McKinsey & Company survey. In 2025, **79% of respondents** reported regular generative AI use in at least one business function at their organization, compared with **71% in 2024**. The separate all-AI figure was **88% in 2025**. The exact 70% figure in all three v0.2 replies is not supported by this figure. These are self-reported, directional results, not a census, an industry-specific estimate, or a measure of workflow benefit. The original JSON is preserved as test evidence. Use the corrected figures only with these qualifications. [Stanford report](https://hai.stanford.edu/ai-index/2026-ai-index-report/economy)
- **NIST AI 600-1.** The supplied issuer PDF confirms the title, DOI and July 2024 edition. Sections 2.2, 2.4 and 2.8 discuss confabulation, data privacy and information integrity. This verifies the cited risk-management scope. The PDF alone does not establish the exact webpage publication day or whether later guidance exists. [NIST report](https://doi.org/10.6028/NIST.AI.600-1)
- **EUR-Lex.** The exact 2026-07-27 consolidation and Article 4 citation remained inaccessible through the proxy. The package retains the original citation for audit but does not rely on it for a legal or pilot conclusion. The primary pilot gate remains a request for determination by accountable legal and security reviewers once actual jurisdictions, actors and data flows are known.
- **Disposition.** The three cases and both test rounds are complete for the technical package. Shared conversation context, the outstanding legal citation, and the missed primary survey-refresh trigger are documented limitations. No new model output or prompt revision is represented here.
