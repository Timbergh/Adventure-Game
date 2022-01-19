import random as rand

from item_pool import *
from inventory import *
from random_encounter import *
from clearConsole import clearConsole


def shop(player):
    shop_item = []
    shop_choice = ""
    for i in range(3):
        rand_shop_item = rand.choice(item_pool)
        item_pool.remove(rand_shop_item)
        shop_item.append(rand_shop_item)
    item_pool.append(shop_item[0])
    item_pool.append(shop_item[1])
    item_pool.append(shop_item[2])
    try:
        item_one = shop_item[0]
    except:
        item_one = "      "
    try:
        item_two = shop_item[1]
    except:
        item_two = "      "
    try:
        item_three = shop_item[2]
    except:
        item_three = "      "
    while shop_choice != "q":
        if player.wallet < 10:
            clearConsole()
            print("You don't have enough money to buy anything")
        else:
            clearConsole()
        print(
            f"""

                        |  {item_one} (1) |  {item_two} (2) |  {item_three} (3) |

                        Money: {player.wallet}
                        All items cost 10 gold coins
                        """
        )
        shop_choice = input(
            "Which item whould you like to buy 1, 2, 3 or [q] to leave -> ").casefold()
        if shop_choice == "1":
            if player.wallet >= 10:
                your_items.append(shop_item[0])
                shop_item.remove(shop_item[0])
                player.wallet = player.wallet - 10
                try:
                    item_one = shop_item[0]
                except:
                    item_one = "      "
                try:
                    item_two = shop_item[1]
                except:
                    item_two = "      "
                try:
                    item_three = shop_item[2]
                except:
                    item_three = "      "
                clearConsole()
        elif shop_choice == "2":
            if player.wallet >= 10:
                your_items.append(shop_item[1])
                shop_item.remove(shop_item[1])
                player.wallet = player.wallet - 10
                try:
                    item_one = shop_item[0]
                except:
                    item_one = "      "
                try:
                    item_two = shop_item[1]
                except:
                    item_two = "      "
                try:
                    item_three = shop_item[2]
                except:
                    item_three = "      "
                clearConsole()
        elif shop_choice == "3":
            if player.wallet >= 10:
                your_items.append(shop_item[2])
                shop_item.remove(shop_item[2])
                player.wallet = player.wallet - 10
                try:
                    item_one = shop_item[0]
                except:
                    item_one = "      "
                try:
                    item_two = shop_item[1]
                except:
                    item_two = "      "
                try:
                    item_three = shop_item[2]
                except:
                    item_three = "      "
                clearConsole()
        elif shop_choice == "q":
            clearConsole()
            return player.wallet
