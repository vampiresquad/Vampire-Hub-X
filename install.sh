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

# Installation Check Function
check_installation() {
  echo -e "\e[1;34m[+] Checking dependencies... \e[0m"

  # List of essential tools
  tools=("curl" "python3" "git" "nmap" "whois" "pkg" "apt")

  # Check each tool
  for tool in "${tools[@]}"
  do
    echo -e "\e[1;36m[*] Checking for $tool...\e[0m"
    if ! command -v $tool &> /dev/null; then
      echo -e "\e[1;31m[!] $tool is not installed. Attempting to install...\e[0m"
      if [[ "$tool" == "pkg" || "$tool" == "apt" ]]; then
        sudo apt update && sudo apt install -y $tool
      else
        sudo apt install -y $tool
      fi
    else
      echo -e "\e[1;32m[✔] $tool is already installed.\e[0m"
    fi
  done
}

# Error Fix Function
auto_fix() {
  echo -e "\e[1;33m[+] Attempting to auto-fix common issues...\e[0m"

  # Fix broken packages (for Ubuntu/Debian-based systems)
  sudo apt update && sudo apt upgrade -y
  sudo apt --fix-broken install -y
  sudo apt autoremove -y

  # Installing missing Python dependencies
  echo -e "\e[1;36m[*] Installing Python dependencies... \e[0m"
  python3 -m pip install --upgrade pip
  python3 -m pip install -r requirements.txt

  echo -e "\e[1;32m[+] All issues fixed and dependencies installed.\e[0m"
}

# Installation Process
install_process() {
  echo -e "\e[1;36m[+] Starting the installation process... \e[0m"
  banner
  check_installation
  auto_fix
  echo -e "\e[1;32m[+] Installation completed successfully.\e[0m"
}

# Usage Guide
usage() {
  echo -e "\e[1;33m[+] Usage Instructions:\e[0m"
  echo -e "\e[1;32m1. Run the installation script using the following command:\e[0m"
  echo -e "\e[1;36m   bash install.sh\e[0m"
  echo -e "\e[1;32m2. Follow the prompts to ensure all dependencies are installed and configured properly.\e[0m"
  echo -e "\e[1;32m3. Once the installation is complete, you can start the tool by running:\e[0m"
  echo -e "\e[1;36m   python3 vampire_hub_x.py\e[0m"
  echo -e "\e[1;32m4. For more help and options, consult the tool's documentation or type 'help' in the command line.\e[0m"
}

# Main function to run the installation
main() {
  install_process
  usage
}

# Start the installation
main
