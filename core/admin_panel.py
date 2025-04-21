# core/admin_panel.py

import os
import time
from modules import ddos, recon, encryption
from utils.colors import *
from utils.helper import slow_print

def admin_banner():
    os.system("clear")
    print(f"""{cyan}
 █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████
 ████▒▒{red}      VAMPIRE ADMIN ACCESS       {cyan}▒▒████
 ███▒▒{green}      Coded by Muhammad Shourov    {cyan}▒▒███
 ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
 █▒▒{yellow}       High Privileged Access Granted       {cyan}▒▒█
 █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
{reset}""")
    print()

def admin_disclaimer():
    slow_print(f"{blue}You are in Admin Mode of VAMPIRE-HUB-X.")
    slow_print(f"{red}Unauthorized usage is prohibited. All actions are logged.")
    slow_print(f"{green}Use with caution and responsibility...{reset}\n")
    time.sleep(1)

def show_admin_menu():
    while True:
        admin_banner()
        print(f"""{magenta}
 [1] Launch High-Powered DDoS Attack
 [2] Run Advanced Recon & Intelligence
 [3] Launch Custom Encryption Module
 [4] System & Tool Integrity Check
 [5] Exit Admin Panel
{reset}""")
        try:
            choice = input(f"{yellow}[+] Select Option: {reset}")
            if choice == '1':
                ddos.run_admin_ddos()
            elif choice == '2':
                recon.run_admin_recon()
            elif choice == '3':
                encryption.run_advanced_encryption()
            elif choice == '4':
                tool_integrity_check()
            elif choice == '5':
                print(f"{cyan}[-] Exiting Admin Panel...{reset}")
                break
            else:
                print(f"{red}[!] Invalid Option. Try Again.{reset}")
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{red}[-] Interrupted. Returning to main menu.{reset}")
            break

def tool_integrity_check():
    print(f"{green}[√] Checking tools and modules integrity...{reset}")
    time.sleep(1)
    essential_tools = ["curl", "python3", "git", "nmap", "whois"]
    for tool in essential_tools:
        print(f"{blue}[*] Checking {tool}...{reset}")
        if os.system(f"command -v {tool} > /dev/null") != 0:
            print(f"{red}[!] {tool} not found. Attempting auto-fix...{reset}")
            os.system(f"pkg install -y {tool} || apt install -y {tool}")
        else:
            print(f"{green}[✓] {tool} is installed.{reset}")
    print(f"{green}[+] All essential tools are ready.{reset}")
    time.sleep(2)
