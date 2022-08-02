import requests

from config import * 
from utils.parser import *

global cnt
cnt = 0

def send_attack(cookie_str, village_id, dest_x, dest_y, template = ATTACK_DATA_TEMPLATES[0]):
    req_headers = HEADERS_TEMPLATE 
    req_headers['cookie'] = cookie_str 

    req_params_first = {
        'village': str(village_id),
        'screen': 'place',
        'ajax': 'confirm'
    }

    attack_data = template

    attack_data['x'] = dest_x
    attack_data['y'] = dest_y
    attack_data['village'] = village_id
    attack_data['source_village'] = village_id
    attack_data['cb'] = 'troop-confirm'

    resp_first = requests.post(ENDPOINT + '/game.php', params=req_params_first, headers=req_headers, data=attack_data)

    #print(resp_first.text)

    if ('{"error":' in resp_first.text):
        print('\033[91mВОЗНИКЛА ОШИБКА (ВОЗМОЖНО ПРОБЛЕМА С cookie_str)\033[0m') 
        return 
    
    attack_codes = parse_attack_code(resp_first.text) 

    #print(resp_first.text[0:2000])

   # print(attack_code)

    if (len(attack_codes['ch']) < 10):
        print("\033[91mНЕ БЫЛ ПОЛУЧЕН КОД АТАКИ\033[0m")
        return
    
    

    req_params_attack = {
        'village': str(village_id),
        'screen': 'place',
        'ajaxaction': 'popup_command'
    }

    attack_data['ch'] = attack_codes['ch']
    attack_data['h'] = attack_codes['csrf']
    attack_data['cb'] = 'troop_confirm_submit'

    resp_attack = requests.post(ENDPOINT + '/game.php', params=req_params_attack, headers=req_headers, data=attack_data)

    #print(resp_attack.text)

    if ('{"error":' in resp_first.text):
        print('\033[91mАтака не была отправлена\033[0m') 
        return 

    print('\033[92mАтака была отправлена на координату ({x}, {y})\033[0m'.format(x = dest_x, y = dest_y))
    
