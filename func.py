from Characters import Hero
import random
def create_hero(lists_heroes):
    classes = lists_heroes
    choose_name = input('Введите имя героя: ')
    choose_hero = input('Введите класс героя: ')
    while True:
        for class_ in classes:
            if choose_hero == class_['name']:
                print(f'Отличный выбор! Ваш класс: {class_["name"]}')
                hero = Hero(choose_name, class_)
                return hero
        print('Неправильный ввод класса.')
        print('Попробуй: Маг, Лучник, Воин.')
        choose_hero = input('Введите класс героя: ')
def mystery(list_of_mysterys, lists_of_artefacts, hero):
     random_mystery = list_of_mysterys.pop(random.randint(0,len(list_of_mysterys)-1))
     answer, mystery = tuple(random_mystery.items())
     while True:
        player_answer = input(f'{answer[1]}\nВведите ответ. Если не хотите решать загадку - введите 0:').title()
        if player_answer == '0':
            break
        elif player_answer == answer[0]:
            print('Правильно!')
            artefact = random.choice(lists_of_artefacts[mystery[1]-1])
            print(f'В награду герой получает: {artefact["name"]}\n{artefact["short_desc"]}')
            hero.inventory.append(artefact)
            break
        else:
            print('Неправильно! Попробуй еще')



