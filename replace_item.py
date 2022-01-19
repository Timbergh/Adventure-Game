from item_pool import *
from clearConsole import clearConsole
from inventory import *


def replace_item(player):
    inv = ""
    item_recieved = your_items[3]
    your_items.remove(item_recieved)
    while inv != "q":
        item_one = your_items[0]
        item_two = your_items[1]
        item_three = your_items[2]
        clearConsole()
        print(
            f"""
                                        -INVENTORY-
                    |   {item_three}   | ->{item_one}<- |   {item_two}   | 

                    Item recieved: {item_recieved}

                    Money: {player.wallet}
        """
        )
        print("          Select Item to replace")
        inv = input(
            "            Scroll A/D | Confirm [C] | Keep Items [Q] -> ").casefold()
        clearConsole()
        if inv == "a":
            your_items.insert(0, your_items.pop())
            item_one = your_items[0]
            item_two = your_items[1]
            item_three = your_items[2]
            print(
                f"""
                                            -INVENTORY-
                        |   {item_three}   | ->{item_one}<- |   {item_two}   |

                        Item recieved: {item_recieved}

                        Money: {player.wallet}
            """
            )
        elif inv == "d":
            your_items.append(your_items.pop(0))
            item_one = your_items[0]
            item_two = your_items[1]
            item_three = your_items[2]
            print(
                f"""
                                            -INVENTORY-
                        |   {item_three}   | ->{item_one}<- |   {item_two}   |

                        Item recieved: {item_recieved}

                        Money: {player.wallet}
            """
            )
        elif inv == "c":
            clearConsole()
            selected_item = item_one
            if selected_item == item_one:
                your_items.pop(0)
                your_items.append(item_recieved)
                your_items.insert(0, your_items.pop())
                break
        elif inv == "q":
            your_items.append(item_recieved)
            your_items.pop(3)
