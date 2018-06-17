class Player:
    def __init__(self, name, game=None, strategy=None):
        self.strategy = strategy
        self.name = name
        self.strategy.set_game(game)

    def get_next_play(self):
        return self.strategy

    def play(self):
        self.strategy.execute()
