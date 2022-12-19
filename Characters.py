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
        self.last_damage = 0
        self.plus_damage = 0
    def use_skills(self, target):
        while True:
            print(f'[0] Если хотите выйти из списка умений')
            for number, skill in enumerate(self.skills, 1): #Показываем скиллы
                print(f'[{number}] {skill["name"]}\n             Время отката:{self.skill_colldown[number - 1]} комнат ') #Показываем скиллы
            question = input('Выберите умение: ')
            if question == '0':
                break
            if question.isdigit():
                question = int(question) - 1
                if question in range(len(self.skills)):
                    skill = self.skills[question]
                    if self.skill_colldown[question] == 0:
                        if skill['1hit'] == True:
                            target.health -= target.health
                            print('Враг падает замертво от этого удара!')
                        if skill['damage'] != None:
                            if target.armor > 0:
                                target.armor -= skill['damage']
                                print(f'Вы нанесли врагу {skill["damage"]} урона по броне способностью {skill["name"]}')
                            else:
                                target.health -= skill['damage']
                                print(f'Вы нанесли врагу {skill["damage"]} урона по здоровью способностью {skill["name"]}')

                        if skill['crit_damage'] != None:
                            self.chance_critical_damage += skill['crit_damage']
                            print(f'Вы повысили свой шанс критического урона на {skill["crit_damage"] * 100} %')
                        if skill['health'] != None:
                            self.health += skill['health']
                            print(f'Вы восстановили себе {skill["health"]} пунктов здоровья')
                        if skill['armor'] != None:
                            self.armor += skill['armor']
                            print(f'Вы восстановили себе {skill["armor"]} пунктов брони')
                        if skill['plus_damage'] != None:
                            self.plus_damage += skill['plus_damage']
                            print(f'Вы увеличили свой урон на {skill["plus_damage"]}')
                        if 'овечк' in skill['name']:
                            target.kill_status = True
                            target.health -= target.health
                        if skill['ignore'] != False:
                            target.health = - skill['damage']
                            print(f'Вы нанесли врагу {skill["damage"]} чистого урона способностью {skill["name"]}')
                        self.skill_colldown[question] = skill['skill_colldown']
                    else:
                        print(f'Способность еще не перезарядилась. Время перезарядки {self.skill_colldown[question]} комнат')



                else:
                    print('Вы ввели неверное число.')
            else:
                print('Вы ввели неверное число.')







    def colldown_count(self):
        for skill in self.skill_colldown:
            if skill != 0:
                skill -= 1


    def attack(self, target):
        dodge = random.uniform(0,1)
        if self.no_miss == True:
            self.crit_hp_armor_choice(target)
        elif target.dodge < dodge:
            self.crit_hp_armor_choice(target)
        else:
            print(f'{target.class_enemy} удалось уклониться')
    def destroy_item(self):
        item = self.inventory.pop(random.randint(0, len(self.inventory) - 1))
        print(f'Вы потеряли {item["name"]} из своего инвентаря')
    def dice_drop(self):
        enemy_dice1 = random.randrange(1, 6)
        enemy_dice2 = random.randrange(1, 6)
        sum_enemy = enemy_dice1 + enemy_dice2

        hero_dice1 = random.randrange(1, 6)
        hero_dice2 = random.randrange(1, 6)
        sum_hero = hero_dice1 + hero_dice2
        return sum_hero, sum_enemy
    def check_inventory(self, target):
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
                                print(item['short_desc'])
                            else:
                                self.health += item['health']
                                print(item['short_desc'])
                        if item['damage'] != None:
                            self.damage += item['damage']
                            print(item['short_desc'])
                        if item['armor'] != None:
                            if isinstance(item['armor'], str):
                                self.armor += self.maxhealth * (int(item['armor']) / 100)
                                print(item['short_desc'])
                            else:
                                self.armor += item['armor']
                                print(item['short_desc'])
                        if item['dodge'] != None:
                            self.dodge += item['dodge']
                            print(item['short_desc'])
                        if item['critical_damage'] != None:
                            self.critical_damage += item['critical_damage']
                            print(item['short_desc'])
                        if item['chance_critical_damage'] != None:
                            self.chance_critical_damage += item['chance_critical_damage']
                            print(item['short_desc'])
                        if item['add_skill'] == True:
                            self.skills.append(item['skill'])
                            self.skill_colldown.append(0)
                            print(item['short_desc'])
                        if item['add_artefacts'] == True:
                            if item['health'] == -99999:
                                randomchest = random.choice([0, 1])
                                if randomchest == 0:
                                    self.health -= 99999
                                    print(f'Когда открылся {item["name"]} оттуда вылетел дух и забрал вашу душу. Вы погибли.')
                                else:
                                    artefact = random.choice(data.list_of_artefacts[0])
                                    self.inventory.append(artefact)
                                    print(f'Вы получаете {artefact["name"]}')
                                    print(artefact['short_desc'])
                            else:
                                 for i in range(item['add_artefact_count']):
                                    self.inventory.append(random.choice(data.list_of_artefacts[0]))
                        if item['no_miss'] == True:
                            self.no_miss = True
                        if item['rearm'] == True:
                            self.skill_colldown = []
                            for i in self.skills:
                                self.skill_colldown.append(0)
                        if 'кубик' in item['name']:

                            dice1, dice2 = self.dice_drop()
                            if dice1 <= 4:
                                artefact = random.choice(data.list_of_artefacts[0])
                                self.inventory.append(artefact)
                                print(f'Вам повезло - выпало {dice1}. Вы получаете {artefact["name"]}')
                                print(artefact['short_desc'])
                            elif 4 > dice1 <= 8:
                                artefact = random.choice(data.list_of_artefacts[1])
                                self.inventory.append(artefact)
                                print(f'Вам повезло - выпало {dice1}. Вы получаете {artefact["name"]}')
                                print(artefact['short_desc'])
                            else:
                                print(f'Вам не повезло - выпало {dice1}')
                                self.destroy_item()

                        if 'вампиризм' in item['short_desc']:
                            self.vampir = [10, True]
                        if 'Петля' in item['name']:
                            self.health += self.last_damage
                            print(f'Вы восстановили {self.last_damage} ЗДР')
                        if 'Кроличья' in item['name']:
                            if 'стая' in target['name']:
                                target.kill_status = True
                                target.health -= target.health
                            else:
                                print('Противник отбросил кроличью лапку. Эффекта не произошло.')

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
            damage = (self.damage * self.critical_damage) + self.plus_damage
            print(f'У {self.name} прошел критический урон. Он составляет {damage}')
            if target.armor > 0:
                target.armor -= damage
                print(f' {damage} урона нанесено по броне.')
            else:
                target.health -= damage
                print(f' {damage} урона нанесено по здоровью.')
        else:
            damage = self.damage + self.plus_damage
            if target.armor > 0:
                target.armor -= damage
                print(f' {damage} урона нанесено по броне.')
            else:
                target.health -= damage
                print(f' {damage} урона нанесено по здоровью.')

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
        self.kill_status = False
        self.skill1 = enemy_data['skill1']
        self.skill_colldown = [0, 0]


    def attack(self, target):
        dodge = random.uniform(0,1)
        if target.dodge < dodge:
            chance_critical = random.uniform(0,1)
            if self.chance_critical_damage > chance_critical:
                damage = self.damage * self.critical_damage
                print(f'У {self.class_enemy} прошел критический урон. Он составляет {damage}')
                if target.armor > 0:
                    target.armor -= damage
                    print(f' {damage} урона нанесено по броне.')
                else:
                    target.health -= damage
                    print(f' {damage} урона нанесено по здоровью.')
            else:
                damage = self.damage
                if target.armor > 0:
                    target.armor -= damage
                    print(f' {damage} урона нанесено по броне.')
                else:
                    target.health -= damage
                    print(f' {damage} урона нанесено по здоровью.')
            target.last_damage = damage
        else:
            print(f'{target.name} удалось уклониться')

    def enemy_use_skill(self, target):
        if self.skill1['skill_colldown'] == 0:
            if self.skill1['1hit'] == True:
                target.health -= target.health
                print('Враг убивает Вас с одного удара!')
            if self.skill1['damage'] != None:
                if target.armor > 0:
                    target.armor -= self.skill1['damage']
                    print(f'{self.class_enemy} нанес {self.skill1["damage"]} урона по броне способностью {self.skill1["name"]}')
                else:
                    target.health -= self.skill1['damage']
                    print(f'{self.class_enemy} нанес {self.skill1["damage"]} урона по здоровью способностью {self.skill1["name"]}')

            if self.skill1['crit_damage'] != None:
                self.chance_critical_damage += self.skill1['crit_damage']
                print(f'{self.class_enemy} повысил свой шанс критического урона на {self.skill1["crit_damage"] * 100} %')
            if self.skill1['health'] != None:
                self.health += self.skill1['health']
                print(f'{self.class_enemy} восстановил себе {self.skill1["health"]} пунктов здоровья')
            if self.skill1['armor'] != None:
                self.armor += self.skill1['armor']
                print(f'{self.class_enemy} восстановил себе {self.skill1["armor"]} пунктов брони')
            if self.skill1['plus_dodge'] != None:
                self.dodge += self.skill1['plus_dodge']
                print(f'{self.class_enemy} увеличил своё уклонение на {self.skill1["plus_dodge"]}')
            if self.skill1['plus_damage'] != None:
                self.dodge += self.skill1['plus_damage']
                print(f'{self.class_enemy} увеличил свою силу атаки на {self.skill1["plus_damage"]}')


