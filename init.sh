#!/bin/bash

# assumptions
echo "==> Assumptions"
echo "* Xcode is installed and opend at least once"
echo "* SSH key was created and added to GitHub"
read

# install homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew tap homebrew/dupes

# install Ansible
brew install python --universal
brew install ansible

# clone Ansible repo
git clone https://github.com/mtneug/cfg_mgmt-macos.git ~/projects/src/github.com/mtneug/cfg_mgmt-macos
echo "To run the playbook execute the following commands:"
echo "   cd ~/projects/src/github.com/mtneug/cfg_mgmt-macos && make install"
