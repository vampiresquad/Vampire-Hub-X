# core/__init__.py

import os
import sys
import platform
import warnings

warnings.filterwarnings("ignore")

# Terminal Color Support Check
def supports_color():
    plat = sys.platform
    supported_platform = plat != 'Pocket PC' and (plat != 'win32' or 'ANSICON' in os.environ)
    is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    return supported_platform and is_a_tty

# Detect OS & Python
SYSTEM_INFO = {
    "platform": platform.system(),
    "platform_release": platform.release(),
    "architecture": platform.machine(),
    "python_version": platform.python_version(),
    "terminal_color": supports_color()
}

# Security Environment Check
def security_check():
    if os.geteuid() != 0 and SYSTEM_INFO["platform"] != "Windows":
        print("[!] Warning: Not running as root. Some features may be limited.")
    if 'ANDROID_ROOT' in os.environ:
        print("[+] Android environment detected.")
    if 'TERMUX_VERSION' in os.environ:
        print("[+] Termux environment detected.")

# Debug Print
def debug_info():
    print("\n[ Vampire Squad - Core Initialized ]")
    for k, v in SYSTEM_INFO.items():
        print(f"  {k}: {v}")

# Init Runner
def initialize_core(verbose=False):
    security_check()
    if verbose:
        debug_info()
