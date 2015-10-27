from scapy.all import *

# our packet callback
def packet_callback(packet):
	print packet.show()

# fire up our sniffer
sniffer(prn=packet_callback,count=1)