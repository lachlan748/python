import getpass
import os
import shutil
from pexpect import pxssh

devices = {'R01': {'prompt': 'R01#', 'ip': '10.1.1.1'},
           'R02': {'prompt': 'R02#', 'ip': '10.1.1.2'},
           'R03': {'prompt': 'R03#', 'ip': '10.1.1.3'},
           'R04': {'prompt': 'R04#', 'ip': '10.1.1.4'},
           'R05': {'prompt': 'R05#', 'ip': '10.1.1.5'}}

commands = ['term length 0', 'show version', 'show ip route']

username = input('Username: ')
password = getpass.getpass('Password: ')

def cleanup():
    """ Create and clean an 'outputs' folder """
    path = "./outputs"
    try:
        shutil.rmtree(path, ignore_errors = True, onerror = None)
    except:
        print('Error while deleting directory')
    os.mkdir(path)
    os.chdir(path)


def getinfo(): 
    """ Grab command outputs and write to file """
    for device in devices.keys():
        os.mkdir(device)
        output = (f"{device}_output.txt")
        device_prompt = devices[device]['prompt']
        child = pxssh.pxssh()
        child.login(devices[device]['ip'], username.strip(), password.strip(), auto_prompt_reset=False)
        with open(f"{device}/{output}", 'wb') as f:
            for command in commands:
                child.sendline(command)
                child.expect(device_prompt)
                f.write(child.before)
        child.logout()

cleanup()
getinfo()
