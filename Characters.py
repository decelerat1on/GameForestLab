class Hero:
    def __init__(self, name, class_name):
        self.inventory = {}
        self.name = name
        self.class_name = class_name
        # if self.class_name == "Маг":
        #     self.health = 1500
        #     self.damage = 150
        #     self.armor = 7
        #     self.dodge = 0.13
        #     self.critical_damage = 3
        #     self.chance_critical_damage = 0.1
        # elif class_name == "Лучник":
        #     self.health = 2000
        #     self.damage = 100
        #     self.armor = 9
        #     self.dodge = 0.20
        #     self.critical_damage = 2
        #     self.chance_critical_damage = 0.08
        # elif class_name == "Воин":
        #     self.health = 2500
        #     self.damage = 100
        #     self.armor = 12
        #     self.dodge = 0.15
        #     self.critical_damage = 2
        #     self.chance_critical_damage = 0.05
    def attack(self, target):
        target.health -= self.damage
class Enemy:
    def __init__(self, enemy_data):
        self.name = enemy_data['name']
        self.health = enemy_data['health']
        self.damage = enemy_data['damage']
        self.armor = enemy_data['armor']
        self.dodge = enemy_data['dodge']
        self.critical_damage = enemy_data['critical_damage']
        self.chance_critical_damage = enemy_data['chance_critical_damage']

        # self.level = level
        # self.class_enemy = class_enemy
        # if self.level == 1:
        #     if class_enemy == 'Волчья стая':
        #         self.health = 250
        #         self.damage = 15
        #         self.armor = 0
        #         self.dodge = 0.03
        #         self.critical_damage = 0
        #         self.chance_critical_damage = 0
        #     elif class_enemy == 'Гоблин с копьем':
        #         self.health = 200
        #         self.damage = 20
        #         self.armor = 1
        #         self.dodge = 0.15
        #         self.critical_damage = 0
        #         self.chance_critical_damage = 0
        #     elif class_enemy == 'Иссушенный труп':
        #         self.health = 550
        #         self.damage = 10
        #         self.armor = 1
        #         self.dodge = 0
        #         self.critical_damage = 0
        #         self.chance_critical_damage = 0
        # elif self.level == 2:
        #     if class_enemy == 'Странствующий маг':
        #         self.health = 400
        #         self.damage = 40
        #         self.armor = 5
        #         self.dodge = 0.1
        #         self.critical_damage = 0
        #         self.chance_critical_damage = 0
        #     elif class_enemy == 'Страж лабиринта':
        #         self.health = 600
        #         self.damage = 25
        #         self.armor = 10
        #         self.dodge = 0
        #         self.critical_damage = 0
        #         self.chance_critical_damage = 0
        #     elif class_enemy == 'Душа грешника':
        #         self.health = 350
        #         self.damage = 35
        #         self.armor = 0
        #         self.dodge = 0.3
        #         self.critical_damage = 2
        #         self.chance_critical_damage = 0.2
        # elif self.level == 3:
        #     if class_enemy == 'Тролль':
        #         self.health = 700
        #         self.damage = 30
        #         self.armor = 15
        #         self.dodge = 0.25
        #         self.critical_damage = 0
        #         self.chance_critical_damage = 0
        #     elif class_enemy == 'Демон лабиринта':
        #         self.health = 650
        #         self.damage = 60
        #         self.armor = 15
        #         self.dodge = 0.2
        #         self.critical_damage = 0
        #         self.chance_critical_damage = 0
        #     elif class_enemy == 'Огенный дракон':
        #         self.health = 700
        #         self.damage = 40
        #         self.armor = 20
        #         self.dodge = 0.1
        #         self.critical_damage = 0
        #         self.chance_critical_damage = 0
        # elif self.level == 4:
        #     if class_enemy == 'Хранитель лабиринта':
        #         self.health = 1000
        #         self.damage = 40
        #         self.armor = 15
        #         self.dodge = 0.18
        #         self.critical_damage = 0
        #         self.chance_critical_damage = 0
        #     elif class_enemy == 'Осколок леса':
        #         self.health = 3000
        #         self.damage = 0
        #         self.armor = 0
        #         self.dodge = 0
        #         self.critical_damage = 0
        #         self.chance_critical_damage = 0


