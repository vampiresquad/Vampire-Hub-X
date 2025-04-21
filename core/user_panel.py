# core/user_panel.py

import os
import time
from modules import ddos, recon
from utils.colors import *
from utils.helper import slow_print

def user_banner():
    os.system("clear")
    print(f"""{blue}
 █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████
 ████▒▒{yellow}         FREE USER ACCESS         {blue}▒▒████
 ███▒▒{green}      Created by: Muhammad Shourov     {blue}▒▒███
 ██▒▒{cyan} Founder & CEO: Vampire Squad (VAMPIRE)  {blue}▒▒██
 ██▒▒{cyan} GitHub     : github.com/vampiresquad     {blue}▒▒██
 ██▒▒{cyan} Facebook   : fb.com/Junior.Writer.SHourov {blue}▒▒██
 ██▒▒{cyan} Email      : vampiresquad.org@gmail.com   {blue}▒▒██
 █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
{reset}""")

def user_disclaimer():
    slow_print(f"{cyan}Welcome to Vampire-Hub-X [Free User Mode]")
    slow_print(f"{red}Warning: You are using the limited version of this tool.")
    slow_print(f"{yellow}Upgrade to Admin Mode for full power and advanced features.")
    slow_print(f"{green}Use all features ethically. Unauthorized use is prohibited.{reset}\n")
    time.sleep(1)

def show_user_menu():
    while True:
        user_banner()
        print(f"""{magenta}
 [1] Basic DDoS Attack (Safe Mode)
 [2] Basic Recon & Info Gathering
 [3] Exit User Panel
{reset}""")
        try:
            choice = input(f"{yellow}[+] Select Option: {reset}")
            if choice == '1':
                ddos.run_user_ddos()
            elif choice == '2':
                recon.run_user_recon()
            elif choice == '3':
                print(f"{cyan}[-] Exiting User Panel...{reset}")
                break
            else:
                print(f"{red}[!] Invalid option. Try again.{reset}")
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{red}[-] Interrupted by user. Returning...{reset}")
            break
