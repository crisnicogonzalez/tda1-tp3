class Player:
    def __init__(self,strategy):
        self.strategy = strategy

    def get_next_play(self):
        return self.strategy

    def play(self):
        ##Something
