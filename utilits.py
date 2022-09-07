# ╔ ╗╚ ╝ ╠ ╣ ╦ ╩ ╬ ═ ║
import random
#TODO Додумать карту и комнаты с загадками
map = """
╔═╗
║ ║
╠═╣
║ ║
╩═╬═╗
  ║ ║
  ╩═╝"""
#TODO Добить загадки по карте
list_of_mysterys = [
    {'50':'На двух руках - 10 пальцев. Сколько пальцев на 10 руках?'},
    {'Корень':'Он слово или часть его. Он есть у зуба и у ели.Нет у добра его, но, говорят,у зла бывает?'},
    {'Скрипка':'Её прародители живут в лесу. Своим голосом она может очаровать любого. Её имя связано с ключом. Что это?'}
]
#TODO Добить артефакты разных уровней
list_of_artefacts1 = [
    ['Родниковая вода', 250],
    ['Красный талисман', 0.05],
    ['Оберег медведя', 3]
]


def mystery(mysterys, artefacts, hero):
    random_mystery = mysterys.pop(random.randint(0,len(mysterys)-1))
    answer, mystery = tuple(random_mystery.items())[0]
    player_answer = input(f'{mystery}: ')
    if player_answer == answer:
        print('Правильно!')
        artefact = random.choice(artefacts)
        if artefact[0] != 'Родниковая вода':
            if artefact in hero.inventory:
                hero.inventory.append(['Родниковая вода', 250])
        else:
            hero.inventory.append()
#TODO Добавить выдачу артефактов
    else:
        print('Неправильно! Попробуй еще')
#TODO Добавить удар на неправильный ответ


mystery(list_of_mysterys)