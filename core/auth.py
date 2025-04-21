# core/auth.py

import getpass
import hashlib
from modules.encryption import verify_password
from utils.colors import *
import sys
import time

# Stored hashed passwords (hash with sha256)
MASTER_PASSWORD_HASH = hashlib.sha256("VampireX".encode()).hexdigest()
ADMIN_PASSWORD_HASH = hashlib.sha256("SH404".encode()).hexdigest()

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def authenticate():
    slow_print(f"{cyan}[!] Master Authentication Required")
    password = getpass.getpass(f"{blue}[?] Enter Master Password: ")

    if hashlib.sha256(password.encode()).hexdigest() != MASTER_PASSWORD_HASH:
        print(f"{red}[x] Incorrect Master Password! Access Denied.")
        exit(1)
    
    slow_print(f"{green}[✓] Master Authentication Successful.\n")
    return True

def access_mode():
    slow_print(f"{cyan}[!] Select Access Mode")
    print(f"{yellow}[1] Admin Mode")
    print(f"{green}[2] User Mode\n")

    choice = input(f"{blue}[?] Enter choice (1/2): ").strip()

    if choice == "1":
        password = getpass.getpass(f"{blue}[?] Enter Admin Password: ")
        if verify_password(password, ADMIN_PASSWORD_HASH):
            print(f"{green}[✓] Admin Access Granted.\n")
            return "admin"
        else:
            print(f"{red}[x] Incorrect Admin Password! Switching to User Mode.\n")
            return "user"
    else:
        print(f"{green}[✓] Free User Access Enabled.\n")
        return "user"
