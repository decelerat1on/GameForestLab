import random
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
        self.skills = [data_hero['skill1'], data_hero['skill2']]
        self.inventory = []
        self.no_miss = False
    def use_skills(self, target):
        for number, skill in enumerate(self.skills, 1):
            print(f'[{number}] {skill["name"]}')
        question = input('Выберите умение: ')
 #        try:
#            skill = self.skills[int(question) - 1]
#            if skill['1hit'] == True:
#                return False
 #           if skill['damage'] != None:
                #TODO Не забыть про чистый урон. Дописать скиллы и награду.



    def attack(self, target):
        dodge = random.uniform(0,1)
        if self.no_miss == True:
            self.crit_hp_armor_choice(target)
        elif target.dodge < dodge:
            target_dodge_int = round(target.dodge * 100)
            print(f'{target.class_enemy} не уклонился с шансом {target_dodge_int}%')
            self.crit_hp_armor_choice(target)
        else:
            print(f'{target.class_enemy} удалось уклониться')

    def check_inventory(self):
        print('В вашем инвентаре:')
        for number, item in enumerate(self.inventory, 1):
            print(f'[{number}] {item["name"]}')
    def crit_hp_armor_choice(self, target):
        chance_critical = random.uniform(0, 1)
        if self.chance_critical_damage > chance_critical:
            damage = self.damage * self.critical_damage
            print(f'У {self.name} прошел критический урон. Он составляет {damage}')
            if target.armor > 0:
                target.armor -= damage
                print('Урон нанесён по броне.')
            else:
                target.health -= damage
                print('Урон нанесён по здоровью.')

        else:
            damage = self.damage
            if target.armor > 0:
                target.armor -= damage
                print('Урон нанесён по броне.')
            else:
                target.health -= damage
                print('Урон нанесён по здоровью.')
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
        dodge = random.uniform(0,1)
        if target.dodge < dodge:
            target_dodge_int = round(target.dodge * 100)
            print(f'{target.name} не уклонился с шансом {target_dodge_int}%')
            chance_critical = random.uniform(0,1)
            if self.chance_critical_damage > chance_critical:
                damage = self.damage * self.critical_damage
                print(f'У {self.class_enemy} прошел критический урон. Он составляет {damage}')
                if target.armor > 0:
                    target.armor -= damage
                    print('Урон нанесён по броне.')
                else:
                    target.health -= damage
                    print('Урон нанесён по здоровью.')
            else:
                damage = self.damage
                if target.armor > 0:
                    target.armor -= damage
                    print('Урон нанесён по броне.')
                else:
                    target.health -= damage
                    print('Урон нанесён по здоровью.')
        else:
            print(f'{target.name} удалось уклониться')



