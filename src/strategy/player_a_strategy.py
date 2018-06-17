import logging

FORMAT = "%(class)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
log_info = {'class': 'Game'}


class MoveShipsStrategy:
    def __init__(self, game_manager=None):
        self.game_manager = game_manager

    def execute(self):
        self.game_manager.move_ships()