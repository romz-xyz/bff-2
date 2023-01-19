#     *Brute Force Facebook (BFF)²
#     *file name: hasil.py
#     *copyright: (C) © 2022 ~ Romi Afrizal
#     *contact me on whatsap: +6281273018924

from xyz import *
from time import sleep as jeda
from datetime import datetime
from romz.banner import Banner as ld

oke = []
cepe = []

#--- CEK HASIL FACEBOOK
def hasil_fb():
	tulis(Panel(f"{Te}{U} •{P} 01 {O}Cek hasil akun {H}OK \n{U} •{P} 02 {O}Cek hasil akun {K}CP \n{U} •{P} 03 {O}Hapus hasil crack \n{U} •{M} 00 {O}Kembali",style='#FF0022'))
	rom = input('%s╰─%s Pilih %s>%s '%(p,o,m,k))
	if rom in['']:
		print ('%s╰─%s isi yang benar'%(p,m));jeda(2)
		os.system("python bff-2.py")
	elif rom in['1','01']: 
		try:
			dirs = os.listdir('OK')
			for file in dirs:
				oke.append(file)
		except:pass 
		if len(oke)==0:
			exit("%s╰─ %sfile tidak tersedia "%(p,m))
		else:
			tulis(Panel(f"{Te}{U} •{O} Hasil akun{H} OK{O} yang tersimpan di folder anda ",style='#FF0022'))
			nomor = 0
			for i in oke:
				fil = open(f"OK/{i}").read().splitlines() 
				nomor+=1
				print(f"{p} {str(nomor)}.{h} {i} {o}-{h} {str(len(fil))} ")
			tulis(Panel(f"{Te}{U} •{O} Silahkan pilih nomor yang ingin di cek ",style='#FF0022'))
			file = input(f"{p}╰─{o} nomor {m}>{h} ")
			try:
				hasil = oke[int(file)-1]
			except (KeyError,IndexError,ValueError):
				exit ('%s╰─%s isi yang benar kentod'%(p,m));jeda(2)
			nm_file = hasil.replace("-", " ")
			file_nm = nm_file.replace('.txt', '')
			totalok = open(f"OK/{hasil}", "r").read().splitlines()
			tulis(Panel(f"{Te}{U} •{O} hasil tanggal{M} : {H}{file_nm} {O}total {M}: {H}{len(totalok)}",style='#FF0022'))
			for ngontol in totalok:
				kontol = ngontol.replace("\n","")
				pukimek = kontol.replace(" *--> ","\x1b[1;97m╰───\x1b[1;92m ")
				print('%s'%(pukimek));jeda(0.07)
			print ('')
			exit()
	elif rom in['2','02']: 
		try:
			dirs = os.listdir('CP')
			for file in dirs:
				cepe.append(file)
		except:pass 
		if len(cepe)==0:
			exit("%s╰─ %sfile tidak tersedia"%(p,m))
		else:
			tulis(Panel(f"{Te}{U} •{O} Hasil akun{H} OK{O} yang tersimpan di folder anda ",style='#FF0022'))
			nomor = 0
			for i in cepe:
				fil = open(f"CP/{i}").read().splitlines() 
				nomor+=1
				print(f"{p} {str(nomor)}.{k} {i} {o}-{k} {str(len(fil))} ")
			tulis(Panel(f"{Te}{U} •{O} Silahkan pilih nomor yang ingin di cek ",style='#FF0022'))
			file = input(f"{p}╰─{o} nomor {m}>{k} ")
			try:
				hasil = cepe[int(file)-1]
			except (KeyError,IndexError,ValueError):
				exit ('%s╰─%s isi yang benar kentod'%(p,m));jeda(2)
			nm_file = hasil.replace("-", " ")
			file_nm = nm_file.replace('.txt', '')
			totalcp = open(f"CP/{hasil}", "r").read().splitlines()
			tulis(Panel(f"{Te}{U} •{O} hasil tanggal{M} : {K}{file_nm} {O}total {M}: {K}{len(totalcp)}",style='#FF0022'))
			for ngontol in totalcp:
				kontol = ngontol.replace("\n","")
				pukimek = kontol.replace(" *--> ","\x1b[1;97m╰───\x1b[1;93m ")
				print('%s'%(pukimek));jeda(0.07)
			print ('')
			exit()
	elif rom in['3','03']:
		os.system('rm -rf CP/*.txt && rm -rf OK/*.txt');print('')
		ld().loads()
		jalan (f'{m} berhasil menghapus hasil crack ');jeda(2)
		os.system("python bff-2.py")
	elif rom in['0','00']:
		os.system("python bff-2.py")
	else:
		print ('\n%s╰─%s isi yang benar kentod'%(p,m));jeda(2)
		os.system("python bff-2.py")

#--- JALAN
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)