#!/usr/bin/python3

#####################################################
## Dark Operating System (DrkOS)                   ##
## A tool for Operating Systems                    ##
## https://voidsecurity.ml                         ##
## Coded by: drk                                   ##
##                                                 ##
#####################################################

# Imports
import os
import sys 
import platform
from colorama import Fore
import pyfade
import time
import socket
import re
import uuid
import json
import psutil
import logging
# Code/Defines
def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')
def back():
    input(f"{Fore.YELLOW}Press enter to go back.")
def banner():
  print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_cyan, """
   DRK OS Alpha (0.9)
    ██████╗ ██████╗ ██╗  ██╗     ██████╗ ███████╗
    ██╔══██╗██╔══██╗██║ ██╔╝    ██╔═══██╗██╔════╝
    ██║  ██║██████╔╝█████╔╝     ██║   ██║███████╗
    ██║  ██║██╔══██╗██╔═██╗     ██║   ██║╚════██║
    ██████╔╝██║  ██║██║  ██╗    ╚██████╔╝███████║
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝                                              
                                                                          """))
def options():
    banner()
    print("""
    [1] Basic OS Info
    [2] Spoofer (Under Development)
    [3] Coming Soon

    [4] Quit
    
    """)
    USER_OPTION = input(f"Option\n{Fore.RED}>")
    if USER_OPTION == "1":
        clearcmd()
        print("Getting Information...")
        time.sleep(1.5)
        clearcmd()
        print(f"{Fore.LIGHTWHITE_EX}DRK OS BY{Fore.YELLOW} DRK#1337\n\n ")
        getSysInfo()
        print("\n")
        back()
        clearcmd()
        options()

    elif USER_OPTION == "2":
        pass
    elif USER_OPTION == "3":
        pass
    elif USER_OPTION == "4":
        clearcmd()
        quit()

def getSysInfo():
    print(f"{Fore.LIGHTWHITE_EX}System: {Fore.GREEN}{platform.system()}")
    print(f"{Fore.LIGHTWHITE_EX}Platform-Release: {Fore.GREEN}{platform.release()}")
    print(f"{Fore.LIGHTWHITE_EX}Architecture: {Fore.GREEN}{platform.machine()}")
    print(f"{Fore.LIGHTWHITE_EX}Local IP: {Fore.GREEN}{socket.gethostbyname(socket.gethostname())}")
    print(f"{Fore.LIGHTWHITE_EX}Mac Address: {Fore.GREEN}{':'.join(re.findall('..', '%012x' % uuid.getnode()))}")


# Main Code
def main():
    try:
        clearcmd()
        options()
        
    except KeyboardInterrupt:
        print(f"Interrupted. {Fore.RED}Quitting..")
        time.sleep(1)
        clearcmd()
        quit()

main()
