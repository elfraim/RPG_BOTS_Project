## RPG Bots game
import random
import os
import sys
import math
import time

running = True

#colors 
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4M'
    ORANGE = '\033[33m'
    PURPLE = '\033[35m'

## classes of player, enemy and spells
## Person, Players or npc
class Person:
    def __init__(self, name, hp, atk, mp, dfc, magic, items, pclass, plevel, exp, upexp, gold):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atk = atk
        self.dfc = dfc
        self.magic = magic
        self.actions = ["Attack", "Magic", "Items", "Run"]
        self.menu_actions = ["Locations", "Inventory", "Medic", "Weapon Shop"]
        self.locations = ["Farm land"]
        self.items = items
        self.pclass = pclass
        self.plevel = plevel
        self.exp = exp
        self.upexp = upexp
        self.gold = gold
        self.str = 5
        self.agi = 5
        self.int = 5
        self.con = 8
        self.mainh = 0
        self.main_equiped = hands

## Defining the spell class for future skills
class Spell:
    def __init__(self, name, mpcost, mind, maxd, element, price):
        self.name = name
        self.mpcost = mpcost
        self.mind = mind
        self.maxd = maxd
        self.type = element
        self.price = price


## Defining the items
class Item:
    def __init__(self, name, type, description, prop, quantity):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop
        self.quantity = quantity

class Weapon:
    def __init__(self, name, mind, maxd, price, minlevel):
        self.name = name
        self.mind = mind
        self.maxd = maxd
        self.price = price
        self.minlevel = minlevel





#ITEMS 
small_hp_pot = Item("Small Hp Potion", "potion", "Heals for 10 HP", 10, 0)
big_hp_pot = Item("Big Hp Potion", "potion", "Heals for 20 HP", 20, 0)


#player inventory dictonary, default starts with 1 shp 1 bhp
player_items_dic = {"Small hp potion": 1, "Big hp potion": 0}




hands = Weapon('Hands', 1, 2, 0, 0) # Default weapon
# Warrior Weapons
bronze_sword = Weapon('Bronze Sword', 4, 6, 50, 2)
iron_sword = Weapon('Iron Sword', 6, 8, 100, 4)
steel_sword = Weapon('Steel Sword', 6, 13, 200, 5)

#Mage Spells
#Magic spells
magic_hands = Spell("Hands", 0, 1, 2, "black", 0)
fire_bolt = Spell("Fire Bolt", 3, 4, 6, "black", 50)
ice_bolt = Spell("Ice Bolt", 5, 5, 12, "black", 100)

## shops
general_shop_dic = {"Small Hp potion": 10, "Big Hp potion": 25}

#Weapon shops
warrior_weapons = [bronze_sword, iron_sword, steel_sword] # List of weapons inserted into warrior_weapon_shop() function
spell_shop_li =[fire_bolt, ice_bolt] # List of spells inserted into spell_shop() function
current_learned_spells = [] #player spells list, Each time you learn a spell by buying it it appends to this list


#MONSTERS > name, hp, atk, mp, dfc, magic, items, pclass, plevel, exp, upexp, gold
#Farmland mobs
goat = Person("Goat", 15, 1, 0, 1, [], [], "Monster", 1, 2, 0, 12)
dog = Person("Dog", 18, 1, 0, 1, [], [], "Monster", 1, 3, 0, 12)
snake = Person("Snake", 25, 2, 0, 2, [], [], "Monster", 2, 4, 0, 16)
horse = Person("Horse", 28, 3, 0, 3, [], [], "Monster", 3, 6, 0, 17)
bull = Person("Bull", 32, 5, 0, 4, [], [], "Monster", 4, 9, 0, 20)
hog = Person("Hog", 35, 6, 0, 4, 0, [], "Monster", 4, 10, 0, 22)
farmland_mobs = [goat, snake, horse, bull, hog]

