# Emerging Technology Landscape Agent

Assignment 8, v0.2, revised on 2026-11-22. This specialist compares Generative AI, incumbent workflows, and complementary tools to identify which external changes could alter an organization's decision.

Repository branch: `assignment8-landscape`. Tested v0.2 prompt commit: `80d9f753652b451cbfaa8f0e10094f18aea67f39`. Archived test evidence and source review commit: `0369014c62f0a5e87c9e88d125987959e04cd887`.

## Reproduce the packaged checks

The completed package contains three cases and six original responses across v0.1 and v0.2. See the internal Agent Record for testing metadata, verified findings, and remaining limitations. The v0.1 prompt packets document the earlier test round.

| Case | Packet in `prompts/` | Original response in `responses/` |
| --- | --- | --- |
| Cross-border consulting | `assignment8_primary_v0.2_prompt.txt` | `assignment8_primary_v0.2_run1.json` |
| Hospital communications | `assignment8_contrast_1_v0.2_prompt.txt` | `assignment8_contrast_1_v0.2_run1.json` |
| Ecommerce catalog | `assignment8_contrast_2_v0.2_prompt.txt` | `assignment8_contrast_2_v0.2_run1.json` |

From the repository root, rebuild a packet or validate a preserved response with the scaffold:

```sh
python3 tools/check_frozen_core.py
python3 tools/build_prompt.py --agent agents/landscape_agent --case agents/landscape_agent/cases/primary.json --out /tmp/assignment8_primary_v0.2_prompt.txt
python3 tools/validate_response.py agents/landscape_agent/responses/assignment8_primary_v0.2_run1.json
```

## Integration

Provide the frozen context intake and consume the frozen JSON output. Keep the general, application, and organizational findings separate. Preserve source dates, verification status, monitoring triggers, and abstention conditions in any team synthesis. The specialist informs a management decision, with release, procurement, and legal determinations reserved for accountable owners.
