
class Hero:
    def __init__(self, name, data_hero):
        self.name = name
        self.class_name = data_hero['name']
        self.health = data_hero['health']
        self.damage = data_hero['damage']
        self.armor = data_hero['armor']
        self.dodge = data_hero['dodge']
        self.critical_damage = data_hero['critical_damage']
        self.chance_critical_damage = data_hero['chance_critical_damage']
        self.skill_colldown = [0,0]
        self.skill1 = data_hero['skill1']
        self.skill2 = data_hero['skill2']

    def attack(self, target):
        target.health -= self.damage
class Enemy:
    def __init__(self, enemy_data):
        self.class_enemy = enemy_data['name']
        self.health = enemy_data['health']
        self.damage = enemy_data['damage']
        self.armor = enemy_data['armor']
        self.dodge = enemy_data['dodge']
        self.critical_damage = enemy_data['critical_damage']
        self.chance_critical_damage = enemy_data['chance_critical_damage']
    def attack(self, target):
        target.health -= self.damage




