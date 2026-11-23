# MASY1-GC 1800 Common Emerging Technology Agent Scaffold v1.0

This is the **frozen course baseline** distributed through Brightspace for Emerging Technologies Assignments 2-8.

## What this scaffold does

It gives every specialist agent the same:
- contextual intake;
- three-level analytical rule: **ET generally -> ET for the application -> ET for that application in the organization**;
- structured output contract;
- prompt-building workflow;
- response-validation workflow.

Students specialize the files under `agents/<agent-name>/`. Files under `core/` are FROZEN CORE.

## Reference course workflow

1. Keep the original Brightspace ZIP unchanged.
2. Unzip a working copy and place it in your own GitHub repository.
3. Use ChatGPT + Codex with the weekly assignment memo to create a specialist from `agents/_template/`.
4. Run `python tools/build_prompt.py ...` to create a ChatGPT-ready prompt packet.
5. Submit that packet to ChatGPT.
6. Save ChatGPT's JSON response and run `python tools/validate_response.py ...`.
7. Test contrasting contexts, revise the specialist logic, and commit the final version.

**No OpenAI API key is required by this scaffold.** It does not call the OpenAI API. ChatGPT is the interactive model runtime; the Python tools are local prompt/validation utilities.

Start with `START_HERE.md` and the Student Operating Guide in `docs/`.


## Assignment 8 technical Agent package

The Emerging Technology Landscape Agent is version **v0.2**. Repository branch: `assignment8-landscape`. Tested v0.2 prompt commit: `80d9f753652b451cbfaa8f0e10094f18aea67f39`. Archived test evidence and source review commit: `0369014c62f0a5e87c9e88d125987959e04cd887`.

See the [specialist README](agents/landscape_agent/README.md) and [internal Agent Record](agents/landscape_agent/records/agent_record.md) for reproduction steps, verified findings, and source limitations. The package includes the v0.1 and v0.2 test rounds.
