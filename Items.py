class Items:
    def __init__(self, desc, name):
        self.name = name
        self.desc = desc

    def __str__(self):
        return "{}".format(self.name)
