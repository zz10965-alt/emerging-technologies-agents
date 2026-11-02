#!/usr/bin/env python3
"""Validate five preserved actual outputs and the exact mixed-version test lineage."""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile

AGENT = Path(__file__).resolve().parents[1]
ROOT = AGENT.parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main(full_repository=False):
    command = [sys.executable, str(AGENT/'tests/check_development.py'), '--responses']
    if full_repository:
        command.append('--full-repository')
    subprocess.run(command, cwd=ROOT, check=True)
    spec = importlib.util.spec_from_file_location('existing_contract_checks', AGENT/'tests/check_development.py')
    contract = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(contract)
    schema = json.loads((ROOT/'core/output_schema.json').read_text())
    manifest = json.loads((AGENT/'records/all_five_outputs_manifest.json').read_text())
    expected = {item['filename'] for item in manifest['outputs']}
    contract.require(len(expected) == 5, 'Exactly five actual outputs required')
    contract.require({p.name for p in (AGENT/'responses').glob('*.json')} == expected, 'Unexpected/missing response or fabricated Startup v0.3 file')
    for item in manifest['outputs']:
        path = AGENT/item['path']
        contract.require(digest(path) == item['sha256'], f"Preserved output changed: {item['filename']}")
        subprocess.run([sys.executable, str(ROOT/'tools/validate_response.py'), str(path)], cwd=ROOT, check=True)
        data = json.loads(path.read_bytes())
        contract.validate(data, schema)
        metadata_path = AGENT/('revisions/v0.3/agent_metadata.json' if item['version'] == '0.3-provenance-fix' else 'agent_metadata.json')
        metadata = json.loads(metadata_path.read_text())
        contract.require(all(data['agent'][k] == metadata[k] for k in ['name','specialty','version']), 'Response/authoring version mismatch')
    for row in json.loads((AGENT/'records/response_preservation_v0.2.json').read_text()):
        contract.require(digest(ROOT/row['saved_path']) == row['sha256'], 'Original v0.2 upload changed')
    for row in json.loads((AGENT/'records/validation_results_v0.3_run1.json').read_text())['new_actual_retests']:
        contract.require(digest(ROOT/row['saved_path']) == row['sha256'], 'Original v0.3 upload changed')
    retests = json.loads((AGENT/'revisions/v0.3/retest_manifest.json').read_text())
    with tempfile.TemporaryDirectory(prefix='diffusion-final-', dir='/tmp') as directory:
        for item in retests['affected_cases']:
            case = AGENT/item['case_path']
            packet = AGENT/item['packet_path']
            contract.require(digest(packet) == item['packet_sha256'], 'Original v0.3 packet changed')
            contract.require(case.read_bytes() == (AGENT/f"cases/{item['case']}.json").read_bytes(), 'Case changed across targeted revision')
            out = Path(directory)/packet.name
            subprocess.run([sys.executable, str(ROOT/'tools/build_prompt.py'), '--agent', str(AGENT/'revisions/v0.3'), '--case', str(case), '--out', str(out)], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
            contract.require(out.read_bytes() == packet.read_bytes(), 'v0.3 packet no longer reproduces')
    release = json.loads((AGENT/'release_manifest.json').read_text())
    contract.require(release['actual_test_totals'] == {'v0.2_originals':3,'v0.3_targeted_retests':2,'total':5,'startup_v0.3':0}, 'Misstated test lineage')
    contract.require(release['selected_case_results']['contrast_1']['version'] == '0.2-test-ready', 'Startup mislabeled v0.3')
    contract.require(release['planning_horizon_months'] == 6 and digest(AGENT/'evidence/shared_snapshot.md') == release['shared_evidence_sha256'], 'Horizon/evidence drift')
    print('FINAL CHECK PASS: five exact actual outputs; 3 original v0.2 + 2 targeted v0.3; Startup v0.2 preserved; no Startup v0.3 file.')
    print('Frozen core, source hashes, version-specific packets, six-month assumption and schema checks: PASS.')
    print('Analytical conclusions are documented manual review of these outputs, not proof of repeatability.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full-repository', action='store_true')
    args = parser.parse_args()
    try:
        main(args.full_repository)
    except (ValueError, OSError, json.JSONDecodeError, subprocess.CalledProcessError) as error:
        print('FINAL CHECK FAILED:', error, file=sys.stderr)
        sys.exit(1)
