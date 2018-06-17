from src.game.game import Game
from src.game.player import Player
from src.factory.factory import *
from src.strategy.dinamic_strategy import DynamicStrategy
from src.strategy.player_a_strategy import MoveShipsStrategy
import logging

FORMAT = "%(class)-8s     %(message)s"
logging.basicConfig(format=FORMAT)
logging.getLogger().setLevel(logging.INFO)
log_info = {'class': 'Main'}


number_of_shooters = 3
ships_live_points, damage_table = create_board_configuration_from_file('basic')
ships = create_ships(ships_live_points)
number_of_ships = len(damage_table)


# Create game
game = Game(ships, len(damage_table), damage_table)
dynamic_strategy = DynamicStrategy(game, damage_table, number_of_shooters)
move_strategy = MoveShipsStrategy(game)

player_a = Player('player_a', strategy=move_strategy)
player_b = Player('player_b', strategy=dynamic_strategy)
game.add_player(player_b)
game.add_player(player_a)
game.play()
