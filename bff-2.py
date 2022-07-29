#-------------------------------------->
# *recode mulu pleer 
#-------------------------------------->
# *Coding by Romi Afrizal
# *Name tool bff-2 <--- don't remove name bff-2
# *version 1.3

import os, sys, shutil, subprocess
	
#--- CEK VERSI PYTHON
if sys.version_info.major != 3:
	exit("\n\t\x1b[0m type: python bff-2.py\n")

#--- INSTALL MODULE
try:
	import requests, bs4, mechanize, concurrent.futures, rich
except ImportError as ngontol:
	print ('\n\t\x1b[0m $ install module ...\n')
	os.system("python -m pip install --upgrade pip && pip install "+ngontol)
	os.system("rm -rf data/indo.txt && rm -rf data/english.txt && rm -rf data/pengguna.txt")

try: # music mp3
	bff_2 = open(os.devnull, "w")
	my_music = subprocess.call(["dpkg","-s","play-audio"],stdout=bff_2,stderr=subprocess.STDOUT)
	bff_2.close()
	if my_music !=0:
		os.system('pkg install play-audio' )
except FileNotFoundError:
	os.system('pkg install play-audio' )

#--- FILE DIRECTORY
from romz import romz_xyz_ganteng_banget
	
runtah = [
			"romz/__pycache__",
			"log/__pycache__",
			"xyz/__pycache__"
		]
try:
	[shutil.rmtree(xz) for xz in runtah]
except: 
	pass
romz_xyz_ganteng_banget() 
