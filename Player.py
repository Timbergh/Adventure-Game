class Player:
    def __init__(self, name, maxhp, hp, dmg, wallet):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.dmg = dmg
        self.wallet = wallet
        self.frog_item = False

    def __str__(self):
        return """
        -------------
        Name: {}
        Hp: {}
        Damage: {}
        -------------""".format(self.name, self.hp, self.dmg)
