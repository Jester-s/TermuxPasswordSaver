import os
import sys
import colorama
colorama.init()
from colorama import Fore, Back, Style

try:
    print(Fore.LIGHTRED_EX + "Page:" + Fore.WHITE)
    page = input()
    print(Fore.LIGHTRED_EX + "Username:" + Fore.WHITE)
    nick = input()
    print(Fore.LIGHTRED_EX + "Pasword:" + Fore.WHITE)
    password = input()
except:
    print(Fore.RED + "ERROR:" + Fore.WHITE + "Enterning Value")


pagenickpass = ("Page:" + page + " " + "Username:" + nick + " " + "Password:" + password)

file = open("data.termux", "a")
file.write(pagenickpass + "\n")