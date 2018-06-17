
class MoveShipsStrategy:

    def __init__(self):
        self.game_manager = None

    def execute(self):
        print('execute')

    def set_game(self, game_manager):
        self.game_manager = game_manager
