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
    #'cookie': 'cid=1101699082; locale=en_DK; en_auth=cadfbf2cd0ae:bf5d4955d36ae0e18766e711892826c18ad22e404972938cf6a2f86bf08667c4; sid=0%3Aba4ed37a21515591bda67c23265e97e261104ad4fd269724ed23015bf386e691e1d8430895e126c3cb83246b971cfa881942fee092b030c295e6ea5b0911dc0e; global_village_id=24094; websocket_available=true; io=iNzUkWcn4BT5ZZsJEG3A',
    'cookie': 'cid=48963876; ru_auth=b3758df860cb:cc7158f4cef0c309dbd36268d8dbbd805ab0079e9c604b6ca9e6466f8ec5b5ef; sid=0%3A49a33703bdab4f2ed60667077f2da154c5fff49c242672c14283b8771f84b6ff8e4c885dc152d35197cf9cb58abb8bb170126329300f21c0411e94d714155a8a; global_village_id=5514; websocket_available=true; io=7qHZxjcCEdkzxBC6BZiR',
    'origin': 'https://ru79.voynaplemyon.com',
    'referer': 'https://ru79.voynaplemyon.com/game.php?village=5514&screen=map',
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
    'ch': '33ff18079d2b41d0c3255cfc674e63b6:aa89af11eed45aaff4957f90892109407b5bd3b4f1353bb92b06b047872ce519',
    'cb': 'troop_confirm_submit',
    'x': 474,
    'y': 434,
    'source_village': '5514',
    'village': '5514',
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
    'h': '249c4afd',
}

session = requests.Session() 

#session.cookies.clear()
#session.cookies.update(cookies)

print('\n\n-------------\n\n')
resp = session.post('https://ru79.voynaplemyon.com/game.php?village=5514&screen=place&ajaxaction=popup_command',headers=headers, data=payload)

#print(resp.headers)

parsed = json.loads(resp.content)
print(parsed)