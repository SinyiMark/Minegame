import random
import os
import sys
import print_modul


def game_start():
    answer = ''
    print('Welcome back hero''\n''Press "n" to start e new adtventure or "l" to load game')
    while answer != 'n' and answer != 'l':
        answer = input()
    if answer == 'n':
        new_game()
    elif answer == 'l':
        pass


def new_game():
    you = {'name':'You', 'hp': 12, 'atk': 20, 'armor': 0, 'gold': 20, 'exp': 0 , 'maxhp': 12, 'level':1}
    floor = 1
    cleared_room_counter = 0
    gameover = False
    while gameover == False:
        print_modul.basic_ui(floor, you,  cleared_room_counter)
        level_up(you)
        enter_to_room(floor, you,  cleared_room_counter)
        gameover = fight(you, floor, cleared_room_counter)
        if gameover == True:
            input()
            os.system('cls') 
            print(' You Die ')
            input()
            sys.exit(0)
        else:
            input('\n''Press "enter" to countinue or "s" to save')
        cleared_room_counter = cleared_room_counter + 1
        if cleared_room_counter % 3 == 0:
            in_the_shop(you)
            os.system('cls')
            print_modul.your_stat(you, 'full')
            answer = input('If you want to go next floor write "go" : ')
            if answer == 'go':
                floor = floor + 1

def enemy_generator(floor):  
    random_enemy = random.randint(1,10)
    if floor == 1:
        slime_count = [1, 2, 3,]
        goblin_count = [5, 6, 7]
        skeleton_count = [8, 9, 10]
        lvl2_goblin = [4]
        if random_enemy in slime_count:
            enemy = enemy_stat_storage('slime') 
        elif random_enemy in goblin_count:
            enemy = enemy_stat_storage('goblin') 
        elif random_enemy in skeleton_count:
             enemy = enemy_stat_storage('skeleton')
        elif random_enemy in lvl2_goblin:
                enemy = enemy_stat_storage('lvl2_goblin')    
    elif floor == 2:
        slime_count = [1, 2,]
        goblin_count = [5, 6]
        skeleton_count = [8, 9, 10]
        ork_count =[3, 4]
        lvl2_goblin = [7]
        if random_enemy in slime_count:
                enemy = enemy_stat_storage('slime') 
        elif random_enemy in goblin_count:
            enemy = enemy_stat_storage('goblin') 
        elif random_enemy in skeleton_count:
            enemy = enemy_stat_storage('skeleton')
        elif random_enemy in ork_count:
            enemy = enemy_stat_storage('ork')
        elif random_enemy in lvl2_goblin:
            enemy = enemy_stat_storage('lvl2_goblin')    
    return enemy


def enemy_stat_storage(enemy_name):
    if enemy_name == 'slime':
        return {'hp': 3, 'atk': 1, 'armor': 0, 'gold': 2, 'exp':2, 'name':'slime'}
    elif enemy_name == 'goblin':
        return {'hp': 4, 'atk': 2, 'armor': 1, 'gold': 3, 'exp':5, 'name':'goblin'} 
    elif enemy_name == 'skeleton':
        return {'hp': 6, 'atk': 2, 'armor': 0, 'gold': 3, 'exp':5, 'name':'skeleton'}
    elif enemy_name == 'ork':
        return {'hp': 10, 'atk': 4, 'armor': 0, 'gold': 10, 'exp':15, 'name':'ork'}
    elif enemy_name == 'lvl2_goblin':
        return {'hp': 5, 'atk': 3, 'armor': 1, 'gold': 6, 'exp':7, 'name':'goblin [lvl 2]'} 


def fight(you, floor, cleared_room):
    enemy = enemy_generator(floor)
    while True:
        enemy = your_turn(you, floor, enemy, cleared_room)
        if enemy['hp'] < 1:
            print('You killed the {}'.format(enemy['name']))
            you['gold'] = you['gold'] + enemy['gold']
            you['exp'] = you['exp'] + enemy['exp']
            print('You get {} gold and {} exp'.format(enemy['gold'], enemy['exp']))
            return False
        else:
            input('End your turn')
            print_modul.basic_ui(floor, you,  cleared_room, enemy)
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


