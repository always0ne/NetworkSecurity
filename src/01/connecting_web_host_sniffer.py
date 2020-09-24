# Created by always0ne on 2020.09.04

from scapy.all import *
from scapy.layers.tls.extensions import *
from scapy.layers.http import *

interface = "Your Network Interface"
	
def print_host(packet):
	# Handle HTTP
	# Catch Host in header data
	if packet.haslayer(HTTPRequest):
		print(packet.Host.decode())
	# Handle HTTPS 
	# HTTPS (TLS) encrypt all data but expose server name when handshaking
	# Catch Client Hello Packet and get server_name in extension field 
	if packet.haslayer(ServerName):
		print(packet.getlayer(ServerName).servername.decode())

print("[*] Start sniffing...")
load_layer("tls")
sniff(iface=interface, filter = "tcp port 443 or port 80", prn=print_host)
print("[*] Stop sniffing")
