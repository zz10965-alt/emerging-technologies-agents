# Assignment 7 — Codex Implementation Brief
## SubAgent 6: Organizational Adoption of Emerging Technologies Agent

**Course:** NYU SPS MASY1-GC 1800 Emerging Technologies  
**Assignment:** Lab 7 / Assignment 7 — Organizational Adoption of Emerging Technologies Agent  
**Working language:** English for code, agent outputs, and submitted written artifacts  
**Source of authority:** The attached Assignment 7 memo, Student Operating Guide, frozen scaffold, Agent Record Template, and Common Individual Assignment Instructions. If this brief conflicts with those documents, follow the course documents and report the conflict.

## 0. Your Role and Execution Rules

Act as a careful Codex development partner. Build the specialist using the **provided frozen MASY1800 Common Emerging Technology Agent Scaffold v1.0**; do not design a replacement architecture. Perform routine implementation, tests, documentation, and packaging where your tools permit. Clearly distinguish completed steps from prepared-but-not-executed steps. **Do not fabricate model responses, validation passes, external evidence, Git commits, or uploads.**

Before editing, inspect the scaffold structure and existing repository. Briefly state which student-editable files you will modify and why, then proceed without unnecessary approval checkpoints. If a required external action is inaccessible, continue with the remaining work and list exactly what the student must do.

The instructor expects **60–90 minutes of bounded effort**. Prioritize analytical rigor, evidence, working scaffold compatibility, tests, and an honest audit trail over elaborate extra engineering.

## 1. Inputs and Working Repository

I am providing these four attachments:

1. `07_Assignment_7_Organizational_Adoption_Agent_V3.docx` — weekly assignment requirements.
2. `MASY1800_ET_Agent_Scaffold_v1_0 (9).zip` — canonical frozen course scaffold.
3. `Emerging_Technologies_Common_Agent_Scaffold_Student_Guide_v2 (6).docx` — student operating guide.
4. `Emerging_Technologies_Agent_Record_Template (4).docx` — record template.

Also consult the common individual assignment front matter if supplied. If the earlier Assignment 6 working repository is available, reuse its **working-copy structure, coding conventions, and development workflow**, not its specialist conclusions or test responses. Create an Assignment 7-specific branch and agent folder. Do not overwrite Assignment 6 or any earlier submission. If repository access is unavailable, work from a separate extracted copy of the ZIP and record the pending repository/commit work.

The ZIP includes, among other files, `agents/_template/`, `tools/new_agent.py`, `tools/build_prompt.py`, `tools/validate_response.py`, and `tools/check_frozen_core.py`. Inspect their actual usage before running commands. Preserve the original ZIP separately and unchanged.

**Non-negotiable constraints:**
- Never edit `core/`, frozen schemas, frozen common instructions, or other marked FROZEN CORE assets.
- Keep the common input contract, common output contract, and three-level distinction intact.
- Do not require an OpenAI API account or API key. The reference workflow builds local prompt packets and runs them interactively in ChatGPT.
- Keep each genuine original model result unchanged in its own file.
- Verify frozen-core integrity before and after implementation with the supplied checker.
- Use real Git branch/commit identifiers only if they exist and are accessible.

## 2. Specialist Purpose: Different From Assignment 6

**Specialist name:** Organizational Adoption of Emerging Technologies Agent (SubAgent 6).

**Governing question:** "Even if adoption is strategically appropriate, can this organization actually absorb, govern, and sustain the proposed application?"

This is **not** a repetition of the previous Adoption Agent's technology/adoption timing assessment. Evaluate **organizational readiness to execute and sustain** an attractive technology application. Separate:

1. ET generally — grounded general observations about generative AI relevant to this specialist's scope.
2. ET for the intended application — application-specific fit and prerequisites.
3. ET for that application **in the specified organization** — actual strengths, readiness gaps, remediation, ownership, confidence, and decision timing.

Do not interpret low organizational readiness as low technology maturity. Do not use the organization's adoption posture to rewrite general technology evidence. Organizational context changes feasibility, acceptable risk, implementation sequencing, and management action.

## 3. Primary Scenario: Hypothetical Educational Case

**Emerging technology:** Generative AI, especially LLM-based research synthesis and drafting assistance.  
**Intended application:** AI-assisted preparation of client-facing market research reports for cross-border consulting engagements.  
**Business objective:** Reduce repetitive synthesis and drafting effort while maintaining factual traceability, expert review, confidentiality, and accountable delivery.  
**Organization:** A hypothetical, mid-sized cross-border market consulting company serving international business clients.  
**Adoption posture:** Moderate / cautious fast follower, interested in a bounded pilot rather than immediate enterprise-wide rollout.  
**Decision horizon:** Whether to begin a carefully controlled pilot within approximately three months and the minimum conditions for any broader rollout.  
**Risk context:** Client confidentiality, unreliable or inadequately sourced claims, quality assurance, reputational damage, and continued operations after the pilot.

