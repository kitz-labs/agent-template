import json, tempfile, unittest
from pathlib import Path
from tools.validate_templates import validate_repository

class ValidatorTests(unittest.TestCase):
    def make_repo(self):
        root=Path(tempfile.mkdtemp())
        (root/'README.md').write_text('# fixture\n')
        (root/'VERSION').write_text('1.0.0\n')
        (root/'tools').mkdir(); (root/'tools'/'validate_templates.py').write_text('# fixture\n')
        (root/'tests').mkdir(); (root/'tests'/'test_validator.py').write_text('# fixture\n')
        (root/'00-core').mkdir()
        (root/'00-core'/'template.json').write_text(json.dumps({'id':'core','version':'1.0.0','status':'stable','risk':'low','owner':'platform','required_files':['template.json']}))
        (root/'TEMPLATE_REGISTRY.json').write_text(json.dumps({'schema_version':1,'templates':{'core':{'version':'1.0.0','status':'stable','path':'00-core','risk':'low','dependencies':[],'conflicts':[]}}}))
        return root
    def test_valid(self): self.assertTrue(validate_repository(self.make_repo()).ok)
    def test_missing_required_file(self):
        r=self.make_repo(); d=json.loads((r/'00-core'/'template.json').read_text()); d['required_files'].append('MISSING.md'); (r/'00-core'/'template.json').write_text(json.dumps(d)); self.assertFalse(validate_repository(r).ok)
    def test_cycle(self):
        r=self.make_repo(); reg=json.loads((r/'TEMPLATE_REGISTRY.json').read_text()); reg['templates'].update({'a':{'version':'1.0.0','status':'stable','path':'a','risk':'low','dependencies':['b'],'conflicts':[]},'b':{'version':'1.0.0','status':'stable','path':'b','risk':'low','dependencies':['a'],'conflicts':[]}})
        for n in ('a','b'):(r/n).mkdir(); (r/n/'template.json').write_text(json.dumps({'id':n,'version':'1.0.0','status':'stable','risk':'low','owner':'p','required_files':['template.json']}))
        (r/'TEMPLATE_REGISTRY.json').write_text(json.dumps(reg)); self.assertTrue(any('cycle' in e.lower() for e in validate_repository(r).errors))
    def test_unknown_dependency(self):
        r=self.make_repo(); reg=json.loads((r/'TEMPLATE_REGISTRY.json').read_text()); reg['templates']['core']['dependencies']=['ghost']; (r/'TEMPLATE_REGISTRY.json').write_text(json.dumps(reg)); self.assertTrue(any('unknown dependency' in e.lower() for e in validate_repository(r).errors))
    def test_conflict(self):
        r=self.make_repo(); reg=json.loads((r/'TEMPLATE_REGISTRY.json').read_text()); reg['templates']['a']={'version':'1.0.0','status':'stable','path':'a','risk':'low','dependencies':[],'conflicts':['core']}; (r/'a').mkdir(); (r/'a'/'template.json').write_text(json.dumps({'id':'a','version':'1.0.0','status':'stable','risk':'low','owner':'p','required_files':['template.json']})); (r/'TEMPLATE_REGISTRY.json').write_text(json.dumps(reg)); self.assertTrue(any('conflict' in e.lower() for e in validate_repository(r,['core','a']).errors))
    def test_secret(self):
        r=self.make_repo(); (r/'00-core'/'bad.env').write_text('OPENAI_API_KEY='+'sk-proj-'+'abcdefghijklmnopqrstuvwxyz123456'); self.assertTrue(any('secret' in e.lower() for e in validate_repository(r).errors))
    def test_semver(self):
        r=self.make_repo(); reg=json.loads((r/'TEMPLATE_REGISTRY.json').read_text()); reg['templates']['core']['version']='v1'; (r/'TEMPLATE_REGISTRY.json').write_text(json.dumps(reg)); self.assertTrue(any('semver' in e.lower() for e in validate_repository(r).errors))
    def test_production_dependencies(self):
        r=self.make_repo(); reg=json.loads((r/'TEMPLATE_REGISTRY.json').read_text()); reg['templates']['production-agent']={'version':'1.0.0','status':'stable','path':'prod','risk':'high','dependencies':[],'conflicts':[],'kind':'production-agent'}; (r/'prod').mkdir(); (r/'prod'/'template.json').write_text(json.dumps({'id':'production-agent','version':'1.0.0','status':'stable','risk':'high','owner':'p','required_files':['template.json']})); (r/'TEMPLATE_REGISTRY.json').write_text(json.dumps(reg)); errs=validate_repository(r).errors; self.assertTrue(any('security-baseline' in e for e in errs)); self.assertTrue(any('validator-tests' in e for e in errs))
    def test_control_file(self):
        r=self.make_repo(); (r/'README.md').unlink(); self.assertTrue(any('README.md' in e for e in validate_repository(r).errors))
    def test_security_invariants(self):
        r=self.make_repo(); reg=json.loads((r/'TEMPLATE_REGISTRY.json').read_text()); reg['templates']['security-baseline']={'version':'1.0.0','status':'stable','path':'sec','risk':'critical','dependencies':['core'],'conflicts':[],'kind':'security-baseline'}; (r/'sec').mkdir(); (r/'sec'/'template.json').write_text(json.dumps({'id':'security-baseline','version':'1.0.0','status':'stable','risk':'critical','owner':'s','required_files':['template.json','security-policy.json']})); (r/'sec'/'security-policy.json').write_text(json.dumps({'default_decision':'allow','deny_wins':False,'secrets_in_prompt_or_config':True,'risk_levels':['low','medium','high','critical'],'confirmation_required_for':[]})); (r/'TEMPLATE_REGISTRY.json').write_text(json.dumps(reg)); errs=validate_repository(r).errors; self.assertTrue(any('default_decision' in e for e in errs)); self.assertTrue(any('deny_wins' in e for e in errs)); self.assertTrue(any('secrets_in_prompt_or_config' in e for e in errs))

if __name__=='__main__': unittest.main()
