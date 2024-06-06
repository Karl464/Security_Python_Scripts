#!/usr/bin/python3
"""	
#pip install scapy

change privileges of script:
	chmod +x Scapy_ARP_Scanner.py
execute script code: 
	sudo python3 Scapy_ARP_Scanner.py
"""

from scapy.all import ARP, Ether, srp
from colorama import init, Fore

# some color
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
CYAN = Fore.CYAN
GRAY = Fore.LIGHTBLACK_EX

target_ip= "10.0.2.15/24"
# IP Address for the destination
# Create ARP Packet

arp = ARP (pdst=target_ip)
# Create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting 
ether = Ether (dst="ff:ff:ff:ff:ff:ff")

# stack them
packet = ether/arp

result = srp (packet, timeout=3, verbose=0) [0]

# a list of clients, we will fill this in the upcoming loop 
clients = []
for sent, received in result:
    # for each response, append ip and mac address to clients' list 
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# print clients
print(CYAN + "Available devices in the network: ")
print("IP" + " "*18+"MAC" + RESET)
for client in clients:
    print(GREEN + "{:16} {}".format(client ['ip'], client['mac']) + RESET)
