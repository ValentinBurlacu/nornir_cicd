# import sys
# import os
from nornir import InitNornir
from nornir_scrapli.tasks import get_prompt,send_command, send_commands, send_commands_from_file, send_config, send_configs, send_configs_from_file
from nornir_scrapli.functions import print_structured_result
from nornir_utils.plugins.functions import print_result
from nornir.core.exceptions import NornirExecutionError
import getpass
import ipdb # is a python debugger
from rich import print as rprint
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="napalm")

nr = InitNornir(config_file="/home/val/cicd/_config.yaml")

# username = getpass.getpass(prompt="Username: ")
# north_password = getpass.getpass(prompt="North Group password: ")
# south_password = getpass.getpass(prompt="South Group password: ")
# south7_password = getpass.getpass(prompt="North South7 password: ")
# nr.inventory.defaults.username = username
# nr.inventory.defaults.password = password
# nr.inventory.defaults.username = sys.argv[2]    # python 02_scrapli.py val
# nr.inventory.defaults.username = os.environ["NORNIR_USERNAME"]
# nr.inventory.defaults.password = os.environ["NORNIR_PASSWORD"]
# nr.inventory.defaults.username = os.environ["DEFAULT_USERNAME"]
# nr.inventory.defaults.password = os.environ["DEFAULT_PASSWORD"]
# nr.inventory.groups["north"].password = north_password
# nr.inventory.groups["south"].password = south_password
# nr.inventory.groups["south7"].password = south7_password
# nr.inventory.hosts["vios4"].password = 

# command_list = ["show ip int bri | i 192.168", "show version | i Software"] # , "show run | i ntp"

# def show_command_test(task):
    # task.run(task=send_command, command="show ip int bri | i 192.168")
    # task.run(task=send_commands, commands=command_list)
    # for cmd in command_list:
    #     task.run(task=send_command, command=cmd)
    # task.run(task=get_prompt)
    # task.run(task=send_commands_from_file, file="commands1.txt")
            #  file=f"{nornir_dir}/cbt_nuggets_adv_net_auto_062025/commands1.txt")

def send_config_test(task):
    # task.run(task=send_config, config="ntp server 1.1.1.20")
    # task.run(task=send_configs, configs=["ntp server 1.1.1.3", "ntp server 1.1.1.4"])
    task.run(task=send_configs_from_file, file="configs.txt", dry_run=False)

# def pull_structured_data(task):
#     version_result = task.run(task=send_command, command="show version") # this gives us unstructured data
    # version_result = task.run(task=send_command, command="show ip interface")
    # version_result = task.run(task=send_command, command="show cdp nei")
    # task.host["facts"] = version_result.scrapli_response.genie_parse_output()                             # genie parser
    # structured_output = clock_result.scrapli_response.textfsm_parse_output()                                # textfsm parser
    # print(structured_output)
    # neighbors = task.host["facts"]["vrf"]["default"]["address_family"][""]["routes"]
    # interfaces = task.host["facts"]["interfaces"]
    # print(task.host["facts"])
    # uptime = task.host["facts"]["version"]["uptime"]
    # rprint(f"Device {task.host} has {uptime} uptime")
    # rprint(f"{task.host}: {neighbors}")
    # rprint(f"{task.host}: {interfaces}")
    # for key in interfaces:
    #     neighors = interfaces[key]["neighbors"]
    #     print(f"{task.host}, {key}, {state}")
    # cdp_index = task.host["facts"]["cdp"]["index"]
    # for num in cdp_index:
    #     local_interface = cdp_index[num]["local_interface"]
    #     remote_device = cdp_index[num]["device_id"]
    #     remote_port = cdp_index[num]["port_id"]
    #     # rprint(f"Host {task.host} via interface {local_interface} is conncted to {remote_device} port {remote_port}")
    #     config_commands = [f"interface {local_interface}", f"description Connected to {remote_device} via its {remote_port}"]
    #     task.run(task=send_configs, configs = config_commands)

    # clock_result = task.run(task=send_command, command = "show version")
    # structured_output = clock_result.scrapli_response.textfsm_parse_output()
    # print(structured_output)

    # mcast_groups = task.host['facts']['GigabitEthernet0/0']['multicast_groups']
    # for mcast_ip in mcast_groups:
    #     print(f"{task.host}, {mcast_ip}")

    # uptime = task.host["facts"]["version"]["uptime"]
    # version_number = task.host["facts"]["version"]["version"]
    # if version_number == "15.5(3)M":
    #     rprint(f"{task.host} [green]version has passed[/green]")
    # else:
    #     rprint(f"{task.host} [red]version has failed[/red]")
    # rprint(f"{task.host} has an uptime of {uptime} and has verion {version_number}")
    # print(task.host["facts"]["version"]["hostname"])

# results = nr.run(task=show_command_test)
# results = nr.run(task=show_command_test)
results = nr.run(task=send_config_test)
print_result(results)
# print_structured_result(results, parser="genie")
# print_structured_result(results, parser="textfsm")
# ipdb.set_trace() #nr.inventory.hosts["R1"]["facts"]

failures = nr.data.failed_hosts
if failures:
    # print("Failure")
    raise NornirExecutionError("Nornir Failure Detected")