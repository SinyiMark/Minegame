import random
import os
import sys


def game():
    answer = ''
    print('Welcome back hero''\n''Press "n" to start e new adtventure or "l" to load game')
    while answer != 'n' and answer != 'l':
        answer = input()
    if answer == 'n':
        new_game()
    elif answer == 'l':
        pass

#slime = {'hp': 4, 'atk': 1, 'armor': 0, 'gold': 1, 'exp':2, 'name':'slime'}  
#goblin = {'hp': 5, 'atk': 2, 'armor': 1, 'gold': 3, 'exp':5, 'name':'goblin'}
#skeleton = {'hp': 5, 'atk': 3, 'armor': 0, 'gold': 3, 'exp':5, 'name':'skeleton'}
#ork = {'hp': 10, 'atk': 4, 'armor': 0, 'gold': 10, 'exp':15, 'name':'ork'}


def print_warrior(you):
    print('Warrior statistic')
    print("HP: {} Attack: {} Armor: {}".format(you['hp'], you['atk'], you['armor']))   


def print_enemy(enemy):
    print('\n''\n')
    print('{}'.format(enemy['name']))
    print("HP: {} Attack: {} Armor: {}".format(enemy['hp'], enemy['atk'], enemy['armor']))


def print_basic_ui(floor, you, enemy = 0):
    os.system('cls')
    print('Floor: ', floor)
    print_warrior(you)
    if enemy != 0:
        print_enemy(enemy)


def enemy_generator(floor):  
    random_enemy = random.randint(1,10)
    if floor == 1:
        slime_count = [1, 2, 3, 4]
        goblin_count = [5, 6, 7]
        skeleton_count = [8, 9, 10]
        if random_enemy  in slime_count:
            enemy = {'hp': 3, 'atk': 1, 'armor': 0, 'gold': 1, 'exp':2, 'name':'slime'} 
        elif random_enemy  in goblin_count:
            enemy = {'hp': 4, 'atk': 2, 'armor': 1, 'gold': 3, 'exp':5, 'name':'goblin'} 
        elif random_enemy  in skeleton_count:
            enemy = {'hp': 6, 'atk': 2, 'armor': 0, 'gold': 3, 'exp':5, 'name':'skeleton'}
    return enemy


def fight(you, floor):
    enemy = enemy_generator(floor)
    while True:
        enemy = your_turn(you, floor, enemy)
        print('')
        if enemy['hp'] < 1:
            print('You killed the {}'.format(enemy['name']))
            you['gold'] = you['gold'] + enemy['gold']
            you['exp'] = you['exp'] + enemy['exp']
            print('You get {} gold and {} exp'.format(enemy['gold'], enemy['exp']))
            print('\n''You have {} gold and {} exp'.format(you['gold'], you['exp']))
            return False
        else:
            input('End your turn')
            print_basic_ui(floor, you, enemy)
            you = enemy_turn(you, enemy)
            if you['hp'] < 1:
                return True
            input('Press "enter" to start your turn')

        
def your_turn(you, floor, enemy):
    answer = ''
    attack_helper = ['l', 'm', 'h']
    print_basic_ui(floor, you, enemy)
    print('\n')
    print('Light attack: damgage[{}] 100°% chance'.format(you['atk']))
    print('Medium attack: damgage[{}], 60°% chance'.format(you['atk'] * 2))
    print('Heavy attack: damgage[{}], 30°% chance'.format(you['atk'] * 3))
    while answer not in attack_helper:
        answer = input('Press "l" to light, "m" to medium and "h" to heavy attack: ')
        if answer not in attack_helper:
            print('{} is not an option'.format(answer))
    if answer == 'l':
        damage = you['atk'] - enemy['armor']
        if damage < 1:
            damage = 0
        print('\n''{} -{} hp'.format(enemy['name'], damage))       
        enemy['hp'] = enemy['hp'] -damage
    elif answer == 'm':
        chance = random.randint(1,10)
        if chance > 0 and chance < 7:
            damage = you['atk'] * 2 - enemy['armor']
            if damage < 1:
                damage = 0
            print('\n''{} -{} hp'.format(enemy['name'], damage))       
            enemy['hp'] = enemy['hp'] -damage
        else:
            print('Miss')    
    elif answer == 'h':
        chance = random.randint(1,10)
        if chance > 0 and chance < 4:
            damage = you['atk'] * 3 - enemy['armor']
            if damage < 1:
                damage = 0
            print('\n''{} -{} hp'.format(enemy['name'], damage))       
            enemy['hp'] = enemy['hp'] -damage
        else:
            print('Miss')
    return enemy


def enemy_turn(you, enemy):
    attack_type = random.randint(1,3)
    if attack_type == 1 or attack_type == 2:
        enemy_chance = random.randint(1,4)
        if enemy_chance == 4:
            print('{} missed the light attack'.format(enemy['name']))
        else:            
            damage = enemy['atk'] - you['armor']
            if damage < 1:
                damage = 0
            print('{} hit you with ligth attack you lose [{}]hp'.format(enemy['name'], damage))
            you['hp'] = you['hp'] - damage
    elif attack_type == 3:
        enemy_chance = random.randint(1,4)
        if enemy_chance == 4 or enemy_chance == 3:
            print('{} missed the medium attack'.format(enemy['name']))
        else:
            damage = enemy['atk'] * 2 - you['armor']
            if damage < 1:
                damage = 0
            print('{} hit you with medium attack you lose [{}]hp'.format(enemy['name'], damage))
            you['hp'] = you['hp'] - damage
    return you


def new_game():
    warrior = {'hp': 1, 'atk': 2, 'armor': 0, 'gold': 0, 'exp':0 , 'maxhp':15, 'level':1}
    floor = 1
    gameover = False
    while gameover == False:
        print_basic_ui(floor, warrior)
        if warrior['exp'] >= warrior['level'] *2:
            answer = 0
            print('level up')
            while  answer != '1' and answer != '2':
                answer = input('Press "1" to increase max hp by 2 or "2" to increase atk by 1: ')
            if answer == '1':
                warrior['maxhp'] = warrior['maxhp'] + 2
                warrior['hp'] = warrior['hp'] + 2
                print('Your max hp now {}'.format(warrior['maxhp']))
            elif answer == '2':
                warrior['atk'] = warrior['atk'] + 1  
                print('Your attack now {}'.format(warrior['atk']))
            input('Press "enter" to countine')
        input('\n''\n''Press "enter" to kick the door') 
        gameover = fight(warrior, floor)
        if gameover == True:
            input()
            os.system('cls') 
            print(' You Die ')
        else:
            input('\n''Press "enter" to countine or "s" to save')

game()
