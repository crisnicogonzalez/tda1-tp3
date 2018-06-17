
class MoveShipsStrategy:

    def __init__(self, game_manager=None):
        self.game_manager = game_manager

    def execute(self):
        self.game_manager.move_ships()