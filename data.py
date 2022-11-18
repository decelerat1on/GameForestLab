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
                 'chance_critical_damage': 0.1,
                 'skill1': 'Превратить врага в безобидную овечку',
                 'skill2': 'Огненная волна - 300 урона врагу'},
                {'name':'Лучник',
                 'health': 1600,
                 'damage': 100,
                 'armor': 400,
                 'dodge': 0.20,
                 'critical_damage': 2,
                 'chance_critical_damage': 0.08,
                 'skill1': 'Повышает шанс критического урона на 20%.',
                 'skill2': 'Восстанавливает 150 здоровья.'},
                {'name': 'Воин',
                 'health': 2000,
                 'damage': 100,
                 'armor': 500,
                 'dodge': 0.15,
                 'critical_damage': 2,
                 'chance_critical_damage': 0.05,
                 'skill1': 'Удар топором - 250 урона и +10 брони в бою',
                 'skill2': 'Увеличивает урон на 100.'
                 }]
# Список с загадками
list_of_mysterys = [
    {'50':'На двух руках - 10 пальцев. Сколько пальцев на 10 руках?'},
    {'Корень':'Он слово или часть его. Он есть у зуба и у ели.Нет у добра его, но, говорят,у зла бывает?'},
    {'Скрипка':'Её прародители живут в лесу. Своим голосом она может очаровать любого. Её имя связано с ключом. Что это?'},
    {'Огонь':'Это чудище сжирает Всё, что встретит на пути.Но, насытившись едою, Умирает вместе с ней. Что это?'},
    {'Одуванчик':'Кто может дать потомство лишь однажды? Кто может дать потомство, став седым?'}
]
# Список с артефактами
#TODO Передалать в словарь
list_of_artefacts = [[{'name': 'Родниковая вода',
                       'health': 250,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None},
                       {'name': 'Красный талисман',
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': 5},
                       {'name': 'Оберег медведя',
                       'health': None,
                       'damage': None,
                       'armor': 3,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None},
                       {'name': 'Золотая кисть', #TODO Одна атака с двойным уроном
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None},
                       {'name': 'Петля времени', #TODO Откат последней атаки по герою
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None}],
                     [{'name': 'Браслет короля ', #TODO Атаки без промахов
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None},
                       {'name': 'Песочные часы', #TODO Должны восстанавливать все colldown's
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None},
                      {'name': 'Запечатанный ветер', #TODO +5 к доджу, но -100 к health
                       'health': -100,
                       'damage': None,
                       'armor': None,
                       'dodge': 5,
                       'critical_damage': None,
                       'chance_critical_damage': None}],
                     [{'name': 'Мистический ларец', #TODO 2 рандомных артефакта 1 уровня
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None},
                      {'name': 'Джокер', #TODO Выдаёт новое умение: Бросок карты - 250 чистого урона сквозь уклонение и броню с кд в 3 клетки
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None},
                      {'name': 'Болотная пиявка', #TODO Вампиризм + 10%
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None},
                      {'name': 'Глаз бога', #TODO Позволяет посмотреть на 2 клетки вперед
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None}],
                     [{'name': 'Сундук смерти', #TODO Выдаёт 1 артефакт 1 уровня, 1 артефакт 2 уровня, 1 артефакт 3 уровня ИЛИ убивает героя
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None},
                      {'name': 'Зелье здоровья', #TODO Восстанавливает 50 проц здоровья
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None},
                      {'name': 'Кукла некроманта', #TODO Позволяет сменить персонажа с восстановлением
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None}]]





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
