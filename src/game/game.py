from src.factory.factory import create_ships
from .ship import Ship
from .board import Board
from .observer import Observer
from threading import *
from multiprocessing import Queue

class Game:
    
    def __init__(self, numbers_of_ships, numbers_of_columns ,number_of_shooters, player_a, player_b,life_points,damage_table):
        # Configuration es la tabla que se lee del archivo
        super().__init__()
        self.board = Board(numbers_of_ships,numbers_of_columns)
        self.number_of_turn = 0
        self.ships_with_life = create_ships(life_points)
        self.queue = None
        self.__init_players_queue(player_a,player_b)
        self.damage_table = damage_table
        self.curret_colum = 0

    def __init_players_queue(self,player_a,player_b):
        self.queue = Queue()
        self.queue.put(player_a,player_b)

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

    def play(self):
        while self.number_of_dead_ships != self.numbers_of_ships:
            current_player = self.queue.get()
            current_player.play()
            self.queue.put(current_player)

    def get_result(self):
        return self.result


    def move_ships(self):

    def get_current_column(self):
        return self.curret_colum    

    def ship_of_position_is_alive(self,row):
        current_ship = self.board.get_item_from_position(self.curret_colum,row)
        return !current_ship.is_dead()

    def attack_to_position(self,row):
        current_ship = self.board.get_item_from_position(column,row)
        current_ship.attack_with_points(damage_table[column][row])