**Supplied hypothetical organization profile:**
- Senior management supports experimentation, but there is no formal implementation governance structure yet.
- Analysts have strong market research skills but uneven generative-AI skills.
- Report creation is largely manual; AI-specific review checkpoints have not been standardized.
- Some internal data sources are fragmented, and data access permissions/integration capacity are not fully documented.
- A limited pilot budget is envisaged, but sustained operating funding is unverified.
- A designated operational owner, escalation pathway, and post-launch monitoring process are not documented.
- Employee receptiveness varies; structured training and change-management plans are incomplete.
- Relevant client-information handling rules and permissions must be verified before any live client data is processed.

**Evidence boundary:** These are **assumptions for a hypothetical classroom test case**, not audited findings about a real company. Do not invent headcounts, budgets, data volumes, regulatory obligations, security certifications, pilots, or measured business benefits. Explicitly tag case assertions as supplied assumptions, analytical implications as inferences, and unknowns as missing evidence.

## 4. Required Readiness Analysis

Create a reproducible **eight-dimension organizational readiness framework**:

1. Leadership / executive sponsorship
2. Workforce capabilities / skills
3. Workflow / process integration
4. Infrastructure / data readiness
5. Resources / budget
6. Governance / risk / accountability
7. Culture / organizational change
8. Operating ownership / long-term sustainability

For **each** dimension, analyze:
- Evidence-supported readiness strengths
- Material readiness gaps and their mechanisms of failure
- Evidence sufficiency, uncertainties, and missing inputs
- Business consequences if unresolved
- Priority for action, justified by consequence, dependency, and immediacy
- Concrete corrective action or gating condition
- Accountable function/role where reasonably inferable; do not invent a named person
- Verification or monitoring trigger for reassessment

Avoid an arbitrary numerical scoring system unless the provided specialist format supports it and criteria, assumptions, and uncertainty are transparent. Qualitative judgments are acceptable when calibrated.

Key behavior requirements:
- Explain why an action addresses a **specific observed or explicitly hypothesized gap**; reject generic management checklists.
- Distinguish blockers for a tightly controlled pilot from blockers for scaled production.
- Prioritize only the consequential gaps; not every dimension deserves equal attention.
- Explicitly identify existing organizational advantages, not just deficiencies.
- Recommend proportionate controls and human authority for any client-facing work.
- Avoid unsupported claims about external laws or contractual obligations. State where legal/security review is needed without pretending it is already complete.

## 5. Structured Output and Management Judgment

Preserve the **exact frozen common JSON output schema**. Put specialist-specific analysis inside the allowed fields, without adding unpermitted top-level keys. Use the schema file to determine exact placement and formatting. The output should convey:

- General ET finding
- Application-specific finding / technology fit
- Organization-specific readiness finding, separate from technology fit
- Eight-dimension strengths, gaps, evidence quality, and key dependencies
- Prioritized and context-specific readiness actions with plausible functional ownership
- Bounded recommendation: proceed to controlled pilot, proceed only after defined gates, or defer, as the evidence warrants
- Distinct requirements for pilot versus broader deployment
- Confidence and material uncertainties
- Missing-information request / abstention condition
- Reassessment signals or triggers
- Contradictory evidence and known limitations

**Critical missing-evidence behavior:** The agent must flag at least one readiness factor where supplied information is not sufficient; identify exactly what is missing, why it affects the decision, where evidence might be obtained, and which finding must remain qualified or withheld. Example: permissions and controls for real client documents, confirmed operational ownership, or funded ongoing maintenance. Do not convert uncertainty into an unsupported definitive conclusion.

## 6. Context-Contrast Test Design — Hold Technology AND Application Constant

Create at least two executed cases total (primary plus one contrast); three cases preferred if feasible within the time limit.

### Primary
The mid-sized consulting organization described above, with mixed readiness and important unverified organizational capabilities.

### Contrast 1 — More mature organization
A hypothetical larger cross-border consulting firm using the **identical** AI-assisted market research report workflow. Assume documented executive sponsorship, an identified service owner, trained analyst cohorts, established data access rules, standardized editorial and quality gates, dedicated IT/security support, and an approved pilot budget. Do not simply assert that all risk is gone; preserve uncertainties and distinguish pilot from scale readiness.