def your_turn(you, floor, enemy,  cleared_room):
    answer = ''
    attack_helper = ['l', 'm', 'h']
    print_modul.basic_ui(floor, you,  cleared_room, enemy)
    print('\n')
    while answer not in attack_helper:
        answer = input('Press "l" to light, "m" to medium and "h" to heavy attack: ')
        if answer not in attack_helper:
            print('{} is not an option'.format(answer))
    print_modul.basic_ui(floor, you,  cleared_room, enemy)
    if answer == 'l':
        print('\n''You hit the {} with light attack'.format(enemy['name']))
        enemy = attack(you, enemy)
    elif answer == 'm':
        chance = random.randint(1,10)
        if chance > 0 and chance < 7:
            print('\n''You hit the {} with medium attack'.format(enemy['name']))
            enemy = attack(you, enemy, 2)
        else:
            print('Miss')    
    elif answer == 'h':
        chance = random.randint(1,10)
        if chance > 0 and chance < 4:
            print('\n''You hit the {} with heavy attack'.format(enemy['name']))
            enemy = attack(you, enemy, 3)
        else:
            print('Miss')
    return enemy


def enemy_turn(you, enemy):
    attack_type = random.randint(1,3)
    if attack_type == 1 or attack_type == 2:
        enemy_chance = random.randint(1,4)
        if enemy_chance == 4:
            print('\n''{} missed the light attack'.format(enemy['name']))
        else:            
            print('\n''{} hit you with light attack'.format(enemy['name']))
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
    if you['exp'] >= you['level'] *10:
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
        you['exp'] = you['exp'] - you['level'] *10
        input('Press "enter" to countine')


def enter_to_room(floor, you, cleared_room_counter):
     while True:
        print_modul.basic_ui(floor, you, cleared_room_counter)
        answer = input('\n''Press "enter" to kick the door or "i" to info: ') 
        if answer == 'i':
            print('')
            print_modul.your_stat(you, 'full')
            print('Your attacks:''\n''Light attack: damgage[{}] 100°% chance'.format(you['atk']))
            print('Medium attack: damgage[{}], 60°% chance'.format(you['atk'] * 2))
            print('Heavy attack: damgage[{}], 30°% chance'.format(you['atk'] * 3))
            print('')
            input('Press "enter" to countiun')

        else:
            break


def in_the_shop(you):
    shop_items = get_shop_items()
    while True:
        in_shop_ind = False
        print_modul.shop_ui(you)
        shop_items = print_modul.shop_item(shop_items)            
        chosen = input('\n' 'Write the item name wich you want to buy or press "x" to countinu: ')
        if chosen == 'x':
            break
        else:
            try:
                chosen = int(chosen)              
            except:
                input('Pless enter an existing id or "x" ')
                continue
            for item_name, item_stat in shop_items.items():
                if chosen == item_stat['id'] and item_name == 'MAX Heal potion':
                    you['hp'] == you['maxhp']
                    in_shop_ind = True
                    break
                elif chosen == item_stat['id'] and item_name in you:
                    input('{} is already in your inventory'.format(chosen))
                elif item_stat['id'] == chosen:  
                    if item_stat['price'] <= you['gold']:
                        if item_name != 'Heal potion':                           
                            you[item_name] = item_name
                        you[item_stat['bonustype']] = you[item_stat['bonustype']] + item_stat['bonus']
                        you['gold'] = you['gold'] - item_stat['price']
                        in_shop_ind = True
                        break
                    else:
                        input('You dont have enougth gold ')
                        in_shop_ind = True               
            if in_shop_ind == False:    
                input('item with this id {} is not in shop'.format(chosen))
            else:
                shop_items.pop(item_name, None)
            if you['hp'] > you['maxhp']:
                you['hp'] > you['maxhp']


def get_shop_items():
    ''' 
    creat a item list and return to in_the_shop fun
    items is all possiable item
    '''
    items = {'Wooden shield':{'bonustype':'armor', 'bonus':1, 'price':10, 'id':0}, 
            'THE LEGENDARY SWORD':{'bonustype':'atk', 'bonus':5, 'price':40, 'id':0}, 
            'Helmet':{'bonustype':'maxhp', 'bonus':2, 'price':10, 'id':0}, 
            'Chest':{'bonustype':'maxhp', 'bonus':3, 'price':15, 'id':0}, 
            'Iron sword':{'bonustype':'atk', 'bonus':2, 'price':15, 'id':0}, 
            'Iron shield':{'bonustype':'armor', 'bonus':2, 'price':20, 'id':0}
            }
    for i in range(2):
        deleted_item = random.choice(list(items.keys()))
        items.pop(deleted_item, None)
    items['Heal potion'] = {'bonustype':'hp', 'bonus':5, 'price':10, 'id':0}
    items['MAX Heal potion'] = {'bonustype':'hp', 'bonus':'restore full hp', 'price':20, 'id':0}
    return items

game_start()
