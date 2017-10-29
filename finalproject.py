import os
import time
import smtplib
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

def follow(name):
    current = open(name, "r")
    curino = os.fstat(current.fileno()).st_ino
    while True:
        while True:
            line = current.readline()
            if not line:
                break
            yield line

        try:
            if os.stat(name).st_ino != curino:
                new = open(name, "r")
                current.close()
                current = new
                curino = os.fstat(current.fileno()).st_ino
                continue
        except IOError:
            pass
        time.sleep(1)

sender = ["ch948913@dal.ca"]
receivers = ["chaitanyapatel4@gmail.com"]




message = """From: ch948913@dal.ca
To :chaitanyapatel4@gmail.com
Subject_SMTP e-mail test

This is a test e-mail message"""


if __name__ == '__main__':
    fname = "/var/log/router.log"
    for l in follow(fname):
        if 'Interface Serial3/3, changed state to up' in l:
            smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtpObj.sendmail("ch948913@dal.ca","chaitanyapatel4@gmail.com", message)
