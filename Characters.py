import os
import random
import data
class Hero:
    def __init__(self, name, data_hero):
        self.name = name
        self.class_name = data_hero['name']
        self.health = data_hero['health']
        self.maxhealth = self.health
        self.damage = data_hero['damage']
        self.armor = data_hero['armor']
        self.dodge = data_hero['dodge']
        self.critical_damage = data_hero['critical_damage']
        self.chance_critical_damage = data_hero['chance_critical_damage']
        self.skill_colldown = [0,0]
        self.skills = [data_hero['skill1'], data_hero['skill2']]
        self.inventory = []
        self.no_miss = False
        self.vampir = [0, False]
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
        while True:
            print('В вашем инвентаре:')
            print('[0] Если хотите выйти из инвентаря.')
            for number, item in enumerate(self.inventory, 1):
                print(f'[{number}] {item["name"]} [{item["count"]} шт]')
            question = input('Введите номер используемого предмета:')
            if question == '0':
                break
            if question.isdigit():
                question = int(question) - 1
                if question in range(len(self.inventory)):
                    item = self.inventory[question]
                    print(f'{item["short_desc"]} [{item["count"]} шт]')
                    second_quest = input("Использовать предмет? Да/Нет").lower()
                    if second_quest == "да":
                        if item['health'] != None:
                            if isinstance(item['health'], str):
                                self.health += self.maxhealth * (int(item['health']) / 100)
                            else:
                                self.health += item['health']
                        if item['damage'] != None:
                            self.damage += item['damage']
                        if item['armor'] != None:
                            self.armor += item['armor']
                        if item['dodge'] != None:
                            self.dodge += item['dodge']
                        if item['critical_damage'] != None:
                            self.critical_damage += item['critical_damage']
                        if item['chance_critical_damage'] != None:
                            self.chance_critical_damage += item['chance_critical_damage']
                        if item['add_skill'] == True:
                            self.skills.append(item['skill'])
                            self.skill_colldown.append(0)
                        if item['add_artefacts'] == True:
                            if item['health'] == -99999:
                                randomchest = random.choice([0, 1])
                                if randomchest == 0:
                                    self.health -= 99999
                                else:
                                    self.inventory.append(random.choice(data.list_of_artefacts[0]))
                            else:
                                 for i in range(item['add_artefact_count']):
                                    self.inventory.append(random.choice(data.list_of_artefacts[0]))
                        if item['no_miss'] == True:
                            self.no_miss = True
                        if item['rearm'] == True:
                            self.skill_colldown = []
                            for i in self.skills:
                                self.skill_colldown.append(0)
                        if 'вампиризм' in item['short_desc']:
                            self.vampir = [10, True]

                        item['count'] -= 1
                        if item['count'] <= 0:
                            self.inventory.remove(item)
                    else:
                        continue
                else:
                    print('Неверный номер предмета')
            else:
                print('Вы ввели неверное значение. Введите номер предмета.')
            os.system('cls')

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

    def add_item(self, item):
        for item_inventory in self.inventory:
            if item['name'] == item_inventory['name']:
                item_inventory['count'] += 1
            else:
                self.inventory.append(item)
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



