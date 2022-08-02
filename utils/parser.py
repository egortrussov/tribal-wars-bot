import json
from config import *

def get_attack_ch(str:str):

    to_search = '<input type="hidden" name="ch" value="'

    index = str.find(to_search) 
    index += len(to_search) 

    index1 = str.find('" />n', index) 

    if (index1 < 0):
        return ''
    
    return str[index:index1]

def get_attack_csrf(str: str):
    to_search = '"csrf":'

    index = str.find(to_search) 
    index += len(to_search) + 1

    index1 = str.find('",', index) 

    if (index1 < 0):
        return ''
    
    return str[index:index1]



def parse_attack_code(str: str):
    str = str.replace('\\', '')

    ch = get_attack_ch(str) 
    csrf = get_attack_csrf(str)


    return {
        "ch": ch,
        "csrf": csrf
    }

def parse_troops_info(str):
    str_troops_begin = 'TribalWars.updateGameData('

    index_troops_begin = str.find('TribalWars.updateGameData(')
    index_troops_begin += len(str_troops_begin)
    index_troops_end = str.find('});', index_troops_begin) 

    troops_list = json.loads(str[index_troops_begin:index_troops_end + 1])['units']

    troops_info = {}

    for troop in troops_list:
        troops_info[troop] = 0 

        str_to_search = 'data-count="{troop_name}">'.format(troop_name=troop) 
        index_start = str.find(str_to_search) 

        if (index_start < 0):
            continue 

        index_start += len(str_to_search) 

        index_end = str.find('<', index_start)

        troops_info[troop] = int(str[index_start:index_end]) 

    return troops_info
