from src.utils.quicksort import quicksort
import logging

FORMAT = "%(class)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'class': 'DynamicStrategy'}


class DynamicStrategy:
    def __init__(self, game=None, damage_table=None, shooters=None):
        self.game = game
        self.known_states = {}
        self.damage_table = damage_table
        self.shooters = shooters
        self.game_manager = game

    def step(self, column):
        if column in self.known_states:
            return self.known_states[column]
        else:
            priority_list = quicksort(self.get_damage_board_column(column))
            self.known_states[column] = priority_list
        return priority_list

    def get_priority_list_from_column(self,column):
        sorted_list = quicksort(self.get_damage_board_column(column))
        priority_list = []
        for element in reversed(sorted_list):
            index = sorted_list.index(element)
            priority_list.append(index)
        return priority_list

    def execute(self):
        current_column = self.game.get_current_column()
        priority_list = self.step(current_column)
        logging.debug('priority list {}'.format(priority_list), extra=log_info)
        for i in range(self.shooters):
            index_priority = -1
            ship_position = priority_list[index_priority]
            while not self.attack(ship_position):
                index_priority -= 1
            self.known_states[current_column] = priority_list[:index_priority]

    def attack(self, ship_position):
        logging.debug('Atacando', extra=log_info)
        if self.game.ship_of_position_is_alive(ship_position):
            self.game.attack_to_position(ship_position)
            return True
        else:
            return False

    def get_damage_board_column(self,column):
        return [row[column] for row in self.damage_table]

    def set_game_manager(self, game_manager):
        self.game_manager = game_manager
