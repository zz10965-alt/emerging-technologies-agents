"""Verify all six genuine outputs, final packet reproduction and frozen/prior-work preservation."""
from pathlib import Path
from zipfile import ZipFile
import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from jsonschema import Draft202012Validator

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--portable',action='store_true')
args=parser.parse_args()
A=Path(__file__).resolve().parents[1]; R=A.parents[1]
def load(p): return json.loads(p.read_text())
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
subprocess.run([sys.executable,str(R/'tools/check_frozen_core.py')],check=True)
with ZipFile(next((A/'sources').glob('MASY1800*.zip'))) as z:
    prefix='MASY1800_ET_Agent_Scaffold_v1_0/'
    assert z.read(prefix+'FROZEN_CORE_SHA256.txt')==(R/'FROZEN_CORE_SHA256.txt').read_bytes()
    for line in (R/'FROZEN_CORE_SHA256.txt').read_text().splitlines():
        expected, name=line.split('  ',1)
        assert digest(R/name)==expected
        assert z.read(prefix+name)==(R/name).read_bytes()
    for p in (R/'agents/_template').rglob('*'):
        if p.is_file(): assert z.read(prefix+p.relative_to(R).as_posix())==p.read_bytes()
for n,h in load(A/'records/source_manifest.json').items():assert digest(A/'sources'/n)==h
missing=0
for n,h in load(A/'records/prior_work_sha256.json').items():
    p=R/n
    if not p.exists() and args.portable: missing+=1;continue
    assert digest(p)==h,n
print('PASS: frozen/template/source bytes; prior assignment preservation; portable omissions:',missing)
receipt=load(A/'records/v0.1_archive_receipt.json')
assert digest(A/'sources'/receipt['file'])==receipt['sha256']
with ZipFile(A/'sources/Assignment7_v0.1_original_test_responses.zip') as z:
    assert z.testzip() is None
    for n,m in load(A/'records/v0.1_response_manifest.json').items():
        p=A/'responses'/n
        assert z.read(m['archive_member'])==p.read_bytes()
        assert digest(p)==m['sha256']
print('PASS: all 3 original v0.1 response files byte-identical to uploaded archive')
schema=Draft202012Validator(load(R/'core/output_schema.json'))
metadata=load(A/'agent_metadata.json')
case_validator=Draft202012Validator(load(R/'core/input_schema.json'))
cases={n:load(A/'cases'/f'{n}.json') for n in ['primary','contrast_1','contrast_2']}
for n,c in cases.items():
    case_validator.validate(c)
    p=A/'responses'/f'{n}_v0.1_run1.json'
    subprocess.run([sys.executable,str(R/'tools/validate_response.py'),str(p)],check=True)
    data=load(p);schema.validate(data);assert data['agent']==metadata
print('PASS: all 3 actual v0.1 outputs official validator/full schema/historical metadata')
base=cases['primary']
for c in cases.values():
    for k in base:
        if k not in ['organization','capabilities_constraints','additional_context']:assert c[k]==base[k],k
    assert c['additional_context'].split('\nCase ID:')[0]==base['additional_context'].split('\nCase ID:')[0]
old_instructions=(A/'revisions/specialist_instructions_v0.1.md').read_text()
new_instructions=(A/'specialist_instructions.md').read_text()
assert new_instructions==(A/'revisions/specialist_instructions_v0.2.md').read_text()
assert old_instructions!=new_instructions
with tempfile.TemporaryDirectory(prefix='a7-review-') as temp:
    for n,c in cases.items():
        old=A/'prompts'/f'{n}_v0.1_prompt.txt'
        assert digest(old)==load(A/'records/packet_manifest.json')[old.name]['sha256']
        text=old.read_text()
        assert old_instructions in text
        assert json.dumps(c,indent=2) in text
        assert json.dumps(metadata,indent=2) in text
        new=A/'prompts'/f'{n}_v0.2_prompt.txt'
        assert digest(new)==load(A/'records/v0.2_packet_manifest.json')[new.name]['sha256']
        generated=Path(temp)/f'{n}.txt'
        subprocess.run([sys.executable,str(R/'tools/build_prompt.py'),'--agent',str(A),'--case',str(A/'cases'/f'{n}.json'),'--out',str(generated)],check=True,capture_output=True)
        assert generated.read_bytes()==new.read_bytes()
        assert new_instructions in new.read_text()
print('PASS: cases/shared evidence unchanged; v0.1 packets/snapshot preserved; v0.2 exact rebuilds')
receipt=load(A/'records/v0.2_archive_receipt.json')
assert digest(A/'sources'/receipt['file'])==receipt['sha256']
expected=metadata | {'version':'0.2-context-sequencing'}
with ZipFile(A/'sources'/receipt['file']) as z:
    assert z.testzip() is None
    for n,m in load(A/'records/v0.2_response_manifest.json').items():
        p=A/'responses'/n
        assert z.read(m['archive_member'])==p.read_bytes()
        assert digest(p)==m['sha256']
        subprocess.run([sys.executable,str(R/'tools/validate_response.py'),str(p)],check=True)
        data=load(p);schema.validate(data);assert data['agent']==expected
assert len(list((A/'responses').glob('*_run1.json')))==6
print('PASS: all 3 v0.2 originals byte-identical to uploaded archive; official/full schema/effective version')
print('FINAL CHECKS PASSED: 6 genuine outputs validated; frozen/prior work unchanged; both packet versions preserved')
print('Analytical improvement is assessed separately in records/v0.2_before_after_review.md, not inferred from schema validity')
