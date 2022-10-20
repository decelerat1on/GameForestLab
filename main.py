from map_info import movehero, findhero
from data import maptest as map, lists_heroes, lists_enemy
from func import create_hero
from Fight import fight_events, create_enemy, event_fight

print('Добро пожаловать в Лесной лабиринт')
print('Ваша цель: Пройти лабиринт до конца и не умереть.')
print('Доступные классы: Маг, Лучник, Воин')
print()

print('Маг - увеличенный критический урон и шанс критического урона, но низкий уровень здоровья и брони.')
print('Умения: Превратить врага в безобидную овечку / Огненная волна - 300 урона врагу.')
print()
print('Лучник - увеличенный шанс уклонения от атак и шанс критического урона, средние показатели брони.')
print('Умения: Повышает шанс критического урона на 20%. / Восстанавливает 150 здоровья.')
print()
print('Воин - Высокий уровень здоровья и брони, средний урон, низкий шанс критического урона')
print('Умения: Удар топором - 250 урона и +10 брони в бою / Увеличивает урон на 100. ')

hero = create_hero(lists_heroes)

print(map)
x, y = findhero(map)
while True:
    wheremove = input('Введите движение: ').upper()
    map,x,y,event = movehero(map, x, y, wheremove)
    print(map)
    if event in fight_events:
        enemy = create_enemy(event,lists_enemy)
        event_fight(hero,enemy,event)



