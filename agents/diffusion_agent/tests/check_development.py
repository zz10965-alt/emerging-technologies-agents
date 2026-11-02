#!/usr/bin/env python3
"""Structural preparation checks; no model execution or semantic pass claim."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from zipfile import ZipFile

AGENT = Path(__file__).resolve().parents[1]
ROOT = AGENT.parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(data, schema, path='$'):
    """Enforce the types/required/properties/items used by this frozen schema."""
    kind = schema.get('type')
    types = {'object': dict, 'array': list, 'string': str}
    require(kind in types, f'{path}: unsupported schema type {kind}')
    require(isinstance(data, types[kind]), f'{path}: expected {kind}')
    if kind == 'object':
        require(set(schema.get('required', [])) <= data.keys(), f'{path}: missing required keys')
        properties = schema.get('properties', {})
        if schema.get('additionalProperties') is False:
            require(data.keys() <= properties.keys(), f'{path}: extra properties')
        for name, item in data.items():
            if name in properties:
                validate(item, properties[name], f'{path}.{name}')
    elif kind == 'array':
        for index, item in enumerate(data):
            validate(item, schema['items'], f'{path}[{index}]')


def run(full_repository=False, responses=False):
    checks = []
    subprocess.run([sys.executable, str(ROOT/'tools/check_frozen_core.py')], cwd=ROOT, check=True)
    checks.append('Frozen core manifest: PASS')
    if full_repository:
        baseline = json.loads((AGENT/'records/predevelopment_sha256.json').read_text())
        for relative, expected in baseline.items():
            path = ROOT/relative
            require(path.is_file() and digest(path) == expected, f'Original file changed/missing: {relative}')
        checks.append(f'All {len(baseline)} original repository files unchanged: PASS')
    else:
        checks.append('Full original repository comparison: NOT REQUESTED (use --full-repository in original checkout)')
    baseline = json.loads((AGENT/'baselines/v0.1_files_sha256.json').read_text())
    with ZipFile(AGENT/'baselines/v0.1_complete_candidate.zip') as archive:
        require(archive.testzip() is None, 'v0.1 baseline ZIP corrupt')
        expected_paths = {'diffusion_agent/' + relative for relative in baseline}
        require(set(archive.namelist()) == expected_paths, 'Incomplete v0.1 baseline membership')
        for relative, expected in baseline.items():
            actual = hashlib.sha256(archive.read('diffusion_agent/' + relative)).hexdigest()
            require(actual == expected, f'v0.1 baseline file changed: {relative}')
            if relative.startswith('prompts/'):
                require(digest(AGENT/relative) == expected, f'Original live packet changed: {relative}')
    checks.append(f'Entire v0.1 baseline ({len(baseline)} files) and original live packets: PASS')
    input_schema = json.loads((ROOT/'core/input_schema.json').read_text())
    output_schema = json.loads((ROOT/'core/output_schema.json').read_text())
    metadata = json.loads((AGENT/'agent_metadata.json').read_text())
    snapshot = (AGENT/'evidence/shared_snapshot.md').read_text().rstrip('\n')
    packet_manifest = json.loads((AGENT/'records/packet_manifest.json').read_text())
    case_data = []
    with tempfile.TemporaryDirectory(prefix='diffusion-check-', dir='/tmp') as temporary:
        for item in packet_manifest:
            slug = item['case']
            case = json.loads((AGENT/f'cases/{slug}.json').read_text())
            validate(case, input_schema)
            require(snapshot in case['additional_context'], f'{slug}: incomplete shared evidence')
            packet_path = AGENT/item['path']
            require(digest(packet_path) == item['sha256'], f'{slug}: packet hash changed')
            require(packet_path.stat().st_size == item['bytes'], f'{slug}: packet size changed')
            require(digest(AGENT/'evidence/shared_snapshot.md') == item['evidence_snapshot_sha256'], f'{slug}: evidence version mismatch')
            regenerated = Path(temporary)/f'{slug}.txt'
            subprocess.run([sys.executable, str(ROOT/'tools/build_prompt.py'), '--agent', str(AGENT), '--case', str(AGENT/f'cases/{slug}.json'), '--out', str(regenerated)], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
            require(regenerated.read_bytes() == packet_path.read_bytes(), f'{slug}: packet differs from frozen builder')
            packet = packet_path.read_text()
            require('REPLACE' not in packet, f'{slug}: unresolved template text')
            require(json.dumps(case, indent=2) in packet, f'{slug}: incomplete case')
            require(json.dumps(output_schema, indent=2) in packet, f'{slug}: incomplete schema')
            require(json.dumps(metadata, indent=2) in packet, f'{slug}: incomplete metadata')
            require((ROOT/'core/common_instructions.md').read_text() in packet, f'{slug}: incomplete core instructions')
            require((AGENT/'specialist_instructions.md').read_text() in packet, f'{slug}: incomplete specialist')
            case_data.append(case)
            checks.append(f'{slug}: intake schema, complete standalone packet, original-builder byte match, manifest hashes: PASS')
    require(len(case_data) == 3, 'Expected exactly three cases')
    require(len({x['emerging_technology'] for x in case_data}) == 1, 'Technology drift')
    require(len({x['additional_context'] for x in case_data}) == 1, 'Shared evidence/assumption note drift')
    require(case_data[0]['intended_application'] == case_data[1]['intended_application'], 'Coding application drift')
    require('clinical documentation' in case_data[2]['intended_application'], 'Hospital application missing')
    checks.append('Three-case technology/evidence equality and intended application contrast: PASS')
    register = json.loads((AGENT/'evidence/source_register.json').read_text())
    for source in register['verified_original_artifacts']:
        path = AGENT/'evidence'/source['local_file']
        require(digest(path) == source['sha256'], f"Source {source['id']}: archived bytes changed")
        require(source['commit'] in source['immutable_url'], f"Source {source['id']}: missing immutable URL")
    checks.append('Preserved original product-source hashes and immutable references: PASS')
    for artifact in register['archived_artifacts']:
        require(digest(AGENT/'evidence'/artifact['local_file']) == artifact['sha256'], f"Empirical artifact changed: {artifact['local_file']}")
        if not artifact.get('derivative'):
            require(artifact['commit'] in artifact['url'], f"Unpinned original: {artifact['local_file']}")
    required_source_fields = ['publication_date', 'observation_period', 'population', 'scope', 'methodology', 'claims', 'limitations', 'primary_artifacts', 'immutable_url']
    claim_ids = set()
    for source in register['empirical_sources']:
        require(all(source.get(key) for key in required_source_fields), f"Incomplete empirical metadata: {source['id']}")
        for relative in source['primary_artifacts']:
            require((AGENT/'evidence'/relative).is_file(), f'Missing source material: {relative}')
        for claim in source['claims']:
            require(claim['id'] not in claim_ids, f"Duplicate claim ID: {claim['id']}")
            claim_ids.add(claim['id'])
            require(all(claim.get(key) for key in ['exact_supported_claim','measure','denominator','locator','qualification']), f"Incomplete claim record: {claim['id']}")
            require(claim['id'] in snapshot, f"Claim not embedded in standalone evidence: {claim['id']}")
    # Inspectable exact original text supports the historical numeric claims.
    original_extract = (AGENT/'evidence/raw/E4_verified_pages_extracted.txt').read_text()
    require('75.9%' in original_extract and '74.9%' in original_extract, 'Historical numeric claim text missing')
    questions = json.loads((AGENT/'evidence/raw/E1_questions.json').read_text())
    question_text = json.dumps(questions)
    require('Do you currently use AI tools as part of your work?' in question_text, 'Current-use measure missing')
    require('In the last 3 months, when you encountered a problem' in question_text, 'Frequency reference period missing')
    require(metadata['version'] == '0.2-test-ready' and metadata['evidence_snapshot'] == register['snapshot_id'], 'Active version mismatch')
    require('working_branch' not in metadata, 'Ambiguous branch field retained')
    require(metadata['local_checkout_branch'] == 'work' and metadata['intended_repository_branch'] == 'assignment4-promethean', 'Branch identity conflation')
    checks.append(f"Empirical source metadata, {len(claim_ids)} claim mappings, {len(register['archived_artifacts'])} archived-artifact hashes, original question wording and numeric locators: PASS")
    checks.append('Explicit local-versus-intended branch provenance and v0.2 version consistency: PASS')
    if responses:
        for item in packet_manifest:
            path = AGENT/item['response_path']
            require(path.is_file(), f'Actual response missing: {path.name}')
            subprocess.run([sys.executable, str(ROOT/'tools/validate_response.py'), str(path)], cwd=ROOT, check=True)
            data = json.loads(path.read_text())
            validate(data, output_schema)
            for key in ['name', 'specialty', 'version']:
                require(data['agent'][key] == metadata[key], f'{path.name}: agent metadata mismatch')
        checks.append('Three actual output basic validators and strict frozen-schema shape checks: PASS; semantic review still required')
    else:
        checks.append('Actual model execution, output validation and semantic review: PENDING / NOT EXECUTED')
    return checks


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full-repository', action='store_true', help='Verify all 78 pre-existing checkout files against the development baseline')
    parser.add_argument('--responses', action='store_true', help='Require and structurally validate all three actual run1 outputs')
    args = parser.parse_args()
    try:
        for result in run(args.full_repository, args.responses):
            print(result)
    except (ValueError, OSError, json.JSONDecodeError, subprocess.CalledProcessError) as error:
        print(f'CHECK FAILED: {error}', file=sys.stderr)
        sys.exit(1)
