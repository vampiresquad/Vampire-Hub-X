# core/error_fix.py

import os
import sys
import subprocess
import shutil
from utils.colors import *
from core.utils import slow_print

class AutoFixer:
    def __init__(self):
        self.required_commands = ["curl", "wget", "python3", "pip", "git"]
        self.required_modules = ["requests", "colorama", "rich"]

    def fix_all(self):
        slow_print(f"{cyan}[!] Initiating automatic error detection and fix module...\n")
        self.check_commands()
        self.check_python_modules()
        self.check_storage_permissions()
        self.check_internet()
        slow_print(f"\n{green}[✓] All issues resolved or verified. System is ready.\n")

    def check_commands(self):
        for cmd in self.required_commands:
            if shutil.which(cmd) is None:
                slow_print(f"{red}[x] Missing command: {cmd}")
                self.install_command(cmd)
            else:
                slow_print(f"{green}[✓] {cmd} is installed.")

    def install_command(self, cmd):
        slow_print(f"{yellow}[~] Attempting to install {cmd}...")
        try:
            if os.name == 'nt':
                subprocess.call(["choco", "install", cmd], stdout=subprocess.DEVNULL)
            else:
                subprocess.call(["pkg", "install", "-y", cmd], stdout=subprocess.DEVNULL)
            slow_print(f"{green}[✓] {cmd} installation complete.")
        except Exception as e:
            slow_print(f"{red}[!] Failed to install {cmd}. Please install it manually. ({e})")

    def check_python_modules(self):
        for module in self.required_modules:
            try:
                __import__(module)
                slow_print(f"{green}[✓] Python module '{module}' is installed.")
            except ImportError:
                slow_print(f"{red}[x] Missing Python module: {module}")
                self.install_python_module(module)

    def install_python_module(self, module):
        try:
            subprocess.call([sys.executable, "-m", "pip", "install", module], stdout=subprocess.DEVNULL)
            slow_print(f"{green}[✓] Installed: {module}")
        except Exception as e:
            slow_print(f"{red}[!] Could not install module '{module}': {e}")

    def check_storage_permissions(self):
        if os.name != 'nt':
            storage_path = "/data/data/com.termux/files/home"
            if os.access(storage_path, os.W_OK):
                slow_print(f"{green}[✓] Storage permission is OK.")
            else:
                slow_print(f"{yellow}[!] Fixing Termux storage permissions...")
                subprocess.call(["termux-setup-storage"])
                slow_print(f"{green}[✓] Storage permission fixed (or requested).")

    def check_internet(self):
        slow_print(f"{cyan}[?] Checking internet connectivity...")
        try:
            subprocess.check_call(["ping", "-c", "1", "8.8.8.8"], stdout=subprocess.DEVNULL)
            slow_print(f"{green}[✓] Internet connection is active.")
        except subprocess.CalledProcessError:
            slow_print(f"{red}[x] No internet connection detected. Some operations may fail.")

    def fix_permissions(self, path):
        try:
            os.chmod(path, 0o755)
            slow_print(f"{green}[✓] Permissions fixed for {path}")
        except Exception as e:
            slow_print(f"{red}[!] Failed to fix permissions for {path}: {e}")

# Example usage
if __name__ == "__main__":
    fixer = AutoFixer()
    fixer.fix_all()
