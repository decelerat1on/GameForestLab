from map_info import movehero, findhero
from data import maptest as map, lists_heroes, lists_enemy
from func import create_hero
from Fight import fight_events, create_enemy, event_fight
import os

print('''Добро пожаловать в Лесной лабиринт
Ваша цель: Пройти лабиринт до конца и не умереть.
Доступные классы: Маг, Лучник, Воин

Маг - увеличенный критический урон и шанс критического урона, но низкий уровень здоровья и брони.
Умения: Превратить врага в безобидную овечку / Огненная волна - 300 урона врагу.

Лучник - увеличенный шанс уклонения от атак и шанс критического урона, средние показатели брони.
Умения: Повышает шанс критического урона на 20%. / Восстанавливает 150 здоровья.

Воин - Высокий уровень здоровья и брони, средний урон, низкий шанс критического урона
Умения: Удар топором - 250 урона и +10 брони в бою / Увеличивает урон на 1''')
hero = create_hero(lists_heroes)

print(map)
x, y = findhero(map)
while True:
    wheremove = input('Введите движение: ').upper()
    map,x,y,event = movehero(map, x, y, wheremove)
    os.system('cls')
    print(map)
    print('_' * 50)
    hero.skill_colldown()
    if event in fight_events:
        if event == '꠳':
            enemy = create_enemy('1', lists_enemy)
            event_fight(hero, enemy, '1')
            enemy = create_enemy('1', lists_enemy)
            event_fight(hero, enemy, '1')
            print(map)
            continue

        elif event == '꠴':
            enemy = create_enemy('2', lists_enemy)
            event_fight(hero, enemy, '2')
            enemy = create_enemy('2', lists_enemy)
            event_fight(hero, enemy, '2')
            print(map)
            continue

        enemy = create_enemy(event, lists_enemy)
        event_fight(hero,enemy,event)
        print(map)



