import random as rand

from item_pool import *
from inventory import *
from clearConsole import clearConsole


def shop(wallet):
    shop_choice = ""
    shop_item1 = rand.choice(shop_items)
    shop_items.remove(shop_item1)
    shop_item2 = rand.choice(shop_items)
    shop_items.remove(shop_item2)
    shop_item3 = rand.choice(shop_items)
    shop_items.remove(shop_item3)
    shop_items.append(shop_item1)
    shop_items.append(shop_item2)
    shop_items.append(shop_item3)
    while shop_choice != "q":
        clearConsole()
        print(
            f"""
                                                            
                        |  {shop_item1} (1) |  {shop_item2} (2) |  {shop_item3} (3) |

                        Money: {wallet}
                        All items cost 15 gold coins
                        """
        )
        shop_choice = input(
            "Which item whould you like to buy 1, 2, 3 or [q] to leave -> ")
        if shop_choice == 1:
            your_items.appand(shop_item1)
            wallet = wallet - 15
        elif shop_choice == 2:
            your_items.apand(shop_item2)
            wallet = wallet - 15
        elif shop_choice == 3:
            your_items.apand(shop_item3)
            wallet = wallet - 15
        elif shop_choice == "q":
            clearConsole()
