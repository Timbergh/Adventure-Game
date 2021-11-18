import random as rand
import os
import time
import math


class Player:
    def __init__(self, name, maxhp, hp, dmg):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.dmg = dmg

    def __str__(self):
        return """
        -------------
        Name: {}
        Hp: {}
        Damage: {}
        -------------""".format(self.name, self.hp, self.dmg)


class Items:
    def __init__(self, desc, name):
        self.name = name
        self.desc = desc

    def __str__(self):
        return "{}".format(self.name)


class Enemy(Player):

    def __str__(self):
        return """
        -------------
        Name: {}
        Hp: {}
        Damage: {}
        -------------""".format(self.name, self.hp, self.dmg)


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


burgir = Items("Burgir! (+3 Hp)", "Burgir")
roids = Items("Makes you a glasscannon (+5 dmg -Hp)", "Roids")
stick = Items("You hit harder (+1 dmg)", "Stick")
belt = Items(
    "Permanently increase your damage by one and hp by two", "Belt")
dripcap = Items("You look extra good and gain one max hp", "Drip Cap")

e_hp = 1
e_dmg = 1


def random_encounter(rand_index, your_items):
    global hp, e_hp, e_dmg, random_item
    item_pool = [burgir, roids, stick, belt, dripcap]
    ogre = Enemy("Ogre", e_hp, e_hp, e_dmg)
    enemy_pool = [ogre]
    if rand_index == 1:
        random_item = rand.choice(item_pool)
        your_items.append(random_item)
    if rand_index == 2:
        e_hp = e_hp + rounds * 0.5
        e_hp = round(e_hp)
        ogre.maxhp = e_hp
        e_dmg = e_dmg + rounds * 0.5
        e_dmg = math.floor(e_dmg)
        random_enemy = rand.choice(enemy_pool)
        attack = False
        open_inventory = False
        opend_inv = False
        turn = 1
        clearConsole()
        print(
            f"""
                            | Your Hp: {player.hp}/{player.maxhp}       | Ogre Hp: {e_hp}/{ogre.maxhp}
                            | Your Damage: {player.dmg}     | Ogre Damage: {e_dmg}

                            | Attack [A] | | Inventory [I] | | Confirm [C] |

                    """)
        while e_hp != 0 or player.hp != 0:
            if opend_inv == True:
                print(
                    f"""
                        | Your Hp: {player.hp}/{player.maxhp}       | Ogre Hp: {e_hp}/{ogre.maxhp}
                        | Your Damage: {player.dmg}     | Ogre Damage: {e_dmg}

                        | Attack [A] | | ->Inventory<- [I] | | Confirm [C] |

                    """)
                opend_inv = False
            if turn % 2 != 0:
                battle = input("What do you want to do? -> ").casefold()
                if battle == "a":
                    open_inventory = False
                    attack = True
                    clearConsole()
                    print(
                        f"""
                        | Your Hp: {player.hp}/{player.maxhp}       | Ogre Hp: {e_hp}/{ogre.maxhp}
                        | Your Damage: {player.dmg}     | Ogre Damage: {e_dmg}

                        | ->Attack<- [A] | | Inventory [I] | | Confirm [C] |

                    """)
                elif battle == "i":
                    attack = False
                    open_inventory = True
                    clearConsole()
                    print(
                        f"""
                        | Your Hp: {player.hp}/{player.maxhp}       | Ogre Hp: {e_hp}/{ogre.maxhp}
                        | Your Damage: {player.dmg}     | Ogre Damage: {e_dmg}

                        | Attack [A] | | ->Inventory<- [I] | | Confirm [C] |

                    """)
                if battle == "c":
                    if attack == True:
                        e_hp = e_hp - player.dmg
                        turn = turn + 1
                        clearConsole()
                        print(
                            f"""
                        | Your Hp: {player.hp}/{player.maxhp}       | Ogre Hp: {e_hp}/{ogre.maxhp}
                        | Your Damage: {player.dmg}     | Ogre Damage: {e_dmg}

                        | ->Attack<- [A] | | Inventory [I] | | Confirm [C] |

                        """)
                    elif open_inventory == True:
                        clearConsole()
                        opend_inv = True
                        inventory(your_items)
                        clearConsole()
            elif turn % 2 == 0:
                clearConsole()
                player.hp = player.hp - e_dmg
                turn = turn + 1
                print(
                    f"""
                        | Your Hp: {player.hp}/{player.maxhp}       | Ogre Hp: {e_hp}/{ogre.maxhp}
                        | Your Damage: {player.dmg}     | Ogre Damage: {e_dmg}

                        | Attack [A] | | Inventory [I] | | Confirm [C] |

                        """)
                time.sleep(0.5)
            if e_hp <= 0 or player.hp <= 0:
                clearConsole()
                if e_hp <= 0:
                    print(
                        f"""
                        | Your Hp: {player.hp}/{player.maxhp}       | Ogre Hp: 0/{ogre.maxhp}
                        | Your Damage: {player.dmg}     | Ogre Damage: {e_dmg}

                        | You defeted the Ogre! |

                        """)
                    input("Press enter to continue ")
                    e_hp = 1
                    ogre.maxhp = e_hp
                    e_dmg = 1
                    clearConsole()
                elif player.hp <= 0:
                    print(
                        f"""
                        | Your Hp: 0/{player.maxhp}       | Ogre Hp: {e_hp}/{ogre.maxhp}
                        | Your Damage: {player.dmg}     | Ogre Damage: {e_dmg}

                        | You were defeted by the Ogre! |

                        """)
                    input("Press enter to continue ")
                    clearConsole()
                break

    if rand_index == 3:
        player.hp = player.hp - 0


