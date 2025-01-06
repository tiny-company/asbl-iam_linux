import os
import pytest
import warnings

import testinfra.utils.ansible_runner

'''
python test with test infra (example below)
'''

# testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
#     os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

# warnings.filterwarnings("ignore", category=DeprecationWarning)


# def test_iptables_is_installed(host):
#     iptables = host.package("iptables")
#     assert iptables.is_installed


# def test_iptables_running_and_enabled(host):
#     iptables = host.service("iptables")
#     assert iptables.is_running
#     assert iptables.is_enabled


