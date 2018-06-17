from src.game.game import Game
from src.game.player import Player
from .src.factory.factory import create_board_configuration_from_file


player_a = Player('player_a')
player_b = Player('player_b')
number_of_ships = 2
number_of_shoots = 3
configuration_board = create_board_configuration_from_file('basic')
game = Game(number_of_shoots, configuration_board, player_a, player_b)
game.play()
game.get_result()
