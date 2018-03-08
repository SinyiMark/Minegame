import os


def your_stat(you, stat = ''):
    '''
        'you' is your hero dictonary
        if 'stat' is equal 'full' the fun will print the hero's full stat
    '''

    if stat == 'full':
        print('Your full stat')
        print("HP: {} Max HP: {} Attack: {} Armor: {} Gold: {} EXp: {} Level: {}".format(you['hp'], 
                you['maxhp'], you['atk'], you['armor'], you['gold'], you['exp'], you['level']))
    else:
        print('Your figthing stat')
        print("HP: {} Attack: {} Armor: {}".format(you['hp'], you['atk'], you['armor']))   
    

def enemy_stat(enemy):
    print('\n')
    print('{}'.format(enemy['name']))
    print("HP: {} Attack: {} Armor: {}".format(enemy['hp'], enemy['atk'], enemy['armor']))


def basic_ui(floor, you, cleared_room, enemy = 0):
    os.system('cls')
    print('Floor: {} Cleared room: {}'.format(floor,cleared_room))
    your_stat(you)
    if enemy != 0:
        enemy_stat(enemy)


def shop_ui(you):
    os.system('cls')
    print('You arrive in shop')
    your_stat(you, 'full')


def shop_item(shop_items):
    ''' items is  a dictionary in a dictionary '''
    item_id = 0
    for item_name,item_stat in shop_items.items():
        item_id = item_id + 1
        print('\n', 'Id: {} {}'.format(item_id, item_name))
        print(' +{} {} Price: {} gold'.format(item_stat['bonus'], item_stat['bonustype'], item_stat['price']))
        item_stat['id'] = item_id
    return shop_items