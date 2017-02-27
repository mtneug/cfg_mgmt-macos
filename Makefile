all: help

help:
	@echo "all      Default target, which runs help"
	@echo "help     Prints this message"
	@echo "install  Executes the Ansible playbook"
	@echo "check    Checks the Ansible playbooks for errors"

install:
	@ansible-playbook -i hosts -K site.yml

check:
	@ansible-playbook -i hosts --syntax-check site.yml
