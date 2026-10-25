# Verified-source register — evidence snapshot v0.2

Access/review date: 25 October 2026 (America/New_York). This is a bounded evidence dossier, not an agent output, final classification, systematic review or assertion of latest universal capability. Seven original sources were inspected. Source findings have been checked against the retrieved original methods/results/limitations, not independently replicated. Historical experiments remain historical. Sources S3–S5 share METR and are not three independent replications.

Course authority retained: C11 (Fortino, Chapter 11, August 2026 draft rev 0.1, supplied PDF §§11.2/11.5/11.7, pp. 3–4 and 7–11); A4 (supplied Assignment 4 memo, date unspecified); COMMON/GUIDE (supplied common instructions and operating guide, dates unspecified). These establish course method, not contemporary empirical proof. The original Phase 2 course-only register is preserved in Git commit 63f816a.

## S1 — The Impact of AI on Developer Productivity: Evidence from GitHub Copilot

- Authors/issuer: Sida Peng, Eirini Kalliamvakou, Peter Cihon, Mert Demirer.
- Publication/version: 2023-02-13 (arXiv v1; experiment May–June 2022).
- Original: https://arxiv.org/abs/2302.06590v1
- Checked location: PDF pp. 3–5, Study Design/Results; pp. 7–8, discussion/limitations.
- Verification: Original full paper or issuer report retrieved over verified HTTPS; relevant methods, results and limitations inspected. Findings below are source claims, not independently replicated results.
- Supported source claim: 95 professional programmers recruited and randomized; among task completers, mean completion time 71.17 minutes with Copilot versus 160.89 without, a 55.8% reduction in a standardized JavaScript HTTP-server task.
- Method: Randomized controlled experiment; outcome conditional on completing the task.
- Qualifications/opposition: Authors report 35 completers in each group. Completion is based on passing 12 tests, not a comprehensive maintainability/security assessment. Narrow task, older tool and nonrepresentative recruitment; paper explicitly leaves code-quality effects unexamined. Microsoft/GitHub affiliations are disclosed on p. 1.
- Relevance: Supports useful code-generation assistance; opposes extrapolating a narrow result into universal productivity, autonomy or a 10x criterion.
- Numerical check: 1 - 71.17/160.89 = 0.557648 (~55.8% less time); 160.89/71.17 = 2.26064 times the task throughput if quality/task assumptions hold, not 10x. The speed-ratio interpretation is analyst arithmetic, not an independently measured population effect.
- Retrieved original SHA-256: `60d9bbb58e67a3ba5c5df28926227994086baa9767c0b0f4bc61b11035c15a9c`.

## S2 — Generative AI at Work

- Authors/issuer: Erik Brynjolfsson, Danielle Li, Lindsey R. Raymond.
- Publication/version: April 2023; revised November 2023 (NBER Working Paper 31161).
- Original: https://www.nber.org/papers/w31161
- Checked location: PDF abstract p. 2; data p. 13; empirical strategy p. 15; conclusion PDF pp. 29–30 (printed pp. 27–28).
- Verification: Original full paper or issuer report retrieved over verified HTTPS; relevant methods, results and limitations inspected. Findings below are source claims, not independently replicated results.
- Supported source claim: Study of 5,179 customer-support agents reports 14% higher issues resolved per hour on average, with larger gains for novice/lower-skilled workers, from staggered introduction of a generative-AI assistant.
- Method: Field evidence; difference-in-differences and identifying assumptions.
- Qualifications/opposition: Observational staggered rollout with difference-in-differences, not a randomized trial; one business setting and human agents remain in the workflow. Does not establish long-run labor-market outcomes or generalize to every firm. The NBER page points to a 2025 QJE publication, but this dossier verifies and cites the November-2023 working-paper version, not uninspected final-version estimates.
- Relevance: Supports usefulness beyond coding and possible diffusion of expertise; does not prove multi-tier categorical dissolution or measured society-wide democratization.
- Numerical check: 14% higher issues/hour corresponds to 1.14 times that metric, not 10 times. Do not treat it as a time reduction or combine it numerically with S1.
- Retrieved original SHA-256: `9af82b90f2a94f8757ace8c7b7ef0934b145a00f4156fc806f4fb8a33e1bddc2`.

## S3 — Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity

- Authors/issuer: Joel Becker, Nate Rush, Beth Barnes, David Rein (METR).
- Publication/version: 2025-07-10 organizational report; retrieved arXiv paper v2 dated 2025-07-25.
- Original: https://arxiv.org/abs/2507.09089v2
- Checked location: PDF abstract and §§2–3; original report Core Result/Methodology and its 2026 update warning.
- Verification: Original full paper or issuer report retrieved over verified HTTPS; relevant methods, results and limitations inspected. Findings below are source claims, not independently replicated results.
- Supported source claim: 16 experienced open-source developers completed 246 tasks with randomized AI access; early-2025 tools increased implementation time by 19% in that setting.
- Method: Task-level randomized controlled trial, realistic repository work.
- Qualifications/opposition: Specific developers, mature familiar repositories and February–June 2025 tools, chiefly Cursor and Claude 3.5/3.7 Sonnet. Not a claim about all developers or current tools. The original METR web page explicitly says the historical result is out of date; read S4 and S5 with it.
- Relevance: Opposes universal acceleration and equating perceived gains with measured gains; does not establish that LLMs lack useful capability.
- Numerical check: 19% longer time means 1.19 times completion time, not 19% less throughput; inverse throughput would be ~0.8403 under identical-task assumptions. Do not compare its time outcome directly to S2 issues/hour.
- Retrieved original SHA-256: `3e18d9e097a3163dbae662e8b7c68ace0510be433891994b136ae7730beab25c`.