def doors():
    choose_door = ""
    rand_door = [1, 2, 3]
    left_open = False
    middle_open = False
    right_open = False
    fountain = False
    holyopen = False
    re = False
    if rounds % 5 == 0 and rounds % 10 != 0:
        fountain = True
    else:
        fountain = False
    if fountain == False:
        print(f"""
                                        Round {rounds}
                |You walk into an unkown place and see three doors|
                    _____________   _____________   _____________
                    |           |   |           |   |           |
                    |           |   |           |   |           |
                    |           |   |           |   |           |
                    |         * |   |         * |   |         * |
                    |           |   |           |   |           |
                    |    [L]    |   |    [M]    |   |    [R]    |
                    |___________|   |___________|   |___________|
                    """)
    else:
        print(f"""
                                                Round {rounds}
                        |You walk into an unkown place and see four doors?|
                    _____________   _____________   _____________   _____________
                    |           |   |           |   |           |   |     _     |
                    |           |   |           |   |           |   |   _| |_   |
                    |           |   |           |   |           |   |  |_   _|  |
                    |         * |   |         * |   |         * |   |    | |  * |
                    |           |   |           |   |           |   |    |_|    |
                    |    [L]    |   |    [M]    |   |    [R]    |   |           |
                    |___________|   |___________|   |___________|   |___________|
                    """)
        print(
            "Do you wish to enter the Holy door?")
        holy_door = input(
            "If you enter you will skip this round y/n -> ").casefold()
        if holy_door == "y":
            hdopen1 = open("dooropen/hdopen1.txt", "r")
            hdopen2 = open("dooropen/hdopen2.txt", "r")
            toilet = open("toilet.txt", "r")
            clearConsole()
            print(hdopen1.read())
            time.sleep(0.3)
            clearConsole()
            print(hdopen2.read())
            time.sleep(1)
            clearConsole()
            print(toilet.read())
            input(
                f"\n\nYou took a sip of the holy fountains water and gained {player.maxhp - player.hp} Hp\nPress any button to continue")
            toilets_gift = player.maxhp - player.hp
            player.hp = player.hp + toilets_gift
            holyopen = True
        elif holy_door == "n":
            clearConsole()
            hd1 = open("holydoor/hd1.txt", "r")
            hd2 = open("holydoor/hd2.txt", "r")
            hd3 = open("holydoor/hd3.txt", "r")
            hd4 = open("holydoor/hd4.txt", "r")
            hd5 = open("holydoor/hd5.txt", "r")
            hd6 = open("holydoor/hd6.txt", "r")
            hd7 = open("holydoor/hd7.txt", "r")
            print(hd1.read())
            time.sleep(0.3)
            clearConsole()
            print(hd2.read())
            time.sleep(0.3)
            clearConsole()
            print(hd3.read())
            time.sleep(0.3)
            clearConsole()
            print(hd4.read())
            time.sleep(0.3)
            clearConsole()
            print(hd5.read())
            time.sleep(0.3)
            clearConsole()
            print(hd6.read())
            time.sleep(0.3)
            clearConsole()
            print(hd7.read())

    while choose_door != "q":
        if holyopen == True:
            clearConsole()
            break
        if re == True:
            print(f"""
                                        Round {rounds}
                |You walk into an unkown place and see three doors|
                    _____________   _____________   _____________
                    |           |   |           |   |           |
                    |           |   |           |   |           |
                    |           |   |           |   |           |
                    |         * |   |         * |   |         * |
                    |           |   |           |   |           |
                    |    [L]    |   |    [M]    |   |    [R]    |
                    |___________|   |___________|   |___________|
                    """)
            re = False
        choose_door = input(
            "Which door would you like to enter? [L] [M] [R] or [Q] quit to menu -> ").casefold()
        if choose_door == "l":  # LEFT DOOR
            if left_open == True:
                clearConsole()
                print(f"""
                                    Round {rounds}
                _____________   _____________   _____________
                |  |        |   |           |   |           |
                |  |        |   |           |   |           |
                | .|        |   |           |   |           |
                |  |        |   |         * |   |         * |
                |  |        |   |           |   |           |
                | /         |   |    [M]    |   |    [R]    |
                |/__________|   |___________|   |___________|

                There is nothing left in this door
                """)
            elif left_open == False:
                rand_index = rand.choice(rand_door)
                rand_door.remove(rand_index)
                if rand_index == 1:
                    ri = "found an item!"
                elif rand_index == 2:
                    ri = "encounterd a monster!"
                elif rand_index == 3:
                    ri = "found out you are standing on a trap!"
                time.sleep(0.3)
                clearConsole()
                print(f"""
                                    Round {rounds}
                _____________   _____________   _____________
                |      |    |   |           |   |           |
                |      |    |   |           |   |           |
                |    * |    |   |           |   |           |
                |      |    |   |         * |   |         * |
                |      |    |   |           |   |           |
                |    /      |   |    [M]    |   |    [R]    |
                |__/________|   |___________|   |___________|

                """)
                time.sleep(0.3)
                clearConsole()
                print(f"""
                                    Round {rounds}
                _____________   _____________   _____________
                |  |        |   |           |   |           |
                |  |        |   |           |   |           |
                | .|        |   |           |   |           |
                |  |        |   |         * |   |         * |
                |  |        |   |           |   |           |
                | /         |   |    [M]    |   |    [R]    |
                |/__________|   |___________|   |___________|

                You opend the left door and {ri}
                """)
                left_open = True
                if rand_index == 2:
                    input("Press enter to continue")
                    re = True
                    random_encounter(rand_index, your_items)
                else:
                    random_encounter(rand_index, your_items)

        elif choose_door == "m":  # MIDDLE DOOR
            if middle_open == True:
                clearConsole()
                print(f"""
                                    Round {rounds}
                _____________   _____________   _____________
                |           |   |  |        |   |           |
                |           |   |  |        |   |           |
                |           |   | .|        |   |           |
                |         * |   |  |        |   |         * |
                |           |   |  |        |   |           |
                |    [L]    |   | /         |   |    [R]    |
                |___________|   |/__________|   |___________|

                There is nothing left in this door
                """)
            elif middle_open == False:
                rand_index = rand.choice(rand_door)
                rand_door.remove(rand_index)
                if rand_index == 1:
                    ri = "found an item!"
                elif rand_index == 2:
                    ri = "encounterd a monster!"
                elif rand_index == 3:
                    ri = "found out you are standing on a trap!"
                time.sleep(0.3)
                clearConsole()
                print(f"""
                                    Round {rounds}
                _____________   _____________   _____________
                |           |   |      |    |   |           |
                |           |   |      |    |   |           |
                |           |   |   *  |    |   |           |
                |         * |   |      |    |   |         * |
                |           |   |      |    |   |           |
                |    [L]    |   |    /      |   |    [R]    |
                |___________|   |__/________|   |___________|

                """)
                time.sleep(0.3)
                clearConsole()
                print(f"""
                                    Round {rounds}
                _____________   _____________   _____________
                |           |   |  |        |   |           |
                |           |   |  |        |   |           |
                |           |   | .|        |   |           |
                |         * |   |  |        |   |         * |
                |           |   |  |        |   |           |
                |    [L]    |   | /         |   |    [R]    |
                |___________|   |/__________|   |___________|

                You opend the middle door and {ri}
                """)
                middle_open = True
                if rand_index == 2:
                    input("Press enter to continue")
                    re = True
                    random_encounter(rand_index, your_items)
                else:
                    random_encounter(rand_index, your_items)

        elif choose_door == "r":  # RIGHT DOOR
            if right_open == True:
                clearConsole()
                print(f"""
                                    Round {rounds}
                _____________   _____________   _____________
                |           |   |           |   |  |        |
                |           |   |           |   |  |        |
                |           |   |           |   | .|        |
                |         * |   |         * |   |  |        |
                |           |   |           |   |  |        |
                |    [L]    |   |    [M]    |   | /         |
                |___________|   |___________|   |/__________|

                There is nothing left in this door
                """)
            elif right_open == False:
                rand_index = rand.choice(rand_door)
                rand_door.remove(rand_index)
                if rand_index == 1:
                    ri = "found an item!"
                elif rand_index == 2:
                    ri = "encounterd a monster!"
                elif rand_index == 3:
                    ri = "found out you are standing on a trap!"
                time.sleep(0.3)
                clearConsole()
                print(f"""
                                    Round {rounds}
                _____________   _____________   _____________
                |           |   |           |   |      |    |
                |           |   |           |   |      |    |
                |           |   |           |   |      |    |
                |         * |   |         * |   |    * |    |
                |           |   |           |   |      |    |
                |    [L]    |   |    [M]    |   |    /      |
                |___________|   |___________|   |__/________|

                """)
                time.sleep(0.3)
                clearConsole()
                print(f"""
                                    Round {rounds}
                _____________   _____________   _____________
                |           |   |           |   |  |        |
                |           |   |           |   |  |        |
                |           |   |           |   | .|        |
                |         * |   |         * |   |  |        |
                |           |   |           |   |  |        |
                |    [L]    |   |    [M]    |   | /         |
                |___________|   |___________|   |/__________|

                You opend the right door and {ri}
                """)
                right_open = True
                if rand_index == 2:
                    input("Press enter to continue")
                    re = True
                    random_encounter(rand_index, your_items)
                else:
                    random_encounter(rand_index, your_items)

        elif choose_door == "q":  # BACK TO MENU
            clearConsole()
            print("Returning to menu...")
        if player.hp == 0:
            clearConsole()
            break
        if left_open == True and middle_open == True and right_open == True:
            input(
                "You have no doors left\nPress enter to continue").casefold()
            clearConsole()
            print("Returning to menu...")
            break


