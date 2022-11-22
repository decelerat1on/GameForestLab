from Characters import *
import os
from data import *


fight_events = ['1','2','3','Б']
def dice_drop():
    enemy_dice1 = random.randrange(1, 6)
    enemy_dice2 = random.randrange(1, 6)
    sum_enemy = enemy_dice1 + enemy_dice2

    hero_dice1 = random.randrange(1, 6)
    hero_dice2 = random.randrange(1, 6)
    sum_hero = hero_dice1 + hero_dice2
    return sum_hero, sum_enemy
# Бой начинается с броска кубика D6.
def whoseattack():
    sum_hero, sum_enemy = dice_drop()
    while sum_hero == sum_enemy:
        sum_hero, sum_enemy = dice_drop()
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
        #TODO Написать проверку инвентаря
        #TODO Checkinventory: Список словарей в классе
        #TODO Прописать награду за убийство врага ( артефакт )
        if choise == '1':
            hero.check_inventory()
        elif choise == '2':
            hero.use_skills()
        elif choise == '3':
            print(f'{hero.name} атакует {enemy.class_enemy}')
            hero.attack(enemy)
def event_fight(hero, enemy, event):
     count = 1

     print(f'Ваш враг: {enemy.class_enemy} {event} уровня')
     print(f'Бросайте кости!')
     input('Нажмите Enter чтобы бросить кости')
     os.system('cls')
     if whoseattack():
         while hero.health > 0 and enemy.health > 0:
             os.system('cls')
             print(f'Ваш враг: {enemy.class_enemy} {event} уровня.\nХод:{count}')
             choise_action(hero,enemy)
             print('_' * 50)
             print(f'{enemy.class_enemy} атакует {hero.name}')
             enemy.attack(hero)
             input('Нажмите Enter чтобы завершить ход')
             count += 1

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
         return True
     else:
         os.system('cls')
         print('Победил монстр')
         return False