#Forest mobs
bear = Person("Bear", 38, 7, 0, 5, [], [], "Monster", 5, 12, 0, 30)
ghost = Person("Ghost", 42, 9, 0, 6, [], [], "Monster", 6, 15, 0, 32)
witch = Person("Witch", 47, 11, 0, 7, [], [], "Monster", 7, 18, 0, 34)
unicorn = Person("Unicorn", 52, 13, 0, 8, [], [], "Monster", 8, 20, 0, 36)
wild_stag = Person("Wild Stag", 60, 15, 0, 9, [], [], "Monster", 9, 22, 0, 38)

## Damage functions
def weapon_damage():
    dmg_low = player.main_equiped.mind + player.atk
    dmg_high = player.main_equiped.maxd + player.atk
    damage = random.randrange(dmg_low, dmg_high)
    if damage < 0:
        damage = 0
    else:
        pass
    return damage

def spell_dmg():
    dmg_low = player.main_equiped.mind + player.atk
    dmg_high = player.main_equiped.maxd + player.atk
    damage = random.randrange(dmg_low, dmg_high)
    if damage < 0:
        damage = 0
    else:
        pass
    return damage

def generate_damage():
    dmg_low = player.atk - 5
    dmg_high = player.atk + 5
    damage = random.randrange(dmg_low, dmg_high)
    if damage < 0:
        damage = 0
    else:
        pass
    return damage

def generate_edamage():
    dmg_low = enemy.atk - 5
    dmg_high = enemy.atk + 5
    damage = random.randint(dmg_low, dmg_high)
    if damage < 0:
        damage = 0
    else:
        pass
    return damage
 
################################################### 
# Play activity functions, Menu.. fighting actions, showing inventory, magic etc..
def choose_menu_action():
    print("\nClass:" + player.pclass +  "|Level:" + str(player.plevel) + "|" + bcolors.PURPLE + "Exp:" + str(player.exp) + "/" + str(round(player.upexp)) + bcolors.OKGREEN + "\nHealth:" + str(player.hp) + "/" + str(round(player.maxhp)) + bcolors.OKBLUE + "\nMana:" + str(player.mp) + "/" + str(player.maxmp) + bcolors.ENDC +  "\nAttack Power:" + str(player.atk))
    print(bcolors.WARNING + "Gold:" + str(player.gold) + bcolors.ENDC)
    if player.pclass == "Warrior":
        print("Main hand:" + player.main_equiped.name + "(" + str(player.main_equiped.mind) + "-" + str(player.main_equiped.maxd) + ")")
    elif player.pclass == "Mage":
        print(bcolors.BOLD + "Main Spell:" + player.main_equiped.name + "(" + str(player.main_equiped.mind) + "-" + str(player.main_equiped.maxd) + ")" + bcolors.ENDC)
    i = 1
    print("Actions")
    for item in player.menu_actions:
        print("    " + str(i) + ".", item)
        i += 1

def choose_location():
    i = 1
    print("Locations")
    for item in player.locations:
        print("    " + str(i) + ".", item)
        i += 1

def choose_fight_action():
    i = 1
    print("Actions")
    for item in player.actions:
        print("    " + str(i) + ".", item)
        i += 1

def choose_magic():
        i = 0
        for spell in player.magic:
            if player.magic == []:
                print("You have no spells, Please visit the mage shop")
                time.sleep(2)
                break
            i += 1
            print("    " + str(i) + "." + " Equip:", spell.name, str(spell.mpcost) + "MP each cast")

def show_inventory():
    i = 1
    print("Inventory")
    for item, val in player.items.items(): ## iteratin through a dictonary!
        print("    " + str(i) + "." + item + ": " + "x" + str(val))
        i += 1

def general_shop():
    i = 1
    print("General Shop")
    for item, val in general_shop_dic.items():
        print("    " + str(i) + ".", item + ": " + "Price:" + str(val))
        i += 1

