from src.part_one.game.game import Game
from src.part_one.game.player import Player
from src.part_one.factory.factory import *
from src.part_one.strategy.dinamic_strategy import DynamicStrategy
from src.part_one.strategy.player_a_strategy import MoveShipsStrategy
from src.part_one.strategy.greedy_strategy import GreedyStrategy

import logging

FORMAT = "%(class)-8s     %(message)s"
logging.basicConfig(format=FORMAT)
logging.getLogger().setLevel(logging.INFO)
log_info = {'class': 'Main'}


def play_game(strategy_a, strategy_b, game_manager):
    player_a = Player('player_a', strategy=strategy_a)
    player_b = Player('player_b', strategy=strategy_b)
    game_manager.add_player(player_b)
    game_manager.add_player(player_a)
    game_manager.play()


def get_ships_and_damage_table(file_name):
    ships_live_points, damage_table = create_board_configuration_from_file(file_name)
    ships = create_ships(ships_live_points)
    return ships, damage_table


number_of_shooters = 3
ships, damage_table = get_ships_and_damage_table('basic')
number_of_ships = len(damage_table)

# Create game
game_one = Game(ships, len(damage_table[0]), damage_table)
game_two = Game(ships[:], len(damage_table[0]), damage_table)

dynamic_strategy = DynamicStrategy(game_one, damage_table, number_of_shooters)
move_strategy_one = MoveShipsStrategy(game_one)
play_game(move_strategy_one, dynamic_strategy, game_one)


move_strategy_two = MoveShipsStrategy(game_two)
greedy_strategy = GreedyStrategy(game_two, number_of_shooters, damage_table, ships)
#play_game(move_strategy_two, greedy_strategy, game_two)
