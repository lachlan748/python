#!/usr/bin/env python
from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException, NetMikoTimeoutException
from jinja2 import Environment, PackageLoader, FileSystemLoader
from copy import copy
from pprint import pprint
from datetime import datetime
import getpass
import shutil
import os
import re
import concurrent.futures

# Get login credentials
username = input("Username: ") 
password = getpass.getpass(prompt = "Password: ")

# Read the ansible inventory and decode host info using regex:
def process_hosts():
    """ create a top level empty dict which we'll use to populate with inventory data """
    master = {}
    with open('./hosts.yml') as f:
        # read the entire file as a string
        contents = f.read()
        # perform a regex match to grab host info
        match = re.findall(r'(\S+):\n\s+ansible_host:\s(\S+)\n\s+ansible_network_os:\s(\S+)', contents, re.DOTALL)
        # findall returns a list, process each item in the list
        for line in match:
            # create a dict per line (host)
            data = {}
            # grab name, ip, os from items in the line
            node_name = line[0]
            node_os = line[2]
            # clean node_os
            if node_os == 'eos':
                node_os = 'arista_eos'
            elif node_os == 'ios':
                node_os = 'cisco_ios'
            # populate data dict with details required by netmiko
            data['ip'] = line[1]
            data['device_type'] = node_os
            data['port'] = '22'
            data['username'] = username
            data['password'] = password
            data['secret'] = password
            master[node_name] = data
    return master


def show_command(device_data):
    """ Execute show version command using Netmiko. """
    try:
        netconnect = ConnectHandler(**device_data)
        netconnect.enable()
        # define an empty dictionary which will store the output for each 'show' command, per device
        data = {}
        commands = ["show version",
                    "show ip route"]
        # connect to each device and run each 'show' command
        for command in commands:
            data[command] = netconnect.send_command(command)
        # copy the populated 'data' dictionary into the master dicionary
            device_data.setdefault('outputs', data)
    except NetMikoAuthenticationException:
        print("\n" + f"{device} SSH login failed, authentication error.")
    except NetMikoTimeoutException:
        print("\n" + f"{device} SSH login failed due to timeout.")
    except Exception as exc:
        print("\n" + f"{device} Some other exception: { exc }")


def main(master):
    start_time = datetime.now()
    with concurrent.futures.ThreadPoolExecutor(15) as executor:
        futures = {}
        for device, device_data in master.items():
            print(f"Gathering data from {device}..." + "\n")
            futures[executor.submit(show_command, device_data)] = device

    print("\nElapsed time: " + str(datetime.now() - start_time))



def clean_data(master):
    for device, device_data in master.items():
        # remove  details from master dict
        del device_data['password']
        del device_data['username']
    return master


def write_to_file(master):
    # load template file to parse data
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
    for device, device_data in master.items():
        if 'outputs' in device_data:
            os.mkdir(device)
            for command, output in device_data['outputs'].items():
                # when creating filenames based on command, swap 'spaces' with 'underscores':
                command = re.sub(r"\s", r"_", command)
                open(f"{device}/{command}.txt", 'a').write(
                    output_template.render(node=device, data=output))
    print("\n" + f"Job complete. If data gathering was successful, see 'outputs' directory for relevant data.")
    return master


if __name__ == "__main__":
    data = process_hosts()
    main(data)
    clean_data(data)
    write_to_file(data)
