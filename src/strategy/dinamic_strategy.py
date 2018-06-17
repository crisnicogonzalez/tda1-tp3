from src.utils.quicksort import quicksort
import logging

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
            priority_list = self.get_priority_list_from_column(column)
            self.known_states[column] = priority_list
        return priority_list

    def get_priority_list_from_column(self, column):
        damage_board_column = self.get_damage_board_column(column)
        logging.debug('board column {}'.format(damage_board_column), extra=log_info)
        sorted_list = quicksort(damage_board_column[:])
        logging.debug('sorted list {}'.format(sorted_list), extra=log_info)

        priority_list = []
        for x in range(len(sorted_list)):
            index = damage_board_column.index(sorted_list[x])
            logging.debug('element {} and index {}'.format(sorted_list[x], index), extra=log_info)
            priority_list.insert(0, index)
        return priority_list

    def execute(self):
        current_column = self.game.get_current_column()
        priority_list = self.step(current_column)
        logging.debug('priority list {}'.format(priority_list), extra=log_info)
        index_priority = 0
        for i in range(self.shooters):
            logging.info('Realizando el ataque con la lanzadera {}'.format(i),extra=log_info)
            ship_position = priority_list[index_priority]
            while not self.attack(ship_position):
                index_priority += 1
                ship_position = priority_list[index_priority]
            self.known_states[current_column] = priority_list[index_priority:]

    def attack(self, ship_position):
        logging.info('Iniciando ataque', extra=log_info)
        if self.game.ship_of_position_is_alive(ship_position):
            self.game.attack_to_position(ship_position)
            return True
        else:
            logging.debug('No se pudo atacar, el barco ya no se encuentra con vida', extra=log_info)
            return False

    def get_damage_board_column(self, column):
        logging.debug('damage board {}'.format(self.damage_table), extra=log_info)
        list_to_return = []
        for x in range(len(self.damage_table)):
            list_to_return.append(self.damage_table[x][column])
        return list_to_return

    def set_game_manager(self, game_manager):
        self.game_manager = game_manager
