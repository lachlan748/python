import getpass
import sys
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()

f = open ('my_routers')

for IP in f:
    IP=IP.strip()
    print("Getting show version info from " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")
       tn.write(b"enable\n")
       tn.write(b"cisco\n")
    tn.write(b"terminal length 0\n")
    tn.write(b"show version\n")
    tn.write(b"exit\n")
    str1 = (tn.read_all().decode('ascii'))
    int1 = (str1.index('Version'))
    print(str1[int1: int1 + 18])


