# modules/recon.py

import os
import sys
import socket
import subprocess
import threading
import requests
import json
from core.utils import color, slowprint
from core.error_fix import ensure_package

# Ensure required packages
ensure_package("requests")

# ==== BANNER ==== #
def banner(mode="user"):
    os.system("clear")
    title = "VAMPIRE RECON ENGINE - ADMIN" if mode == "admin" else "VAMPIRE RECON - USER MODE"
    print(color("bold_green", f"""
   __      ___      _                       _____                      
   \ \    / (_)    | |                     |  __ \                     
    \ \  / / _  ___| |_ ___  _ __ ___ ___  | |__) |_ _ ___ _____   __  
     \ \/ / | |/ __| __/ _ \| '__/ __/ _ \ |  ___/ _` / __/ __\ \ / /  
      \  /  | | (__| || (_) | | | (_|  __/ | |  | (_| \__ \__ \\ V /   
       \/   |_|\___|\__\___/|_|  \___\___| |_|   \__,_|___/___/ \_/    
                        [{title}]
    """))

# ===== USER TOOLS ===== #
def basic_ping(host):
    print(color("cyan", f"\n[+] Pinging {host}...\n"))
    os.system(f"ping -c 4 {host}")

def whois_lookup(domain):
    print(color("cyan", f"\n[+] Performing WHOIS on {domain}...\n"))
    os.system(f"whois {domain}")

def dns_lookup(domain):
    print(color("cyan", f"\n[+] DNS Records for {domain}...\n"))
    os.system(f"dig {domain} ANY +short")

# ===== ADMIN TOOLS ===== #
def subdomain_enum(domain):
    print(color("magenta", f"\n[+] Subdomain Brute Force for {domain}\n"))
    wordlist = "/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt"
    if not os.path.exists(wordlist):
        print(color("yellow", "[!] Wordlist not found, downloading..."))
        os.system("mkdir -p /usr/share/seclists/Discovery/DNS/")
        os.system(f"wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/subdomains-top1million-110000.txt -O {wordlist}")
    
    def brute_sub(domain, sub):
        try:
            ip = socket.gethostbyname(f"{sub}.{domain}")
            print(color("green", f"[+] Found: {sub}.{domain} -> {ip}"))
        except:
            pass

    with open(wordlist) as f:
        subs = f.read().splitlines()
        threads = []
        for sub in subs:
            t = threading.Thread(target=brute_sub, args=(domain, sub))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

def port_scan(ip):
    print(color("cyan", f"\n[+] Port scanning {ip}...\n"))
    for port in range(1, 1025):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((ip, port))
            print(color("green", f"[OPEN] {ip}:{port}"))
            s.close()
        except:
            pass

def geoip_lookup(ip):
    print(color("cyan", f"\n[+] IP Location Lookup for {ip}...\n"))
    try:
        data = requests.get(f"http://ip-api.com/json/{ip}").json()
        for key, val in data.items():
            print(color("yellow", f"{key.capitalize()}: {val}"))
    except:
        print(color("red", "[!] Failed to fetch IP info."))

def http_headers(domain):
    print(color("cyan", f"\n[+] Fetching HTTP headers for {domain}\n"))
    try:
        res = requests.get(f"http://{domain}")
        for k, v in res.headers.items():
            print(color("green", f"{k}: {v}"))
    except:
        print(color("red", "[!] Error fetching headers."))

# ==== MAIN ENTRY ==== #
def start_recon(mode="user"):
    try:
        banner(mode)
        if mode == "admin":
            print(color("cyan", "\n[1] Subdomain Enum\n[2] Port Scan\n[3] IP Lookup\n[4] HTTP Headers\n"))
            choice = input(color("green", "[?] Choose option: "))

            if choice == "1":
                domain = input(color("cyan", "Enter target domain: "))
                subdomain_enum(domain)
            elif choice == "2":
                ip = input(color("cyan", "Enter target IP: "))
                port_scan(ip)
            elif choice == "3":
                ip = input(color("cyan", "Enter IP address: "))
                geoip_lookup(ip)
            elif choice == "4":
                domain = input(color("cyan", "Enter domain: "))
                http_headers(domain)

        else:
            print(color("cyan", "\n[1] Ping\n[2] WHOIS\n[3] DNS Lookup\n"))
            choice = input(color("green", "[?] Choose option: "))

            if choice == "1":
                host = input(color("cyan", "Target Host/IP: "))
                basic_ping(host)
            elif choice == "2":
                domain = input(color("cyan", "Domain: "))
                whois_lookup(domain)
            elif choice == "3":
                domain = input(color("cyan", "Domain: "))
                dns_lookup(domain)

    except Exception as e:
        print(color("red", f"[!] Error: {e}"))
