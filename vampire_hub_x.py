import os
import time
from core.admin_panel import show_admin_menu
from core.user_panel import show_user_menu
from core.banner import display_banner
from core.auth import authenticate_user
from core.disclaimer import show_disclaimer
from core.error_fix import auto_fix_tools
from utils.colors import *

def initialize():
    os.system("clear")
    display_banner()
    show_disclaimer()

def main():
    while True:
        initialize()
        user_choice = input(f"{yellow}[+] Are you an Admin or User? (admin/user): {reset}").lower()
        if user_choice == "admin":
            authenticate_user("admin")
            show_admin_menu()
        elif user_choice == "user":
            authenticate_user("user")
            show_user_menu()
        else:
            print(f"{red}[!] Invalid input. Please select either 'admin' or 'user'.{reset}")
            time.sleep(1)

def setup_tools():
    print(f"{green}[+] Performing automatic tool integrity check...{reset}")
    auto_fix_tools()  # Automatically fixes missing tools and dependencies
    time.sleep(1)
    print(f"{green}[+] All required tools are ready.{reset}")
    time.sleep(1)

def run():
    try:
        setup_tools()
        main()
    except KeyboardInterrupt:
        print(f"\n{red}[-] Program interrupted. Exiting...{reset}")
        exit()

if __name__ == "__main__":
    run()
