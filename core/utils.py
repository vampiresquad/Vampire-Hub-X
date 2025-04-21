# core/utils.py

import os
import sys
import time
import platform
import subprocess
from datetime import datetime
from utils.colors import *

def slow_print(text, delay=0.03):
    """Prints text slowly, simulating typing."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def system_info():
    """Prints basic system information."""
    slow_print(f"{cyan}[+] System Information:")
    slow_print(f"{yellow}[+] OS: {platform.system()} {platform.release()} {platform.version()}")
    slow_print(f"{yellow}[+] Processor: {platform.processor()}")
    slow_print(f"{yellow}[+] Architecture: {platform.architecture()[0]}")
    slow_print(f"{yellow}[+] Machine: {platform.machine()}")
    slow_print(f"{yellow}[+] Node: {platform.node()}")
    slow_print(f"{yellow}[+] Platform: {platform.platform()}")
    slow_print(f"{yellow}[+] Python Version: {platform.python_version()}")
    slow_print(f"{green}[✓] System Info Retrieved Successfully.\n")

def get_current_time():
    """Returns the current time in a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_activity(message, log_file="vampire_hub_log.txt"):
    """Logs activity to a log file with a timestamp."""
    with open(log_file, "a") as log:
        log.write(f"[{get_current_time()}] {message}\n")

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def check_internet_connection():
    """Checks if the system has internet access by pinging Google's DNS server."""
    try:
        subprocess.check_call(["ping", "-c", "3", "8.8.8.8"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def display_help():
    """Displays help information about the tool."""
    slow_print(f"{yellow}[!] Help Information:")
    slow_print(f"{blue}[?] Vampire-Hub-X is a multi-functional tool for ethical hacking, penetration testing, and DDoS attacks.")
    slow_print(f"{green}[✓] Features include powerful DDoS attacks, information gathering, and much more.")
    slow_print(f"{cyan}[+] Use the following commands to access different features:")
    slow_print(f"{yellow}[1] DDoS Attack - Perform DDoS attacks.")
    slow_print(f"{yellow}[2] Information Gathering - Collect data about targets.")
    slow_print(f"{red}[!] Always use this tool ethically and legally!")
    slow_print(f"{green}[✓] For further assistance, consult the user manual or online documentation.\n")

def check_requirements(requirements):
    """Checks and installs missing requirements."""
    missing_requirements = []
    for req in requirements:
        try:
            __import__(req)
        except ImportError:
            missing_requirements.append(req)

    if missing_requirements:
        slow_print(f"{red}[x] Missing required packages: {', '.join(missing_requirements)}")
        slow_print(f"{yellow}[!] Installing missing packages...")
        install_requirements(missing_requirements)
    else:
        slow_print(f"{green}[✓] All requirements are installed.\n")

def install_requirements(requirements):
    """Installs required packages."""
    for req in requirements:
        slow_print(f"{yellow}[+] Installing {req}...")
        subprocess.call([sys.executable, "-m", "pip", "install", req])

def validate_input(input_str, valid_choices):
    """Validates user input to match available choices."""
    if input_str not in valid_choices:
        slow_print(f"{red}[x] Invalid input. Please choose a valid option.\n")
        return False
    return True

def generate_unique_id():
    """Generates a unique ID for user sessions or tasks."""
    import uuid
    return str(uuid.uuid4())

def check_permissions(file_path):
    """Checks if the user has the necessary permissions for a file."""
    if os.access(file_path, os.R_OK):
        slow_print(f"{green}[✓] Read access to {file_path} granted.")
    else:
        slow_print(f"{red}[x] No read access to {file_path}. Please check permissions.")
