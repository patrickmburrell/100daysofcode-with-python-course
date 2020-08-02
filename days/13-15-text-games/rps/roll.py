class Roll:
    def __init__(self, name, greater_than, lesser_than):
        self.name = name
        self.greater_than = greater_than
        self.lesser_than = lesser_than

    def can_defeat(self, roll):
        defeats = roll.name in self.greater_than
        return defeats