def warrior_weapon_shop():
    i = 1
    for wep in warrior_weapons:
        print("    " + str(i) + ".", wep.name + "(" + str(wep.mind) + "-" + str(wep.maxd) + ")" + " Req lv:" + str(wep.minlevel) + " Price:" + str(wep.price))
        i += 1

def spell_shop():
    i = 1
    for spell in spell_shop_li:
        print("    " + str(i) + ".", spell.name + "(" + str(spell.mind) + "-" + str(spell.maxd) + ")" + " Mp cost:" + str(spell.mpcost) + " Price:" + str(spell.price))
        i += 1
###################################################
##Character functions
def stats_maker():
    if player.pclass == "Warrior": # Warrior stats
        calcu_damage = (player.str + player.agi) / 2.2 ## Calculates warrior attack damage
        calcu_health = player.con * 1.5
        player.atk = round(calcu_damage)
        player.maxhp = round(calcu_health)
        player.hp = round(calcu_health)
    elif player.pclass == "Mage":
        calcu_damage = (player.int + player.agi) / 2.0 ## Calculates mage attack damage
        calcu_health = player.con * 1.4
        calcu_mana = player.mp * 1.2
        player.atk = round(calcu_damage)
        player.maxhp = round(calcu_health)
        player.hp = round(calcu_health)

def level_up():
    player.plevel += 1
    player.upexp *= 2.1
    player.exp = 0
    print(bcolors.HEADER + bcolors.ORANGE + "\nYou have gained a level!" + bcolors.ENDC)
    if player.pclass == "Warrior":
        player.str *= 1.5
        player.agi *= 1.2
        player.int *= 1.1
        player.con *= 1.5
    elif player.pclass == "Mage":
        player.str *= 1.1
        player.agi *= 1.2
        player.int *= 1.7
        player.con *= 1.3
    stats_maker()
    print(bcolors.OKBLUE + "Your stats:")
    print("Attack:" + str(player.atk) + "\nStrength: " + str(round(player.str)) + "\nAgility: " + str(round(player.agi)) + "\nIntelligence: " + str(round(player.int)) + "\nEndurance: " + str(round(player.con) + bcolors.ENDC))
    time.sleep(5)   
    os.system("cls")
    if player.plevel == 3:
        player.locations.append("Forest")
        print("You have unlocked Forest map")
        time.sleep(2)         

