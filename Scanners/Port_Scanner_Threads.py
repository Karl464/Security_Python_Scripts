#!/usr/bin/python3
"""	
change privileges of script:
	chmod +x Port_Scanner_Threads.py
execute script code: 
	python3 Port_Scanner_Threads.py

Note:
use N_THREADS to improve scan speed
Delete "end="\r"" on print funtion to see all non conected ports
"""

import socket
from threading import Thread
from colorama import init, Fore

N_THREADS = 4

# some color
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX


def is_port_open(host, port):
        """
        determine whether host' has the 'port' open
        """
        
        #create a new socket
        s = socket.socket()
        try:
            # tries to connect to host using that port
            s.connect((host, port))
            # make timeout if you want it a little faster less accuracy) 
            #s.settimeout (0.2)
        except:
            # cannot connect, port is closed
            # return false
            return False
        else:
            # the connection was established, port is open! 
            return True


def main(host, ports):
    global q
    for t in range (N_THREADS):
    # for each thread, start it
        t = Thread(target-scan_thread)

        # when we set daemon to true, that thread will end when the main thread ends
        t.daemon - True
        #start the daemon thread
        t.start()

    for worker in ports:
        #for each port, put that port into the queue
        #to start scanning
        q.put (worker)
    
    # wait the threads (port scanners) to finish
    q.join()

# get the host from the user
host = input("Enter the host: ")

# iterate over ports, from 1 to 1024 
for port in range(1, 1025):
    if is_port_open(host, port):
        print(GREEN + "[+] ",host," : ",port," is open" + RESET)
    else:
        print(GRAY + "[+] ",host," : ",port," is close" + RESET, end="\r")

    
