import random as rand
import os
import time


class Player:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.hp, self.dmg)


class Items:
    def __init__(self, desc, name):
        self.name = name
        self.desc = desc

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.desc)


class Enemy:
    def __init__(self):
        pass


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def random_encounter(rand_index):
    if rand_index == 1:
        re = "found an item"
    if rand_index == 2:
        re = "encounter a monster"
    if rand_index == 3:
        re = "found out you are standing on a trap!"
    return re


def doors():
    choose_door = ""
    rand_door = [1, 2, 3]
    left_open = False
    middle_open = False
    right_open = False
    print("""
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
    while choose_door != "q":
        choose_door = input(
            "Which door would you like to enter? [L] [M] [R] or [Q] quit to menu -> ").casefold()
        if choose_door == "l":  # LEFT DOOR
            if left_open == True:
                clearConsole()
                print("""
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
                _____________   _____________   _____________
                |      |    |   |           |   |           |
                |      |    |   |           |   |           |
                |    * |    |   |           |   |           |
                |      |    |   |         * |   |         * |
                |      |    |   |           |   |           |
                |    /      |   |    [M]    |   |    [R]    |
                |__/________|   |___________|   |___________|

                You opend the left door and {random_encounter(rand_index)}
                """)
                time.sleep(0.3)
                clearConsole()
                print(f"""
                _____________   _____________   _____________
                |  |        |   |           |   |           |
                |  |        |   |           |   |           |
                | .|        |   |           |   |           |
                |  |        |   |         * |   |         * |
                |  |        |   |           |   |           |
                | /         |   |    [M]    |   |    [R]    |
                |/__________|   |___________|   |___________|

                You opend the left door and {random_encounter(rand_index)}
                """)
            left_open = True

        elif choose_door == "m":  # MIDDLE DOOR
            if middle_open == True:
                clearConsole()
                print("""
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
                _____________   _____________   _____________
                |           |   |      |    |   |           |
                |           |   |      |    |   |           |
                |           |   |   *  |    |   |           |
                |         * |   |      |    |   |         * |
                |           |   |      |    |   |           |
                |    [L]    |   |    /      |   |    [R]    |
                |___________|   |__/________|   |___________|

                You opend the middle door and {random_encounter(rand_index)}
                """)
                time.sleep(0.3)
                clearConsole()
                print(f"""
                _____________   _____________   _____________
                |           |   |  |        |   |           |
                |           |   |  |        |   |           |
                |           |   | .|        |   |           |
                |         * |   |  |        |   |         * |
                |           |   |  |        |   |           |
                |    [L]    |   | /         |   |    [R]    |
                |___________|   |/__________|   |___________|

                You opend the middle door and {random_encounter(rand_index)}
                """)
            middle_open = True
        elif choose_door == "r":  # RIGHT DOOR
            if right_open == True:
                clearConsole()
                print("""
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
                _____________   _____________   _____________
                |           |   |           |   |      |    |
                |           |   |           |   |      |    |
                |           |   |           |   |      |    |
                |         * |   |         * |   |    * |    |
                |           |   |           |   |      |    |
                |    [L]    |   |    [M]    |   |    /      |
                |___________|   |___________|   |__/________|

                You opend the right door and {random_encounter(rand_index)}
                """)
                time.sleep(0.3)
                clearConsole()
                print(f"""
                _____________   _____________   _____________
                |           |   |           |   |  |        |
                |           |   |           |   |  |        |
                |           |   |           |   | .|        |
                |         * |   |         * |   |  |        |
                |           |   |           |   |  |        |
                |    [L]    |   |    [M]    |   | /         |
                |___________|   |___________|   |/__________|

                You opend the right door and {random_encounter(rand_index)}
                """)
            right_open = True
        elif choose_door == "q":  # BACK TO MENU
            clearConsole()
            print("Returning to menu...")
        if left_open == True and middle_open == True and right_open == True:
            quit = input(
                "You have no doors left\nReturn to menu [Q]").casefold()
            if quit == "q":
                print("Returning to menu...")
                break


def inventory():
    burgir = Items("Heals you for __HP", "Burgir")
    your_items = [burgir.name]
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
    print(f"""
            ----------------INVENTORY-----------------
            |   {item_one}    |   {item_two}    |   {item_three}    |   {item_four}    |   {item_five}    |
            ------------------------------------------
    """)
    while True:
        inv = int(input("            Select your item 1-5 -> "))
        clearConsole()
        if inv == 1:
            clearConsole()
            print(f"""
            ----------------INVENTORY----------------
            |  ->{item_one}<-  |   {item_two}    |   {item_three}    |   {item_four}    |   {item_five}    |
            -----------------------------------------
            """)
        elif inv == 2:
            clearConsole()
            print(f"""
            ----------------INVENTORY----------------
            |   {item_one}    |  ->{item_two}<-  |   {item_three}    |   {item_four}    |   {item_five}    |
            -----------------------------------------
            """)
        elif inv == 3:
            clearConsole()
            print(f"""
            ----------------INVENTORY-----------------
            |   {item_one}    |   {item_two}   |   ->{item_three}<-   |   {item_four}    |   {item_five}    |
            ------------------------------------------
            """)
        elif inv == 4:
            clearConsole()
            print(f"""
            ----------------INVENTORY-----------------
            |   {item_one}    |   {item_two}   |   {item_three}    |   ->{item_four}<-   |   {item_five}    |
            ------------------------------------------
            """)
        elif inv == 5:
            clearConsole()
            print(f"""
            ----------------INVENTORY-----------------
            |   {item_one}    |   {item_two}   |   {item_three}    |   {item_four}    |   ->{item_five}<-   |
            ------------------------------------------
            """)


while True:
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
        inventory()
    elif menu == "c":
        clearConsole()
        doors()
    elif menu == "q":
        clearConsole()
        print("Quiting game...")
        break
