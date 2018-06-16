class Player:
    def __init__(self, name, strategy=None):
        self.strategy = strategy
        self.name = name

    def get_next_play(self):
        return self.strategy

    def play(self):
        print('Jugar %s', self.name)
