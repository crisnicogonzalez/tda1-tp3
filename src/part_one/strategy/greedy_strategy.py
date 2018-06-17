import operator
import logging
log_info = {'class': 'GreedyStrategy'}


class GreedyStrategy:
    def __init__(self, game_manager=None, number_of_shooters=0, damage_table=None, ships=None):
        self.game_manager = game_manager
        self.number_of_shooters = number_of_shooters
        self.damage_table = damage_table
        self.alive_ships = set(ships)

    def execute(self):
        logging.info('Iniciando ataque', extra=log_info)
        damage_by_ship = {}
        for alive_ship in self.alive_ships:
            current_damage = self.damage_table[alive_ship.get_row()][alive_ship.get_column()]
            live_after_attack = alive_ship.get_life_points() - current_damage
            damage_by_ship[alive_ship] = live_after_attack
        sorted_ships = sorted(damage_by_ship.items(), key=operator.itemgetter(1))

        ship_position_in_sorted_ships = 0
        for x in range(self.number_of_shooters):
            logging.info('Ataca mortero {}'.format(x), extra=log_info)
            while ship_position_in_sorted_ships < len(sorted_ships) and not self.attack_in_row(sorted_ships[ship_position_in_sorted_ships][0].get_row()):
                self.alive_ships.remove(sorted_ships[ship_position_in_sorted_ships][0])
                ship_position_in_sorted_ships += 1
                logging.info('ship_position_in_sorted_ships {}'.format(ship_position_in_sorted_ships), extra=log_info)

    def attack_in_row(self, row):
        if self.game_manager.ship_of_position_is_alive(row):
            self.game_manager.attack_to_position(row)
            return True
        else:
            logging.debug('No se pudo atacar, el barco ya no se encuentra con vida', extra=log_info)
            return False
