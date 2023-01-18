import math
import time
import random

from attack.send_attack import send_attack 

from ..config import VILLAGES_TO_ATTACK, cookie_str, ATTACK_DATA_TEMPLATES

from ..village_info.village_info import get_troops_info

from ..utils.attack_templates import get_available_template_id
from ..utils.expressions import RequestException

def start_scavenging(village_id: str,  attacks_num: int = 1) -> None: 
    mx: int = len(VILLAGES_TO_ATTACK)
    
    for inx in range(attacks_num):
        dest_x: int = VILLAGES_TO_ATTACK[inx % mx][0] 
        dest_y: int = VILLAGES_TO_ATTACK[inx % mx][1] 

        send_attack(cookie_str=cookie_str, village_id=village_id, dest_x=dest_x, dest_y=dest_y) 

        time_to_delay: int = math.ceil(random.random() * 10)

        time.sleep(time_to_delay)

def start_auto_scavenging(village_id: str) -> None:
    max_index = len(VILLAGES_TO_ATTACK) 
    index = 0 

    delay_between_checking = 5

    while True:
        troops_info: dict = get_troops_info(village_id)

        if ('error' in troops_info.keys()):
            raise RequestException()

        template_id: int = get_available_template_id(troops_info)
            
        if template_id != None:
            send_attack(
                cookie_str, 
                village_id, 
                VILLAGES_TO_ATTACK[index][0], 
                VILLAGES_TO_ATTACK[index][1], 
                ATTACK_DATA_TEMPLATES[template_id]
            )

            index = (index + 1) % max_index
        else:
            print('\033[93m Недостаточно войск\033[0m')


        time.sleep(delay_between_checking)