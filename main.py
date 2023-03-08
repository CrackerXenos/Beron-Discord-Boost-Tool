import httpx
import random
import time
import datetime
import json
import os
import hashlib
from keyauth import *
import colorama
from colorama import Fore, Back, Style

if os.name == 'nt':
    import ctypes

def cls():
    if os.name == 'nt':
        os.system('cls')

if os.name == 'nt':
    ctypes.windll.kernel32.SetConsoleTitleW('Cracked By Xenos#1181')



keyauthapp = api('Boost Tool', '5n86P9Ufi4', 'bb0061b5ef7b75c81862521e256e97fdf65e700d65d7b7046c475e51a2377a20', '1.0', ('name', 'ownerid', 'secret', 'version'))
cls()



print(Fore.CYAN + 'cracked by Xenos#1181.' + Fore.RESET)
time.sleep(5)




def getinviteCode(invite_input):
    if 'discord.gg' not in invite_input:
        return invite_input
    if None in invite_input:
        invite = invite_input.split('discord.gg/')[1]
        return invite
    if None in invite_input:
        invite = invite_input.split('https://discord.gg/')[1]
        return invite
    if None in invite_input:
        invite = invite_input.split('/invite/')[1]
        return invite


def menu():
    print(Fore.MAGENTA + f'''
 /$$   /$$                                           /$$ /$$     /$$     /$$    /$$$$$$    /$$  
| $$  / $$                                          / $$/ $$   /$$$$   /$$$$   /$$__  $$ /$$$$  
|  $$/ $$/  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$$$$$|_  $$  |_  $$  | $$  \ $$|_  $$  
 \  $$$$/  /$$__  $$| $$__  $$ /$$__  $$ /$$_____/|   $$  $$_/  | $$    | $$  |  $$$$$$/  | $$  
  >$$  $$ | $$$$$$$$| $$  \ $$| $$  \ $$|  $$$$$$  /$$$$$$$$$$  | $$    | $$   >$$__  $$  | $$  
 /$$/\  $$| $$_____/| $$  | $$| $$  | $$ \____  $$|_  $$  $$_/  | $$    | $$  | $$  \ $$  | $$  
| $$  \ $$|  $$$$$$$| $$  | $$|  $$$$$$/ /$$$$$$$/  | $$| $$   /$$$$$$ /$$$$$$|  $$$$$$/ /$$$$$$
|__/  |__/ \_______/|__/  |__/ \______/ |_______/   |__/|__/  |______/|______/ \______/ |______/

\nChoose Your Option:\n1. Boost Server\n2. View Stock\n3. Exit      \n
                                                                                                
                                                                                                
                                                                                                
    ''' + Fore.RESET)
    choice = input(f'''{Fore.MAGENTA}[>] ''' + Fore.RESET)
    if choice == '1':
        invite = getinviteCode(input(f'''{Fore.MAGENTA}Invite Link/Code (Example: discord.gg/duyDkavjpV): {Fore.RESET}'''))
        amount = input(f'''{Fore.MAGENTA}Amount of Boosts: {Fore.RESET}''')
        if amount.isdigit() != True:
            print(Fore.RED + 'Amount cannot be a string.' + Fore.RESET)
            amount = input(f'''{Fore.MAGENTA}Amount of Boosts: {Fore.RESET}''')
            if not amount.isdigit() != True:
                months = input(f'''{Fore.MAGENTA}Number of months: {Fore.RESET}''')
                if amount.isdigit() != True:
                    print(Fore.RED + 'Months cannot be a string.' + Fore.RESET)
                    months = input(f'''{Fore.MAGENTA}Number of months: {Fore.RESET}''')
                    if not amount.isdigit() != True:
                        start = time.time()
                        boosted = thread_boost(invite, int(amount), int(months), config['nickname'])
                        end = time.time()
                        print()
                        sprint(f'''Boosted https://discord.gg/{invite} {variables.boosts_done} times in {round(end - start, 2)} seconds.''', True)
                        print()
                        input(Fore.MAGENTA + 'Press enter to return to menu' + Fore.RESET)
                        cls()
                        menu()
                        if choice == '2':
                            print(f'''{Fore.WHITE}1 Month Nitro Tokens: {len(open('input/1m_tokens.txt', 'r').readlines())}{Fore.RESET}''')
                            print(f'''{Fore.WHITE}1 Month Boosts: {len(open('input/1m_tokens.txt', 'r').readlines()) * 2}{Fore.RESET}''')
                            print()
                            print(f'''{Fore.WHITE}3 Month Nitro Tokens: {len(open('input/3m_tokens.txt', 'r').readlines())}{Fore.RESET}''')
                            print(f'''{Fore.WHITE}3 Month Nitro Tokens: {len(open('input/3m_tokens.txt', 'r').readlines()) * 2}{Fore.RESET}''')
                            print()
                            input(Fore.MAGENTA + 'Press enter to return to menu' + Fore.RESET)
                            cls()
                            menu()
    if choice == '3':
        quit()

if __name__ == '__main__':
    cls()
    menu()
