from scapy.all import *

# our packet callback
def packet _callback(packet):
	print packet.show()

# fire up our sniffer
sniffer(prn=packet_callback,count=1)