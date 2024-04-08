'''
Author: Valentin
'''

import os
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_command

# cf = "/Volumes/t7-2tb-blue/files/_drive_dropbox_files/Dropbox/develop/net_auto/_config.yaml"
# nr = InitNornir(config_file=cf)
nr = InitNornir(config_file="_config.yaml")

nr.inventory.defaults.username = os.getenv("NORNIR_USERNAME")
nr.inventory.defaults.password = os.getenv("NORNIR_PASSWORD")

def pull_info(task):
    result = task.run(task=send_command, command="show ip ospf nei")
    task.host['facts'] = result.scrapli_response.genie_parse_output()
    interfaces = task.host['facts']['interfaces']
    for int in interfaces:
        neighbors = interfaces[int]["neighbors"]
        for neighbor in neighbors:
            state = neighbors[neighbor]['state']
            return state


state_result = nr.run(task=pull_info)
for host in nr.inventory.hosts.values():
    # print(host)
    state = state_result[f"{host}"][0].result
    # print(state)
    assert "FULL" in state, 'Failed'
print("PASSED")