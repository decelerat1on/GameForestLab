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
                {'name':'Огненный дракон',
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
                 'skill1': {'name': 'Превратить врага в безобидную овечку',
                            '1hit': True,
                            'damage': None,
                            'crit_damage': None,
                            'health': None,
                            'armor': None,
                            'plus_damage': None},
                 'skill2': {'name': 'Огненная волна - 300 урона врагу',
                            '1hit': False,
                            'damage': 300,
                            'crit_damage': None,
                            'health': None,
                            'armor': None,
                            'plus_damage': None}
                 },
                {'name':'Лучник',
                 'health': 1600,
                 'damage': 100,
                 'armor': 400,
                 'dodge': 0.20,
                 'critical_damage': 2,
                 'chance_critical_damage': 0.08,
                 'skill1': {'name': 'Повышает шанс критического урона на 20%.',
                            '1hit': False,
                            'damage': None,
                            'crit_damage': 0.2,
                            'health': None,
                            'armor': None,
                            'plus_damage': None},
                 'skill2': {'name': 'Восстанавливает 150 здоровья.',
                            '1hit': False,
                            'damage': None,
                            'crit_damage': None,
                            'health': 150,
                            'armor': None,
                            'plus_damage': None}},


                {'name': 'Воин',
                 'health': 2000,
                 'damage': 100,
                 'armor': 500,
                 'dodge': 0.15,
                 'critical_damage': 2,
                 'chance_critical_damage': 0.05,
                 'skill1': {'name': 'Удар топором - 250 урона и +10 брони в бою',
                            '1hit': False,
                            'damage': 250,
                            'crit_damage': None,
                            'health': None,
                            'armor': 10,
                            'plus_damage': None},
                 'skill2': {'name': 'Увеличивает урон на 100 в данном бою.',
                            '1hit': False,
                            'damage': None,
                            'crit_damage': None,
                            'health': None,
                            'armor': None,
                            'plus_damage': 100},
}]

