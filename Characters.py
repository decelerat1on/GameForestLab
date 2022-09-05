class Hero:
    def __init__(self, name, class_name):
        self.inventory = {}
        self.name = name
        self.class_name = class_name
        if self.class_name == "Волшебник":
            self.health = 1500
            self.damage = 150
            self.armor = 7
            self.dodge = 0.13
            self.critical_damage = 3
            self.chance_critical_damage = 0.1
        elif class_name == "Лучник":
            self.health = 2000
            self.damage = 100
            self.armor = 9
            self.dodge = 0.20
            self.critical_damage = 2
            self.chance_critical_damage = 0.08
        elif class_name == "Воин":
            self.health = 2500
            self.damage = 100
            self.armor = 12
            self.dodge = 0.15
            self.critical_damage = 2
            self.chance_critical_damage = 0.05

class Enemy:
    def __init__(self, level, class_enemy):
        self.level = level
        self.class_enemy = class_enemy
        if self.level == 1:
            if class_enemy == 'Волчья стая':
                self.health = 250
                self.damage = 15
                self.armor = 0
                self.dodge = 0.03
            elif class_enemy == 'Гоблин с копьем'
                self.health = 200
                self.damage = 20
                self.armor = 1
                self.dodge = 0.15
            elif class_enemy == 'Иссушенный труп'
                self.health = 550
                self.damage = 10
                self.armor = 1
                self.dodge = 0
        elif self.level == 2:
            if class_enemy == 'Станствующий маг'


