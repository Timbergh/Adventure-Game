import random as rand
import os
import time
import math


class Player:
    def __init__(self, name, maxhp, hp, dmg):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.dmg = dmg

    def __str__(self):
        return """
        -------------
        Name: {}
        Hp: {}
        Damage: {}
        -------------""".format(self.name, self.hp, self.dmg)


class Enemy(Player):

    def __str__(self):
        return """
        -------------
        Name: {}
        Hp: {}
        Damage: {}
        -------------""".format(self.name, self.hp, self.dmg)


class Boss(Player):

    def __str__(self):
        return """
        -------------
        Name: {}
        Hp: {}
        Damage: {}
        -------------""".format(self.name, self.hp, self.dmg)


class Items:
    def __init__(self, desc, name):
        self.name = name
        self.desc = desc

    def __str__(self):
        return "{}".format(self.name)


class Trap:
    def __init__(self, name, desc, end1, end2, end3,):
        self.name = name
        self.desc = desc
        self.end1 = end1
        self.end2 = end2
        self.end3 = end3


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def health_bar(self):
    """
    copy paste:
    ▒
    ░
    ▓
    """
    missing_hp = self.maxhp - self.hp
    hp_bar = "▓"*self.hp + f" {self.hp}/{self.maxhp}"
    if self.hp < self.maxhp:
        hp_bar = ("▓"*self.hp + "░"*missing_hp +
                  f" {self.hp}/{self.maxhp}")
    return hp_bar


def boss_encounter(rounds, player):
    if rounds == 10:
        name = "The Frog-King"
        boss_hp = 30
        boss_dmg = 1
        frogking = Boss(name, boss_hp, boss_hp, boss_dmg)
        frog_txt = open("frogking.txt", "r")
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
                clearConsole()
                if frogking.hp <= 0:
                    frogking.hp = 0
                    print(
                        f"""                            {frog_txt.read()}
                            | Your Hp: {health_bar(player)}  | Frog-King Hp: {health_bar(frogking)}
                            | Your Damage: {player.dmg}     | Frog-king Damage: {frogking.dmg}

                        | You defeted the Frog-king! |

                        """)
                    input("Press enter to continue ")
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


burgir = Items("Burgir! (+3 Hp)", "Burgir")
roids = Items(
    "Makes you a buff ass hell for a short while (+5 Dmg for one turn)", "Roids")
stick = Items("You hit harder (+1 Dmg)", "Stick")
belt = Items(
    "Permanently increase your damage by one and hp by two (+1 Dmg, +2 Max Hp)", "Belt")
dripcap = Items("You look fabulous and gain one max hp(+1 Max Hp)", "Drip Cap")
jordans = Items(
    "These drippy kicks look fresh as hell dawg (+1 Max Hp)", "Jordans")

boulder = Trap("Bouldertrap", "A large boulder comes rolling towards you what will you do?", "You punched the boulder and took damage what did you expect?",
               "You tried to flee but did not make it your toes got cruched", "You did nothing and the boulder decided to leave you alone")
cheese = Trap("Cheesetrap", "You see a large block of cheese on a pedestal what do you want to do?",
              "You ate the cheese and went to sleep", "You moved on and tripped hitting your knee", "You fed the cheese to a mouse and he gave you his dripcap")
santa = Trap("Santatrap", "You walked in to a room and saw Santa claus :D, what do you want to do?", "You opened the present and found a bomb, ouch!", "Whilst you were sitting on his lap, santa stole one of your items",
             "Santa became furious and hit you with a belt 4 times, but you managed to catch and take the belt")
jordan = Trap("Jordantrap", "After entering through the door you find yourself on a basketball court with Michael Jordan, he asks you to play a 1v1 basketball game, what do you do?",
              "You chose to let him win and he gave you a token of appreciation", "You beat him in the most embarrasing way possible, and in return, he beats you to a pulp", "You run away crying and escape with your life")
""" joebiden = Trap("Joebidentrap", "You enter the oval office and you see president Joseph Robinette Biden Junior sitting at his desk, what is your next action?", "You waved and left","You sneezed killing the president in an instant, and took the oppertunity to steal his tie","You got an asswhopping by Joe") """
""" """
trap_pool = [boulder, cheese, santa]


