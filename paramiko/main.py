import getpass
import paramiko
import time
import os
import shutil

devices = {'R01': {'prompt': 'R01#', 'ip': '10.1.1.1'},
           'R02': {'prompt': 'R02#', 'ip': '10.1.1.2'},
           'R03': {'prompt': 'R03#', 'ip': '10.1.1.3'},
           'R04': {'prompt': 'R04#', 'ip': '10.1.1.4'},
           'R05': {'prompt': 'R05#', 'ip': '10.1.1.5'}}

commands = ['show version\n', 'show ip route\n']

username = input('Username: ')
password = getpass.getpass('Password: ')

max_buffer = 65535

def cleanup():
    """ Create and clean an outputs folder """
    path = "./outputs"
    try:
        shutil.rmtree(path, ignore_errors = True, onerror = None)
    except:
        print('Error while deleting directory')
    os.mkdir(path)
    os.chdir(path)


def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)


def getinfo(): 
    """ Grab command outputs and write to file """
    for device in devices.keys():
        os.mkdir(device)
        output_file = (f"{device}_output.txt")
        connection = paramiko.SSHClient()
        connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        connection.connect(devices[device]['ip'], username=username, password=password,
                           look_for_keys=False, allow_agent=False)
        new_connection = connection.invoke_shell()
        output = clear_buffer(new_connection)
        time.sleep(1)
        new_connection.send("terminal length 0\n")
        output = clear_buffer(new_connection)
        with open(f"{device}/{output_file}", 'wb') as f:
            for command in commands:
                print(f"[*] Sending {command} to {device}")
                new_connection.send(command)
                time.sleep(2)
                output = new_connection.recv(max_buffer)
                f.write(output)

        new_connection.close()

if __name__ == "__main__":
    cleanup()
    connection = getinfo()
    #clear_buffer(connection)
