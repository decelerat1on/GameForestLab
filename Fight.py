from Characters import *
import os
from data import *


fight_events = ['1','2','3','Б','I']
#TODO Подобрать символы к комнатам с несколькими врагами
# Бой начинается с броска кубика D6.
def whoseattack(hero):
    sum_hero, sum_enemy = hero.dice_drop()
    while sum_hero == sum_enemy:
        sum_hero, sum_enemy = hero.dice_drop()
        print(f'Выпало одинаковое значение. Перебрасываем!')
        input('Нажмите Enter чтобы бросить кости')
        os.system('cls')
    if sum_hero > sum_enemy:
        print(f'Вы выйграли. У вас выпало {sum_hero}, у противника выпало {sum_enemy}\nВы ходите первым.')
        print('_' * 50)
        input('Нажмите Enter чтобы продолжить')
        return True
    elif sum_hero < sum_enemy:
        print(f'Вы проиграли. У вас выпало {sum_hero}, у противника выпало {sum_enemy}\nПротивник ходит первым.')
        print('_' * 50)
        input('Нажмите Enter чтобы продолжить')
        return False


def create_enemy(enemy_level,lists_enemy):
    enemy_data = random.choice(lists_enemy[int(enemy_level)-1])
    enemy = Enemy(enemy_data)
    return enemy



def choise_action(hero,enemy):
        print('_' * 50)
        choise = input('[1] - Посмотреть инвентарь\n[2] - Использовать умение\n[3] - Ударить\nВведите действие: ')
        os.system('cls')
        if choise == '1':
            hero.check_inventory(enemy)
        elif choise == '2':
            hero.use_skills(enemy)
        elif choise == '3':
            print(f'{hero.name} атакует {enemy.class_enemy}')
            hero.attack(enemy)
def event_fight(hero, enemy, event):
     count = 1

     print(f'Ваш враг: {enemy.class_enemy} {enemy.health} ЗДР {event} уровня')
     print(f'Бросайте кости!')
     input('Нажмите Enter чтобы бросить кости')
     os.system('cls')
     if whoseattack(hero):
         while hero.health > 0 and enemy.health > 0:
             os.system('cls')
             print(f'Ваш враг: {enemy.class_enemy} {event} уровня.\nХод:{count}')
             choise_action(hero,enemy)
             print('_' * 50)
             print(f'{enemy.class_enemy} атакует {hero.name}')
             enemy.attack(hero)
             input('Нажмите Enter чтобы завершить ход')
             count += 1

#TODO Сюда прописать рандомный выбор использования или неиспользования скилла противника.
#TODO Создать скиллы у противников по примеру с героем - data
#TODO Использование врагом в его классе все на примере героя


     else:
         while hero.health > 0 and enemy.health > 0:
             os.system('cls')
             print(f'Ваш враг: {enemy.class_enemy} {event} уровня.\nХод:{count}')
             print(f'{enemy.class_enemy} атакует {hero.name}')
             enemy.attack(hero)
             print('_' * 50)
             choise_action(hero,enemy)
             input('Нажмите Enter чтобы завершить ход')
             count += 1
     if hero.health > 0:
         os.system('cls')
         print('Победил герой')
         hero.plus_damage = 0
         hero.no_miss = False
         if enemy.kill_status == True:
             return True
         else:
             treasure = random.choice(data.list_of_artefacts[int(event)-1])
             print(f'В награду герой получает: {treasure["name"]}\n{treasure["description"]}')
             hero.inventory.append(treasure)
             return True

     else:
         os.system('cls')
         print('Победил монстр')
         return False



