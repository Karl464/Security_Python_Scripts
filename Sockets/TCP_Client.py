#!/usr/bin/python3
"""	
TCP Socket:

change privileges of script:
	chmod +x TCP_Client.py
execute script code: 
	python ./TCP_Client.py
or
    python ./TCPClient.py menssage

Note: As server (Endpoint) u can use:
A standar FQDNS and port, like www.vulnweb.com to port 80
If u want to use TCP_Server.py use localhost and corresponded port.
Try with netcad "nc -l -p 9999"
"""
import socket
import sys

#HOST, PORT = "www.vulnweb.com", 80
#message = 'GET / HTTP/1.0\nHost: www.vulnweb.com\n\n'

HOST, PORT = "localhost", 9999
message = " ".join(sys.argv[1:])

received_data = ""
# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(message + "\n", "utf-8"))

    # Receive data from the server and shut down
    while 1:
        received = str(sock.recv(1024), "utf-8")
        if received == "":
            break
        received_data = received_data + received
    print (received_data)

print("Sent:     {}".format(message))
print("Received: {}".format(received_data))