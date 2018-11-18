#!/bin/bash

set -e

# Xcode
echo "==> You will now recieve a prompt for installing Xcode"
echo "    After Xcode is installed and you opened it at least once press enter"
read

xcode-select --install

read

# add SSH key
echo "==> When creating the SSH key you will be prompted for a passphrase"
read

ssh-keygen -t rsa -b 8192 -f ~/.ssh/id_git -C "mtneug@mailbox.org"
cat <<EOF > ~/.ssh/config
Host *
 AddKeysToAgent yes
 UseKeychain yes
 IdentityFile ~/.ssh/id_git
EOF
ssh-add -K ~/.ssh/id_git
cat ~/.ssh/id_git.pub | pbcopy

echo "==> The new public key was placed into your clipboard"
echo "    After you added the new key in GitHub press enter"
read
open "https://github.com/settings/ssh/new"
read

# install homebrew
echo "==> Installing Homebrew"
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew tap homebrew/dupes

# install Ansible
echo "==> Installing Ansible"
brew install python --universal
brew install ansible

# clone Ansible repo
echo "==> Cloning repository"
git clone git@github.com:mtneug/cfg_mgmt-macos.git ~/projects/src/github.com/mtneug/cfg_mgmt-macos
echo "To run the playbook execute the following commands:"
echo "   cd ~/projects/src/github.com/mtneug/cfg_mgmt-macos && make install"
