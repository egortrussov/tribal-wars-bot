import math
from re import I
import time
import random

from attack.send_attack import send_attack 
from config import *
from village_info.village_info import get_troops_info

def start_scavenging(village_id,  attacks_num): 
    mx = len(VILLAGES_TO_ATTACK)
    
    for inx in range(attacks_num):
        dest_x = VILLAGES_TO_ATTACK[inx % mx][0] 
        dest_y = VILLAGES_TO_ATTACK[inx % mx][1] 

        send_attack(cookie_str=cookie_str, village_id=village_id, dest_x=dest_x, dest_y=dest_y) 

        time_to_delay = math.ceil(random.random() * 10)

        print('Delay:', time_to_delay)
        time.sleep(time_to_delay)

def start_auto_scavenging(village_id):
    mx = len(VILLAGES_TO_ATTACK) 
    inx = 0 

    delay_between_checking = 5

    while 1:
        
        troops_info = get_troops_info(village_id) 

        if ('error' in troops_info.keys()):
            print('\033[33mCookie error\033[0m')
            break 

        template_id = None 

        for i in range(len(ATTACK_DATA_TEMPLATES)):
            can_send = True 
            attack_data = ATTACK_DATA_TEMPLATES[i]

            for troop in troops_info.keys():
                if not troop in attack_data.keys():
                    continue
                if troops_info[troop] < attack_data[troop]:
                    can_send = False 
                    break 
            
            if can_send:
                template_id = i
                break
            
        if template_id != None:
            send_attack(cookie_str, village_id, VILLAGES_TO_ATTACK[inx][0], VILLAGES_TO_ATTACK[inx][1], ATTACK_DATA_TEMPLATES[template_id])

            inx += 1
            inx %= mx
        else:
            print('\033[93mНедостаточно войск\033[0m')


        time.sleep(delay_between_checking)