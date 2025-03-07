import requests
from time import sleep
import os
import socket
import pwinput

name_devices = socket.gethostname()
# === password ===    
os.system("cls" if os.name == "nt" else "clear")
print("          DIRECTORY BRUTE FORCE")
print()
password = pwinput.pwinput("PASSWORD 🔐: ",mask="*")
if password.lower() == "b7tvbt34tmhdyqw6":
    # === menu ===        
    os.system("cls" if os.name == "nt" else "clear")
    print("                       DBF")
    print("          ──────────────────────────────")
    print("              DIRECTORY BRUTE FORCE")
    print("                      V1.1.0")
    print("                   cyborg-prjkt")
    print("          ──────────────────────────────")
    print()
    print("       ex: https://site.com/ | http://site.com/")
    print()
    print("┌──( @"+name_devices+" )-[~/DBF]")
    print("│")
    url = input("└─$ URL ")

    if not url.endswith("/"):
        url += "/"

    wordlist_path = "worldlist.txt"

    if not os.path.exists(wordlist_path):
        print("\n[!] ERROR: File wordlist not found!")
        exit()

    with open(wordlist_path, 'r') as file:
        worldlist = [line.strip() for line in file.readlines()]

    print("\n[+] Scanning directories...\n")

    for word in worldlist:
        target_url = url + word
        try:
            response = requests.get(target_url, timeout=5)
            if response.status_code == 200:
                print(f"[✔] FOUND: {target_url} [Status: {response.status_code}]")
            elif response.status_code == 403:
                print(f"[!] FORBIDDEN: {target_url} [Status: {response.status_code}]")
            else:
                print(f"[-] Not Found: {target_url} [Status: {response.status_code}]")
        except requests.exceptions.RequestException:
            print(f"[!] ERROR: Unable to access {target_url}")

        sleep(0.5)
else:
    print("\n[✖] WRONG PASSWORD!")