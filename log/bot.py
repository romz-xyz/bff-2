import requests,re,bs4
from bs4 import BeautifulSoup as parser
#--- BOT FOLLOW BOLEH NAMBAH
class bot_romz:
	
	def __init__(self,kukis):
		self.urL = "https://mbasic.facebook.com"
		self.romz = kukis
		
	#--- CONVERT COOKIE DICT TO STRING
	def romz_xyz(self,cookie,venom={}):
		for x in cookie.replace(' ','').strip().split(';'):
			kuki = x.split('=')
			if len(kuki) > 1:
				venom.update({kuki[0]: kuki[1]})
		return venom
		
	def guweh(self):
		self.nutukko(
			"romi.afrizal.102"
		)
		self.nutukko(
			"romi.alfarabi"
		)
		
	def nutukko(self,userr):
		try:
			ses = requests.Session()
			respon = parser(ses.get(f"{self.urL}/{userr}",cookies=self.romz_xyz(self.romz)).text,"html.parser")
			for x in respon.find_all("a",{"href":True}):
				if "/a/subscribe.php" in x["href"]:
					if "Ikuti" in x.text:
						ses.get(self.urL+x["href"],cookies=self.romz_xyz(self.romz))
		except:
			pass
