import threading
import datetime
import time
def time_count():
    global sec,min
    while True:
        time_now = time.time()
        time_now = time.ctime(time_now).split(' ')[3].split(':')[1:]
        sec, min = int(time_now[1]), int(time_now[0])

#def privet():
 #   while True:
  #      print('Hello!')
   #     time.sleep(3)
# thread1 = threading.Thread(target=time_count)
# thread2 = threading.Thread(target=privet)
# thread1.start()
# thread2.start()
# print('Конец')
# start_time = time.time()
#time_now = time.ctime(time_now).split(' ')[3].split(':')[1:]
#sec,min = int(time_now[1]),int(time_now[0])
#while start_time + 60 > time.time():
#    print(start_time + 60 - time.time())


list_of_artefacts = [{'name': 'Родниковая вода',
                       'description': 'Фляжка с целительной родниковой водой из глубин лабиринта.',
                       'short_desc': 'Восстанавливает 250 здоровья',
                       'add_artefacts': False,
                       'add_artefact_level': None,
                       'add_artefact_count': None,
                       'count': 1,
                       'health': 250,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None,
                       'add_skill': False,
                       'double_attack': None,
                       'no_miss': False,
                       'rearm': False},

                       {'name': "Красный талисман",
                       'description': 'Талисман яркого красного цвета на серебряной цепочке. В ваших руках светится еще сильнее',
                       'short_desc': 'Даёт +5% к вероятности критического урона',
                       'add_artefacts': False,
                       'add_artefact_level': None,
                       'add_artefact_count': None,
                       'count': 1,
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': 0.05,
                       'add_skill': False,
                       'double_attack': None,
                       'no_miss': False,
                       'rearm': False},

                       {'name': 'Оберег медведя',
                       'description': 'Оберег из клыков медведя, украшенный бархатной шерстью. Даже пахнет дичью.',
                       'short_desc': 'Даёт +3 к броне',
                       'add_artefacts': False,
                       'add_artefact_level': None,
                       'add_artefact_count': None,
                       'count': 1,
                       'health': None,
                       'damage': None,
                       'armor': 3,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None,
                       'add_skill': False,
                       'double_attack': None,
                       'no_miss': False,
                       'rearm': False}]

def add_int(item,inventory):
    for item_inventory in inventory:
        if item['name'] == item_inventory['name']:
            item_inventory['count'] += 1
            break
        else:
            inventory.append(item)
            break

#TODO добавление предмета доделать
inventory = [list_of_artefacts[0]]
add_int(list_of_artefacts[0],inventory)
add_int(list_of_artefacts[0],inventory)
add_int(list_of_artefacts[1],inventory)
add_int(list_of_artefacts[2],inventory)
add_int(list_of_artefacts[0],inventory)
add_int(list_of_artefacts[1],inventory)
add_int(list_of_artefacts[2],inventory)
for item in inventory:
    print(item['name'],item['count'])