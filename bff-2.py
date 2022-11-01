#-------------------------------------->
#     *recode mulu pleer 
#-------------------------------------->
#     *Coding by Romi Afrizal
#     *Name tool bff-2 <--- don't remove name bff-2
#     *version 1.3
	
#--- JALANKAN TOOL
if __name__=="__main__":
	import os, sys, shutil, subprocess 
	if sys.version_info.major != 3: # cek versi python 
		exit("\n\t\x1b[0m type: python bff-2.py \n")
	
	# Don't delete the --> coox <-- file, you will get an error
	coox = ("rm -rf data/indo.txt && rm -rf data/english.txt && rm -rf data/pengguna.txt")
	try: # install module
		import requests 
	except ImportError:
		print ('\n\t\x1b[0m $ install module requests ...\n')
		os.system("python -m pip install --upgrade pip && pip install requests")
		os.system(coox)
	try:
		import bs4 
	except ImportError:
		print ('\n\t\x1b[0m $ install module bs4 ...\n')
		os.system("python -m pip install --upgrade pip && pip install bs4")
		os.system(coox)
	try:
		import mechanize 
	except ImportError:
		print ('\n\t\x1b[0m $ install module mechanize ...\n')
		os.system("python -m pip install --upgrade pip && pip install mechanize")
		os.system(coox)
	try:
		import concurrent.futures 
	except ImportError:
		print ('\n\t\x1b[0m $ install module futures ...\n')
		os.system("python -m pip install --upgrade pip && pip install futures")
		os.system(coox)
	try:
		import rich 
	except ImportError:
		print ('\n\t\x1b[0m $ install module rich ...\n')
		os.system("python -m pip install --upgrade pip && pip install rich")
		os.system(coox)
		
	try: # music mp3
		bff_2 = open(os.devnull, "w")
		my_music = subprocess.call(["dpkg","-s","play-audio"],stdout=bff_2,stderr=subprocess.STDOUT)
		bff_2.close()
		if my_music !=0:
			os.system('pkg install play-audio' )
			#os.system(coox)
	except FileNotFoundError:
		os.system('pkg install play-audio' )
		#os.system(coox)
			
	from romz import romz_xyz_ganteng_banget as onichan
	from shutil import rmtree as lolichan
	runtah = [
		"romz/__pycache__",
		"log/__pycache__",
		"xyz/__pycache__"
	]
	try:
		[lolichan(xz) for xz in runtah]
	except: 
		pass 
	os.system('git pull')
	onichan() 
		
