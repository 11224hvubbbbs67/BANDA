import sys
import os
import socket
import hashlib
import time
from googlesearch import *
###############################
os.system("clear")
print("""\033[0;34m
..............
            ..,;:ccc,.
          ......''';lxO.
.....''''..........,:ld;
           .';;;:::;,,.x,
      ..'''.            0Xxoc:,.  ...
  ....                ,ONkc;,;cokOdc',.
 .                   OMo           ':c1}o.
                    dMc               :OO;
                    0M.                 .:o.
                    ;Wd                      ____ _   _  ___  ____ _____
                     ;XO,                   / ___| | | |/ _ \/ ___|_   _|
                    ..',;:cdOOd::.,        | |  _| |_| | | | \___ \ | |
                                .:d;.      | |_| |  _  | |_| |___) || |
                                   'd,  .'  \____|_| |_|\___/|____/ |_|
                                     ;l   ..
                                       .o
                                          c
                                            .'
                                             . \033[0;31m  by obaida """)

print("""\033[0;32m
[1] PortScanner
[2] search for website with sqli
[3] Hasher

[X] exit
""")

a = input("BANDA > ")

if a == "1":
    os.system("clear")
    print('''\033[0;32m
     ____            _   ____
    |  _ \ ___  _ __| |_/ ___|  ___ __ _ _ __  _ __   ___ _ __
    | |_) / _ \| '__| __\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
    |  __/ (_) | |  | |_ ___) | (_| (_| | | | | | | |  __/ |
    |_|   \___/|_|   \__|____/ \___\__,_|_| |_|_| |_|\___|_|''')
    print("\033[0;31m make by OBAIDA")
    time.sleep(1)
    ip = input("\033[0;33m --ENTER IP--/")
    try:
        for port in range(0,65335):
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            if (s.connect_ex((ip,port))==0):
                try:
                    serv = socket.getservbyport(port)
                except socket.error:
                    serv="not-found"

                print(("the PORT %s:OPEN  Service:%s  "%(port,serv)))

        print("Scanning Completed Good By :)  %s!!")


    except KeyboardInterrupt:
        print("""
        COOD  BYE :( """)
        sys.exit

elif a == "2":
    os.system("clear")
    print("""\033[0;32m
     ____   ___  _     _
    / ___| / _ \| |   (_)
    \___ \| | | | |   | |
     ___) | |_| | |___| |
    |____/ \__\_\_____|_|""")
    print("\033[0;31m by obaida")
    time.sleep(1)
    h = input("\033[0;33m ENTER SQL DORK : ")
    for url in search(h):
        print("""\033[0;32m
        URL IS : """+url)

elif a == "3":
    os.system("clear")
    print("""

     _   _    _    ____  _   _ _____ ____
    | | | |  / \  / ___|| | | | ____|  _ \
    | |_| | / _ \ \___ \| |_| |  _| | |_) |
    |  _  |/ ___ \ ___) |  _  | |___|  _ <
    |_| |_/_/   \_\____/|_| |_|_____|_| \_\

    """)
    print("\033[0;33m by obaida")
    print(" ")
    time.sleep(1)
    text = str(input("--ENTER TEXT--/ "))
    time.sleep(1)
    hash_type = str(input("--ENTER HASH TYPE--/ "))
    text = text.encode("utf-8")
    hash_hash = hashlib.new(hash_type)
    hash_hash.update(text)
    hasher = hash_hash.hexdigest()
    time.sleep(1)
    print(" HASH IS : "+hasher)
elif a == "X" or a == "x":
    print("""
    GOOD BYE :(
    """)

else:
    print("wrong ...")
    time.sleep(1)
    os.system("python banda.py")
