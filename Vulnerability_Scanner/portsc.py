import socket 
from IPy import IP
import threading


ports = []
banners =[]


def port_scanner(target,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            trarget_ip =IP(target) 
        except:
            target_ip = socket.gethostbyname(target)   

        s.connect((target_ip, port))
        try:
            banner_name = banner(s).decode()
            ports.append(port)
            banners.append(banner_name.strip())
        except:
            pass
    except:
        pass

def banner(s):
    return s.recv(1024)

target = input("Enter Target IP address, localhost or www.domainname.com : ")

portsc = int(input("Enter Number of ports to be scanned"))
for port in range(1,portsc):
    thread = threading.Thread(target =port_scanner, args=[target,port])
    thread.start()

with open("vulnarable_banners.txt", "r") as file:
    data = file.read()
    for i in range(len(banners)):
        if banners[i] in data:
            print(f"[!]Vulneribility found: {banners[i]} at port {ports[i]}")
