import getpass
import sys
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()

f = open ('my_routers')

for IP in f:
    IP=IP.strip()
    print("I'm going to configure switch " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")
       tn.write(b"enable\n")
       tn.write(b"cisco\n")
    tn.write(b"conf t\n")
    tn.write(b"snmp-server community test ro 99" + b"\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
