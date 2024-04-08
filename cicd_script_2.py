'''
Author: Valentin
'''

import os
import sys
from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result
from nornir.core.exceptions import NornirExecutionError

# cf = "/Volumes/t7-2tb-blue/files/_drive_dropbox_files/Dropbox/develop/net_auto/_config.yaml"
# nr = InitNornir(config_file=cf)
# nr = InitNornir(config_file="_config.yaml")

config_file=sys.argv[1]
nr = InitNornir(config_file=config_file)

nr.inventory.defaults.username = os.getenv("NORNIR_USERNAME")
nr.inventory.defaults.password = os.getenv("NORNIR_PASSWORD")


def random_config(task):
    task.run(task=send_configs_from_file, file="config.txt")

results = nr.run(task=random_config)
print_result(results)

failures = nr.data.failed_hosts
if failures:
    # print("FAILURE")
    raise NornirExecutionError("Nornit Failure Detected")