def attack():
    print("A " + enemy.name + "(lvl " + str(enemy.plevel) + ")\n") # enemy name + level
    choose_fight_action() # choose an action against the monster
    step = input("> ")
    if step == "1": # ATTACK 
        os.system("cls")
        while True: # Fighting loop
            ### Fighting code in while loop       future plan to add agility to determain who attacks first     
            if player.hp > 0 and enemy.hp > 0:
                player_damage = weapon_damage() # Generate player damage
                enemy.hp -= player_damage
                if enemy.hp < 0:
                    enemy.hp = 0
                else:
                    pass
                print("You hit with your " + bcolors.BOLD + player.main_equiped.name + bcolors.ENDC + " and deal " + bcolors.OKBLUE + str(player_damage) + bcolors.ENDC + " Damage, Enemy has " + bcolors.FAIL + str(enemy.hp) + bcolors.ENDC + " Hp left")
                time.sleep(1)

                if player.hp > 0 and enemy.hp <= 0: # this runs if player is still alive and mob is dead
                    player.exp += enemy.exp
                    player.gold += round(enemy.gold)
                    enemy.hp = enemy.maxhp
                    print("You have killed the " + enemy.name + " And gained " + bcolors.PURPLE + str(enemy.exp) + " Exp" + bcolors.ENDC + " and " + bcolors.WARNING + str(round(enemy.gold)) + " Gold!" + bcolors.ENDC)
                    time.sleep(2)
                    if player.exp >= player.upexp: # Also checks if player leveled up from the exp of the mob all Can be made into a function!!
                        level_up()
                        break  
                    else: # if didnt level up just pass
                        break
                    
                enemy_damage = generate_edamage() # Generate enemy damage
                player.hp -= enemy_damage
                if player.hp < 0:
                    player.hp = 0
                else:
                    pass
                print("The enemy did " + bcolors.FAIL + str(enemy_damage) + bcolors.ENDC + " Damage, You have " + bcolors.OKGREEN + str(player.hp) + bcolors.ENDC + " Hp left")

                time.sleep(1)
                if player.hp <= 0 and enemy.hp > 0: # If player is dead and enemy still alive
                    player.hp = 0
                    enemy.hp = enemy.maxhp
                    print(bcolors.FAIL + "You are dead! Visit the Medic." + bcolors.ENDC)
                    time.sleep(3)
                    os.system("cls")
                    break # Breaks the while loop that attacks the mob
            elif player.hp <= 0:
                print("You are dead! Visit the Medic to revive")
                time.sleep(2)
                break       
    elif step == "2": ## MAGIC, WIP
        choose_magic()
        spell = input("> ")
        if spell == '1' and fire_bolt in current_learned_spells:
            player.main_equiped = fire_bolt
            print("You are now using Fire Bolt!")
            time.sleep(1)
        elif spell == '2' and ice_bolt in current_learned_spells:
            player.main_equiped = ice_bolt
            time.sleep(1)

    elif step == "3": # CHOOSE ITEM
        os.system("cls")
        show_inventory()
        choose_item = input("> ")
        if choose_item == "1":
            if player_items_dic["Small hp potion"] > 0:
                while player.hp < player.maxhp:
                    if player.hp < player.maxhp - 10:
                        player.items["Small hp potion"] -= 1
                        player.hp += 10
                        os.system('cls')
                        print("Used small hp pot")
                        time.sleep(1)
                        break
                    elif player.hp == player.maxhp:
                        os.system('cls')
                        print("You're already max hp")
                        time.sleep(1)
                        break
                    else:
                        os.system('cls')
                        player.items["Small hp potion"] -= 1
                        player.hp = player.maxhp
                        print("You used a small hp potion")
                        time.sleep(1)
                        break
            else:
                os.system('cls')
                print("You don't have enough")
                time.sleep(1)
        elif choose_item == "2":
            if player.items["Big hp potion"] > 0:
                while player.hp < player.maxhp:
                    if player.hp < player.maxhp - 20:
                        player.items["Big hp potion"] -= 1
                        player.hp += 20
                        print("Used big hp potion")
                        time.sleep(1)
                        os.system('cls')
                        break
                    elif player.hp == player.maxhp:
                        print("You're already max hp")
                        time.sleep(1)
                        os.system('cls')
                        break
                    else:
                        player.items["Big hp potion"] -= 1
                        player.hp = player.maxhp
                        print("Used a big hp potion")
                        time.sleep(1)
                        os.system('cls')
                        break
            else:
                os.system('cls')
                print("You don't have enough")
                time.sleep(1)
        else:
            os.system('cls')
            print("Invalid input")
            time.sleep(1)             

