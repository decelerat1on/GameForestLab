from Characters import Hero
# def mystery(mysterys, artefacts, hero):
#     random_mystery = mysterys.pop(random.randint(0,len(mysterys)-1))
#     answer, mystery = tuple(random_mystery.items())[0]
#     player_answer = input(f'{mystery}: ')
#     if player_answer == answer:
#         print('Правильно!')
#         artefact = random.choice(artefacts)
#         if artefact[0] != 'Родниковая вода':
#             if artefact in hero.inventory:
#                 hero.inventory.append(['Родниковая вода', 250])
#         else:
#             hero.inventory.append()
#     else:
#         print('Неправильно! Попробуй еще')

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