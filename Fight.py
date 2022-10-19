from Characters import *
import random

hero = Hero('Garold', 'Лучник')  # Создает объект класса Hero
enemy = Enemy(1, 'Волчья стая')  # Создаем объект класса Enemy ( нужно выбрать рандомный объект из класса такого-то уровня )


# Бой начинается с броска кубика D6.
def dice():
    enemy_dice1 = random.randrange(1,6)
    enemy_dice2 = random.randrange(1,6)
    sum_enemy = enemy_dice1 + enemy_dice2

    hero_dice1 = random.randrange(1, 6)
    hero_dice2 = random.randrange(1, 6)
    sum_hero = hero_dice1 + hero_dice2

    if sum_hero == sum_enemy:
        print(f'Выпало одинаковое значение. Перебрасывайте!')
    elif sum_hero > sum_enemy:
        print(f'Вы выйграли. У вас выпало {sum_hero}, у противника выпало {sum_enemy}\nВы ходите первым.')
    elif sum_hero < sum_enemy:
        print(f'Вы проиграли. У вас выпало {sum_hero}, у противника выпало {sum_enemy}\nПротивник ходит первым.')
    return sum_hero, sum_enemy




def fight(hero, enemy):
     print(f'Ваш враг: {enemy.class_enemy} {enemy.level} уровня')
     print(f'Бросайте кости!')
     dice()




fight(hero, enemy)










# print(fight(hero, enemy))