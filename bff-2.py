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
		
	try: # install module
		import requests, bs4, mechanize, concurrent.futures, rich
	except (ImportError,ModuleNotFoundError) as ngontol:
		print ('\n\t\x1b[0m $ install module ...\n')
		os.system("python -m pip install --upgrade pip && pip install "+str(ngontol))
		os.system("rm -rf data/indo.txt && rm -rf data/english.txt && rm -rf data/pengguna.txt")
	
	try: # music mp3
		bff_2 = open(os.devnull, "w")
		my_music = subprocess.call(["dpkg","-s","play-audio"],stdout=bff_2,stderr=subprocess.STDOUT)
		bff_2.close()
		if my_music !=0:
			os.system('pkg install play-audio' )
	except FileNotFoundError:
		os.system('pkg install play-audio' )
			
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
		
