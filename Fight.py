from Characters import *
import random
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
    if sum_hero > sum_enemy:
        print(f'Вы выйграли. У вас выпало {sum_hero}, у противника выпало {sum_enemy}\nВы ходите первым.')
        return True
    elif sum_hero < sum_enemy:
        print(f'Вы проиграли. У вас выпало {sum_hero}, у противника выпало {sum_enemy}\nПротивник ходит первым.')
        return False


def create_enemy(enemy_level,lists_enemy):
    enemy_data = random.choice(lists_enemy[int(enemy_level)-1])
    enemy = Enemy(enemy_data)
    return enemy



def choise_action(hero,enemy):
        choise = input('[1] - Посмотреть инвентарь\n[2] - Использовать умение\n[3] - Ударить\nВведите действие: ')
        #TODO Прописать атаку
        #TODO Написать проверку инвентаря
        #TODO Очистка консоли после действий
        #TODO Checkinventory: Список словарей в классе
        if choise == '1':
            hero.check_inventory()
        elif choise == '2':
            hero.use_skills()
        elif choise == '3':
            hero.attack(enemy)

def event_fight(hero, enemy,event):


     print(f'Ваш враг: {enemy.class_enemy} {event} уровня')
     print(f'Бросайте кости!')
     if whoseattack():
         while hero.health > 0 and enemy.health > 0:
             choise_action(hero,enemy)
             enemy.attack(hero)
             print(hero.health, enemy.health)
     else:
         while hero.health > 0 and enemy.health > 0:
             enemy.attack(hero)
             choise_action(hero,enemy)
             print(hero.health, enemy.health)
     if hero.health > 0:
         print('Победил герой')
         return True
     else:
         print('Победил монстр')
         return False



