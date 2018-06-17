from .board import Board
from queue import Queue
import logging

log_info = {'class': 'Game'}


class Game:
    def __init__(self, ships, numbers_of_columns, damage_table):
        logging.info('Creando juego', extra=log_info)
        super().__init__()
        self.board = Board(len(ships), numbers_of_columns)
        self.number_of_turn = 0
        self.alive_ships = ships
        self.queue = Queue()
        self.damage_table = damage_table
        self.number_of_plays = 0
        self.numbers_of_columns = numbers_of_columns
        self.number_of_dead_ships = 0
        self.number_of_ships = len(ships)
        self.__locate_ships()

    def add_player(self, player):
        self.queue.put(player)

    def __locate_ships(self):
        i = 0
        for ship in self.alive_ships:
            self.board.insert_item_in_position(ship, i, 0)
            i += 1
        # self.board.print()

    def increment_number_of_dead_ships(self):
        self.number_of_dead_ships += 1

    def play(self):
        self.number_of_plays = 0
        while self.number_of_dead_ships < self.number_of_ships:
            current_player = self.queue.get()
            current_player.play()
            self.queue.put(current_player)
            self.number_of_plays += 1
        print('La cantidad de turnos es {}'.format(self.number_of_plays // 2))

    def move_ships(self):
        logging.debug('La cantidad de barcos disponibles es {}'.format(self.number_of_ships - self.number_of_dead_ships), extra=log_info)
        logging.info('Moviendo los barcos', extra=log_info)
        for ship in self.alive_ships:
            if not ship.is_dead():
                column = ship.get_column()
                row = ship.get_row()
                self.board.remove_from_position(row, column)
                self.board.insert_item_in_position(ship, row, column+1)
                logging.debug('Row={} y column+1={}'.format(row,column+1),extra=log_info)
                logging.info('El barco tiene {} de vida y tiene un ataque potencial de {}'.format(ship.get_life_points(), self.damage_table[row][(column+1) % self.numbers_of_columns]),extra=log_info)
        # self.board.print()

    def get_current_column(self):
        current_column = (self.number_of_plays // 2) % self.numbers_of_columns
        logging.debug('Current column {}'.format(current_column), extra=log_info)
        return current_column

    def ship_of_position_is_alive(self, row):
        logging.info('Viendo si el barco en la fila {} tiene vida'.format(row), extra=log_info)
        current_ship = self.board.get_item_from_position(row, self.get_current_column())
        return current_ship is not None and not current_ship.is_dead()

    def attack_to_position(self, row):
        column = self.get_current_column()
        current_ship = self.board.get_item_from_position(row, column)
        logging.info('Ataca a la posicion {} con vida {}'.format(row, current_ship.get_life_points()), extra=log_info)
        current_ship.attack_with_points(self.damage_table[row][column])
        if current_ship.is_dead():
            self.number_of_dead_ships += 1
        logging.info('Se Ataco el barco y quedo con {}'.format(current_ship.get_life_points()), extra=log_info)
