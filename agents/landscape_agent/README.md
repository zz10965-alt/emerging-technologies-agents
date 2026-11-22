# Emerging Technology Landscape Agent

Assignment 8, v0.1, prepared on 2026-11-22. This specialist compares Generative AI, incumbent workflows, and complementary tools to identify which external changes could alter an organization's decision.

## Run the fresh tests

Start a separate ChatGPT conversation for each packet. Use the same model and source-access settings where possible. Submit the entire packet and save the original JSON response without edits. Record the run date, displayed model, and whether original-source browsing was available separately from the raw response.

| Case | Packet in `prompts/` | Return filename for `responses/` |
| --- | --- | --- |
| Cross-border consulting | `assignment8_primary_v0.1_prompt.txt` | `assignment8_primary_v0.1_run1.json` |
| Hospital communications | `assignment8_contrast_1_v0.1_prompt.txt` | `assignment8_contrast_1_v0.1_run1.json` |
| Ecommerce catalog | `assignment8_contrast_2_v0.1_prompt.txt` | `assignment8_contrast_2_v0.1_run1.json` |

If ChatGPT returns non-JSON text, preserve it verbatim and flag it separately. Keep original results if a rerun is needed.

From the repository root, rebuild a packet or validate a returned response with the scaffold:

```sh
python3 tools/check_frozen_core.py
python3 tools/build_prompt.py --agent agents/landscape_agent --case agents/landscape_agent/cases/primary.json --out /tmp/assignment8_primary_v0.1_prompt.txt
python3 tools/validate_response.py agents/landscape_agent/responses/assignment8_primary_v0.1_run1.json
```

## Integration

Provide the frozen context intake and consume the frozen JSON output. Keep the general, application, and organizational findings separate. Preserve source dates, verification status, monitoring triggers, and abstention conditions in any team synthesis. The specialist informs a management decision, with release, procurement, and legal determinations reserved for accountable owners.
