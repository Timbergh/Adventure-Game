import time

from Boss import Boss
from health_bar import health_bar
from inventory import inventory, your_items
from item_pool import *
from clearConsole import clearConsole


def boss_encounter(rounds, player):
    if rounds == 10:
        name = "The Frog-King"
        boss_hp = 30
        boss_dmg = 1
        frogking = Boss(name, boss_hp, boss_hp, boss_dmg)
        frog_txt = open("art/frogking.txt", "r")
        attack = False
        open_inventory = False
        opend_inv = False
        turn = 1
        clearConsole()
        print(
            f"""                            {frog_txt.read()}
                            | Your Hp: {health_bar(player)}  | Frog-King Hp: {health_bar(frogking)}
                            | Your Damage: {player.dmg}     | Frog-king Damage: {frogking.dmg}

                            | Attack [A] | | Inventory [I] | | Confirm [C] |

                    """)
        while frogking.hp != 0 or player.hp != 0:
            frog_txt = open("art/frogking.txt", "r")
            if opend_inv == True:
                print(
                    f"""                            {frog_txt.read()}
                            | Your Hp: {health_bar(player)}  | Frog-King Hp: {health_bar(frogking)}
                            | Your Damage: {player.dmg}     | Frog-king Damage: {frogking.dmg}

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
                        f"""                            {frog_txt.read()}
                            | Your Hp: {health_bar(player)}  | Frog-King Hp: {health_bar(frogking)}
                            | Your Damage: {player.dmg}     | Frog-king Damage: {frogking.dmg}

                        | ->Attack<- [A] | | Inventory [I] | | Confirm [C] |

                    """)
                elif battle == "i":
                    attack = False
                    open_inventory = True
                    clearConsole()
                    print(
                        f"""                            {frog_txt.read()}
                            | Your Hp: {health_bar(player)}  | Frog-King Hp: {health_bar(frogking)}
                            | Your Damage: {player.dmg}     | Frog-king Damage: {frogking.dmg}

                        | Attack [A] | | ->Inventory<- [I] | | Confirm [C] |

                    """)
                if battle == "c":
                    if attack == True:
                        frogking.hp = frogking.hp - player.dmg
                        turn = turn + 1
                        clearConsole()
                        print(
                            f"""                            {frog_txt.read()}
                            | Your Hp: {health_bar(player)}  | Frog-King Hp: {health_bar(frogking)}
                            | Your Damage: {player.dmg}     | Frog-king Damage: {frogking.dmg}

                        | ->Attack<- [A] | | Inventory [I] | | Confirm [C] |

                        """)
                        if player.frog_item == True:
                            frogking.hp = round(
                                frogking.hp - frogking.maxhp*0.1)
                            time.sleep(0.1)
                            clearConsole()
                            print(
                                f"""                            {frog_txt.read()}
                            | Your Hp: {health_bar(player)}  | Ogre Hp: {health_bar(frogking)}
                            | Your Damage: {player.dmg}     | Ogre Damage: {frogking.dmg}

                            | ->Attack<- [A] | | Inventory [I] | | Confirm [C] |

                        """)
                    elif open_inventory == True:
                        clearConsole()
                        opend_inv = True
                        inventory(player, your_items)
                        clearConsole()
            elif turn % 2 == 0:
                clearConsole()
                player.hp = player.hp - frogking.dmg
                turn = turn + 1
                print(
                    f"""                            {frog_txt.read()}
                            | Your Hp: {health_bar(player)}  | Frog-King Hp: {health_bar(frogking)}
                            | Your Damage: {player.dmg}     | Frog-king Damage: {frogking.dmg}

                        | Attack [A] | | Inventory [I] | | Confirm [C] |

                        """)
                time.sleep(0.5)
            if frogking.hp <= 0 or player.hp <= 0:
                frog_txt = open("art/frogking.txt", "r")
                clearConsole()
                if frogking.hp <= 0:
                    frogking.hp = 0
                    print(
                        f"""                            {frog_txt.read()}
                            | Your Hp: {health_bar(player)}  | Frog-King Hp: {health_bar(frogking)}
                            | Your Damage: {player.dmg}     | Frog-king Damage: {frogking.dmg}

                        | You defeted the Frog-king! (Obtained a poisonous tongue) |

                        """)
                    input("Press enter to continue ")
                    your_items.append(frog_tongue)
                    clearConsole()
                elif player.hp <= 0:
                    player.hp = 0
                    print(
                        f"""                            {frog_txt.read()}
                            | Your Hp: {health_bar(player)}  | Frog-King Hp: {health_bar(frogking)}
                            | Your Damage: {player.dmg}     | Frog-king Damage: {frogking.dmg}

                        | You were defeted by the Frog-king! |

                        """)
                    input("Press enter to continue ")
                    clearConsole()
                break
    elif rounds == 20:
        name = "Dominus GT"
        boss_hp = 45
        boss_dmg = 2
        dominus = Boss(name, boss_hp, boss_hp, boss_dmg)
