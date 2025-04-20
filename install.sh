#!/bin/bash

# Colors
R='\033[1;31m'
G='\033[1;32m'
Y='\033[1;33m'
C='\033[1;36m'
W='\033[1;37m'
NC='\033[0m'

# Banner
clear
echo -e "${R}"
echo "██    ██  █████  ███    ███ ██████  ██ ██████  ███████     ██   ██ ██    ██ ██████  ██"
echo "██    ██ ██   ██ ████  ████ ██   ██ ██ ██   ██ ██          ██   ██ ██    ██ ██   ██ ██"
echo "██    ██ ███████ ██ ████ ██ ██████  ██ ██████  ███████     ███████ ██    ██ ██████  ██"
echo "██    ██ ██   ██ ██  ██  ██ ██      ██ ██           ██     ██   ██ ██    ██ ██      ██"
echo " ██████  ██   ██ ██      ██ ██      ██ ██      ███████     ██   ██  ██████  ██      ██"
echo -e "${C}                       The Ultimate Multi Functional Hub"
echo -e "${G}                       Created by: Muhammad Shourov (VAMPIRE)"
echo -e "${NC}"

# Disclaimer
echo -e "${Y}[!] This tool is only for educational & authorized security testing purposes.${NC}"
sleep 2

# Auto Fix Function
auto_fix() {
    echo -e "${Y}[~] Trying to fix: $1 ...${NC}"
    case $1 in
        "apt")
            pkg install apt -y || apt update -y && apt upgrade -y
            ;;
        "pip")
            pkg install python -y
            curl -sS https://bootstrap.pypa.io/get-pip.py | python || echo -e "${R}[x] Pip install failed.${NC}"
            ;;
        "git")
            pkg install git -y
            ;;
        "python")
            pkg install python -y
            ;;
        "requests")
            pip install requests || pip3 install requests
            ;;
        *)
            echo -e "${R}[!] Unknown fix target: $1${NC}"
            ;;
    esac
}

# Check & Install Required Packages
check_install() {
    for pkg in git python; do
        if ! command -v $pkg &>/dev/null; then
            echo -e "${R}[!] $pkg not found.${NC}"
            auto_fix $pkg
        else
            echo -e "${G}[✓] $pkg is installed.${NC}"
        fi
    done

    if ! python -c "import requests" &>/dev/null; then
        echo -e "${R}[!] Python module 'requests' not found.${NC}"
        auto_fix "requests"
    else
        echo -e "${G}[✓] Python 'requests' module is available.${NC}"
    fi
}

# Begin Setup
echo -e "${C}[*] Starting advanced setup...${NC}"
sleep 1
pkg update -y && pkg upgrade -y

check_install

# Set execution permissions
chmod +x hub.py >/dev/null 2>&1

echo -e "${G}[✓] All dependencies installed successfully!${NC}"
echo -e "${Y}[!] To run the tool: ${C}python3 hub.py${NC}"
