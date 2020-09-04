from scapy.all import *
from scapy.layers.tls.extensions import *
from scapy.layers.http import *

interface = "wlp2s0"
	
def print_host(packet):
	if packet.haslayer(HTTPRequest):
		print(packet.Host.decode())
	if packet.haslayer(ServerName):
		tmp =  packet.getlayer(ServerName)
		print(tmp.servername.decode())

print("[*] Start sniffing...")
load_layer("tls")
sniff(iface=interface, filter = "tcp port 443 or port 80", prn=print_host)
print("[*] Stop sniffing")
