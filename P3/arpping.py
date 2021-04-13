import scapy
from scapy.all import srp,Ether,ARP,conf

conf.verb =0
ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.0.0/24"),timeout=2)

for snd,rcv in ans:
	print rcv.sprintf(r"%Ether.src%, en la IP %ARP.psrc%")
