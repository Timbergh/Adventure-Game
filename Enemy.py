class Enemy:
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
