import random as rand
import math
import time

from item_pool import *
from clearConsole import clearConsole
from Enemy import Enemy
from health_bar import health_bar
from inventory import *
from trap_pool import *
from trap_pool import trap_pool


def random_encounter(rounds, player, e_hp, e_dmg, rand_index, your_items):
    item_pool = [burgir, roids, stick, belt, dripcap,
                 tie, butter_stone, gucci_flip_fops]
    ogre = Enemy("Ogre", e_hp, e_hp, e_dmg)
    if rand_index == 1:
        random_item = rand.choice(item_pool)
        your_items.append(random_item)
    if rand_index == 2:
        e_hp = 1 + rounds * 0.5
        e_hp = round(e_hp)
        ogre.hp = e_hp
        ogre.maxhp = e_hp
        e_dmg = 1 + rounds * 0.5
        e_dmg = math.floor(e_dmg)
        attack = False
        open_inventory = False
        opend_inv = False
        turn = 1
        clearConsole()
        print(
            f"""
                            | Your Hp: {health_bar(player)}  | Ogre Hp: {health_bar(ogre)}
                            | Your Damage: {player.dmg}     | Ogre Damage: {e_dmg}

                            | Attack [A] | | Inventory [I] | | Confirm [C] |

                    """)
        while e_hp != 0 or player.hp != 0:
            if opend_inv == True:
                print(
                    f"""
                        | Your Hp: {health_bar(player)}  | Ogre Hp: {health_bar(ogre)}
                        | Your Damage: {player.dmg}     | Ogre Damage: {e_dmg}

                        | Attack [A] | | ->Inventory<- [I] | | Confirm [C] |

                    """)
                opend_inv = False
            if turn % 2 != 0:
                battle = input("What do you want to do? -> ").casefold()
                if battle == "a":
                    open_inventory = False
                    attack = True
                    clearConsole()
                    print(
                        f"""
                        | Your Hp: {health_bar(player)}  | Ogre Hp: {health_bar(ogre)}
                        | Your Damage: {player.dmg}     | Ogre Damage: {e_dmg}

                        | ->Attack<- [A] | | Inventory [I] | | Confirm [C] |

                    """)
                elif battle == "i":
                    attack = False
                    open_inventory = True
                    clearConsole()
                    print(
                        f"""
                        | Your Hp: {health_bar(player)}  | Ogre Hp: {health_bar(ogre)}
                        | Your Damage: {player.dmg}     | Ogre Damage: {e_dmg}

                        | Attack [A] | | ->Inventory<- [I] | | Confirm [C] |

                    """)
                if battle == "c":
                    if attack == True:
                        ogre.hp = ogre.hp - player.dmg
                        turn = turn + 1
                        for i in temporary_items:
                            if i == roids:
                                player.dmg = player.dmg - 5
                                temporary_items.remove(roids)
                        clearConsole()
                        print(
                            f"""
                        | Your Hp: {health_bar(player)}  | Ogre Hp: {health_bar(ogre)}
                        | Your Damage: {player.dmg}     | Ogre Damage: {e_dmg}

                        | ->Attack<- [A] | | Inventory [I] | | Confirm [C] |

                        """)
                        if player.frog_item == True:
                            ogre.hp = round(ogre.hp - ogre.maxhp*0.1)
                            time.sleep(0.1)
                            clearConsole()
                            print(
                                f"""
                            | Your Hp: {health_bar(player)}  | Ogre Hp: {health_bar(ogre)}
                            | Your Damage: {player.dmg}     | Ogre Damage: {e_dmg}

                            | ->Attack<- [A] | | Inventory [I] | | Confirm [C] |

                        """)
                    elif open_inventory == True:
                        clearConsole()
                        opend_inv = True
                        inventory(player, your_items)
                        clearConsole()
            elif turn % 2 == 0:
                clearConsole()
                player.hp = player.hp - e_dmg
                turn = turn + 1
                print(
                    f"""
                        | Your Hp: {health_bar(player)}  | Ogre Hp: {health_bar(ogre)}
                        | Your Damage: {player.dmg}     | Ogre Damage: {e_dmg}

                        | Attack [A] | | Inventory [I] | | Confirm [C] |

                        """)
                time.sleep(0.5)
            if ogre.hp <= 0 or player.hp <= 0:
                clearConsole()
                if ogre.hp <= 0:
                    ogre.hp = 0
                    print(
                        f"""
                        | Your Hp: {health_bar(player)}  | Ogre Hp: {health_bar(ogre)}
                        | Your Damage: {player.dmg}     | Ogre Damage: {e_dmg}

                        | You defeated the Ogre! |

                        """)
                    player.wallet = player.wallet + rand.randint(1, 3)
                    print(f"You have {player.wallet} coins")
                    input("Press enter to continue ")
                    clearConsole()
                elif player.hp <= 0:
                    player.hp = 0
                    print(
                        f"""
                        | Your Hp: {health_bar(player)}  | Ogre Hp: {health_bar(ogre)}
                        | Your Damage: {player.dmg}     | Ogre Damage: {e_dmg}

                        | You were defeated by the Ogre! |

                        """)
                    input("Press enter to continue ")
                    clearConsole()

                break

    if rand_index == 3:
        random_trap = rand.choice(trap_pool)
        if random_trap == boulder:
            print(boulder.desc)
            t_choice = int(
                input("1. Punch the boulder, 2. Run away, 3. Do nothing: "))
            if t_choice == 1:
                print(boulder.end1)
                player.hp = player.hp - 1
            elif t_choice == 2:
                print(boulder.end2)
                player.hp = player.hp - 1
            elif t_choice == 3:
                print(boulder.end3)
        if random_trap == cheese:
            print(cheese.desc)
            t_choice = int(
                input("1. Eat the cheese, 2. Continue on without doing anything, 3. Give the cheese to a passing mouse: "))
            if t_choice == 1:
                print(cheese.end1)
                player.hp = player.hp + 1
            elif t_choice == 2:
                print(cheese.end2)
                player.hp = player.hp - 1
            elif t_choice == 3:
                print(cheese.end3)
                your_items.append(dripcap)
        if random_trap == santa:
            print(santa.desc)
            t_choice = int(
                input("1. Ask for a present, 2. Ask to sit in his lap, 3. Compliment his wife: "))
            if t_choice == 1:
                print(santa.end1)
                player.hp = player.hp - 1
            elif t_choice == 2:
                print(santa.end2)
                try:
                    santa_steal = rand.choice(your_items)
                    if santa_steal != "      ":
                        your_items.remove(santa_steal)
                    elif santa_steal == "      ":
                        print("Fortunaly you had noone")
                except:
                    print("Fortunaly you had noone")
            elif t_choice == 3:
                print(santa.end3)
                player.hp = player.hp - 1
                your_items.append(belt)
        if random_trap == jordan:
            print(jordan.desc)
            t_choice = int(
                input("1. Let him win, 2. Play him in a fair 1v1, 3. Run away: "))
            if t_choice == 1:
                print(jordan.end1)
                your_items.append(jordans)
            elif t_choice == 2:
                print(jordan.end2)
                player.hp = player.hp - 2
            elif t_choice == 3:
                print(jordan.end3)
        if random_trap == joebiden:
            print(joebiden.desc)
            t_choice = int(
                input("1.You feel a bit chilly, would you like to sneeze, 2. Wave and leave, 3. Show him your middle finger: "))
            if t_choice == 1:
                print(joebiden.end1)
                your_items.append(tie)
            elif t_choice == 2:
                print(joebiden.end2)
            elif t_choice == 3:
                print(joebiden.end3)
                player.hp = player.hp - 1
        if random_trap == alchemist:
            print(alchemist.desc)
            t_choice = int(
                input("1.Take the green potion, 2. Take the red potion, 3. Take the blue potion: "))
            if t_choice == 1:
                print(alchemist.end1)
                player.hp = player.hp - 2

            elif t_choice == 2:
                print(alchemist.end2)
                your_items.append(red_potion)
            elif t_choice == 3:
                print(alchemist.end3)
                player.maxhp = player.maxhp + 1
        if random_trap == lake:
            print(lake.desc)
            t_choice = int(
                input("1.Fish from the cliff, 2.Dive in to catch one, 3.Sit and rest: "))
            if t_choice == 1:
                print(lake.end1)
                your_items.append(fish)
            elif t_choice == 2:
                print(lake.end2)
                player.hp = player.hp - 2
            elif t_choice == 3:
                print(lake.end3)
        if random_trap == monke:
            print(monke.desc)
            t_choice = int(
                input("1.Walk away, 2. Trade with the Monke, 3. Run away: "))
            if t_choice == 1:
                print(monke.end1)
            elif t_choice == 2:
                print(monke.end2)
                your_items.append(knife)
            elif t_choice == 3:
                print(monke.end3)
                your_items.append(poop)
        if random_trap == theo:
            print(theo.desc)
            t_choice = int(
                input("1.Tell him you're cold, 2. Confess your feelings for him, 3. Run away: "))
            if t_choice == 1:
                print(theo.end1)
                your_items.append(theos_jacket)
            elif t_choice == 2:
                print(theo.end2)
                player.maxhp = player.maxhp - 1
            elif t_choice == 3:
                print(theo.end3)
        if random_trap == computer:
            print(computer.desc)
            t_choice = int(
                input("1.Smash it to bits, 2. Plug it in, 3. Ignore it: "))
            if t_choice == 1:
                print(computer.end1)
                your_items.append(cd_disc)
            elif t_choice == 2:
                print(computer.end2)
                player.hp = player.hp - 2
            elif t_choice == 3:
                print(computer.end3)
        if random_trap == spikes:
            print(spikes.desc)
            t_choice = int(
                input("1.Jump over the spikes, 2. Break off a spike, 3. Carefully walk through the spikes: "))
            if t_choice == 1:
                print(spikes.end1)
                player.hp = player.hp - 1
            elif t_choice == 2:
                print(spikes.end2)
                your_items.append = pointy_spike
            elif t_choice == 3:
                print(spikes.end3)
        if random_trap == old_man:
            print(old_man.desc)
            t_choice = int(
                input("1.Take the first bag, 2. Take the second bag, 3. Take the third bag: "))
            if t_choice == 1:
                print(old_man.end1)
                your_items.append = red_potion
            elif t_choice == 2:
                print(old_man.end2)
                your_items.append = stick
            elif t_choice == 3:
                print(old_man.end3)
                player.hp = player.hp - 1
        if random_trap == caves:
            print(caves.desc)
            t_choice = int(
                input("1.The left cave, 2. The middle cave, 3. The right cave: "))
            if t_choice == 1:
                print(caves.end1)
                your_items.append(rand.choice(item_pool))
            elif t_choice == 2:
                print(caves.end2)

            elif t_choice == 3:
                print(old_man.end3)
                player.hp = player.hp - 1
                your_items.append(stalactite)
    return player, ogre
