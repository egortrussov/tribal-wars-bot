import requests

from config import HEADERS_TEMPLATE, cookie_str, ENDPOINT

from utils.parser import parse_troops_info

def get_troops_info(village_id: str) -> dict:
    headers: dict = HEADERS_TEMPLATE 
    headers['cookie'] = cookie_str 
    headers['accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'

    req_params: dict = {
        'village': str(village_id),
        'screen': 'overview'
    }

    session = requests.Session()

    resp: requests.Response = session.get(ENDPOINT + '/game.php?village={id}&screen=overview'.format(id=village_id), headers=headers, data=req_params) 

    if (resp.status_code != 200):
        return {
            'error': True
        } 
    
    data: dict = parse_troops_info(resp.text) 

    return data
