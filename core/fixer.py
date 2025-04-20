import os
import sys
import subprocess
import shutil

def run_command(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"[!] Failed to run: {cmd}")

def is_installed(pkg):
    return shutil.which(pkg) is not None

def fix_errors():
    print("[*] Checking system environment and dependencies...")

    essential_pkgs = ["python", "python3", "curl", "wget", "git", "figlet", "toilet", "nc", "nmap"]
    for pkg in essential_pkgs:
        if not is_installed(pkg):
            print(f"[!] Missing: {pkg} — trying to install...")
            run_command(f"pkg install -y {pkg} || apt install -y {pkg} || apt-get install -y {pkg}")

    # Pip check
    pip_status = subprocess.getoutput("pip3 --version || pip --version")
    if "not found" in pip_status:
        print("[!] pip not found. Installing...")
        run_command("apt install python3-pip -y || pkg install python3-pip -y")

    # Requests module check
    try:
        import requests
    except ImportError:
        print("[!] requests module missing. Installing...")
        run_command("pip install requests || pip3 install requests")

    print("[✓] All basic dependencies are installed and errors auto-fixed!")

if __name__ == "__main__":
    fix_errors()
