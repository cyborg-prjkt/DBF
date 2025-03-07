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
    print("                      V1.0.1")
    print("                   cyborg-prjkt")
    print("          ──────────────────────────────")
    print()
    print("       ex: https://site.com | http://site.com")
    print()
    print("┌──( @"+name_devices+" )-[~/DBF]")
    print("│")
    url = input("└─$ URL ")

    wrdlst = "worldlist.txt"
    with open(wrdlst, 'r') as file:
        worldlist = [line.strip() for line in file.readlines()]

    for word in worldlist:
        dbf = url + "/" + word
        response = requests.get(dbf)
        if response.status_code == 200:
            print("[+] {dbf} - {response.status_code}")    