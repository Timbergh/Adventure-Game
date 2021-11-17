import random as rand
import os
import time


class Player:
    def __init__(self, name, maxhp, dmg):
        self.name = name
        self.maxhp = maxhp
        self.dmg = dmg

    def __str__(self):
        return """
        -------------
        Name: {}
        Hp: {}
        Damage: {}
        -------------""".format(self.name, self.maxhp, self.dmg)


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
stick = Items("Makes you deal one more damage", "Stick")
belt = Items(
    "Permanently increase your damage by two and hp by two", "Belt")
dripcap = Items("You look extra drip and gain one max hp", "Drip Cap")


def random_encounter(rand_index, your_items):
    item_pool = [burgir, roids, stick, belt, dripcap]
    if rand_index == 1:
        re = "found an item"
        your_items.append(rand.choice(item_pool))
    if rand_index == 2:
        re = "encounter a monster"
    if rand_index == 3:
        re = "found out you are standing on a trap!"
        player.hp - 1
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

                You opend the left door and {random_encounter(rand_index, your_items)}
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

                You opend the middle door and {random_encounter(rand_index, your_items)}
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

                You opend the right door and {random_encounter(rand_index, your_items)}
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
    while True:
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
            if selected_item == burgir:
                print(f"""
                -------------------
                {burgir.name}
                {burgir.desc}
                -------------------
                """)
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    your_items.remove(burgir)
                    inventory(your_items)

        elif inv == "q":
            clearConsole()
            print("Returning to menu...")
            break


def stats(player):
    print(
        f"""
    {player}
    """)
    input("     Press any button to go back to menu")
    clearConsole()


def create_character():
    name = input("Enter your name -> ")
    random_stats = rand.randint(1, 2)
    maxhp = random_stats
    dmg = 3 - random_stats
    return Player(name, maxhp, dmg)


def main():
    global player
    player = create_character()
    clearConsole()
    character = open("char1.txt", "r")
    print(f"Hello {player.name}\nThis is you")
    print(character.read())
    input("Press enter to continue")
    clearConsole()
    print("I will now calculate your stats...\n")
    time.sleep(1.5)
    print(f"HP = {player.maxhp}")
    time.sleep(1.5)
    print(f"Damage = {player.dmg}\n")
    input("Press enter to continue")
    clearConsole()
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
            inventory(your_items)
        elif menu == "c":
            clearConsole()
            doors()
        elif menu == "s":
            clearConsole()
            stats(player)
        elif menu == "q":
            clearConsole()
            print("Quiting game...")
            break


main()

"""
                        @@@   @@                                                 
                  @@@   @@@@@@@@@@@@                                            
               @@@&  @@@@@@@@@@@@@@@@@                                          
             @@@@   @@@@@@@@@@@@@@@@@@@                                         
            @@@   @@@@@@@@@@@@@@@@@@@@@@                                        
           @@@/  @@@@@@@@@@@@@@@@@@@@@@@                                        
          @@@@   @@@@@@@@@@@@@@@@@@@@@@@                                        
          @@@   @@@@@@@@@@@@@@@@@@@@@@@@                                        
          @@@   @@@@@@@@@@@@@@@@@@@@@@@@                                        
          @@@   @@@@@@@@@@@@@@@@@@@@@@@@                                        
          @@@   @@@@@@@@@@@@@@@@@@@@@@@@                                        
          @@@   @@@@@@@@@@@@@@@@@@@@@@@                                         
          @@@&  @@@@@@@@@@@@@@@@@@@@@@@                                         
           @@@   @@@@@@@@@@@@@@@@@@@@@                                          
            @@@   @@@@@@@@@@@@@@@&                                              
             @@@  .@@@@@@@@        @@@@@@@@@@@@@@@@@@                           
                @   @        @@@@@@@@@@@@   (@@@@@@@@@@@@@@@                    
                       @@@@@@@@@                       @@@@@@@@                 
                 %@    @@@@@@@@#                         @@@@@@@@               
                  @@@@    @@@@@@@@@                     @@@@@@@@@               
                   @@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
                    @@@@@@@ @@@       %@@@@@@@@@@@@@@@@@@@@                      
                     *@@@@@@@@@@@@@@@                     @@@@                  
                       .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    
                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      
                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                         
                          @@@@@@@@@@  @@@@@@@@@@                                
                          @@@@@@@@@@@@@@@@@@@@@@@@@@@                           
                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                         
                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                         
                              @@@@@@@@@@@@@@@@@@@@@@@@@                         

  
"""
