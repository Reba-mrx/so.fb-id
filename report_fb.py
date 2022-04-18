import os, sys, time
import os
P = '\x1b[91m'
H = '\x1b[95m'
G = '\x1b[97m'
K = '\x1b[92m'
os.system('clear')
logo = """ \n\033[1;31m  _______     ______    ______     _______ \n\033[1;31m (  ____ )  (  ____ \  (  ___ \   (  ___  )\n | (    )|  | (    \/  | (   ) )  | (   ) |\n\033[1;31m | (____)|  | (__      | (__/ /   | (___) |\n |     __)  |  __)     |  __ (    |  ___  |\n\033[1;31m | (\ (     | (        | (  \ \   | (   ) |\n | ) \ \__  | (____/\  | )___) )  | )   ( |\n\033[1;31m |/   \__/  (_______/  |/ \___/   |/     \|\n\033[1;31m-------------------------------------------------\n\033[1;33m COD BY Reba  """
def Loads():
    for i in range(101):
        time.sleep(0.3)
        sys.stdout.write(G + '\r ' + P + 'PLZZ WAIT : %d%%' % i)
        sys.stdout.flush()


def Report():
    for d in range(101):
        time.sleep(0.2)
        sys.stdout.write(G + '\r ' + P + 'REPORT PROCESSING ... [%d%%] ' % d)
        sys.stdout.flush()

print '' * 49 + H
print(logo)

print P + '=' * 49
B = raw_input(G + '' + K + ' ID fesbook : ')
print '=' * 49
if not B.startswith('1000'):
    print '[!] ID INVILED'
    sys.exit()
    print '=' * 49
Loads()
time.sleep(3)
print ''
print '=' * 49
a = 1
while True:
    print ('{} {}REPORTING PROCESS DONE [{}] => {}{}').format(G, P, a, H, B)
    print ('{} | {}{}\x1b[92mOK BY REBA').format(Report(), K, G)
    print '=' * 49
    a += 1

