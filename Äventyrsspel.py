import random as rand
import os
import time


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
    def __init__(self):
        pass


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


burgir = Items("Heals you for 3 Hp", "Burgir")
roids = Items("Makes you a glasscannon", "Roids")
stick = Items("Makes you deal one more damage this round", "Stick")
belt = Items(
    "Permanently increase your damage by one and hp by two", "Belt")
dripcap = Items("You look extra good and gain one max hp", "Drip Cap")


def random_encounter(rand_index, your_items):
    global hp
    item_pool = [burgir, roids, stick, belt, dripcap]
    if rand_index == 1:
        re = "found an item"
        your_items.append(rand.choice(item_pool))
    if rand_index == 2:
        re = "encounter a monster"
    if rand_index == 3:
        re = "found out you are standing on a trap!"
        player.hp = player.hp - 1
    return re


def doors():
    choose_door = ""
    rand_door = [1, 2, 3]
    left_open = False
    middle_open = False
    right_open = False
    fountain = False
    holyopen = False
    if rounds % 5 == 0:
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
            if left_open == False:
                rand_index = rand.choice(rand_door)
                rand_door.remove(rand_index)
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

                You opend the left door and {random_encounter(rand_index, your_items)}
                """)
            left_open = True

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
            if middle_open == False:
                rand_index = rand.choice(rand_door)
                rand_door.remove(rand_index)
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

                You opend the middle door and {random_encounter(rand_index, your_items)}
                """)
            middle_open = True
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
            if right_open == False:
                rand_index = rand.choice(rand_door)
                rand_door.remove(rand_index)
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

                You opend the right door and {random_encounter(rand_index, your_items)}
                """)
            right_open = True
        elif choose_door == "q":  # BACK TO MENU
            clearConsole()
            print("Returning to menu...")
        if player.hp == 0:
            clearConsole()
            break
        if left_open == True and middle_open == True and right_open == True:
            quit = input(
                "You have no doors left\nReturn to menu [Q]").casefold()
            if quit == "q":
                clearConsole()
                print("Returning to menu...")
                break


your_items = []


def inventory(your_items):
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
    selected_item = None
    print(f"""
            ----------------INVENTORY-----------------
            |   {item_one}    |   {item_two}    |   {item_three}    |   {item_four}    |   {item_five}    |
            ------------------------------------------
    """)
    inv = ""
    while inv != "q":
        inv = input(
            "            Scroll through items 1-5 | Select Item [s] | Back to menu [q] -> ")
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
        elif inv == "s":
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
                    inventory(your_items)
                else:
                    inventory(your_items)

            if selected_item == belt:  # BELT
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
                    inventory(your_items)
                else:
                    inventory(your_items)

            if selected_item == roids:  # ROIDS
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
                    inventory(your_items)
                else:
                    inventory(your_items)

            if selected_item == dripcap:  # DRIP CAP
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
                    inventory(your_items)
                    player.maxhp = player.maxhp + 1
                    player.hp = player.hp + 1
                else:
                    inventory(your_items)

        elif inv == "q":
            clearConsole()
            print("Returning to menu...")
            break


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
    time.sleep(0)
    print(f"HP = {player.maxhp}")
    time.sleep(0)
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
