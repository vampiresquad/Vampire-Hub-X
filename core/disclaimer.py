# core/disclaimer.py

import time
import sys
from utils.colors import *

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def admin_disclaimer():
    slow_print(f"{red}[!] WARNING: {yellow}This tool is for ethical hacking purposes only. Unauthorized use may lead to legal consequences.")
    slow_print(f"{blue}[?] Coded by: {cyan}Muhammad Shourov (VAMPIRE)")
    slow_print(f"{green}[✓] You are entering Admin Mode with full privileges.")
    slow_print(f"{red}[!] Any misuse of this tool is your responsibility. The Vampire Squad does not take any liability.")
    slow_print(f"{yellow}[?] Proceed with caution and respect for privacy laws.\n")

def user_disclaimer():
    slow_print(f"{yellow}[!] DISCLAIMER: {red}This tool is intended for educational and legal penetration testing purposes only.")
    slow_print(f"{blue}[?] Coded by: {cyan}Muhammad Shourov (VAMPIRE)")
    slow_print(f"{green}[✓] You are entering Free User Mode with limited privileges.")
    slow_print(f"{red}[!] Unauthorized use is prohibited and can lead to legal actions.")
    slow_print(f"{yellow}[?] Use this tool responsibly and only for legal and ethical purposes.\n")