def random_encounter(rounds, player, e_hp, e_dmg, rand_index, your_items):
    item_pool = [burgir, roids, stick, belt, dripcap, jordans]
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

                        | You defeted the Ogre! |

                        """)
                    input("Press enter to continue ")
                    clearConsole()
                elif player.hp <= 0:
                    player.hp = 0
                    print(
                        f"""
                        | Your Hp: {health_bar(player)}  | Ogre Hp: {health_bar(ogre)}
                        | Your Damage: {player.dmg}     | Ogre Damage: {e_dmg}

                        | You were defeted by the Ogre! |

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
                input("1. Eat the cheese, 2. Continue on without doing anything, 3. Give the cheese to a passing mouse with copious amonts of drip: "))
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
                your_items.remove(rand.choice(your_items))
            elif t_choice == 3:
                print(santa.end3)
                player.hp = player.hp - 1
                your_items.append(belt)
        if random_trap == jordan:
            print(jordan.desc)
            t_choice = int(
                input("1. Let him win", "2. Play him in a fair 1v1", "3. Run away"))
            if t_choice == 1:
                print(jordan.end1)
                your_items.append(jordans)
            elif t_choice == 2:
                print(jordan.end2)
                player.hp = player.hp - 1
            elif t_choice == 3:
                print(jordan.end3)

    return player, ogre


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
    re = False
    if rounds % 5 == 0 and rounds % 10 != 0:
        fountain = True
    else:
        fountain = False
    if rounds % 10 == 0:
        boss_room = True
    else:
        boss_room = False
    if fountain == False and boss_room == False:
        print(f"""
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
                    """)
    elif fountain == True and boss_room == False:
        print(f"""
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
                    """)
        print(
            "Do you wish to enter the Holy door?")
        holy_door = input(
            "If you enter you will skip this round y/n -> ").casefold()
        if holy_door == "y":
            hdopen1 = open("dooropen/hdopen1.txt", "r")
            hdopen2 = open("dooropen/hdopen2.txt", "r")
            toilet = open("toilet.txt", "r")
            clearConsole()
            print(hdopen1.read())
            time.sleep(0.3)
            clearConsole()
            print(hdopen2.read())
            time.sleep(1)
            clearConsole()
            print(toilet.read())
            input(
                f"\n\nYou took a sip of the holy fountains water and gained {player.maxhp - player.hp} Hp\nPress any button to continue")
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
        """)
        input("Press enter to continue ")
        boss_encounter(rounds, player)
        boss_open = True
    while choose_door != "q":
        if holyopen == True:
            clearConsole()
            break
        if boss_open == True:
            clearConsole()
            break
        if re == True:
            print(f"""
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
                    """)
            re = False
        choose_door = input(
            "Which door would you like to enter? [L] [M] [R] or [Q] quit to menu -> ").casefold()
        if choose_door == "l":  # LEFT DOOR
            if left_open == True:
                clearConsole()
                print(f"""
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
                """)
            elif left_open == False:
                rand_index = rand.choice(rand_door)
                rand_door.remove(rand_index)
                if rand_index == 1:
                    ri = "found an item!"
                elif rand_index == 2:
                    ri = "encounterd a monster!"
                elif rand_index == 3:
                    ri = "found out you are standing on a trap!"
                time.sleep(0.3)
                clearConsole()
                print(f"""
                                    Round {rounds}
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
                """)
                left_open = True
                if rand_index == 2:
                    input("Press enter to continue")
                    re = True
                    random_encounter(rounds, player, e_hp, e_dmg,
                                     rand_index, your_items)
                else:
                    random_encounter(rounds, player, e_hp, e_dmg,
                                     rand_index, your_items)

        elif choose_door == "m":  # MIDDLE DOOR
            if middle_open == True:
                clearConsole()
                print(f"""
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
                """)
            elif middle_open == False:
                rand_index = rand.choice(rand_door)
                rand_door.remove(rand_index)
                if rand_index == 1:
                    ri = "found an item!"
                elif rand_index == 2:
                    ri = "encounterd a monster!"
                elif rand_index == 3:
                    ri = "found out you are standing on a trap!"
                time.sleep(0.3)
                clearConsole()
                print(f"""
                                    Round {rounds}
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
                """)
                middle_open = True
                if rand_index == 2:
                    input("Press enter to continue")
                    re = True
                    random_encounter(rounds, player, e_hp, e_dmg,
                                     rand_index, your_items)
                else:
                    random_encounter(rounds, player, e_hp, e_dmg,
                                     rand_index, your_items)

        elif choose_door == "r":  # RIGHT DOOR
            if right_open == True:
                clearConsole()
                print(f"""
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
                """)
            elif right_open == False:
                rand_index = rand.choice(rand_door)
                rand_door.remove(rand_index)
                if rand_index == 1:
                    ri = "found an item!"
                elif rand_index == 2:
                    ri = "encounterd a monster!"
                elif rand_index == 3:
                    ri = "found out you are standing on a trap!"
                time.sleep(0.3)
                clearConsole()
                print(f"""
                                    Round {rounds}
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
                """)
                right_open = True
                if rand_index == 2:
                    input("Press enter to continue")
                    re = True
                    random_encounter(rounds, player, e_hp, e_dmg,
                                     rand_index, your_items)
                else:
                    random_encounter(rounds, player, e_hp, e_dmg,
                                     rand_index, your_items)

        elif choose_door == "q":  # BACK TO MENU
            clearConsole()
            print("Returning to menu...")
        if player.hp == 0:
            clearConsole()
            break
        if left_open == True and middle_open == True and right_open == True:
            input(
                "You have no doors left\nPress enter to continue").casefold()
            clearConsole()
            print("Returning to menu...")
            break


your_items = []


def inventory(player, your_items):
    item_one = ""
    item_two = ""
    item_three = ""
    item_four = ""
    item_five = ""
    selected_item = None
    item_used = True
    inv = ""
    while inv != "q":
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
        if item_used == True:
            print(f"""
            ----------------INVENTORY-----------------
            |   {item_one}    |   {item_two}    |   {item_three}    |   {item_four}    |   {item_five}    |
            ------------------------------------------
            """)
        item_used = False
        inv = input(
            "            Select items 1-5 | Confirm [C] | Go back [Q] -> ")
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
        elif inv == "c":
            clearConsole()
            if selected_item == burgir:  # BURGIR
                print(f"""
                -------------------
                {burgir.name}
                {burgir.desc}
                -------------------
                """)
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
                print(f"""
                -------------------
                {belt.name}
                {belt.desc}
                -------------------
                """)
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
                print(f"""
                -------------------
                {roids.name}
                {roids.desc}
                -------------------
                """)
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(roids)
                    item_used = True
                else:
                    clearConsole()
                    item_used = True
            elif selected_item == dripcap:  # DRIP CAP
                print(f"""
                -------------------
                {dripcap.name}
                {dripcap.desc}
                -------------------
                """)
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
                print(f"""
                -------------------
                {stick.name}
                {stick.desc}
                -------------------
                """)
                use_item = input(f"Do you want to use {selected_item} y/n -> ")
                if use_item == "y":
                    clearConsole()
                    your_items.remove(stick)
                    player.dmg = player.dmg + 1
                    item_used = True
                else:
                    clearConsole()
                    item_used = True
                    inventory(your_items)
        elif inv == "q":
            clearConsole()
    return player


def stats(player, name):
    if player.hp > player.maxhp:
        player.hp = player.maxhp
    print(
        f"""
    -------------
    Name: {name}
    Hp: {health_bar(player)}
    Damage: {player.dmg}
    -------------
    """)
    input("     Press any button to go back to menu")
    clearConsole()


def create_character():
    name = input("Enter your name -> ")
    random_stats = rand.randint(2, 4)
    maxhp = random_stats
    hp = maxhp
    dmg = 5 - random_stats
    return Player(name, maxhp, hp, dmg)


def main():
    rounds = 0
    player = create_character()
    clearConsole()
    character = open("char1.txt", "r")
    print(f"Hello {player.name}\nThis is you")
    print(character.read())
    input("Press enter to continue")
    clearConsole()
    print("I will now calculate your stats...\n")
    time.sleep(0)  # ÄNDRA PÅ TIDEN
    print(f"HP = {player.maxhp}")
    time.sleep(0)  # ÄNDRA PÅ TIDEN
    print(f"Damage = {player.dmg}\n")
    input("Press enter to continue")
    clearConsole()
    while True:
        if player.hp <= 0:
            clearConsole()
            print("You died...")
            game_over = open("gameover.txt", "r")
            print(game_over.read())
            time.sleep(5)
            break
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
            player = inventory(player, your_items)
        elif menu == "c":
            clearConsole()
            rounds = rounds + 1
            doors(player, rounds)
        elif menu == "s":
            clearConsole()
            stats(player, player.name)
        elif menu == "q":
            clearConsole()
            print("Quiting game...")
            break


main()
"""
___________________
| {x}         {x} |
|   \  _---_  /   |
|    \/     \/    |
|     |0   0|     |
|      \ + /      |
|     / |||  \    |
|    /  \_/   \   |
| {x}         {x} |
|                 |
|   {Boss_namn}   |
|                 |
|_________________|

