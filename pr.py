import getpass
import sys
import telnetlib

HOST = "192.168.16.146"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write((user + "\n").encode('ascii'))
if password:
    tn.read_until(b"Password: ")
    tn.write((password + "\n").encode('ascii'))


tn.write(("enable\n").encode('ascii'))
tn.write(("cisco\n").encode('ascii'))
tn.write(("conf t\n").encode('ascii'))
tn.write(("int loop 0\n").encode('ascii'))
tn.write(("ip address 2.2.2.2 255.255.255.255\n").encode('ascii'))
tn.write(("end\n").encode('ascii'))
tn.write(("exit\n").encode('ascii'))

print (tn.read_all())