def mage_attack():
    print("A " + enemy.name + "(lvl " + str(enemy.plevel) + ")\n") # Enemy name + level
    choose_fight_action() # choose an action against the monster
    step = input("> ")
    if step == "1": # ATTACK 
        os.system("cls")
        while True: # Fighting loop
            ### Fighting code in while loop       future plan to add agility to determain who attacks first     
            if player.hp > 0 and player.mp >= player.main_equiped.mpcost and enemy.hp > 0: # Player alive and has mp and mob is alive
                player_damage = spell_dmg() # Generate player damage
                enemy.hp -= player_damage
                if enemy.hp <= 0:
                    enemy.hp = 0
                else:
                    pass
                player.mp -= player.main_equiped.mpcost
                print("You hit with your " + bcolors.BOLD + player.main_equiped.name + bcolors.ENDC + bcolors.OKBLUE + " (" + str(player.mp) + "/" + str(player.maxmp) + ")" + " Mp Left" + bcolors.ENDC + " and deal " + bcolors.OKBLUE + str(player_damage) + bcolors.ENDC + " Damage, Enemy has " + bcolors.FAIL + str(enemy.hp) + bcolors.ENDC + " Hp left")
                time.sleep(1.5)

                if player.hp > 0 and enemy.hp <= 0: # this runs if player is still alive and mob is dead
                    player.exp += enemy.exp
                    player.gold += round(enemy.gold)
                    enemy.hp = enemy.maxhp
                    player.mp = player.maxmp
                    print("You have killed the " + enemy.name + " And gained " + bcolors.PURPLE + str(enemy.exp) + " Exp" + bcolors.ENDC + " and " + bcolors.WARNING + str(round(enemy.gold)) + " Gold!" + bcolors.ENDC)
                    time.sleep(3)
                    os.system("cls")
                    if player.exp >= player.upexp: # Also checks if player leveled up from the exp of the mob all Can be made into a function!!
                        level_up()
                        break  
                    else: # if didnt level up just pass
                        break
                    
                enemy_damage = generate_edamage() # Generate enemy damage
                player.hp -= enemy_damage
                if player.hp <= 0:
                    player.hp = 0
                else:
                    pass
                print("The enemy did " + bcolors.FAIL + str(enemy_damage) + bcolors.ENDC + " Damage, You have " + bcolors.OKGREEN + str(player.hp) + bcolors.ENDC + " Hp left")
                time.sleep(1)

                if player.hp <= 0 and enemy.hp > 0: # If player is dead and enemy still alive
                    player.hp = 0
                    enemy.hp = enemy.maxhp
                    player.mp = player.maxmp
                    print(bcolors.FAIL + "You are dead! Visit the Medic." + bcolors.ENDC)
                    time.sleep(3)
                    os.system("cls")
                    break # Breaks the while loop that attacks the mob   
            elif player.hp <= 0:
                print("You are DEAD! Revive at the medic.")
                time.sleep(2)
                break
            elif player.mp < player.main_equiped.mpcost:
                print("You are out of Mana!")
                time.sleep(2)
                break

    elif step == "2": ## MAGIC, WIP
        choose_magic()
        spell = input("> ")
        if spell == '1' and fire_bolt in current_learned_spells:
            player.main_equiped = fire_bolt
            print("You are now using Fire Bolt!")
            time.sleep(1)
        elif spell == '2' and ice_bolt in current_learned_spells:
            player.main_equiped = ice_bolt
            time.sleep(1)

    elif step == "3": # CHOOSE ITEM
        os.system("cls")
        show_inventory()
        choose_item = input("> ")
        if choose_item == "1":
            if player_items_dic["Small hp potion"] > 0:
                while player.hp < player.maxhp:
                    if player.hp < player.maxhp - 10:
                        player.items["Small hp potion"] -= 1
                        player.hp += 10
                        os.system('cls')
                        print("Used small hp pot")
                        time.sleep(1)
                        break
                    elif player.hp == player.maxhp:
                        os.system('cls')
                        print("You're already max hp")
                        time.sleep(1)
                        break
                    else:
                        os.system('cls')
                        player.items["Small hp potion"] -= 1
                        player.hp = player.maxhp
                        print("You used a small hp potion")
                        time.sleep(1)
                        break
            else:
                os.system('cls')
                print("You don't have enough")
                time.sleep(1)
        elif choose_item == "2":
            if player.items["Big hp potion"] > 0:
                while player.hp < player.maxhp:
                    if player.hp < player.maxhp - 20:
                        player.items["Big hp potion"] -= 1
                        player.hp += 20
                        print("Used big hp potion")
                        time.sleep(1)
                        os.system('cls')
                        break
                    elif player.hp == player.maxhp:
                        print("You're already max hp")
                        time.sleep(1)
                        os.system('cls')
                        break
                    else:
                        player.items["Big hp potion"] -= 1
                        player.hp = player.maxhp
                        print("Used a big hp potion")
                        time.sleep(1)
                        os.system('cls')
                        break
            else:
                os.system('cls')
                print("You don't have enough")
                time.sleep(1)
        else:
            os.system('cls')
            print("Invalid input")
            time.sleep(1)    

