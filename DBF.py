import requests
from time import sleep
import os
import socket
import pwinput

name_devices = socket.gethostname()
# while True:
if "help" :
    # === password ===    
    os.system("clear")
    print("          DIRECTORY BRUTE FORCE")
    print()
    password = pwinput.pwinput("PASSWORD 🔐: ",mask="*")
    if password == "b7tvbt34tmhdyqw6":
        # === menu ===        
        os.system("clear")
        print("                       DBF")
        print("          ──────────────────────────────")
        print("              DIRECTORY BRUTE FORCE")
        print("                      V1.0.1")
        print("                   cyborg-prjkt")
        print("          ──────────────────────────────")
        print()
        print("               url example: site.com")
        print()
        print("┌──( @"+name_devices+" )-[~/DBF]")
        print("│")
        url = input("├─$ URl ")
        print("│")
        wordlist = input("└─$ WORDLIST ")

        with open(wordlist, "r") as file:
            file = [line.strip() for line in file.readlines()]


        for word in file:
            dbf = url + "/" + word
            response = requests.get(dbf)
            if response.status_code == 200:
                print("[+] {dbf} - {response.status_code}")       