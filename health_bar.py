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
