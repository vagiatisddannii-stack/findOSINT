import os
import sys
import time
import whois
import socket
import requests
import threading

os.system("clear")
print ("#############")
print ("# FindOSINT #")
print ("#   v2.13   #")
print ("#############")

def time(delay):
    time.sleep(1)
    time.time()
    threading.Thread(delay)

ip = input("Type the domain: ")
def get_ip(target):
    try:
        ip = socket.gethostbyname(target)
        print (f"[+] IP found")
        print (f"[+] Domains IP is {ip}")
        return ip
    except sock.gaierror:
        print (f"[-] Could not found domains IP - check the .com")
        sys.exit()
        return None
    except Exception as e:
        print (f"[-] THere was an error {e}")
        sys.exit()
        return None

port = input("Type the port: ")
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, int(port)))
        sock.close()
        if result == 0:
            print (f"[+] Port {port} is OPEN")
        else:
            print (f"[-] Port {port} is CLOSE")
    except Exception as e:
        print (f"[-] There was an error {e}")
        sys.exit()

def get_whois(domain):
    w = whois.whois(domain)
    print(f"[+] Registrar: {w.registrar}")
    print(f"[+] Created: {w.creation_date}")
    print(f"[+] Expires: {w.expiration_date}")

def get_geolocation(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()
    print(data['country'])
    print(data['city'])
    print(data['isp'])

if __name__ == '__main__':
    get_ip(ip)
    scan_port(ip, port)
    get_geolocation(ip)
    get_whois(ip)
