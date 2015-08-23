#!/usr/bin/python
#
# (c) 2015, Matthias Neugebauer

DOCUMENTATION = '''
---
module: apm
short_description: Manage Atom packages with apm
description:
  - Manage Atom packages with Atom Package Manager (apm)
author: Matthias Neugebauer
options:
  name:
    description:
      - The name of a Atom library to install
    required: yes
'''

EXAMPLES = '''
description: Install "minimap" Atom package.
- apm: name=minimap
'''

import re

class Apm(object):
    def __init__(self, module, **kwargs):
        self.module     = module
        self.name       = kwargs['name']
        self.executable = [module.get_bin_path('apm', True)]

    def _exec(self, args, run_in_check_mode=False, check_rc=True):
        if not self.module.check_mode or (self.module.check_mode and run_in_check_mode):
            cmd = self.executable + args + [self.name]
            rc, out, err = self.module.run_command(cmd, check_rc=check_rc, cwd=None)

            return out
        return ''

    def is_installed(self):
        cmd  = ['list', '--bare', '--installed']
        data = self._exec(cmd, True, False)

        return re.search('^' + self.name + '@', data, re.MULTILINE)

    def install(self):
        return self._exec(['install'])

def main():
    module = AnsibleModule(
        argument_spec = dict(
            name = dict(required=True)
        ),
        supports_check_mode=True
    )

    name = module.params['name']
    apm  = Apm(module, name=name)

    changed = False

    if not apm.is_installed():
        changed = True
        apm.install()

    module.exit_json(changed=changed)

from ansible.module_utils.basic import *
main()
