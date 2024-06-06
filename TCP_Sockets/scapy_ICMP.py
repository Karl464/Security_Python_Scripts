#!/usr/bin/python3
"""	
change privileges of script:
	chmod +x scapy_ICMP.py
execute script code: 
	sudo python3 scapy_ICMP.py
"""
import scapy.all as scapy

interfaces = scapy.get_if_list()
print(interfaces)

# Send ICMP query
reply = scapy.sr1(scapy.IP(dst="www.vulnweb.com")/scapy.ICMP(id=1, seq=1, length=64), timeout=3)
if reply is not None:
    print('reply')
    print(reply.src)
    print(reply.dst)