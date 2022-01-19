import random as rand
import time

from boss_encounter import boss_encounter
from random_encounter import random_encounter
from inventory import your_items
from clearConsole import clearConsole
from shop import *


def doors(player, rounds):
    e_hp = 1
    e_dmg = 1

    choose_door = ""
    rand_door = [1, 2, 3]
    left_open = False
    middle_open = False
    right_open = False
    fountain = False
    holyopen = False
    boss_room = False
    boss_open = False
    shopdoor = False
    re = False
    wallet = player.wallet
    if rounds % 5 == 0 and rounds % 10 != 0:
        fountain = True
    else:
        fountain = False
    if rounds % 10 == 0:
        boss_room = True
    else:
        boss_room = False
    if fountain == False and boss_room == False:
        print(
            f"""
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
                    """
        )
    elif fountain == True and boss_room == False:
        holy_door = ""
        while holy_door != "y":
            print(
                f"""
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
                        """
            )
            print("Do you wish to enter the Holy door?")
            holy_door = input(
                "If you don't enter you may enter the shop (Entering will skip this turn and deny you of the shop) y/n -> ").casefold()
            if holy_door == "n":
                break
            elif holy_door != "n":
                clearConsole()
        if holy_door == "y":
            hdopen1 = open("dooropen/hdopen1.txt", "r")
            hdopen2 = open("dooropen/hdopen2.txt", "r")
            toilet = open("art/toilet.txt", "r")
            clearConsole()
            print(hdopen1.read())
            time.sleep(0.3)
            clearConsole()
            print(hdopen2.read())
            time.sleep(1)
            clearConsole()
            print(toilet.read())
            input(
                f"\n\nYou took a sip of the holy fountains water and gained {player.maxhp - player.hp} Hp\nPress any button to continue"
            ).casefold()
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
            hd8 = open("holydoor/hd8.txt", "r")
            hd9 = open("holydoor/hd9.txt", "r")
            hd10 = open("holydoor/hd10.txt", "r")
            hd11 = open("holydoor/hd11.txt", "r")
            hd12 = open("holydoor/hd12.txt", "r")
            hd13 = open("holydoor/hd13.txt", "r")
            hd14 = open("holydoor/hd14.txt", "r")
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
            time.sleep(0.1)
            clearConsole()
            print(hd8.read())
            time.sleep(0.1)
            clearConsole()
            print(hd9.read())
            time.sleep(0.1)
            clearConsole()
            print(hd10.read())
            time.sleep(0.1)
            clearConsole()
            print(hd11.read())
            time.sleep(0.1)
            clearConsole()
            print(hd12.read())
            time.sleep(0.1)
            clearConsole()
            print(hd13.read())
            time.sleep(0.1)
            clearConsole()
            print(hd14.read())
            shopdoor = True

    elif fountain == False and boss_room == True:
        print(
            f"""
                                            Round {rounds}
                |You only see one door this time and it pulls you in against your will!|
                                        ___________________
                                        | (x)         (x) |
                                        |   \  _---_  /   |
                                        |    \/     \/    |
                                        |     |0   0|     |
                                        |      \ + /      |
                                        |     / ||| \     |
                                        |    /  \_/  \    |
                                        | (x)         (x) |
                                        |                 |
                                        |      Boss       |
                                        |                 |
                                        |_________________|
        """
        )
        input("Press enter to continue ").casefold()
        boss_encounter(
            rounds,
            player,
        )
        boss_open = True
    while choose_door != "q":
        if holyopen == True:
            clearConsole()
            break
        if boss_open == True:
            clearConsole()
            break
        if shopdoor == True:
            choose_door = input(
                "Which door would you like to enter? [L] [M] [R] [S] or [Q] quit to menu -> ").casefold()
            if choose_door == "s":
                shopopen1 = open("dooropen/shopopen1.txt", "r")
                shopopen2 = open("dooropen/shopopen2.txt", "r")
                clearConsole()
                print(shopopen1.read())
                time.sleep(0.3)
                clearConsole()
                print(shopopen2.read())
                shopdoor = False
                re = True
                shop(player)
        if re == True:
            print(
                f"""
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
                    """
            )
            re = False
        if shop != True:
            choose_door = input(
                "Which door would you like to enter? [L] [M] [R] or [Q] quit to menu -> "
            ).casefold()
        if choose_door == "l":  # LEFT DOOR
            if left_open == True:
                clearConsole()
                print(
                    f"""
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
                """
                )
            elif left_open == False:
                rand_index = rand.choice(rand_door)
                rand_door.remove(rand_index)
                if rand_index == 1:
                    ri = "found an item!"
                elif rand_index == 2:
                    ri = "encounterd a monster!"
                elif rand_index == 3:
                    ri = "found out you are inside a trap!"
                time.sleep(0.3)
                clearConsole()
                print(
                    f"""
                                    Round {rounds}
                _____________   _____________   _____________
                |      |    |   |           |   |           |
                |      |    |   |           |   |           |
                |    * |    |   |           |   |           |
                |      |    |   |         * |   |         * |
                |      |    |   |           |   |           |
                |    /      |   |    [M]    |   |    [R]    |
                |__/________|   |___________|   |___________|

                """
                )
                time.sleep(0.3)
                clearConsole()
                print(
                    f"""
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
                """
                )
                left_open = True
                if rand_index == 2:
                    input("Press enter to continue").casefold()
                    re = True
                    random_encounter(
                        rounds, player, e_hp, e_dmg, rand_index, your_items
                    )
                else:
                    random_encounter(
                        rounds, player, e_hp, e_dmg, rand_index, your_items
                    )
        elif choose_door == "m":  # MIDDLE DOOR
            if middle_open == True:
                clearConsole()
                print(
                    f"""
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
                """
                )
            elif middle_open == False:
                rand_index = rand.choice(rand_door)
                rand_door.remove(rand_index)
                if rand_index == 1:
                    ri = "found an item!"
                elif rand_index == 2:
                    ri = "encounterd a monster!"
                elif rand_index == 3:
                    ri = "found out you are inside a trap!"
                time.sleep(0.3)
                clearConsole()
                print(
                    f"""
                                    Round {rounds}
                _____________   _____________   _____________
                |           |   |      |    |   |           |
                |           |   |      |    |   |           |
                |           |   |   *  |    |   |           |
                |         * |   |      |    |   |         * |
                |           |   |      |    |   |           |
                |    [L]    |   |    /      |   |    [R]    |
                |___________|   |__/________|   |___________|

                """
                )
                time.sleep(0.3)
                clearConsole()
                print(
                    f"""
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
                """
                )
                middle_open = True
                if rand_index == 2:
                    input("Press enter to continue").casefold()
                    re = True
                    random_encounter(
                        rounds, player, e_hp, e_dmg, rand_index, your_items
                    )
                else:
                    random_encounter(
                        rounds, player, e_hp, e_dmg, rand_index, your_items
                    )

        elif choose_door == "r":  # RIGHT DOOR
            if right_open == True:
                clearConsole()
                print(
                    f"""
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
                """
                )
            elif right_open == False:
                rand_index = rand.choice(rand_door)
                rand_door.remove(rand_index)
                if rand_index == 1:
                    ri = "found an item!"
                elif rand_index == 2:
                    ri = "encounterd a monster!"
                elif rand_index == 3:
                    ri = "found out you are inside a trap!"
                time.sleep(0.3)
                clearConsole()
                print(
                    f"""
                                    Round {rounds}
                _____________   _____________   _____________
                |           |   |           |   |      |    |
                |           |   |           |   |      |    |
                |           |   |           |   |      |    |
                |         * |   |         * |   |    * |    |
                |           |   |           |   |      |    |
                |    [L]    |   |    [M]    |   |    /      |
                |___________|   |___________|   |__/________|

                """
                )
                time.sleep(0.3)
                clearConsole()
                print(
                    f"""
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
                """
                )
                right_open = True
                if rand_index == 2:
                    input("Press enter to continue").casefold()
                    re = True
                    random_encounter(
                        rounds, player, e_hp, e_dmg, rand_index, your_items
                    )
                else:
                    random_encounter(
                        rounds, player, e_hp, e_dmg, rand_index, your_items
                    )

        elif choose_door == "q":  # BACK TO MENU
            clearConsole()
            print("Returning to menu...")
        if player.hp == 0:
            clearConsole()
            break
        if left_open == True and middle_open == True and right_open == True:
            input("You have no doors left\n\nPress enter to continue").casefold()
            clearConsole()
            print("Returning to menu...")
            break
        if choose_door == "l" and choose_door != "m" and choose_door != "r":
            pass
        elif choose_door != "l" and choose_door == "m" and choose_door != "r":
            pass
        elif choose_door != "l" and choose_door != "m" and choose_door == "r":
            pass
        else:
            clearConsole()
            re = True
