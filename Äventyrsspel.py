import random as rand
import os


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
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def doors():
    choose_door = ""
    rand_door = [1, 2, 3]
    left_open = False
    middle_open = False
    right_open = False
    while choose_door != "q":
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
        choose_door = input(
            "Which door would you like to enter? [L] [M] [R] or [Q] quit to menu -> ").casefold()
        if choose_door == "l":
            clearConsole()
            if left_open == True:
                print("There is nothing left here")
            if left_open == False:
                rand_index = rand.choice(rand_door)
                rand_door.remove(rand_index)
            left_open = True
        elif choose_door == "m":
            clearConsole()
            if middle_open == True:
                print("There is nothing left here")
            if middle_open == False:
                rand_index = rand.choice(rand_door)
                rand_door.remove(rand_index)
            middle_open = True
        elif choose_door == "r":
            clearConsole()
            if right_open == True:
                print("There is nothing left here")
            if right_open == False:
                rand_index = rand.choice(rand_door)
                rand_door.remove(rand_index)
            right_open = True
        elif choose_door == "q":
            clearConsole()
            print("Returning to menu...")
        if left_open == True and middle_open == True and right_open == True:
            clearConsole()
            print("You have no doors left\nReturning to menu...")
            break


def inventory():
    burgir = Items("Heals you for __HP", "Burgir")
    your_items = []
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
            ----------------INVENTORY----------------
            |   {item_one}    |   {item_two}    |   {item_three}    |   {item_four}    |   {item_five}    |
            -----------------------------------------
    """)
    while True:
        inv = int(input("            Select your item 1-5 -> "))
        clearConsole()
        if inv == 1:
            clearConsole()
            print(f"""
            ----------------INVENTORY---------------
            |  ->{item_one}<-  |   {item_two}    |   {item_three}    |   {item_four}    |   {item_five}    |
            ----------------------------------------
            """)
        elif inv == 2:
            clearConsole()
            print(f"""
            ----------------INVENTORY---------------
            |   {item_one}    |  ->{item_two}<-  |   {item_three}    |   {item_four}    |   {item_five}    |
            ----------------------------------------
            """)
        elif inv == 3:
            clearConsole()
            print(f"""
            ----------------INVENTORY----------------
            |   {item_one}    |   {item_two}   |   ->{item_three}<-   |   {item_four}    |   {item_five}    |
            -----------------------------------------
            """)
        elif inv == 4:
            clearConsole()
            print(f"""
            ----------------INVENTORY----------------
            |   {item_one}    |   {item_two}   |   {item_three}    |   ->{item_four}<-   |   {item_five}    |
            -----------------------------------------
            """)
        elif inv == 5:
            clearConsole()
            print(f"""
            ----------------INVENTORY----------------
            |   {item_one}    |   {item_two}   |   {item_three}    |   {item_four}    |   ->{item_five}<-   |
            -----------------------------------------
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
