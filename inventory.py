from item_pool import *
from clearConsole import clearConsole

your_items = []
temporary_items = []


def inventory(player, your_items):
    item_one = ""
    item_two = ""
    item_three = ""
    selected_item = None
    item_used = True
    inv = ""
    while inv != "q":
        if len(list(your_items)) < 3:
            your_items.append("      ")
        elif len(list(your_items)) > 3:
            try:
                your_items.remove("      ")
                print(
                    f"""
                                            -INVENTORY-
                        |   {item_three}   | ->{item_one}<- |   {item_two}   |

                        Money: {player.wallet}
                """
                )
            except:
                pass
        try:
            item_one = your_items[0]
        except:
            item_one = "      "
        try:
            item_two = your_items[1]
        except:
            item_two = "      "
        try:
            item_three = your_items[2]
        except:
            item_three = "      "
        if item_used == True:
            clearConsole()
            print(
                f"""
                                            -INVENTORY-
                        |   {item_three}   | ->{item_one}<- |   {item_two}   |

                        Money: {player.wallet}
            """
            )
        item_used = False
        inv = input(
            "            Scroll A/D | Confirm [C] | Go back [Q] -> ").casefold()
        clearConsole()
        if inv == "a":
            your_items.insert(0, your_items.pop())

            try:
                item_one = your_items[0]
            except:
                item_one = "      "
            try:
                item_two = your_items[1]
            except:
                item_two = "      "
            try:
                item_three = your_items[2]
            except:
                item_three = "      "
            print(
                f"""
                                            -INVENTORY-
                        |   {item_three}   | ->{item_one}<- |   {item_two}   |

                        Money: {player.wallet}
            """
            )
        elif inv == "d":
            your_items.append(your_items.pop(0))
            try:
                item_one = your_items[0]
            except:
                item_one = "      "
            try:
                item_two = your_items[1]
            except:
                item_two = "      "
            try:
                item_three = your_items[2]
            except:
                item_three = "      "
            print(
                f"""
                                            -INVENTORY-
                        |   {item_three}   | ->{item_one}<- |   {item_two}   |

                        Money: {player.wallet}
            """
            )
        elif inv == "c":
            clearConsole()
            selected_item = item_one
            if selected_item == "      ":  # EMPTY
                clearConsole()
                print(
                    f"""
                                            -INVENTORY-
                        |   {item_three}   | ->{item_one}<- |   {item_two}   |

                        Money: {player.wallet}
            """
                )
            elif selected_item == burgir:  # BURGIR
                print(
                    f"""
                -------------------
                {burgir.name}
                {burgir.desc}
                -------------------
                """
                )
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
                print(
                    f"""
                -------------------
                {belt.name}
                {belt.desc}
                -------------------
                """
                )
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
                print(
                    f"""
                -------------------
                {roids.name}
                {roids.desc}
                -------------------
                """
                )
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(roids)
                    player.dmg = player.dmg + 5
                    player.hp = player.hp - 1
                    temporary_items.append(roids)
                    item_used = True
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == dripcap:  # DRIP CAP
                print(
                    f"""
                -------------------
                {dripcap.name}
                {dripcap.desc}
                -------------------
                """
                )
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
                print(
                    f"""
                -------------------
                {stick.name}
                {stick.desc}
                -------------------
                """
                )
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(stick)
                    player.dmg = player.dmg + 1
                    item_used = True
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == jordans:  # JORDANS
                print(
                    f"""
                -------------------
                {jordans.name}
                {jordans.desc}
                -------------------
                """
                )
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(jordans)
                    player.maxhp = player.maxhp + 1
                    player.hp = player.hp + 1
                    item_used = True
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == tie:  # Tie
                print(
                    f"""
                -------------------
                {tie.name}
                {tie.desc}
                -------------------
                """
                )
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(tie)
                    player.maxhp = player.maxhp + 1
                    player.hp = player.hp + 1
                    item_used = True
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == red_potion:  # Red potion
                print(
                    f"""
                -------------------
                {red_potion.name}
                {red_potion.desc}
                -------------------
                """
                )
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(red_potion)
                    player.hp = player.hp + 2
                    item_used = True
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == knife:  # knife
                print(
                    f"""
                -------------------
                {knife.name}
                {knife.desc}
                -------------------
                """
                )
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(knife)
                    player.dmg = player.dmg + 3
                    item_used = True
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == theos_jacket:  # theos_jacket
                print(
                    f"""
                -------------------
                {theos_jacket.name}
                {theos_jacket.desc}
                -------------------
                """
                )
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(theos_jacket)
                    player.maxhp = player.maxhp + 3
                    player.hp = player.hp + 3
                    item_used = True
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == poop:  # poop
                print(
                    f"""
                -------------------
                {poop.name}
                {poop.desc}
                -------------------
                """
                )
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(poop)
                    player.hp = player.hp - 1
                    item_used = True
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == gucci_flip_fops:  # gucci_flip_flops
                print(
                    f"""
                -------------------
                {gucci_flip_fops.name}
                {gucci_flip_fops.desc}
                -------------------
                """
                )
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(gucci_flip_fops)
                    player.maxhp = player.maxhp + 1
                    player.hp = player.hp + 1
                    item_used = True
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == frog_tongue:  # poisonous tongue
                print(
                    f"""
                -------------------
                {frog_tongue.name}
                {frog_tongue.desc}
                -------------------
                """
                )
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(frog_tongue)
                    player.frog_item = True
                    item_used = True
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == frog_crown:  # frog-king's crown
                print(
                    f"""
                -------------------
                {frog_crown.name}
                {frog_crown.desc}
                -------------------
                """
                )
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(frog_crown)
                    item_used = True
                    player.maxhp = player.maxhp + 5
                    player.hp = player.hp + 5
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == cd_disc:  # cd-rom disc
                print(
                    f"""
                -------------------
                {cd_disc.name}
                {cd_disc.desc}
                -------------------
                """
                )
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(cd_disc)
                    item_used = True
                    player.dmg = player.dmg + 1
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == pointy_spike:  # pointy spike
                print(
                    f"""
                -------------------
                {pointy_spike.name}
                {pointy_spike.desc}
                -------------------
                """
                )
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(pointy_spike)
                    item_used = True
                    player.dmg = player.dmg + 1
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == stalactite:  # stalactite
                print(
                    f"""
                -------------------
                {stalactite.name}
                {stalactite.desc}
                -------------------
                """
                )
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(stalactite)
                    item_used = True
                    player.dmg = player.dmg + 1
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == power_cable:  # Power cable
                print(
                    f"""
                -------------------
                {power_cable.name}
                {power_cable.desc}
                -------------------
                """
                )
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(power_cable)
                    item_used = True
                    player.dmg = player.dmg + 1
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == graduation_cap:  # Graduation cap
                print(
                    f"""
                -------------------
                {graduation_cap.name}
                {graduation_cap.desc}
                -------------------
                """
                )
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(graduation_cap)
                    item_used = True
                    player.hp = player.hp + 2
                else:
                    clearConsole()
                    item_used = True

        elif inv == "q":
            clearConsole()
        if player.hp > player.maxhp:
            player.hp = player.maxhp
        if inv != "a":
            item_used = True
        elif inv != "d":
            item_used = True
        elif inv != "c":
            item_used = True

    return player
