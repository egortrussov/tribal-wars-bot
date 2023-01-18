VILLAGE_ID = None

cookie_str = 'locale=en_DK; cid=362004223; en_auth=10c0a04d0555:fed2cc15d6b42c61a14a21cdbb1bee05fbbb0b312112e2fc22b691e12cc92e56; sid=0%3A83fa72aae6a4e7e213b8f27d395e1fab6fc49025c8830ef349f4e75d378d016da36ffdfd3cafe1dcd1e1a01afdf440796e93c42435d1633213f306f274f8fcc5; global_village_id=24094; websocket_available=true; io=q_mtVb75Z8mcBqH5APCw'

ENDPOINT = 'https://en128.tribalwars.net'

HEADERS_TEMPLATE = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en,en-US;q=0.9,ru-RU;q=0.8,ru;q=0.7',
    'content-length': '317',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': ENDPOINT,
    'referer': ENDPOINT + '/game.php?village=24094&screen=map',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0,',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-user': '?1',
    'sec-fetch-site': 'same-origin',
    'tribalwars-ajax': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

ATTACK_DATA_TEMPLATES = [
    {
        'attack': True,
        'cb': 'troop_confirm_submit',
        'spear': 40,
        'sword': 4,
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
    }
]

VILLAGES_TO_ATTACK = [
]

