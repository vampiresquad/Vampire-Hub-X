#!/bin/bash

Colors

r='\033[1;31m' g='\033[1;32m' y='\033[1;33m' b='\033[1;34m' c='\033[1;36m' w='\033[1;37m' res='\033[0m'

Banner

banner() { clear echo -e "${r} ██╗░░██╗░█████╗░███╗░░░███╗██████╗░██╗███╗░░██╗ ██║░██╔╝██╔══██╗████╗░████║██╔══██╗██║████╗░██║ █████═╝░███████║██╔████╔██║██████╔╝██║██╔██╗██║ ██╔═██╗░██╔══██║██║╚██╔╝██║██╔═══╝░██║██║╚████║ ██║░╚██╗██║░░██║██║░╚═╝░██║██║░░░░░██║██║░╚███║ ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚══╝ ${y}       [ Vampire-Hub-X Installer ] ${c}       Coded by: Muhammad Shourov ${res}" }

Fix pip block in Termux

fix_pip_termux() { if command -v termux-info &>/dev/null; then if ! command -v pip &>/dev/null; then echo -e "${y}[•] Installing pip workaround...${res}" pkg install python -y curl -sS https://bootstrap.pypa.io/get-pip.py | python fi fi }

Install dependencies

install_deps() { echo -e "${g}[+] Installing required packages...${res}" if command -v apt &>/dev/null; then apt update -y && apt upgrade -y apt install python3 git curl -y elif command -v pkg &>/dev/null; then pkg update -y && pkg upgrade -y pkg install python git curl -y fi

fix_pip_termux

echo -e "${g}[+] Installing Python modules...${res}"
pip install requests > /dev/null 2>&1

}

Run the tool

run_tool() { echo -e "${b}[•] Starting Vampire-Hub-X...${res}" chmod +x vampire_hub_x.py python3 vampire_hub_x.py }

Start

banner install_deps run_tool

