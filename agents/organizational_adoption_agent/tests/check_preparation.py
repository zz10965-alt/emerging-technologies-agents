"""Preparation checks only: never represents a specialist model execution."""
from pathlib import Path
from zipfile import ZipFile
import hashlib
import json
import subprocess
import sys
import tempfile
from jsonschema import Draft202012Validator

A = Path(__file__).resolve().parents[1]
R = A.parents[1]
def read(path):
    return json.loads(path.read_text())
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

subprocess.run([sys.executable, str(R/'tools/check_frozen_core.py')], check=True)
with ZipFile(next((A/'sources').glob('*.zip'))) as archive:
    prefix = 'MASY1800_ET_Agent_Scaffold_v1_0/'
    manifest = archive.read(prefix+'FROZEN_CORE_SHA256.txt').decode()
    assert manifest == (R/'FROZEN_CORE_SHA256.txt').read_text()
    for line in manifest.splitlines():
        expected, name = line.split('  ', 1)
        assert digest(R/name) == expected
        assert archive.read(prefix+name) == (R/name).read_bytes(), name
    for path in (R/'agents/_template').rglob('*'):
        if path.is_file():
            assert archive.read(prefix+str(path.relative_to(R))) == path.read_bytes()
print('PASS: canonical frozen files and original template match uploaded ZIP byte-for-byte')
for name, expected in read(A/'records/source_manifest.json').items():
    assert digest(A/'sources'/name) == expected, name
for name, expected in read(A/'records/prior_work_sha256.json').items():
    assert digest(R/name) == expected, name
print('PASS: supplied sources and all pre-existing tracked files unchanged')
input_validator = Draft202012Validator(read(R/'core/input_schema.json'))
output_validator = Draft202012Validator(read(R/'core/output_schema.json'))
# Deliberate invalid fixture is confined to a temporary directory, never responses/.
assert not output_validator.is_valid({})
cases = {name: read(A/'cases'/f'{name}.json') for name in ['primary','contrast_1','contrast_2']}
for case in cases.values():
    input_validator.validate(case)
base = cases['primary']
for key in base:
    if key not in ['organization','capabilities_constraints','additional_context']:
        assert all(c[key] == base[key] for c in cases.values()), key
assert len({c['organization'] for c in cases.values()}) == 3
boundary = base['additional_context'].split('\nCase ID:')[0]
assert all(c['additional_context'].split('\nCase ID:')[0] == boundary for c in cases.values())
print('PASS: 3 full-schema-valid cases; technology/application/scope/evidence invariant; profiles differ')
manifest = read(A/'records/packet_manifest.json')
with tempfile.TemporaryDirectory(prefix='assignment7-check-') as temp:
    for name, case in cases.items():
        packet = A/'prompts'/f'{name}_v0.1_prompt.txt'
        assert digest(packet) == manifest[packet.name]['sha256']
        generated = Path(temp)/f'{name}.txt'
        subprocess.run([sys.executable,str(R/'tools/build_prompt.py'),'--agent',str(A),'--case',str(A/'cases'/f'{name}.json'),'--out',str(generated)],check=True,capture_output=True)
        assert packet.read_bytes() == generated.read_bytes(), name
        text = packet.read_text()
        assert (R/'core/common_instructions.md').read_text() in text
        assert (A/'specialist_instructions.md').read_text() in text
        assert json.dumps(case,indent=2) in text
        assert json.dumps(read(R/'core/output_schema.json'),indent=2) in text
    bad = Path(temp)/'deliberately_invalid.json'
    bad.write_text('{}')
    result = subprocess.run([sys.executable,str(R/'tools/validate_response.py'),str(bad)],capture_output=True,text=True)
    assert result.returncode == 1 and 'Missing required field' in result.stdout
assert (A/'specialist_instructions.md').read_bytes() == (A/'revisions/specialist_instructions_v0.1.md').read_bytes()
assert not list((A/'responses').glob('*.json')), 'New responses require actual execution review; this is the pre-execution baseline check.'
print('PASS: 3 packet hashes and exact rebuilds; instruction snapshot; invalid-fixture rejection')
print('PREPARATION VERIFIED; specialist ChatGPT executions: 0; output validation/revision: NOT RUN')
