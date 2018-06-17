from .board import Board
from queue import Queue
import logging

FORMAT = "%(class)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'class': 'Game'}


class Game:
    def __init__(self, ships, numbers_of_columns, damage_table):
        logging.info('Creando juego', extra=log_info)
        super().__init__()
        self.board = Board(len(ships), numbers_of_columns)
        self.number_of_turn = 0
        self.ships_with_life = ships
        self.queue = Queue()
        self.damage_table = damage_table
        self.number_of_plays = 0
        self.numbers_of_columns = numbers_of_columns
        self.number_of_dead_ships = 0
        self.number_of_ships = len(ships)

    def add_player(self, player):
        self.queue.put(player)

    def __locate_ships(self):
        i = 0
        for ship in self.ships:
            ship.register_observer(self.board)
            ship.register_observer(self)
            self.board.insert_item_in_position(ship, 0, i)
            i += 1
    
    def notify(self):
        self.number_of_dead_ships += 1
        
    def __next(self):
        if self.number_of_shifts % 2 == 0:
            self.current_player = self.player_a
        else:
            self.current_player = self.player_b
        self.number_of_shifts += 1

    def increment_number_of_dead_ships(self):
        self.number_of_dead_ships += 1

    def play(self):
        self.number_of_plays = 0
        while self.number_of_dead_ships < self.number_of_ships:
            current_player = self.queue.get()
            current_player.play()
            self.queue.put(current_player)
            self.number_of_plays += 1

    def get_result(self):
        return self.result

    def move_ships(self):
        logging.debug('Moviendo los barcos', extra=log_info)
        print('move ships')

    def get_current_column(self):
        return (self.number_of_plays / 2) % self.numbers_of_columns

    def ship_of_position_is_alive(self, row):
        current_ship = self.board.get_item_from_position(self.get_current_column(), row)
        return not current_ship.is_dead()

    def attack_to_position(self, row):
        current_ship = self.board.get_item_from_position(column, row)
        current_ship.attack_with_points(damage_table[column][row])
        if current_ship.is_dead():
            self.number_of_dead_ships += 1
