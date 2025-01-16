# Copyright (c) 2025 Mo78amad

print('Starting...')
import os
import time
import sys
import requests  # Added this import for webhook requests
import colorama

def print_ascii_art():
    ascii_art = """
         ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗ █████╗ ██╗  ██╗
         ██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝██╔══██╗██║  ██║
         ███████║██║   ██║██║   ██║█████╔╝ ███████║███████║
         ██╔══██║██║   ██║██║   ██║██╔═██╗ ██╔══██║██╔══██║
         ██║  ██║╚██████╔╝╚██████╔╝██║  ██╗██║  ██║██║  ██║
         ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝

          Hookah - Discord Webhook Spammer
                  Created by @Mo78amad
    """
    print(colorama.Fore.GREEN + ascii_art + colorama.Style.RESET_ALL)

def set_title():
    title = "Discord Webhook Spammer"
    try:
        os.system(f"title {title}")
    except:
        pass  # Handle environments where setting the title is not allowed

# Directly call set_title to avoid threading issues
set_title()

print_ascii_art()

def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)

def webhook_spammer():
    colorama.init(autoreset=True)
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Webhook: ")
            webhook = input("")
            r_check = requests.get(webhook)
            if r_check.status_code == 200:
                break
            else:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Webhook Invalid, Please Enter A Valid One")
        except Exception:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Webhook Invalid, Please Enter A Valid One")

    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Enter Message: ")
    content = input("")

    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Want An Avatar (y/n): ")
        avatar_y_n = input("").lower()
        if avatar_y_n in ["y", "n"]:
            break
        else:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print015("Enter A Valid Choice")

    avatar_url = ""
    if avatar_y_n == "y":
        while True:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Avatar Url: ")
            avatar_url = input("")
            if avatar_url.startswith("http://") or avatar_url.startswith("https://"):
                break
            else:
                sys.stdout.write(colorama.Fore.CYAN + "> ")
                print015("Enter A Valid Choice")

    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Enter Bot Username: ")
    username = input("")

    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Enter Limit (i for infinity): ")
        limit = input("").lower()
        if limit == "i":
            break
        try:
            limit = int(limit)
            break
        except ValueError:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print015("Enter A Valid Choice")

    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Delay (0 For None): ")
            delay = float(input(""))
            break
        except ValueError:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print015("Enter A Valid Choice")

    den = 0
    if limit == "i":
        while True:
            r = requests.post(webhook, json={"avatar_url": avatar_url, "username": username, "content": content})
            if r.status_code == 204:
                den += 1
                print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{den}{colorama.Fore.CYAN}/INFINITY{colorama.Fore.CYAN}]{colorama.Fore.RESET} Sent Message To The {colorama.Fore.CYAN}Webhook")
            elif r.status_code == 429:
                print(f"{colorama.Fore.RED}[{colorama.Fore.RESET}ERROR{colorama.Fore.RED}]{colorama.Fore.RESET} Rate Limited, {colorama.Fore.RED}Retrying")
            if delay > 0:
                time.sleep(delay)
    else:
        for _ in range(limit):
            while True:
                r = requests.post(webhook, json={"avatar_url": avatar_url, "username": username, "content": content})
                if r.status_code == 204:
                    den += 1
                    print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{den}{colorama.Fore.CYAN}/{limit}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Sent Message To The {colorama.Fore.CYAN}Webhook")
                    break
                elif r.status_code == 429:
                    print(f"{colorama.Fore.RED}[{colorama.Fore.RESET}ERROR{colorama.Fore.RED}]{colorama.Fore.RESET} Rate Limited, {colorama.Fore.RED}Retrying")
                if delay > 0:
                    time.sleep(delay)

    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Done Spamming Webhook, Press Enter To Close The Program")
    input("")
    exit()

webhook_spammer()
