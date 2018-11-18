# My Ansible macOS Playbooks

[![Build Status](https://travis-ci.org/mtneug/cfg_mgmt-macos.svg?branch=master)](https://travis-ci.org/mtneug/cfg_mgmt-macos)

My personal macOS configuration. These playbooks contain some assumptions about my setup. **Run on your own risk.**

## 01. Init setup

```sh
$ bash -c "$(https://raw.githubusercontent.com/mtneug/cfg_mgmt-macos/master/init.sh)"
```

## 02. Run playbook

```sh
$ cd ~/projects/src/github.com/mtneug/cfg_mgmt-macos
$ make install
```
