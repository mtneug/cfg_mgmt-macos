#!/usr/bin/python
#
# (c) 2015, Matthias Neugebauer

DOCUMENTATION = '''
---
module: vcsh
short_description: Manage dotfiles with vcsh
description:
  - Manage dotfiles with vcsh
author: Matthias Neugebauer
options:
  name:
    description:
      - The name of the dotfile repository
    required: yes
  remote:
    description:
      - The remote to clone from
    required: yes
'''

EXAMPLES = '''
description: Install "git" dotfiles
- vcsh: name=git remote=git@github.com:mtneug/dotfiles-git.git
'''

import os

class Vcsh(object):
    def __init__(self, module, **kwargs):
        self.module = module
        self.name   = kwargs['name']
        self.remote = kwargs['remote']

    def is_installed(self):
        return os.path.isdir(os.path.expanduser('~/.config/vcsh/repo.d/' + self.name + '.git'))

    def install(self):
        if not self.module.check_mode:
            cmd = [self.module.get_bin_path('vcsh', True), 'clone', self.remote, self.name]

            rc, out, err = self.module.run_command(cmd, check_rc=True, cwd=None)

            return out
        return ''

def main():
    module = AnsibleModule(
        argument_spec = dict(
            name   = dict(required=True),
            remote = dict(required=True)
        ),
        supports_check_mode = True
    )

    name   = module.params['name']
    remote = module.params['remote']
    vcsh   = Vcsh(module, name=name, remote=remote)

    changed = False

    if not vcsh.is_installed():
        changed = True
        vcsh.install()

    module.exit_json(changed=changed)

from ansible.module_utils.basic import *
main()