## S4 — We are Changing our Developer Productivity Experiment Design

- Authors/issuer: Joel Becker, Nate Rush, Tom Cunningham, David Rein, Khalid Mahamud (METR).
- Publication/version: 2026-02-24.
- Original: https://metr.org/blog/2026-02-24-uplift-update/
- Checked location: Opening summary; Wider adoption of AI has made it more difficult to measure task-level productivity; Details of the productivity study.
- Verification: Original full paper or issuer report retrieved over verified HTTPS; relevant methods, results and limitations inspected. Findings below are source claims, not independently replicated results.
- Supported source claim: METR reports that later-2025 follow-up data gives an unreliable signal of current productivity because participant/task selection and concurrent-agent time measurement undermine interpretation. Authors believe acceleration likely increased, but call their data very weak evidence for its size.
- Method: Follow-up experiment with acknowledged recruitment, task-selection, pay-rate, quality and time-measurement problems.
- Qualifications/opposition: Original follow-up report, not proof of a precise current causal gain. Developer reluctance to work without AI is selection evidence, not proof civilization cannot function without LLMs. Do not use the old 19% slowdown as a current estimate or the follow-up as a verified large gain.
- Relevance: Supports the possibility of increased usefulness and changed workflows; opposes confident current magnitudes and overclaiming suppression-test irreversibility.
- Numerical check: No follow-up point estimate is used in the snapshot because the issuer calls the signal unreliable.
- Retrieved original SHA-256: `8b13e19d428747a15479a85665784152a1f29a103e06260767bab20ef43c4537`.

## S5 — Measuring the Self-Reported Impact of Early-2026 AI on Technical Worker Productivity

- Authors/issuer: Joel Becker (METR).
- Publication/version: 2026-05-11 (survey February–April 2026).
- Original: https://metr.org/blog/2026-05-11-ai-usage-survey/
- Checked location: Summary; Methodology; Results/Productivity gains around March 2026; Qualitative impressions.
- Verification: Original full paper or issuer report retrieved over verified HTTPS; relevant methods, results and limitations inspected. Findings below are source claims, not independently replicated results.
- Supported source claim: Survey of 349 technical workers reports median self-reported value multipliers between 1.4x and 2x across three measures; median self-reported speed multiplier is 3x.
- Method: Original survey, not experiment; shares issuer with S3/S4.
- Qualifications/opposition: Convenience sample, low email response rates, self-reported counterfactuals and possible overstatement; value and speed differ. The authors explicitly warn that internal consistency does not establish reality and are skeptical of especially high estimates. Not causal measured productivity, general-population evidence or demonstrated 10x impact.
- Relevance: Current positive reports supporting perceived usefulness, balanced against measurement and selection weaknesses; not an independent confirmation of S3/S4.
- Numerical check: Retain the distinctions among 1.4–2x self-reported value, 3x self-reported speed and actual measured effects. No metric reaches a verified general 10x conclusion here.
- Retrieved original SHA-256: `240a943b502a8ee8accfffc1b8110ab616f71517f0292096411bed05ed89f9f2`.

## S6 — Towards Conversational Diagnostic AI

- Authors/issuer: Tao Tu, Anil Palepu, Mike Schaekermann, et al. (Google Research / Google DeepMind).
- Publication/version: 2024-01-11 (arXiv v1).
- Original: https://arxiv.org/abs/2401.05654v1
- Checked location: PDF abstract p. 1; study design/results; Discussion pp. 17–20.
- Verification: Original full paper or issuer report retrieved over verified HTTPS; relevant methods, results and limitations inspected. Findings below are source claims, not independently replicated results.
- Supported source claim: Specialized LLM-based AMIE was compared with 20 primary-care physicians across 149 simulated scenarios in a randomized double-blind crossover study of text consultations. Authors report higher diagnostic accuracy and better performance on many rated axes in that evaluation.
- Method: Original experimental preprint, simulated clinical consultations, not routine clinical outcomes.
- Qualifications/opposition: Patient actors, text-only interface unfamiliar to clinicians, specialized system and limited representativeness/blinding; not a live-patient safety trial or an evaluation of clinical-documentation benefits. It does not prove that generic deployable LLM systems inherit AMIE performance. Authors require further research before real-world translation.
- Relevance: Supports the plausibility of capabilities beyond code/customer support; opposes attributing specialized simulated performance to generic LLM systems or authorizing hospital deployment.
- Numerical check: Use the verified 149 scenarios/20 physicians only for study scope, not effect magnitude or tenfold claims. No clinical outcome reduction is inferred.
- Retrieved original SHA-256: `d16d2f4f196a913c37529b066165adc4d7b8375dfb68c3cc1ae374e50ee7531e`.

