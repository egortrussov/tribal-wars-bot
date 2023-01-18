from ..config import ATTACK_DATA_TEMPLATES

def get_available_template_id(troops_info: dict) -> int:
    for template_id in range(len(ATTACK_DATA_TEMPLATES)):
        can_send = True 
        attack_data = ATTACK_DATA_TEMPLATES[i]

        for troop in troops_info.keys():
            if not troop in attack_data.keys():
                continue
            if troops_info[troop] < attack_data[troop]:
                can_send = False 
                break 
        
        if can_send:
            return template_id 
    return None