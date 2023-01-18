import requests

from config import HEADERS_TEMPLATE, ATTACK_DATA_TEMPLATES, ENDPOINT  

from ..utils.parser import parse_attack_code
from ..utils.expressions import AttackException, RequestException

def send_attack(cookie_str: str, village_id: str, dest_x: int, dest_y: int, template = ATTACK_DATA_TEMPLATES[0]) -> None:
    req_headers: dict = HEADERS_TEMPLATE 
    
    req_headers['cookie'] = cookie_str 

    req_params_first: dict = {
        'village': str(village_id),
        'screen': 'place',
        'ajax': 'confirm'
    }

    attack_data: dict = template

    attack_data['x'] = dest_x
    attack_data['y'] = dest_y
    attack_data['village'] = village_id
    attack_data['source_village'] = village_id
    attack_data['cb'] = 'troop-confirm'

    try:
        resp_first: requests.Response = requests.post(ENDPOINT + '/game.php', params=req_params_first, headers=req_headers, data=attack_data) 

        if resp_first.status_code != 200:
            raise RequestException(resp_first.url, resp_first)

        if ('"error"' in resp_first.text):
            raise AttackException('error')  
    except RequestException as e:
        print(e) 
        return 
    except AttackException as e:
        print(e) 
        return 

    attack_codes: dict = parse_attack_code(resp_first.text) 

    if not attack_codes['ch']:
        raise AttackException(error_type='Attack code not found') 

    req_params_attack = {
        'village': str(village_id),
        'screen': 'place',
        'ajaxaction': 'popup_command'
    }

    attack_data['ch'] = attack_codes['ch']
    attack_data['h'] = attack_codes['csrf']
    attack_data['cb'] = 'troop_confirm_submit'

    try:
        resp_attack: requests.Response = requests.post(
            ENDPOINT + '/game.php', 
            params=req_params_attack, 
            headers=req_headers, 
            data=attack_data
        )

        if resp_attack.status_code != 200:
            raise RequestException(resp_attack.url, resp_attack)

        if ('error' in resp_attack.text):
            raise AttackException('error') 

        print('\033[92m Атака была отправлена на координату ({x}, {y})\033[0m'.format(x = dest_x, y = dest_y))
    except RequestException as e:
        return 
    except AttackException as e:
        return 
    
