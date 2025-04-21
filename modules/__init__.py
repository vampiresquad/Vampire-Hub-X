# modules/__init__.py

"""
Vampire-Hub-X Modules Initialization
Author: Muhammad Shourov
GitHub: https://github.com/vampiresquad
"""

import os
import sys
import importlib
from pathlib import Path

# Module Registry (Auto-discover & loadable module names)
MODULE_REGISTRY = []

def discover_modules():
    """
    Auto-discover Python modules in this directory (excluding __init__.py).
    """
    global MODULE_REGISTRY
    current_dir = Path(__file__).parent
    for file in current_dir.glob("*.py"):
        if file.name != "__init__.py":
            module_name = file.stem
            MODULE_REGISTRY.append(module_name)

def load_module(module_name):
    """
    Dynamically import a module from the 'modules' package.
    """
    try:
        return importlib.import_module(f"modules.{module_name}")
    except Exception as e:
        print(f"[!] Error loading module '{module_name}': {e}")
        return None

# Discover available modules at init
discover_modules()

# Optional: print loaded modules (for debugging)
# print(f"[+] Loaded modules: {MODULE_REGISTRY}")
