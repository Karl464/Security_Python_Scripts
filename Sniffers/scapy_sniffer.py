#!/usr/bin/python3
"""	
https://code-maven.com/slides/python/scapy-sniffing

change privileges of script:
	chmod +x scapy_sniff.py
execute script code: 
	sudo python3 scapy_sniff.py
"""

import scapy.all as scapy

snf = scapy.sniff(filter="192.168.10.20", count=4)
#snf = scapy.sniff(filter="dst www.vulnweb.com", count=4)
#snf = scapy.sniff(filter="src 127.0.0.1 and dst 127.0.0.1", count=2)

print("done")
print(snf)
snf.summary()
print('-------')
print(snf[0])
snf[0].display
print('-------')
#print(snf[0].icmp.display)
#icmp = snf[0].getlayer('ICMP')
#icmp.display()