import getpass
import sys
import telnetlib

HOST = "10.0.0.1"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("show ip route\n")
tn.write("exit\n")

print tn.read_all()
