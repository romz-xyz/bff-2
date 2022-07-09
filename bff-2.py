import os, sys, platform, subprocess, shutil
from romz import menu as awikwok
#--- INSTALL MODULE
try:
	import rich
except ImportError:
	print ('\n\t\x1b[0m╰─  mohon tunggu... \n')
	os.system('pip install rich')
try:
	import requests
except ImportError:
	os.system('pip install requests')
try:
	import concurrent.futures
except ImportError:
	os.system('pip install futures')
try:
	import bs4
except ImportError:
	os.system('pip install bs4')
try:
	import mechanize
except ImportError:
	os.system('pip install mechanize')
#--- INSTALL MUSIK
try:
	bff_2 = open(os.devnull, "w")
	my_music = subprocess.call(["dpkg","-s","play-audio"],stdout=bff_2,stderr=subprocess.STDOUT)
	bff_2.close()
except FileNotFoundError:
	os.system('pkg install play-audio')
	
runtah=["romz/__pycache__","xyz/__pycache__","log/__pycache__"]

if __name__=="__main__":
	os.system("git pull")
	awikwok.Menu()