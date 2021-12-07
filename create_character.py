import random as rand

from Player import Player


def create_character():
    name = input("Enter your name -> ")
    random_stats = rand.randint(2, 4)
    maxhp = random_stats
    hp = maxhp
    dmg = 5 - random_stats
    return Player(name, maxhp, hp, dmg, 0)
