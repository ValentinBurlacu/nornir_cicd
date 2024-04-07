from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result
from nornir.core.exceptions import NornirExecutionError

cf = "/Volumes/t7-2tb-blue/files/_drive_dropbox_files/Dropbox/develop/net_auto/_config.yaml"
nr = InitNornir(config_file=cf)

def random_config(task):
    task.run(task=send_configs_from_file, file="config.txt")

results = nr.run(task=random_config)
print_result(results)

failures = nr.data.failed_hosts
if failures:
    # print("FAILURE")
    raise NornirExecutionError("Nornit Failure Detected")