your_items = []


def inventory(your_items):
    item_one = ""
    item_two = ""
    item_three = ""
    item_four = ""
    item_five = ""
    selected_item = None
    item_used = True
    inv = ""
    while inv != "q":
        try:
            item_one = your_items[0]
        except:
            item_one = ""
        try:
            item_two = your_items[1]
        except:
            item_two = ""
        try:
            item_three = your_items[2]
        except:
            item_three = ""
        try:
            item_four = your_items[3]
        except:
            item_four = ""
        try:
            item_five = your_items[4]
        except:
            item_five = ""
        if item_used == True:
            print(f"""
            ----------------INVENTORY-----------------
            |   {item_one}    |   {item_two}    |   {item_three}    |   {item_four}    |   {item_five}    |
            ------------------------------------------
            """)
        item_used = False
        inv = input(
            "            Select items 1-5 | Confirm [C] | Go back [Q] -> ")
        clearConsole()
        if inv == "1":
            clearConsole()
            print(f"""
            ----------------INVENTORY----------------
            |  ->{item_one}<-  |   {item_two}    |   {item_three}    |   {item_four}    |   {item_five}    |
            -----------------------------------------
            """)
            selected_item = item_one
        elif inv == "2":
            clearConsole()
            print(f"""
            ----------------INVENTORY----------------
            |   {item_one}    |  ->{item_two}<-  |   {item_three}    |   {item_four}    |   {item_five}    |
            -----------------------------------------
            """)
            selected_item = item_two
        elif inv == "3":
            clearConsole()
            print(f"""
            ----------------INVENTORY-----------------
            |   {item_one}    |   {item_two}   |   ->{item_three}<-   |   {item_four}    |   {item_five}    |
            ------------------------------------------
            """)
            selected_item = item_three
        elif inv == "4":
            clearConsole()
            print(f"""
            ----------------INVENTORY-----------------
            |   {item_one}    |   {item_two}   |   {item_three}    |   ->{item_four}<-   |   {item_five}    |
            ------------------------------------------
            """)
            selected_item = item_four
        elif inv == "5":
            clearConsole()
            print(f"""
            ----------------INVENTORY-----------------
            |   {item_one}    |   {item_two}   |   {item_three}    |   {item_four}    |   ->{item_five}<-   |
            ------------------------------------------
            """)
            selected_item = item_five
        elif inv == "c":
            clearConsole()
            if selected_item == burgir:  # BURGIR
                print(f"""
                -------------------
                {burgir.name}
                {burgir.desc}
                -------------------
                """)
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(burgir)
                    player.hp = player.hp + 3
                    item_used = True
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == belt:  # BELT
                print(f"""
                -------------------
                {belt.name}
                {belt.desc}
                -------------------
                """)
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(belt)
                    player.maxhp = player.maxhp + 2
                    player.hp = player.hp + 2
                    player.dmg = player.dmg + 1
                    item_used = True
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == roids:  # ROIDS
                print(f"""
                -------------------
                {roids.name}
                {roids.desc}
                -------------------
                """)
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(roids)
                    item_used = True
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == dripcap:  # DRIP CAP
                print(f"""
                -------------------
                {dripcap.name}
                {dripcap.desc}
                -------------------
                """)
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(dripcap)
                    player.maxhp = player.maxhp + 1
                    player.hp = player.hp + 1
                    item_used = True
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == stick:  # STICK
                print(f"""
                -------------------
                {stick.name}
                {stick.desc}
                -------------------
                """)
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(stick)
                    player.dmg = player.dmg + 1
                    item_used = True
                else:
                    clearConsole()
                    item_used = True
                    inventory(your_items)
        elif inv == "q":
            clearConsole()