## S7 — Do Users Write More Insecure Code with AI Assistants?

- Authors/issuer: Neil Perry, Megha Srivastava, Deepak Kumar, Dan Boneh.
- Publication/version: 2022-11-07 initial preprint; 2023 CCS conference paper; retrieved arXiv v3 dated 2023-12-18.
- Original: https://arxiv.org/abs/2211.03622v3
- Checked location: PDF abstract/introduction p. 1; §3 study design and Table 1; §4 security results.
- Verification: Original full paper or issuer report retrieved over verified HTTPS; relevant methods, results and limitations inspected. Findings below are source claims, not independently replicated results.
- Supported source claim: In a 47-participant study of five analyzed security-related programming tasks, participants with an AI assistant generally wrote less secure code and were more likely to believe their code was secure; insecure solutions occurred more often for four of five tasks.
- Method: Randomized user study with unequal group sizes; manually assessed correctness/security.
- Qualifications/opposition: Assistant based on codex-davinci-002, small mostly-student sample, security-task setting and older system. No current incidence or universal risk rate can be inferred. Not a reason to deny all productivity benefits; correctness and security need separate measurement.
- Relevance: Opposes treating code generation as reliable autonomous delivery and supports retaining oversight/security validation.
- Numerical check: Do not invent a pooled vulnerability percentage or claim significance for every task; retain task heterogeneity.
- Retrieved original SHA-256: `c079f7b417079efd03f57848fb011963f9df856156b5a9bd605c00af725d706a`.

## Unverified supplemental guidance and remaining evidence gaps

NIST AI 600-1 at https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf, the attempted NIST publication page, WHO at https://www.who.int/publications/i/item/9789240084759 and its attempted news announcement, and the attempted JAMA article returned 403 Forbidden. They are not cited as verified evidence or used for any substantive claim. A 403 may reflect network/site access restrictions; it does not establish missing credentials. Network-domain additions were saved in an environment configuration draft; this is not proof of application or publication. Research succeeded for the selected dossier through accessible original sources.

No original clinical-documentation trial, applicable jurisdiction-specific legal analysis, quality-adjusted full lifecycle cost comparison, verified broad 10x accessibility effect, society-wide suppression experiment or mature long-run irreversibility finding is established here. Those gaps limit conclusions; they must be explicit in responses. AMIE is specialized and simulated, not a generic-system or documentation-effectiveness proxy. No quantitative finding from an inaccessible source is admitted. No study is claimed to exhaust current October-2026 evidence.

## Gate/criterion evidence map — research guidance, not predetermined findings

| Element | Supporting material to evaluate | Opposition / unresolved requirement |
|---|---|---|
| System/component | S1/S2 deployable assistants; S6 usable specialized research system | Attribute only supported capability; not all AI, an isolated model, or the entire ecosystem |
| Categorical barrier | S1 generated working code; S2 assistance with knowledge-work responses; S6 diagnostic dialogue | Human participation remains in S1/S2; S6 is simulation. Useful task performance does not establish complete removal of a human-mind requirement. Challenge the universal wording of the barrier |
| Suppression | S4/S5 report work habits and perceived dependence worth investigating | Reluctance to forgo AI is not observed infrastructure collapse. No societal suppression test or irreversible dependence is verified |
| Order of magnitude | S1 ~2.26x conditional task-time ratio; S2 1.14x issues/hour; S5 reported gains | None is verified broad 10x quality-adjusted performance/cost/access. Do not turn selected anecdotes, percent changes or survey beliefs into 10x proof |
| Widespread impact | S1/S2 observed in coding/support; S6 explores medicine | Multiple sectors are not automatically multiple tiers of human existence; clinical simulation does not establish population impact |
| Paradigm shift | Potentially changed production of code/knowledge responses is a hypothesis suggested by S1/S2/S6 | Qualitative interpretation, not an empirical conclusion established by these task studies; distinguish changed assumptions from faster existing work |
| Catalytic effect | S1 code assistance and S6 domain adaptation suggest enabling pathways | Downstream innovation causality and general dependence not measured; no claim that these papers prove an innovation wave |
| Democratizing effect | S1 heterogeneity and S2 greater benefits for novices/lower-skilled workers | Restricted populations, human oversight, uneven access; expertise diffusion is not universal democratization |
| Irreversibility | S4/S5 provide contemporary use/dependence signals | Short horizon, selection and self-report; durable cross-tier dependence unverified. Prospective mode cannot be rounded up to Confirmed Promethean |

The same source can inform multiple questions but is not multiple independent proofs. A failed/unresolved barrier gate cannot be overridden by positive task metrics. Classification is left to the actual agent run, with explicit confidence, qualification or abstention.