###################################################
#Map and  random mob generator per map - need to change this to make more then 1 spawn and let user choose..
def random_mob_farmland():
    global enemy
    enemy = random.choice([goat, snake, horse, bull, hog, dog])
    low_gold = enemy.gold - 5
    high_gold = enemy.gold + 5
    enemy.gold = random.randrange(low_gold, high_gold)
    round(enemy.gold)
    if enemy.gold <= 0:
        enemy.gold = 0
    else:
        pass
    return enemy

def random_mob_forest():
    global enemy
    enemy = random.choice([bear, ghost, witch, unicorn, wild_stag])
    low_gold = enemy.gold - 5
    high_gold = enemy.gold + 5
    enemy.gold = random.randrange(low_gold, high_gold)
    round(enemy.gold)
    if enemy.gold <= 0:
        enemy.gold = 0
    else:
        pass
    return enemy
#initiation making you choose class & name also class stats are in here.
def initiate():
    your_name = input("Hello! Please enter your name > ")
    print("Hello " + your_name.title() + " Please choose a class")
    print("Warrior, Mage")   
    your_class = input(" >").lower()
    global player
    if your_class == 'warrior':
        player = Person(your_name, 20, 12, 10, 1, [], player_items_dic, "Warrior", 1, 0, 10, 100)
    elif your_class == 'mage':
        player = Person(your_name, 15, 15, 13, 3, current_learned_spells, player_items_dic, "Mage", 1, 0, 10, 100)
        player.main_equiped = magic_hands        
    else:
        print("Unknown class, Please choose again")
        time.sleep(2)
        initiate()

    stats_maker()
    print("Welcome " + player.name.title() + " We've heard a lot about you from the guild of " + player.pclass + "s")
    print("We need your help clearing out the farmlands which have been attacked by creatures")
    print("They're not very dangerous but we can't handle them without combat experience")
    print("Thank you and good luck!")
    time.sleep(1)
    os.system("cls")

# initiates the function to start the game and get the class / name of the player    
initiate()