### Contrast 2 — Resource-constrained organization (if feasible)
A hypothetical small traditional cross-border consulting firm using the **identical** AI-assisted market research report workflow. Assume limited in-house IT support, informal data governance, fragmented data access, minimal training time, limited budget, and no long-term service owner. Specify different legitimate readiness priorities and implementation conditions.

These are synthetic profiles for **testing the specialist's context sensitivity**, not real-world claims.

**Invariant across all cases:** The technology, specific application, intended scope, and general ET/application-fit evidence should not change due only to organizational differences.

**Expected context-sensitive dimensions:** Readiness conclusions; primary barriers; priority and ownership of remediation; allowable pilot scope; management sequencing and time horizon. Describe why each change follows from organization-specific evidence. Do not impose a predetermined pass/fail outcome; let the agent justify its result.

### Test evaluation rubric
Assess whether the agent:
1. Keeps general ET and application fit stable where warranted.
2. Does not conflate organizational unreadiness with immature technology.
3. Produces materially different, defensible organization-specific conclusions.
4. Uses all eight dimensions without treating them as eight equally weighted checkboxes.
5. Cites supplied case evidence instead of inventing facts.
6. Makes corrective actions relevant and prioritized, with owner where supportable.
7. Explicitly requests material missing evidence and qualifies or abstains accordingly.
8. Gives different pilot-versus-scale recommendations when context warrants.
9. Maintains valid JSON conforming to the frozen contract.

Produce a concise comparison of at least one finding that **appropriately remains stable** and at least one finding that **appropriately changes**, with supporting examples from the actual saved outputs.

## 7. Build → Run → Validate → Revise Workflow

Follow scaffold procedures and their real command-line usage:

1. Inspect existing agent template, metadata, intake schema, output schema, and tests.
2. Create a new agent folder (suggested slug `organizational_adoption_agent`) using `tools/new_agent.py`, where appropriate.
3. Edit only the student-editable specialist instructions, metadata, and case files.
4. Generate standalone ChatGPT-ready prompt packets via `tools/build_prompt.py` for each case.
5. **Run the packets through ChatGPT** as the reference model environment; ask for one complete structured JSON response per case, with no Markdown wrapper.
6. Save **exact** original model outputs to separately named JSON files. If direct ChatGPT execution is unavailable within Codex, stop at this part of the workflow, provide the prompt packets, and clearly ask me to run them in ChatGPT and return the exact outputs. **Do not fabricate or simulate actual ChatGPT responses and present them as tests.**
7. Validate each actual model output using `tools/validate_response.py`. Record the actual command, success/failure, and any validation error.
8. Inspect differences and evaluate the substantive analytical quality, not merely JSON syntax.
9. Preserve a **genuine** weak response, error, unsupported inference, or context-insensitive behavior. Diagnose why it happened, modify editable instructions or another appropriate non-frozen file, and retest. If all initial tests appear sound, run a targeted adversarial diagnostic rather than inventing failure evidence.
10. Preserve before/after instructions, original/retest responses, and a short change log. Record remaining limitations even after successful fixes.
11. Check frozen-core integrity again. Report only the actual checker result.
12. Commit completed work to the appropriate Git branch only if repository access and permissions allow; otherwise identify needed commands and missing branch/commit details without inventing them.

**File organization:** Keep runnable specialist inputs, instructions, and metadata in `agents/<agent_slug>/`; save outputs under its `responses/` folder and records under its `records/` folder. Follow any stronger structure requirements from the scaffold. Place readable final documents in a clearly named `deliverables/` folder if appropriate.

## 8. Evidence and Research Policy

Use original evidence supplied in the case as the basis for organizational readiness findings. Treat hypothetical assertions as assumptions, not independently verified facts.

If claiming any consequential **current** regulatory requirement, technical prerequisite, industry norm, or vendor capability, seek a primary/source-of-record reference when browsing is available; record source, date, and relevance. If verification is unavailable, mark the claim unverified and avoid using it to support a decisive conclusion. Do not cite ChatGPT's own answer as primary evidence. Never invent URL citations or claim an external check was performed when it was not.

Use uncertainty explicitly and identify what evidence, process owner, or verified condition would change the decision.

## 9. Required Documentation and Deliverables

Produce these deliverables based on the **actual** evidence and test outcomes:

### A. Working agent package
Reproducible specialist agent from frozen scaffold, with editable specialist files, case inputs, generated prompt packets, representative actual JSON responses (where executed), testing/validation evidence, revision history, limitations, and team integration notes. Prepare one logical ZIP for submission if suitable. Preserve the canonical original ZIP separately.

