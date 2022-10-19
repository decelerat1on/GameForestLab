# Список с врагами лабиринта и их характеристиками
lists_enemy = [[{'name':'Волчья стая',
                 'health': 250,
                 'damage': 15,
                 'armor': 50,
                 'dodge': 0.03,
                 'critical_damage': 0,
                 'chance_critical_damage': 0},
                {'name': 'Гоблин с копьем',
                 'health': 250,
                 'damage': 15,
                 'armor': 50,
                 'dodge': 0.03,
                 'critical_damage': 0,
                 'chance_critical_damage': 0
                 },
                {'name':'Иссушенный труп',
                 'health': 250,
                 'damage': 15,
                 'armor': 0,
                 'dodge': 0.03,
                 'critical_damage': 0,
                 'chance_critical_damage': 0
                 }],

               [{'name':'Странствующий маг',
                 'health': 400,
                 'damage': 40,
                 'armor': 100,
                 'dodge': 0.1,
                 'critical_damage': 0,
                 'chance_critical_damage': 0
                 },
                {'name':'Страж лабиринта',
                 'health': 600,
                 'damage': 25,
                 'armor': 150,
                 'dodge': 0,
                 'critical_damage': 0,
                 'chance_critical_damage': 0},
                {'name':'Душа грешника',
                 'health': 350,
                 'damage': 35,
                 'armor': 100,
                 'dodge': 0.3,
                 'critical_damage': 2,
                 'chance_critical_damage': 0.2
                 }],

                [{'name':'Тролль',
                  'health': 700,
                  'damage': 30,
                  'armor': 150,
                  'dodge': 0.25,
                  'critical_damage': 0,
                  'chance_critical_damage': 0
                  },
                {'name':'Демон лабиринта',
                 'health': 650,
                 'damage': 60,
                 'armor': 200,
                 'dodge': 0.2,
                 'critical_damage': 0,
                 'chance_critical_damage': 0
                 },
                {'name':'Огенный дракон',
                 'health': 700,
                 'damage': 40,
                 'armor': 400,
                 'dodge': 0.1,
                 'critical_damage': 0,
                 'chance_critical_damage': 0
                 }],

                [{'name':'Хранитель лабиринта',
                  'health': 1000,
                  'damage': 40,
                  'armor': 500,
                  'dodge': 0.18,
                  'critical_damage': 0,
                  'chance_critical_damage': 0
                  },
                {'name':'Осколок леса',
                 'health': 3000,
                 'damage': 0,
                 'armor': 0,
                 'dodge': 0,
                 'critical_damage': 0,
                 'chance_critical_damage': 0
                 }]]
# Список с героями и их характеристиками
lists_heroes = [{'name':'Маг',
                 'health': 1300,
                 'damage': 150,
                 'armor': 300,
                 'dodge': 0.13,
                 'critical_damage': 3,
                 'chance_critical_damage': 0.1},
                {'name':'Лучник',
                 'health': 1600,
                 'damage': 100,
                 'armor': 400,
                 'dodge': 0.20,
                 'critical_damage': 2,
                 'chance_critical_damage': 0.08},
                {'name': 'Воин',
                 'health': 2000,
                 'damage': 100,
                 'armor': 500,
                 'dodge': 0.15,
                 'critical_damage': 2,
                 'chance_critical_damage': 0.05}]
# Список с загадками
list_of_mysterys = [
    {'50':'На двух руках - 10 пальцев. Сколько пальцев на 10 руках?'},
    {'Корень':'Он слово или часть его. Он есть у зуба и у ели.Нет у добра его, но, говорят,у зла бывает?'},
    {'Скрипка':'Её прародители живут в лесу. Своим голосом она может очаровать любого. Её имя связано с ключом. Что это?'},
    {'Огонь':'Это чудище сжирает Всё, что встретит на пути.Но, насытившись едою, Умирает вместе с ней. Что это?'},
    {'Одуванчик':'Кто может дать потомство лишь однажды? Кто может дать потомство, став седым?'}
]
# Список с артефактами
list_of_artefacts1 = [
    ['Родниковая вода', 250],
    ['Красный талисман', 0.05],
    ['Оберег медведя', 3],
    ['Золотая кисть', 999],
    ['Петля времени', 9999],
    ['Стальная пластина', 200]
]
list_of_artefacts2 = [
    ['Сердце великана', 999],
    ['Песочные часы', 999],
    ['Запечатанный ветер', 999],
    ['Кольчуга', 500]
]
list_of_artefacts3 = [
    ['Мистический ларец', 999],
    ['Джокер', 999],
    ['Болотная пиявка', 999],
    ['Улей', 999]
]
list_of_artefacts4 = [
    ['Сундук смерти', 999],
    ['Крепкое зелье здоровья', 999],
    ['Кукла некроманта', 999]
]
# Карта лабиринта
maptest = '''
╔═╦═╦═╦═╦═╦═╦═╦═╗
║x║x║x║x║x║x║x║x║ 
╠═╬═╬═╬═╬═╬═╬═╬═╣
║x║x║x║x║H║x║x║x║
╠═╬═╬═╬═╬═╬═╬═╬═╣
║x║x║x║x║1║x║x║x║
╠═╬═╬═╬═╬═╬═╬═╬═╣
║x║x║x║x║1║x║x║x║
╠═╬═╬═╬═╬═╬═╬═╬═╣
║x║3║1║1║1║з║з║x║
╠═╬═╬═╬═╬═╬═╬═╬═╣
║x║x║x║2║x║x║x║x║
╠═╬═╬═╬═╬═╬═╬═╬═╣
║x║з║з║1║2║x║x║x║
╠═╬═╬═╬═╬═╬═╬═╬═╣
║x║x║x║x║2║x║x║x║
╠═╬═╬═╬═╬═╬═╬═╬═╣
║x║3║2║2║2║x║x║x║
╠═╬═╬═╬═╬═╬═╬═╬═╣
║x║з║x║x║x║x║x║x║
╠═╬═╬═╬═╬═╬═╬═╬═╣
║x║Б║x║x║x║x║x║x║
╠═╬═╬═╬═╬═╬═╬═╬═╣
║x║x║x║x║x║x║x║x║
╚═╩═╩═╩═╩═╩═╩═╩═╝
'''
# ╔ ╗╚ ╝ ╠ ╣ ╦ ╩ ╬ ═ ║
# map = """
#          ╔══╗
#          ║в1║
#          ╠══╣
#          ║в1║
# ╔══╦══╦══╬══╬══╦══╗
# ║в3║в1║в1║в1║з ║з ║
# ╚══╩══╬══╬══╩══╩══╝
#       ║в2║
# ╔══╦══╬══╬══╗
# ║з ║з ║в1║в2║
# ╚══╩══╩══╬══╣
#          ║12║
# ╔══╦══╦══╬══╣
# ║в3║12║в2║в2║
# ╠══╬══╩══╩══╝
# ║з ║
# ╠══╣
# ║б ║
# ╚══╝
# """
