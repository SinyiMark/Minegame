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


def print_your_stat(you, in_shop = ''):
    if in_shop == 'in':
        print('Your figthing stat')
        print("HP: {} Max HP: {} Attack: {} Armor: {} Gold: {} EXp: {} Level: {}".format(you['hp'], 
                you['maxhp'], you['atk'], you['armor'], you['gold'], you['exp'], you['level']))
    else:
        print('Your full stat')
        print("HP: {} Attack: {} Armor: {}".format(you['hp'], you['atk'], you['armor']))   
    

def print_enemy(enemy):
    print('\n''\n')
    print('{}'.format(enemy['name']))
    print("HP: {} Attack: {} Armor: {}".format(enemy['hp'], enemy['atk'], enemy['armor']))


def print_basic_ui(floor, you, enemy = 0):
    os.system('cls')
    print('Floor: ', floor)
    print_your_stat(you)
    if enemy != 0:
        print_enemy(enemy)

def print_shop_ui(you):
    os.system('cls')
    print('You arrive in shop')
    print_your_stat(you, 'in')

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

def attack(attacker, defender, damage_multiplier = 1):
    damage = attacker['atk'] * damage_multiplier - defender['armor']
    if damage < 1:
        damage = 0
    print('\n''{} lose -{} hp'.format(defender['name'], damage))       
    defender['hp'] = defender['hp'] -damage
    print()
    return defender


def your_turn(you, floor, enemy):
    answer = ''
    attack_helper = ['l', 'm', 'h', 'i']
    print_basic_ui(floor, you, enemy)
    print('\n')
    while answer not in attack_helper:
        answer = input('Press "l" to light, "m" to medium and "h" to heavy attack: ')
        if answer not in attack_helper:
            print('{} is not an option'.format(answer))
    if answer == 'l':
       enemy = attack(you, enemy)
    elif answer == 'm':
        chance = random.randint(1,10)
        if chance > 0 and chance < 7:
            enemy = attack(you, enemy, 2)
        else:
            print('Miss')    
    elif answer == 'h':
        chance = random.randint(1,10)
        if chance > 0 and chance < 4:
            enemy = attack(you, enemy, 3)
        else:
            print('Miss')
    elif answer == 'i':
        print('Light attack: damgage[{}] 100°% chance'.format(you['atk']))
        print('Medium attack: damgage[{}], 60°% chance'.format(you['atk'] * 2))
        print('Heavy attack: damgage[{}], 30°% chance'.format(you['atk'] * 3))
    return enemy


def enemy_turn(you, enemy):
    attack_type = random.randint(1,3)
    if attack_type == 1 or attack_type == 2:
        enemy_chance = random.randint(1,4)
        if enemy_chance == 4:
            print('{} missed the light attack'.format(enemy['name']))
        else:            
            print('{} hit you with light attack'.format(enemy['name']))
            you = attack(enemy, you)
    elif attack_type == 3:
        enemy_chance = random.randint(1,4)
        if enemy_chance == 4 or enemy_chance == 3:
            print('{} missed the medium attack'.format(enemy['name']))
        else:
            print('{} hit you with medium attack'.format(enemy['name']))
            you = attack(enemy, you, 2)
    return you


def level_up(you):
    if you['exp'] >= you['level'] *2:
        answer = 0
        print('level up')
        while  answer != '1' and answer != '2':
            answer = input('Press "1" to increase max hp by 2 or "2" to increase atk by 1: ')
        if answer == '1':
            you['maxhp'] = you['maxhp'] + 2
            you['hp'] = you['hp'] + 2
            print('Your max hp now {}'.format(you['maxhp']))
        elif answer == '2':
            you['atk'] = you['atk'] + 1  
            print('Your attack now {}'.format(you['atk']))
        you['level'] = you['level'] + 1
        input('Press "enter" to countine')

def new_game():
    you = {'name':'You', 'hp': 10, 'atk': 2, 'armor': 0, 'gold': 0, 'exp':0 , 'maxhp':15, 'level':1}
    floor = 1
    cleared_room_counter = 0
    gameover = False
    while gameover == False:
        print_basic_ui(floor, you)
        level_up(you)
        while True:
            print_basic_ui(floor, you)
            answer = input('\n''Press "enter" to kick the door or "i" to attack info: ') 
            if answer == 'i':
                print('\n''Light attack: damgage[{}] 100°% chance'.format(you['atk']))
                print('Medium attack: damgage[{}], 60°% chance'.format(you['atk'] * 2))
                print('Heavy attack: damgage[{}], 30°% chance'.format(you['atk'] * 3))
            else:
                break
        gameover = fight(you, floor)
        if gameover == True:
            input()
            os.system('cls') 
            print(' You Die ')
        else:
            input('\n''Press "enter" to countine or "s" to save')
        cleared_room_counter = cleared_room_counter + 1
        if cleared_room_counter == 5:
             print_shop_ui(you)
             input()
game()
