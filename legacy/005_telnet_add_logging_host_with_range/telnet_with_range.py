import getpass
import sys
import telnetlib

HOST = "localhost"
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

    for n in range (2,6):
        tn.write(b"logging host 1.2.3." + str(n).encode('ascii') + b"\n")

    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
