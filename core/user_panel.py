# core/user_panel.py

import os
import time
from modules import ddos, recon, encryption
from utils.colors import *
from utils.helper import slow_print
from core.banner import show_user_banner
from core.disclaimer import show_user_disclaimer
from core.error_fix import basic_auto_fixer

def show_user_panel():
    os.system("clear")
    show_user_banner()
    show_user_disclaimer()

    while True:
        print(f"""{cyan}
 [1] Start Lightweight DDoS Test
 [2] Basic Reconnaissance
 [3] Simple Encryption Tool
 [4] Fix Common Errors Automatically
 [5] Exit User Panel
{reset}""")
        try:
            choice = input(f"{yellow}[+] Choose an option: {reset}")
            if choice == '1':
                ddos.run_user_ddos()
            elif choice == '2':
                recon.run_user_recon()
            elif choice == '3':
                encryption.run_basic_encryption()
            elif choice == '4':
                basic_auto_fixer()
            elif choice == '5':
                print(f"{cyan}[-] Exiting User Mode... Stay Ethical!{reset}")
                break
            else:
                print(f"{red}[!] Invalid Option. Try Again.{reset}")
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{red}[-] Interrupted. Returning to main menu.{reset}")
            break
        except Exception as e:
            print(f"{red}[!] Error: {e}{reset}")
            basic_auto_fixer()
