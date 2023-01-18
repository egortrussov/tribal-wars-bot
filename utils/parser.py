import json

import bs4
from bs4 import BeautifulSoup

from config import *

def get_attack_ch(soup: BeautifulSoup) -> str:
    element: bs4.element.Tag = soup.find('input', { 'name': 'ch' })
    
    return element.attrs['value']

def get_attack_csrf(html_str: str) -> str:
    text_to_search: str = '"csrf":'

    index_start: int = html_str.find(text_to_search) 
    index_start += len(text_to_search) + 1

    index_end: int = html_str.find(',', index_start) 

    if (index_end < 0):
        return ''
    
    return html_str[index_start:index_end]



def parse_attack_code(html_str: str) -> dict:
    soup: BeautifulSoup = BeautifulSoup(html_str, 'html.parser') 

    ch: str = get_attack_ch(soup) 
    csrf: str = get_attack_csrf(html_str)

    return {
        "ch": ch,
        "csrf": csrf
    }

def parse_troops_info(html_str: str) -> dict:
    str_troops_begin: str = 'TribalWars.updateGameData('

    index_troops_begin: int = html_str.find('TribalWars.updateGameData(')
    index_troops_begin += len(str_troops_begin)
    index_troops_end: int = html_str.find('});', index_troops_begin) 

    troops_list: list = json.loads(html_str[index_troops_begin:index_troops_end + 1])['units']

    troops_info = {}

    for troop in troops_list:
        troops_info[troop] = 0 

        str_to_search: str = 'data-count="{troop_name}">'.format(troop_name=troop) 
        index_start: int = html_str.find(str_to_search) 

        if (index_start < 0):
            continue 

        index_start += len(str_to_search) 

        index_end: int = str.find('<', index_start)

        troops_info[troop] = int(str[index_start:index_end]) 

    return troops_info