while running: #main running loop for the game
    os.system("cls")
    choose_menu_action() ## Choose an action, from the player.menu_action class
    action_chosen = input("> ") # user input for action
    if action_chosen == '1': # Choose a location to fight in
        os.system("cls")
        print("Choose a location")
        choose_location()
        location_chosen = input("> ")
        if location_chosen == '1':
            if player.pclass == "Warrior":
                os.system('cls')
                random_mob_farmland() # generates a random mob from farm land mobs
                attack()
            elif player.pclass == "Mage":
                os.system('cls')
                random_mob_farmland() # generates a random mob from farm land mobs
                mage_attack()
        elif location_chosen == '2' and player.plevel >= 3:
            if player.pclass == "Warrior":
                os.system('cls')
                random_mob_forest() # generates a random mob from farm land mobs
                attack()
            elif player.pclass == "Mage":
                os.system('cls')
                random_mob_forest() # generates a random mob from farm land mobs
                mage_attack()
    elif action_chosen == '2': # Inventory
        show_inventory()
        choose_item = input("> ")
        if choose_item == "1":
            if player_items_dic["Small hp potion"] > 0:
                while player.hp < player.maxhp:
                    if player.hp < player.maxhp - 10:
                        player.items["Small hp potion"] -= 1
                        player.hp += 10
                        os.system('cls')
                        print("Used small hp pot")
                        time.sleep(1)
                        break
                    elif player.hp == player.maxhp:
                        os.system('cls')
                        print("You're already max hp")
                        time.sleep(1)
                        break
                    else:
                        os.system('cls')
                        player.items["Small hp potion"] -= 1
                        player.hp = player.maxhp
                        print("You used a small hp potion")
                        time.sleep(1)
                        break
            else:
                os.system('cls')
                print("You don't have enough")
                time.sleep(1)
        elif choose_item == "2":
            if player.items["Big hp potion"] > 0:
                while player.hp < player.maxhp:
                    if player.hp < player.maxhp - 20:
                        player.items["Big hp potion"] -= 1
                        player.hp += 20
                        print("Used big hp potion")
                        time.sleep(1)
                        os.system('cls')
                        break
                    elif player.hp == player.maxhp:
                        print("You're already max hp")
                        time.sleep(1)
                        os.system('cls')
                        break
                    else:
                        player.items["Big hp potion"] -= 1
                        player.hp = player.maxhp
                        print("Used a big hp potion")
                        time.sleep(1)
                        os.system('cls')
                        break
            else:
                os.system('cls')
                print("You don't have enough")
                time.sleep(1)
        else:
            os.system('cls')
            print("Invalid input")
            time.sleep(1)
    elif action_chosen == "3": # Medic tent
        os.system("cls")
        print("Hi I'm Janna the Medic, Would you like to heal your wounds?")
        print("Cost: 25 Gold Coins")
        heal = input("1.Yes\n2.No\n> ")
        if heal == "1":
            print("You healed to max hp, Good luck!")
            player.hp = player.maxhp
            player.gold -= 25
            time.sleep(1)
        else:
            print("Bye!")
            time.sleep(1)
            os.system('cls')
            continue        
    elif action_chosen == "4": # Weapon Shops!
        os.system('cls')
        print("Choose a Weapon shop\n1.Warrior Weapons\n2.Mage Weapons")
        what_shop = input("> ")
        if what_shop == "1": # Warrior shop
            os.system('cls')
            warrior_weapon_shop()
            purchase = input("\n> ")
            if purchase == '1' and player.gold >= bronze_sword.price and player.pclass == "Warrior" and player.plevel >= bronze_sword.minlevel:
                player.gold -= bronze_sword.price
                player.main_equiped = bronze_sword
                print("You bought and equiped an Bronze Sword!")
                time.sleep(2)
            elif purchase == '2' and player.gold >= iron_sword.price and player.pclass == "Warrior" and player.plevel >= iron_sword.minlevel:
                player.gold -= iron_sword.price
                player.main_equiped = iron_sword
                print("You bought and equiped an Iron Sword!")
                time.sleep(2)
            elif purchase == '3' and player.gold >= steel_sword.price and player.pclass == 'Warrior' and player.plevel >= steel_sword.minlevel:
                player.gold -= steel_sword.price
                player.main_equiped = steel_sword
                print("Yout bought and equiped a Steel Sword!")
                time.sleep(2)
            else:
                print("You do not meet the requirements to purchase this weapon")
                time.sleep(3)
        elif what_shop == "2": # Mage shop
            os.system('cls')
            spell_shop()
            purchase = input("> ")
            if purchase == "1" and player.gold >= fire_bolt.price and player.pclass == "Mage":
                player.gold -= fire_bolt.price
                player.main_equiped = fire_bolt
                current_learned_spells.append(fire_bolt)
                print("You have learned Fire Bolt!")
                time.sleep(2)
            elif purchase == "2" and player.gold >= ice_bolt.price and player.pclass == "Mage":
                player.gold -= ice_bolt.price
                player.main_equiped = ice_bolt
                current_learned_spells.append(ice_bolt)
                print("You have learned Ice Bolt!")
                time.sleep(2)
            else:
                print("You do not meet the requirements to purchase this weapon")
                time.sleep(3)