### B. Specialist Agent Record
Complete Sections **A–E** of the supplied **Agent Record Template** (prefer retaining its structure and field names):
- A: Student/version, specialist, date, GitHub repository, branch, commit, frozen scaffold version.
- B: Governing question, ET, application, organization/industry, posture, risk, management horizon.
- C: Three-level finding, bounded implication, confidence, change conditions.
- D: Evidence, primary/contrast test results, what stayed stable/changed, real weakness, revision, remaining limitation/abstention.
- E: Credibility for team integration, key team recommendation, AI/verification note.

Do not populate fields with test results not yet obtained. Use `PENDING—reason` if necessary.

### C. Primary agent output report
Produce a readable report **derived from the actual primary response**, showing separate technology/application fit and organizational readiness; strengths; priority gaps; actions and owners; pilot/rollout conditions; missing evidence; confidence and limitations. Never silently substitute a speculative report for a not-yet-run agent output.

### D. Independent professional judgment (no longer than half a page)
Write an independent first-person judgment answering: Is this organization ready to implement and sustain the proposed application? What is the single most consequential readiness gap? What must change before management should proceed? Which missing evidence could materially change my judgment? Keep the scope limited to the actual scenario and test evidence.

### E. AI / verification note
Briefly document how ChatGPT/Codex materially assisted, which consequential technical/factual/methodological claims were verified and with what source/tool, and which statements rest on original case evidence rather than AI memory or generated summaries. Do not claim verification of unverified facts.

### F. Craft Gained (100 English words or fewer)
Describe **one genuinely learned insight**, specifically what in the analysis, source review, testing, or revision prompted it and how it changes future professional practice. Do not just restate the assignment's definition.

### G. Team handoff
Provide: readiness conclusion; strongest organizational asset; biggest readiness gap and corrective owner/action; missing-information condition; the organization-specific intake field(s) the integrated system must preserve; and one limitation the group should carry into integration.

**Formatting:** Where generating Word documents is supported, use Times New Roman, black text, restrained academic formatting, adequate margins/spacing, and clear headings; avoid corrupted fonts, overlapping text, or artificial padding. If DOCX generation is unavailable, provide clean Markdown drafts without claiming to have created Word files. Short texts D–F may be combined in one concise document, provided each requested element is separately labeled and its length rule is obeyed.

## 10. Final Acceptance Checklist

Before calling the assignment complete, verify with evidence:

- [ ] New specialist is built from the supplied frozen scaffold.
- [ ] No FROZEN CORE modifications; checker result recorded.
- [ ] Common input/output schemas are preserved; no unsupported JSON additions.
- [ ] All eight organizational readiness dimensions are meaningfully evaluated.
- [ ] Technology/application fit is distinct from organization readiness.
- [ ] Strengths, material gaps, prioritized actions, and inferred functional owners are addressed.
- [ ] The same technology/application is held constant across primary and contrast cases.
- [ ] At least primary + one contrast response were actually executed and saved.
- [ ] Actual model JSON outputs validate against the frozen schema.
- [ ] One genuinely observed failure/weakness and the follow-up revision or control are preserved.
- [ ] At least one missing-evidence request and relevant qualified/abstaining conclusion are present.
- [ ] Source verification claims accurately reflect checks actually performed.
- [ ] Agent Record, primary report, independent judgment, AI/verification note, Craft Gained, and handoff are prepared appropriately.
- [ ] GitHub repo/branch/commit accurately reflect accessible artifacts (or are marked pending).
- [ ] The final submission package is reproducible and clearly identifies remaining work.

## 11. What to Report Back to Me

Finish with a concise status table covering:

| Item | Status | Exact evidence/path |
|---|---|---|
| Agent files | Complete / Partial / Pending | Paths |
| Prompt packets | Complete / Partial / Pending | Paths |
| Primary execution and validation | Pass / Fail / Not run | Output + validation log |
| Contrast executions and validation | Pass / Fail / Not run | Outputs + validation logs |
| Weakness and revision | Documented / Pending | Before/after evidence |
| Frozen core | Pass / Fail / Not run | Checker output |
| Reports and Agent Record | Complete / Draft / Pending | Paths |
| Git branch and commit | Committed / Pending | Real identifiers |
| Submission ZIP | Ready / Incomplete | File path |

Then explicitly tell me which steps, if any, I must perform in ChatGPT or GitHub before submitting to Brightspace. Do not say the assignment is complete unless all mandatory evidence exists.
