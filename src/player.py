class Player:
    def __init__(self):
        self.estrategy = None

    def get_next_play(self):
        return self.estrategy