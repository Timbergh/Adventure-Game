import time

from Boss import Boss
from health_bar import health_bar
from inventory import inventory, your_items
from item_pool import *
from clearConsole import clearConsole


def boss_encounter(rounds, player):
    attack = False
    open_inventory = False
    opend_inv = False
    if rounds == 10:
        name = "The Frog-King"
        boss_hp = 30
        boss_dmg = 1
        frogking = Boss(name, boss_hp, boss_hp, boss_dmg)
        frog_txt = open("art/frogking.txt", "r")
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
                    input("Press enter to continue ").casefold()
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
                    input("Press enter to continue ").casefold()
                    clearConsole()
                break
    elif rounds == 20:
        name = "Dominus GT"
        boss_hp = 45
        boss_dmg = 2
        dominus = Boss(name, boss_hp, boss_hp, boss_dmg)
        dominus_txt = open("art/dominus.txt", "r")
        turn = 1
        clearConsole()
        print(
            f"""                            {dominus_txt.read()}
                            | Your Hp: {health_bar(player)}  | Dominus Hp: {health_bar(dominus)}
                            | Your Damage: {player.dmg}     | Dominus Damage: {dominus.dmg}

                            | Attack [A] | | Inventory [I] | | Confirm [C] |

                    """)
        while dominus.hp != 0 or player.hp != 0:
            dominus_txt = open("art/dominus.txt", "r")
            if opend_inv == True:
                print(
                    f"""                            {dominus_txt.read()}
                            | Your Hp: {health_bar(player)}  | Dominus Hp: {health_bar(dominus)}
                            | Your Damage: {player.dmg}     | Dominus Damage: {dominus.dmg}

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
                        f"""                            {dominus_txt.read()}
                            | Your Hp: {health_bar(player)}  | Dominus Hp: {health_bar(dominus)}
                            | Your Damage: {player.dmg}     | Dominus Damage: {dominus.dmg}

                        | ->Attack<- [A] | | Inventory [I] | | Confirm [C] |

                    """)
                elif battle == "i":
                    attack = False
                    open_inventory = True
                    clearConsole()
                    print(
                        f"""                            {dominus_txt.read()}
                            | Your Hp: {health_bar(player)}  | Dominus Hp: {health_bar(dominus)}
                            | Your Damage: {player.dmg}     | Dominus Damage: {dominus.dmg}

                        | Attack [A] | | ->Inventory<- [I] | | Confirm [C] |

                    """)
                if battle == "c":
                    if attack == True:
                        dominus.hp = dominus.hp - player.dmg
                        turn = turn + 1
                        clearConsole()
                        print(
                            f"""                            {dominus_txt.read()}
                            | Your Hp: {health_bar(player)}  | Dominus Hp: {health_bar(dominus)}
                            | Your Damage: {player.dmg}     | Dominus Damage: {dominus.dmg}

                        | ->Attack<- [A] | | Inventory [I] | | Confirm [C] |

                        """)
                        if player.frog_item == True:
                            dominus.hp = round(
                                dominus.hp - dominus.maxhp*0.1)
                            time.sleep(0.1)
                            clearConsole()
                            print(
                                f"""                            {dominus_txt.read()}
                            | Your Hp: {health_bar(player)}  | Dominus Hp: {health_bar(dominus)}
                            | Your Damage: {player.dmg}     | Dominus Damage: {dominus.dmg}

                            | ->Attack<- [A] | | Inventory [I] | | Confirm [C] |

                        """)
                    elif open_inventory == True:
                        clearConsole()
                        opend_inv = True
                        inventory(player, your_items)
                        clearConsole()
            elif turn % 2 == 0:
                clearConsole()
                player.hp = player.hp - dominus.dmg
                turn = turn + 1
                print(
                    f"""                            {dominus_txt.read()}
                            | Your Hp: {health_bar(player)}  | Dominus Hp: {health_bar(dominus)}
                            | Your Damage: {player.dmg}     | Dominus Damage: {dominus.dmg}

                        | Attack [A] | | Inventory [I] | | Confirm [C] |

                        """)
                time.sleep(0.5)
            if dominus.hp <= 0 or player.hp <= 0:
                frog_txt = open("art/frogking.txt", "r")
                clearConsole()
                if dominus.hp <= 0:
                    dominus.hp = 0
                    print(
                        f"""                            {dominus_txt.read()}
                            | Your Hp: {health_bar(player)}  | Dominus Hp: {health_bar(dominus)}
                            | Your Damage: {player.dmg}     | Dominus Damage: {dominus.dmg}

                        | You defeted Dominus! (Obtained a car door) |

                        """)
                    input("Press enter to continue ").casefold()
                    your_items.append(car_door)
                    clearConsole()
                elif player.hp <= 0:
                    player.hp = 0
                    print(
                        f"""                            {dominus_txt.read()}
                            | Your Hp: {health_bar(player)}  | Dominus Hp: {health_bar(dominus)}
                            | Your Damage: {player.dmg}     | Dominus Damage: {dominus.dmg}

                        | You were defeted by Dominus! |

                        """)
                    input("Press enter to continue ").casefold()
                    clearConsole()
                break
    elif rounds == 20:
        name = "Dominus GT"
        boss_hp = 45
        boss_dmg = 2
        dominus = Boss(name, boss_hp, boss_hp, boss_dmg)
        dominus_txt = open("art/dominus.txt", "r")
        turn = 1
        clearConsole()
        print(
            f"""                            {dominus_txt.read()}
                            | Your Hp: {health_bar(player)}  | Dominus Hp: {health_bar(dominus)}
                            | Your Damage: {player.dmg}     | Dominus Damage: {dominus.dmg}

                            | Attack [A] | | Inventory [I] | | Confirm [C] |

                    """)
        while dominus.hp != 0 or player.hp != 0:
            dominus_txt = open("art/dominus.txt", "r")
            if opend_inv == True:
                print(
                    f"""                            {dominus_txt.read()}
                            | Your Hp: {health_bar(player)}  | Dominus Hp: {health_bar(dominus)}
                            | Your Damage: {player.dmg}     | Dominus Damage: {dominus.dmg}

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
                        f"""                            {dominus_txt.read()}
                            | Your Hp: {health_bar(player)}  | Dominus Hp: {health_bar(dominus)}
                            | Your Damage: {player.dmg}     | Dominus Damage: {dominus.dmg}

                        | ->Attack<- [A] | | Inventory [I] | | Confirm [C] |

                    """)
                elif battle == "i":
                    attack = False
                    open_inventory = True
                    clearConsole()
                    print(
                        f"""                            {dominus_txt.read()}
                            | Your Hp: {health_bar(player)}  | Dominus Hp: {health_bar(dominus)}
                            | Your Damage: {player.dmg}     | Dominus Damage: {dominus.dmg}

                        | Attack [A] | | ->Inventory<- [I] | | Confirm [C] |

                    """)
                if battle == "c":
                    if attack == True:
                        dominus.hp = dominus.hp - player.dmg
                        turn = turn + 1
                        clearConsole()
                        print(
                            f"""                            {dominus_txt.read()}
                            | Your Hp: {health_bar(player)}  | Dominus Hp: {health_bar(dominus)}
                            | Your Damage: {player.dmg}     | Dominus Damage: {dominus.dmg}

                        | ->Attack<- [A] | | Inventory [I] | | Confirm [C] |

                        """)
                        if player.frog_item == True:
                            dominus.hp = round(
                                dominus.hp - dominus.maxhp*0.1)
                            time.sleep(0.1)
                            clearConsole()
                            print(
                                f"""                            {dominus_txt.read()}
                            | Your Hp: {health_bar(player)}  | Dominus Hp: {health_bar(dominus)}
                            | Your Damage: {player.dmg}     | Dominus Damage: {dominus.dmg}

                            | ->Attack<- [A] | | Inventory [I] | | Confirm [C] |

                        """)
                    elif open_inventory == True:
                        clearConsole()
                        opend_inv = True
                        inventory(player, your_items)
                        clearConsole()
            elif turn % 2 == 0:
                clearConsole()
                player.hp = player.hp - dominus.dmg
                turn = turn + 1
                print(
                    f"""                            {dominus_txt.read()}
                            | Your Hp: {health_bar(player)}  | Dominus Hp: {health_bar(dominus)}
                            | Your Damage: {player.dmg}     | Dominus Damage: {dominus.dmg}

                        | Attack [A] | | Inventory [I] | | Confirm [C] |

                        """)
                time.sleep(0.5)
            if dominus.hp <= 0 or player.hp <= 0:
                dominus_txt = open("art/dominus.txt", "r")
                clearConsole()
                if dominus.hp <= 0:
                    dominus.hp = 0
                    print(
                        f"""                            {dominus_txt.read()}
                            | Your Hp: {health_bar(player)}  | Dominus Hp: {health_bar(dominus)}
                            | Your Damage: {player.dmg}     | Dominus Damage: {dominus.dmg}

                        | You defeted Dominus! (Obtained a car door) |

                        """)
                    input("Press enter to continue ").casefold()
                    your_items.append(car_door)
                    clearConsole()
                elif player.hp <= 0:
                    player.hp = 0
                    print(
                        f"""                            {dominus_txt.read()}
                            | Your Hp: {health_bar(player)}  | Dominus Hp: {health_bar(dominus)}
                            | Your Damage: {player.dmg}     | Dominus Damage: {dominus.dmg}

                        | You were defeted by Dominus! |

                        """)
                    input("Press enter to continue ").casefold()
                    clearConsole()
                break
    elif rounds == 30:
        name = "Frasse"
        boss_hp = 55
        boss_dmg = 5
        frasse = Boss(name, boss_hp, boss_hp, boss_dmg)
        frasse_txt = open("art/frasse.txt", "r")
        turn = 1
        clearConsole()
        print(
            f"""                            {frasse_txt.read()}
                            | Your Hp: {health_bar(player)}  | Frasse Hp: {health_bar(frasse)}
                            | Your Damage: {player.dmg}     | Frasse Damage: {frasse.dmg}

                            | Attack [A] | | Inventory [I] | | Confirm [C] |

                    """)
        while frasse.hp != 0 or player.hp != 0:
            frasse_txt = open("art/frasse.txt", "r")
            if opend_inv == True:
                print(
                    f"""                            {frasse_txt.read()}
                            | Your Hp: {health_bar(player)}  | Frasse Hp: {health_bar(frasse)}
                            | Your Damage: {player.dmg}     | Frasse Damage: {frasse.dmg}

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
                        f"""                            {frasse_txt.read()}
                            | Your Hp: {health_bar(player)}  | Frasse Hp: {health_bar(frasse)}
                            | Your Damage: {player.dmg}     | Frasse Damage: {frasse.dmg}

                        | ->Attack<- [A] | | Inventory [I] | | Confirm [C] |

                    """)
                elif battle == "i":
                    attack = False
                    open_inventory = True
                    clearConsole()
                    print(
                        f"""                            {frasse_txt.read()}
                            | Your Hp: {health_bar(player)}  | Frasse Hp: {health_bar(frasse)}
                            | Your Damage: {player.dmg}     | Frasse Damage: {frasse.dmg}

                        | Attack [A] | | ->Inventory<- [I] | | Confirm [C] |

                    """)
                if battle == "c":
                    if attack == True:
                        frasse.hp = frasse.hp - player.dmg
                        turn = turn + 1
                        clearConsole()
                        print(
                            f"""                            {frasse_txt.read()}
                            | Your Hp: {health_bar(player)}  | Frasse Hp: {health_bar(frasse)}
                            | Your Damage: {player.dmg}     | Frasse Damage: {frasse.dmg}

                        | ->Attack<- [A] | | Inventory [I] | | Confirm [C] |

                        """)
                        if player.frog_item == True:
                            frasse.hp = round(
                                frasse.hp - frasse.maxhp*0.1)
                            time.sleep(0.1)
                            clearConsole()
                            print(
                                f"""                            {frasse_txt.read()}
                            | Your Hp: {health_bar(player)}  | Frasse Hp: {health_bar(frasse)}
                            | Your Damage: {player.dmg}     | Frasse Damage: {frasse.dmg}

                            | ->Attack<- [A] | | Inventory [I] | | Confirm [C] |

                        """)
                    elif open_inventory == True:
                        clearConsole()
                        opend_inv = True
                        inventory(player, your_items)
                        clearConsole()
            elif turn % 2 == 0:
                clearConsole()
                player.hp = player.hp - frasse.dmg
                turn = turn + 1
                print(
                    f"""                            {frasse_txt.read()}
                            | Your Hp: {health_bar(player)}  | Frasse Hp: {health_bar(frasse)}
                            | Your Damage: {player.dmg}     | Frasse Damage: {frasse.dmg}

                        | Attack [A] | | Inventory [I] | | Confirm [C] |

                        """)
                time.sleep(0.5)
            if frasse.hp <= 0 or player.hp <= 0:
                frasse_txt = open("art/frasse.txt", "r")
                clearConsole()
                if frasse.hp <= 0:
                    frasse.hp = 0
                    print(
                        f"""                            {frasse_txt.read()}
                            | Your Hp: {health_bar(player)}  | Frasse Hp: {health_bar(frasse)}
                            | Your Damage: {player.dmg}     | Frasse Damage: {frasse.dmg}

                        | You defeted Frasse! |

                        """)
                    input("Press enter to continue ").casefold()
                    clearConsole()
                elif player.hp <= 0:
                    player.hp = 0
                    print(
                        f"""                            {frasse_txt.read()}
                            | Your Hp: {health_bar(player)}  | Frasse Hp: {health_bar(frasse)}
                            | Your Damage: {player.dmg}     | Frasse Damage: {frasse.dmg}

                        | You were defeted by Frasse! |

                        """)
                    input("Press enter to continue ").casefold()
                    clearConsole()
                break