# Список с загадками
list_of_mysterys = [
    {'50':'На двух руках - 10 пальцев. Сколько пальцев на 10 руках?'},
    {'Корень':'Он слово или часть его. Он есть у зуба и у ели.Нет у добра его, но, говорят,у зла бывает?'},
    {'Скрипка':'Её прародители живут в лесу. Своим голосом она может очаровать любого. Её имя связано с ключом. Что это?'},
    {'Огонь':'Это чудище сжирает Всё, что встретит на пути.Но, насытившись едою, Умирает вместе с ней. Что это?'},
    {'Одуванчик':'Кто может дать потомство лишь однажды? Кто может дать потомство, став седым?'}
]
#TODO Дополнить новыми ключами все артефакты и скиллами ( Джокер новые ключи add skill true false и skill ко всем + проверка в test inventory)
# Список с артефактами
list_of_artefacts = [[{'name': 'Родниковая вода',
                       'description': 'Фляжка с целительной родниковой водой из глубин лабиринта.',
                       'short_desc': 'Восстанавливает 250 здоровья',
                       'add_artefacts': False,
                       'add_artefact_level': None,
                       'add_artefact_count': None,
                       'artefact_level': 1,
                       'count': 1,
                       'health': 250,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None,
                       'add_skill': False,
                       'double_attack': None,
                       'no_miss': False,
                       'rearm': False},

                       {'name': 'Красный талисман',
                       'description': 'Талисман яркого красного цвета на серебряной цепочке. В ваших руках светится еще сильнее',
                       'short_desc': 'Даёт +5% к вероятности критического урона',
                       'add_artefacts': False,
                       'add_artefact_level': None,
                       'add_artefact_count': None,
                       'artefact_level': 1,
                       'count': 1,
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': 5,
                       'add_skill': False,
                       'double_attack': None,
                       'no_miss': False,
                       'rearm': False},

                       {'name': 'Оберег медведя',
                       'description': 'Оберег из клыков медведя, украшенный бархатной шерстью. Даже пахнет дичью.',
                       'short_desc': 'Даёт +3 к броне',
                       'add_artefacts': False,
                       'add_artefact_level': None,
                       'add_artefact_count': None,
                       'artefact_level': 1,
                       'count': 1,
                       'health': None,
                       'damage': None,
                       'armor': 3,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None,
                       'add_skill': False,
                       'double_attack': None,
                       'no_miss': False,
                       'rearm': False},

                       {'name': 'Золотая кисть',
                       'description': 'Золотая кисть с оперением. Кажется этой кистью писали историю лабиринта.',
                       'short_desc': 'Даёт возможность 1 раз атаковать противника двойным уроном',
                       'add_artefacts': False,
                       'add_artefact_level': None,
                       'add_artefact_count': None,
                       'artefact_level': 1,
                       'count': 1,
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None,
                       'add_skill': False,
                       'double_attack': True,
                       'no_miss': False,
                       'rearm': False},

#TODO 1 Как реализовать петлю времени? Reversed?

                       {'name': 'Петля времени',
                       'description': 'Странная петля из холщёвой веревки. При попытке развязать - затягивается еще сильнее',
                       'short_desc': 'Даёт возможность откатить время назад до получения урона от атаки врага',
                       'add_artefacts': False,
                       'add_artefact_level': None,
                       'add_artefact_count': None,
                       'artefact_level': 1,
                       'count': 1,
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None,
                       'add_skill': False,
                       'double_attack': None,
                       'no_miss': False,
                       'rearm': False}],

                     [{'name': 'Браслет короля обезьян ',
                       'description': 'Красивый браслет короля обезьян, украшенный изумрудами и яшмой. Король никогда не промахивался.',
                       'short_desc': 'Даёт возможность на протяжении 1 боя исключить возможность промаха',
                       'add_artefacts': False,
                       'add_artefact_level': None,
                       'add_artefact_count': None,
                       'artefact_level': 2,
                       'count': 1,
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None,
                       'add_skill': False,
                       'double_attack': None,
                       'no_miss': True,
                       'rearm': False},

                       {'name': 'Песочные часы',
                       'description': 'Старенькие песочные часы. Песка почти не осталось из-за разбитой колбы. А если их перевернуть?',
                       'short_desc': 'Даёт возможность откатить все кулдауны способностей 1 раз.',
                       'add_artefacts': False,
                       'add_artefact_level': None,
                       'add_artefact_count': None,
                       'artefact_level': 2,
                       'count': 1,
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None,
                       'add_skill': False,
                       'double_attack': None,
                       'no_miss': False,
                       'rearm': True},

                      {'name': 'Запечатанный ветер',
                       'description': 'Странная баночка, которая шумит как маленький шторм. Крышка плотно запечатана.',
                       'short_desc': 'Даёт +5% к уклонению, но отнимает 100 здоровья',
                       'add_artefacts': False,
                       'add_artefact_level': None,
                       'add_artefact_count': None,
                       'artefact_level': 2,
                       'count': 1,
                       'health': -100,
                       'damage': None,
                       'armor': None,
                       'dodge': 0.05,
                       'critical_damage': None,
                       'chance_critical_damage': None,
                       'add_skill': False,
                       'double_attack': None,
                       'no_miss': False,
                       'rearm': False}],

                     [{'name': 'Мистический ларец',
                       'description': 'Ларец, который меняет цвета. То он красный, как кровь, то он белый, как снег.',
                       'short_desc': 'Выдаёт 2 случайных артефакта 1 уровня',
                       'add_artefacts': True,
                       'add_artefact_count': 2,
                       'add_artefact_level': 1,
                       'artefact_level': 3,
                       'count': 1,
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None,
                       'add_skill': False,
                       'double_attack': None,
                       'no_miss': False,
                       'rearm': False},

                      {'name': 'Джокер',
                       'description': 'Карта с джокером. Её края настолько острые, что одно прикосновение к ним вызывает боль во всём теле.',
                       'short_desc': 'Выдаёт новое умение: Бросок карты - 250 чистого урона сквозь уклонение и броню с кд в 3 клетки',
                       'add_artefacts': False,
                       'add_artefact_level': None,
                       'add_artefact_count': None,
                       'artefact_level': 3,
                       'count': 1,
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None,
                       'add_skill': True,
                       'double_attack': None,
                       'no_miss': False,
                       'rearm': False},

#TODO Реализация через новую способность?
                      {'name': 'Болотная пиявка',
                       'description': 'Магическая болотная пивка. Кто-то рассказывал, что она может передать часть своих свойств, но никогда не отцепится',
                       'short_desc': 'Даёт +10% вампиризма от атак',
                       'add_artefacts': False,
                       'add_artefact_level': None,
                       'add_artefact_count': None,
                       'artefact_level': 3,
                       'count': 1,
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None,
                       'add_skill': True,
                       'double_attack': None,
                       'no_miss': False,
                       'rearm': False},

#TODO Реализация через новую способность?
                      {'name': 'Глаз бога',
                       'description': 'Глаз, который был утерян неким Вотаном. Кажется его еще называли Один.',
                       'short_desc': 'Выдаёт новую способность: Позволяет посмотреть на 2 клетки вперед с кд 3 клетки',
                       'add_artefacts': False,
                       'add_artefact_level': None,
                       'add_artefact_count': None,
                       'artefact_level': 3,
                       'count': 1,
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None,
                       'add_skill': True,
                       'double_attack': None,
                       'no_miss': False,
                       'rearm': False}],

#TODO Реализация выдачи рандомных артефактов и смерти?
                     [{'name': 'Сундук смерти',
                       'description': 'Чёрный сундук с острыми краями. Из него льётся кровь, а не крышке написано "Не открывать!"',
                       'short_desc': 'Может выпасть 1 артефакт любого уровня или убить вас',
                       'add_artefacts': False,
                       'add_artefact_level': None,
                       'add_artefact_count': None,
                       'artefact_level': 4,
                       'count': 1,
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None,
                       'add_skill': False,
                       'double_attack': None,
                       'no_miss': False,
                       'rearm': False},

#TODO Как сделать восстановление 50 процентов?
                      {'name': 'Зелье здоровья',
                       'description': 'Красненькая склянка с приятными запахом. Так хочется её выпить побыстрее.',
                       'short_desc': 'Восстанавливает 50% от вашего здоровья',
                       'add_artefacts': False,
                       'add_artefact_level': None,
                       'add_artefact_count': None,
                       'artefact_level': 4,
                       'count': 1,
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None,
                       'add_skill': False,
                       'double_attack': None,
                       'no_miss': False,
                       'rearm': False},
#TODO Change class?
                      {'name': 'Кукла некроманта',
                       'description': 'Кажется эта кукла была инструментом чёрном магии или ворожбы.',
                       'short_desc': 'Даёт возможность сменить класс персонажа с полным восстановлением показателей.',
                       'add_artefacts': False,
                       'add_artefact_level': None,
                       'add_artefact_count': None,
                       'artefact_level': 4,
                       'count': 1,
                       'health': None,
                       'damage': None,
                       'armor': None,
                       'dodge': None,
                       'critical_damage': None,
                       'chance_critical_damage': None,
                       'add_skill': False,
                       'double_attack': None,
                       'no_miss': False,
                       'rearm': False}]]





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
