# MODUL IN PYTHON 
# rikod mulu si plerr
import os,sys,requests, re, bs4, json, time,random, datetime
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
from random import randint

# MODUL IN RICH
from rich import print as tulis
from rich.panel import Panel

#--- WARNA RICH
Te = '[b]' # tebal 
P = '[#FFFFFF]' # putih
U = '[#AF00FF]' # ungu
O = '[#00FFFF]' # biru muda
M = '[#FF0022]' # merah
Pi = '[#FF0099]' # pink
H = '[#00FF33]' # hijau
K = '[#FFFF00]' # kuning

#--- WARNA ANSII (PYTHON)
m = '\x1b[1;91m' # merah
h = '\x1b[1;92m' # hijau
k = '\x1b[1;93m' # kuning
b = '\x1b[1;94m' # biru
u = '\x1b[1;95m' # ungu
o = '\x1b[1;96m' # biru muda
p = '\x1b[1;97m' # putih
j = '\033[38;2;255;127;0;1m' # orange
n = '\x1b[0m' # clear
til = '•'
ansixx = random.choice([m, h, k, b, u, o, p, j])

"""

       fiks sekali di ubah error                                                                                                                                                                                                                                                                                                                                                                                                                                                                           CODING BY GUWEH ROMI AFRIZAL :v

"""