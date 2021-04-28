#!/usr/bin/python
# coding=utf-8
# Originally Written By:jam shahrukh
# Source : Python2"
# Donot Recode It. 

#Import module
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('termux-setup-storage -y')
    os.system('apt update && apt install nodejs -y')
    os.system('apt install ruby -y')
    os.system('python2 jam.py')
    
	
#Browser Setting
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_handle_robots(False)
br.set_handle_redirect(True)
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
br.addheader = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
def exit():
	print "[!] Exit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jam(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
os.system('git pull')
os.system('clear')
##### LOGO #####
banner = """
\033[1;91m  ██████████  \033[1;96m██████████  \033[1;93m█████████  \033[1;92m ▀
\033[1;91m  ███    ███  \033[1;96m███    ███  \033[1;93m███   ███  \033[1;92m███ 
\033[1;91m  ███         \033[1;96m███    ███  \033[1;93m███   ███  \033[1;92m███ 
\033[1;91m  ██████████  \033[1;96m██████████  \033[1;93m███   ███  \033[1;92m███ 
\033[1;91m         ███  \033[1;96m███    ███  \033[1;93m███   ███  \033[1;92m███  
\033[1;91m  ███    ███  \033[1;96m███    ███  \033[1;93m███   ███  \033[1;92m███  
\033[1;91m  ██████████  \033[1;96m███    ███  \033[1;93m███   ███  \033[1;92m███ \x1b[1;90mQUEEN
\033[1;94m══════════════════════════════════════════════
\033[1;90m➣ Author : \033[1;97mSTYLISH QUEEN
\033[1;90m➣ Github : \033[1;97mhttps://github.com/stylish-queen
\033[1;90m➣ Fb Page: \033[1;97mJam Shahrukh Official
\033[1;94m══════════════════════════════════════════════ """
# titik #
def tik():
	titik = [".   ","..  ","... "]
	for o in titik:
		print("\r[✔] Logging In "+o),;sys.stdout.flush();time.sleep(1)

back = 0
id = []

def reg():
    os.system('clear')
    print (banner)
    print ''
    print '\033[1;31;1mTake The Free Approval For Login'
    print ''
    time.sleep(1)
    
    try:
        to = open('/sdcard/.hst.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/blacklisted-shahrukh/sani/main/server').text
    if to in r:
	os.system('apt update && apt install nodejs -y')
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(6)
        ip()
    else:
        os.system('clear')
        print (banner)
        print '\tApproved Failed'
        print ' \033[1;92mYour Id Is Not Approved Already '
        print ' \033[1;92mCopy the id and send to Jam'
	print '\033[1;94m-------------------------------------'
        print ' \033[1;92mYour id: ' + to
	print '\033[1;94m-------------------------------------'
        raw_input('\033[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923053176060')
        reg()


def reg2():
    os.system('clear')
    print (banner)
    print '\tApproval not detected'
    print ' \033[1;92mCopy and press enter , then select whatsapp to continue'
    print '\033[1;94m-------------------------------------'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print '\033[1;94m-------------------------------------'
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923053176060')
    sav = open('/sdcard/.jam.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\033[1;92m Press enter to check Approval ')
    reg()


def ip():
    os.system('clear')
    print (banner)
    print '\tCollecting device info'
    print ''
    
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\033[1;92m Your ip: ' + ips
    time.sleep(2)
    print '\033[1;92m Your country: ' + country
    time.sleep(2)
    print '\033[1;92m Your region: ' + regi
    time.sleep(2)
    print ' \033[1;92mYour network: ' + network
    time.sleep(1)
    print '\033[1;94m-------------------------------------'
    print ' Loading ...'
    time.sleep(1)
    methodlogin()

##### Login Method #####


def methodlogin():
    try:
        toket = open('login.txt','r')
	os.system('python2 sani.py')
    except (KeyError,IOError):
	os.system('clear')
	print banner
	print "[1] Login With ID/Password."
	print "[2] Login Using Token."
	print "[0] Exit."
	print ('      ')
	hos = raw_input("\nChoose Option >>  ")
	if hos =="":
		print"[!]  Wrong Input"
		exit()
	elif hos =="1":
		login()
	elif hos =="2":
		os.system('clear')
		print banner
		hosp = raw_input("[+] Give Token : ")
		tik()
		hopa = open('login.txt','w')
		hopa.write(hosp)
		hopa.close()
		print "\n[✓] Logged In Successfully."
		time.sleep(1)
		os.system('xdg-open https://www.facebook.com/jam.shahrukh.official')
		os.system('python2 sani.py')
	
	elif hos =="3":
		os.system('clear')
		os.system('python2 login.py')
		
	elif hos =="0":
		exit()
	else:
		print"[!] Wrong Input"
		exit()
def login():
	os.system("clear")
	try:
		tb=open('login.txt', 'r')
		os.system("python2 sani.py")
	except (KeyError,IOError):
		os.system("clear")
		print (banner)
		jam('[!] JAM X SANI BRAND')
		jam('[!] Use a New Facebook Account To Login')
		print'-------------------------------------'
		iid=raw_input('[+] Number/Email: ')
		id=iid.replace(" ","")
		pwd=raw_input('[+] Password : ')
		tik()
		data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+(id)+"&locale=en_US&password="+(pwd)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		z=json.load(data)
		if 'access_token' in z:
		    st = open("login.txt", "w")
		    st.write(z["access_token"])
		    st.close()
		    print "\n[✓] Logged In Successfully."
		    time.sleep(1)
		    os.system('xdg-open https://www.facebook.com/jam.shahrukh.official')
		    os.system("clear")
		    os.system("python2 sani.py")
		else:
		    if "www.facebook.com" in z["error_msg"]:
		        print ('[!] User Must Verify Account Before Login.')
		        time.sleep(3)
		        login()
		    else:
		        print ('[!]Number/User Id/ Password Is Wrong !')
		        time.sleep(1)
		        login()
if __name__=='__main__':
    reg()
