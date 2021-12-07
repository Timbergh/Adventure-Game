import random as rand

from item_pool import *
from inventory import shop_items


def shop(wallet):
    shop_item1 = rand.choice(shop_items)
    shop_items.remove(shop_item1)
    shop_item2 = rand.choice(shop_items)
    shop_items.remove(shop_item2)
    shop_item3 = rand.choice(shop_items)
    shop_items.remove(shop_item3)
    shop_items.append(shop_item1, shop_item2, shop_item3)
    print(f"""
                    (1)              (2)              (3)
            |  {shop_item1}  |  {shop_item2}  |  {shop_item3}  |
            
            Money: {wallet}
            """)
    shop_choice = input(f"Which item whould you like to buy 1, 2 or 3 -> ")
