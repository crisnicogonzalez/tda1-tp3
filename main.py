from src.game.game import Game
from src.game.player import Player
from src.factory.factory import *
from src.strategy.dinamic_strategy import DinamicStrategy
from src.strategy.player_a_strategy import MoveShipsStrategy


number_of_shoots = 3
ships_live_points, damage_table = create_board_configuration_from_file('basic')
print('ships_life_points:', str(ships_live_points))
print('damage_table:', str(damage_table))
dinamic_strategy = DinamicStrategy(damage_table=damage_table, shooters=number_of_shoots)
move_strategy = MoveShipsStrategy()
ships = create_ships(ships_live_points)
number_of_ships = len(damage_table)
print('number of ships', number_of_ships)

player_a = Player('player_a', strategy=move_strategy)
player_b = Player('player_b', strategy=dinamic_strategy)
game = Game(number_of_shoots, configuration_board, player_a, player_b)
game.play()
game.get_result()
