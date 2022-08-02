import requests 
import json

headers = {
    #'host': 'en128.tribalwars.net',
    #'method': 'POST',
    #'path': '/game.php?village=5514&screen=place&ajaxaction=popup_command',
    #'scheme': 'https',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en,en-US;q=0.9,ru-RU;q=0.8,ru;q=0.7',
    'content-length': '317',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'cid=1101699082; locale=en_DK; en_auth=cadfbf2cd0ae:bf5d4955d36ae0e18766e711892826c18ad22e404972938cf6a2f86bf08667c4; sid=0%3Aba4ed37a21515591bda67c23265e97e261104ad4fd269724ed23015bf386e691e1d8430895e126c3cb83246b971cfa881942fee092b030c295e6ea5b0911dc0e; global_village_id=24094; websocket_available=true; io=iNzUkWcn4BT5ZZsJEG3A',
    'origin': 'https://en128.tribalwars.net',
    'referer': 'https://en128.tribalwars.net/game.php?village=24094&screen=map',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0,',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'tribalwars-ajax': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'

} 

payload = {
    'attack': True,
    'ch': 'c65dd7a7f0f5e66606684fe89f23dd64:6851a782b4ae810540e66d69b2735891d05f9526d7c214a4e4088441caacacf0',
    'cb': 'troop_confirm_submit',
    'x': 360,
    'y': 459,
    'source_village': '24094',
    'village': '24094',
    'spear': 1,
    'sword': 0,
    'axe': 0,
    'archer': 0,
    'spy': 0,
    'light': 0,
    'marcher': 0,
    'heavy': 0,
    'ram': 0,
    'catapult': 0,
    'knight': 0,
    'snob': 0,
    'building': 'main',
    'h': '3c86c59e',
}

session = requests.Session() 

#session.cookies.clear()
#session.cookies.update(cookies)

resp = session.post('https://en128.tribalwars.net/game.php?village=24094&screen=place&ajaxaction=popup_command',headers=headers, data=payload)

print(resp.headers)

parsed = json.loads(resp.content)
print(parsed)