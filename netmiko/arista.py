from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException, NetMikoTimeoutException
from jinja2 import Environment, PackageLoader, FileSystemLoader
from pprint import pprint
import getpass
import shutil
import os
import re

# Get login credentials
username = input("Enter TACACS username: ") 
password = getpass.getpass(prompt = "Enter TACACS password: ")

# Define inventory
inventory = {}
inventory['R01'] = {
             "ip": "192.168.137.231",
             "port": 22,
             "username": username,
             "password": password,
             "device_type": "arista_eos"
          }

inventory['R02'] = {
             "ip": "192.168.137.232",
             "port": 22,
             "username": username,
             "password": password,
             "device_type": "arista_eos"
          }


def run_commands():
    """ Send show commands """
    for node, node_data in inventory.items():
        try:
            netconnect = ConnectHandler(**node_data)
            netconnect.enable()
            # define an empty dictionary which will store the output for each 'show' command, per node
            data = {}
            commands = ["show version",
                        "show ip route",
                        "show ip bgp summary"]
            # connect to each node and run each 'show' command
            for command in commands:
                data[command] = netconnect.send_command(command)
            # copy the populated 'data' dictionary into the inventory dicionary
            node_data.setdefault('outputs', data)
            netconnect.disconnect()
        except NetMikoAuthenticationException:
            print("\n" + f"{node} SSH login failed, authentication error.")
        except NetMikoTimeoutException:
            print("\n" + f"{node} SSH login failed due to timeout.")
        except Exception as exc:
            print("\n" + f"{node} Some other exception: { exc }")
    return inventory


def write_to_file(inventory):
    """ Load template file to parse output """
    env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)
    output_template = env.get_template('output.j2')
    # create and clean an 'outputs' folder
    path = "./outputs"
    try:
        shutil.rmtree(path, ignore_errors = True, onerror = None)
    except:
        print('Error while deleting directory')
    os.mkdir(path)
    os.chdir(path)
    for node, node_data in inventory.items():
        if 'outputs' in node_data:
            os.mkdir(node)
            for command, output in node_data['outputs'].items():
                # when creating filenames based on command, swap 'spaces' with 'underscores':
                command = re.sub(r"\s", r"_", command)
                open(f"{node}/{command}.txt", 'a').write(
                    output_template.render(node=node, data=output))
    print("\n" + f"Job complete. If data gathering was successful, see 'outputs' directory.")
    return inventory
        

if __name__ == "__main__":
    data = run_commands()
    write_to_file(inventory)
