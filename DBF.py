import requests
from time import sleep
import os
import socket

name_devices = socket.gethostname()
# while True:
if "help" :
    # === password ===    
    os.system("cls")
    print(f"          DIRECTORY BRUTE FORCE")
    print()
    password = input(f"PASSWORD 🔐: ")
    if password == "b7tvbt34tmhdyqw6":
        # === menu ===        
        os.system("cls")
        print(f"                       DBF")
        print(f"          ──────────────────────────────")
        print(f"              DIRECTORY BRUTE FORCE")
        print(f"                      V1.0.1")
        print(f"                   cyborg-prjkt")
        print(f"          ──────────────────────────────")
        print()
        print(f"               url example: site.com")
        print()
        print(f"┌──( @"+name_devices+" )-[~/DBF]")
        print(f"│")
        url = input(f"├─$ URl ")
        print(f"│")
        wordlist = input(f"└─$ WORDLIST ")

        with open(wordlist, "r") as file:
            file = [line.strip() for line in file.readlines()]


        for word in file:
            dbf = url + "/" + word
            response = requests.get(dbf)
            if response.status_code == 200:
                print(f"[+] {dbf} - {response.status_code}")       