def stats(player):
    if player.hp > player.maxhp:
        player.hp = player.maxhp
    if player.hp == player.maxhp:
        print(
            f"""
        {player}
        """)
    elif player.hp < player.maxhp:
        print(
            f"""
        -------------
        Name: {name}
        Hp: {player.hp}/{player.maxhp}
        Damage: {player.dmg}
        -------------
        """)
    input("     Press any button to go back to menu")
    clearConsole()


def create_character():
    global maxhp, hp, dmg, name
    name = input("Enter your name -> ")
    random_stats = rand.randint(2, 4)
    maxhp = random_stats
    hp = maxhp
    dmg = 5 - random_stats
    return Player(name, maxhp, hp, dmg)


def main():
    global player, rounds
    rounds = 0
    player = create_character()
    clearConsole()
    character = open("char1.txt", "r")
    print(f"Hello {player.name}\nThis is you")
    print(character.read())
    input("Press enter to continue")
    clearConsole()
    print("I will now calculate your stats...\n")
    time.sleep(0)  # ÄNDRA PÅ TIDEN
    print(f"HP = {player.maxhp}")
    time.sleep(0)  # ÄNDRA PÅ TIDEN
    print(f"Damage = {player.dmg}\n")
    input("Press enter to continue")
    clearConsole()
    while True:
        if player.hp == 0:
            clearConsole()
            print("You died...")
            game_over = open("gameover.txt", "r")
            print(game_over.read())
            time.sleep(5)
            break
        menu = input("""
        --------------MENU--------------
        | [i] Inventory                |
        | [s] Stats                    |
        | [c] Continue                 |
        | [q] Quit                     |
        |                              |
        |                              |
        --------------------------------
        """).casefold()
        if menu == "i":
            clearConsole()
            inventory(your_items)
        elif menu == "c":
            clearConsole()
            rounds = rounds + 1
            doors()
        elif menu == "s":
            clearConsole()
            stats(player)
        elif menu == "q":
            clearConsole()
            print("Quiting game...")
            break


main()
