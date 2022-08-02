from config import *
import time

from attack.send_attack import send_attack
from attack.start_scavenging import start_auto_scavenging, start_scavenging
from village_info.village_info import *

# send_attack(cookie_str, 24094, 360, 459) 

# start_scavenging(VILLAGE_ID, 4)

# start_auto_scavenging(VILLAGE_ID)

print('Привет! Перед использованием программы не забудьте проверить, была ли изменена строка cookie_str в файле config.py!') 

while (True):
    print('\033[96mКакое действие хотите сделать?\033[0m')
    print('1 - отправить атаку на деревню с координатами x, y')
    print('2 - начать автоматическую отправку атак на деревни варваров') 

    type = int(input('выбранное действие (число 1 или 2) - '))  

    if type == 2:
        print('Начинаю автоматическую отправку атак...')
        start_auto_scavenging(VILLAGE_ID) 
    else:
        x = int(input('Введите координату (x) деревни:'))
        y = int(input('Введите координату (y) деревни:'))
        temp_id = int(input('Введите номер шаблона атаки (число от 1 до {cnt}):'.format(cnt=len(ATTACK_DATA_TEMPLATES)))) 

        if (temp_id > len(ATTACK_DATA_TEMPLATES)):
            print('\033[91mОшибка: шаблона с таким номером не существует\033[0m') 
            continue 

        send_attack(cookie_str, VILLAGE_ID, x, y, ATTACK_DATA_TEMPLATES[temp_id - 1])

            
    