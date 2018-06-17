class Player:
    def __init__(self, name, strategy=None,game):
        self.strategy = strategy
        self.name = name
        self.strategy.set_game(game)

    def get_next_play(self):
        return self.strategy

    def play(self):
        print('Jugar %s', self.name)
