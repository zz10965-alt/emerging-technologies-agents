# Evidence preparation v0.2 — actual technical checks

Original command: `python tools/check_frozen_core.py` (repository root).
Exit status: 0. Actual stdout:

```text
FROZEN CORE INTACT
```

- All 32 original archive files were compared byte-for-byte and remain identical, including tools, schemas, template, docs, manifests and examples.
- Specialist instructions are identical to implementation commit 63f816a; architecture/contracts unchanged. Metadata version changes only to identify the new evidence/packet preparation.
- All four cases contain the exact same shared snapshot prefix. Primary/startup application text is identical. Hype/primary differ only in additional_context, with the unsupported hype claim appended.
- Required input string fields and actual serialized inclusion of case data/metadata in all four generated packets were checked successfully. Snapshot text is embedded as a JSON string with escaped newlines, as the original builder requires.
- Original v0.1 packets remain byte-identical to commit 63f816a. New packets use v0.2 filenames.
- responses/ contains only the inherited .gitkeep. No model calls, response validations, analytical pass/fail results, revision/retest outcomes or final reports were produced.
- Every repository change is within agents/promethean_agent/.

Seven original sources/reports were read at relevant methods/results/limitations locations and documented with source hashes and bounded paraphrases. Source experiments were not replicated. Selection, date and scope limits remain explicit; inaccessible NIST/WHO/JAMA content is not admitted. Source verification and technical checks do not establish the correctness of an as-yet unrun agent.

Execution instructions: manual_execution.md. Exact artifact hashes: preparation_v0.2_manifest.json. The next step is four actual fresh-conversation ChatGPT runs and return of the unedited raw responses with actual runtime details.