Frog king:
         o  o   o  o
         |\/ \^/ \/|
         |,-------.|
       ,-.(|)   (|),-.
       \_*._ ' '_.* _/
        /`-.`--' .-'\
   ,--./    `---'    \,--.
   \   |(  )     (  )|   /
    \  | ||       || |  /
     \ | /|\     /|\ | /
     /  \-._     _,-/  \
    //| \\  `---'  // |\\
   /,-.,-.\       /,-.,-.\
  o   o   o      o   o    o
  Dominus GT:
             _____________________
              \                 /
               \ ______________/                          
             ..(.....    ...../,.            
       ,/(((,( ..             . /*((((/      
       /((/( ..    ,******,     . **(((.     
       //(.      .//////////.      .(,/.     
    /(//((((*(((/  ...,,...  /(((/(((((/(/   
   /((/(((((/((((/  ..,,..  /((((/(((((//(/  
  *(((//(((((/((((((((((((((((((//(((((/(((* 
  ,/(((/((((((//////////(///////((((((/(((/, 
   /((// @@ /((,,,,,,((((,,,,,,//( @&  (/(/  
    /(//(// //........((......../( //(////   
    .,//'  //////((((((((((//////  .. //.   
      .......                    ........    
                                                                                                                                                                                                          
        Innocent little puppy:                                                                                                                                                                                              
                                   ..,,,,,,,,,.. 
                     .,;%%%%%%%%%%%%%%%%%%%%;,. 
                   %%%%%%%%%%%%%%%%%%%%////%%%%%%, .,;%%;, 
            .,;%/,%%%%%/////%%%%%%%%%%%%%%////%%%%,%%//%%%, 
        .,;%%%%/,%%%///%%%%%%%%%%%%%%%%%%%%%%%%%%%%,////%%%%;, 
     .,%%%%%%//,%%%%%%%%%%%%%%%%@@%a%%%%%%%%%%%%%%%%,%%/%%%%%%%;, 
   .,%//%%%%//,%%%%///////%%%%%%%@@@%%%%%%///////%%%%,%%//%%%%%%%%, 
 ,%%%%%///%%//,%%//%%%%%///%%%%%@@@%%%%%////%%%%%%%%%,/%%%%%%%%%%%%% 
.%%%%%%%%%////,%%%%%%%//%///%%%%@@@@%%%////%%/////%%%,/;%%%%%%%%/%%% 
%/%%%%%%%/////,%%%%///%%////%%%@@@@@%%%///%%/%%%%%//%,////%%%%//%%%' 
%//%%%%%//////,%/%a`  'a%///%%%@@@@@@%%////a`  'a%%%%,//%///%/%%%%% 
%///%%%%%%///,%%%%@@aa@@%//%%%@@@@S@@@%%///@@aa@@%%%%%,/%////%%%%% 
%%//%%%%%%%//,%%%%%///////%%%@S@@@@SS@@@%%/////%%%%%%%,%////%%%%%' 
%%//%%%%%%%//,%%%%/////%%@%@SS@@@@@@@S@@@@%%%%/////%%%,////%%%%%' 
`%/%%%%//%%//,%%%///%%%%@@@S@@@@@@@@@@@@@@@S%%%%////%%,///%%%%%' 
  %%%%//%%%%/,%%%%%%%%@@@@@@@@@@@@@@@@@@@@@SS@%%%%%%%%,//%%%%%' 
  `%%%//%%%%/,%%%%@%@@@@@@@@@@@@@@@@@@@@@@@@@S@@%%%%%,/////%%' 
   `%%%//%%%/,%%%@@@SS@@SSs@@@@@@@@@@@@@sSS@@@@@@%%%,//%%//%' 
    `%%%%%%/  %%S@@SS@@@@@Ss` .,,.    'sS@@@S@@@@%'  ///%/%' 
      `%%%/    %SS@@@@SSS@@S.         .S@@SSS@@@@'    //%%' 
               /`S@@@@@@SSSSSs,     ,sSSSSS@@@@@' 
             %%//`@@@@@@@@@@@@@Ss,sS@@@@@@@@@@@'/ 
           %%%%@@00`@@@@@@@@@@@@@'@@@@@@@@@@@'//%% 
       %%%%%%a%@@@@000aaaaaaaaa00a00aaaaaaa00%@%%%%% 
    %%%%%%a%%@@@@@@@@@@000000000000000000@@@%@@%%%@%%% 
 %%%%%%a%%@@@%@@@@@@@@@@@00000000000000@@@@@@@@@%@@%%@%% 
%%%aa%@@@@@@@@@@@@@@0000000000000000000000@@@@@@@@%@@@%%%% 
%%@@@@@@@@@@@@@@@00000000000000000000000000000@@@@@@@@@%%%%%      

 ,_-~~~-,    _-~~-_
 /        ^-_/      \_    _-~-.
|      /\  ,          `-_/     \
|   /~^\ '/  /~\  /~\   / \_    \
 \_/    }/  /        \  \ ,_\    }
        Y  /  /~  /~  |  Y   \   |
       /   | {Q) {Q)  |  |    \_/
       |   \  _===_  /   |
       /  >--{     }--<  \
     /~       \_._/       ~\
    /    *  *   Y    *      \
    |      * .: | :.*  *    |
    \    )--__==#==__--     /
     \_      \  \  \      ,/
       '~_    | |  }   ,~'
          \   {___/   /
           \   ~~~   /
           /\._._._./\
          {    ^^^    }
           ~-_______-~
            /       \                                                                                                                        
 """
