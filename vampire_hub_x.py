import os
import time
from core.admin_panel import show_admin_menu
from core.user_panel import show_user_menu
from core.banner import display_banner
from core.auth import authenticate_user
from core.disclaimer import show_disclaimer
from core.error_fix import auto_fix_tools
from utils.colors import *

# ===== Smart Check for Required Directories & Files ===== #
required_structure = {
    "core": ["admin_panel.py", "user_panel.py", "banner.py", "auth.py", "disclaimer.py", "error_fix.py"],
    "utils": ["colors.py"],
    "modules": [],  # Add more as needed
}

def smart_structure_check():
    print(f"{blue}[~] Checking essential file/folder structure...{reset}")
    for folder, files in required_structure.items():
        if not os.path.isdir(folder):
            print(f"{red}[!] Missing folder: {folder}. Creating...{reset}")
            os.makedirs(folder)

        for file in files:
            path = os.path.join(folder, file)
            if not os.path.exists(path):
                print(f"{yellow}[!] Missing file: {path} (You may want to add it manually later).{reset}")
    print(f"{green}[✓] Structure check complete.{reset}")
    time.sleep(1)

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
    smart_structure_check()     # <-- New structure validation
    auto_fix_tools()            # Existing tool checker
    print(f"{green}[✓] All required tools are ready.{reset}")
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
