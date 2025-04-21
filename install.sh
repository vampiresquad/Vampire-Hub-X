#!/bin/bash

# Banner Function
banner() {
  clear
  echo -e "\e[1;36m"
  echo "██████╗ █████╗ ███████╗████████╗███████╗██████╗ ███████╗"
  echo "██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝"
  echo "██████╔╝███████║███████╗   ██║   █████╗  ██████╔╝███████╗"
  echo "██╔═══╝ ██╔══██║╚════██╗  ██╔══╝  ██╔══╝  ██╔═══╝ ╚════██╗"
  echo "██║     ██║  ██║███████╗  ██║     ███████╗██║     ███████╔╝"
  echo "╚═╝     ╚═╝  ╚═╝╚══════╝  ╚═╝     ╚══════╝╚═╝     ╚═════╝"
  echo -e "\e[1;33m  Coded by Muhammad Shourov (VAMPIRE) - Vampire Squad\e[0m"
  echo -e "\e[1;32m  ---------------------------------------------------\e[0m"
}


# Color Codes
RED='\033[0;31m'
GREEN='\033[1;32m'
CYAN='\033[1;36m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Banner Function
show_banner() {
    clear
    echo -e "${RED}"
    echo '      █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████'
    echo '   ████▀░░░░░░░░░░░░░░░░░░░░░░░░░░▀████'
    echo ' ██▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀██'
    echo ' ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██'
    echo ' ██░░░░░░${YELLOW}VAMPIRE SQUAD INSTALLER${RED}░░░░░░░░██'
    echo ' ██░░░░░░${CYAN}Coded by: Muhammad Shourov (VAMPIRE)${RED}░░██'
    echo ' ██▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄██'
    echo '  ███▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄███'
    echo '    ████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄████'
    echo -e "${NC}"
    sleep 1
}

# Start Installation
show_banner
echo -e "${GREEN}[+] Starting Installation of Vampire-Hub-X...${NC}"
sleep 1

# Update Termux
echo -e "${CYAN}[+] Updating & upgrading packages...${NC}"
pkg update -y && pkg upgrade -y

# Required Tools
echo -e "${CYAN}[+] Installing required packages...${NC}"
pkg install -y python git curl wget unzip zip figlet toilet

# Fix pip issues and install Python build tools
echo -e "${CYAN}[+] Fixing pip & installing Python build essentials...${NC}"
pip install --upgrade pip setuptools wheel cython --break-system-packages > /dev/null 2>&1

# Install from requirements.txt if exists
if [ -f "requirements.txt" ]; then
    echo -e "${CYAN}[+] Installing Python dependencies from requirements.txt...${NC}"
    pip install -r requirements.txt --break-system-packages || {
        echo -e "${YELLOW}[!] Warning: Issue with requirements.txt, using fallback...${NC}"
    }
fi

# Manually ensure essential modules
echo -e "${CYAN}[+] Verifying Python modules...${NC}"
pip install requests pyfiglet colorama termcolor --break-system-packages > /dev/null 2>&1

# Final Touch
show_banner
figlet -f slant "Install Complete" | lolcat 2>/dev/null || echo -e "${GREEN}Install Complete${NC}"
echo -e "\n${GREEN}[+] Tool is ready to use!${NC}"
echo -e "${YELLOW}[>] Run with:${NC} ${CYAN}python3 vampire_hub_x.py${NC}"
echo -e "${YELLOW}[>] For help, type:${NC} ${CYAN}--help${NC}\n"

exit 0
