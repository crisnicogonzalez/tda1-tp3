from .ship import Ship
from .board import Board
from .observer import Observer
from threading import *


class Game(Observer):
    
    def __init__(self, numbers_of_ships, number_of_mortars, configuration, rows):
        super().__init__()
        self.numbers_of_ships = numbers_of_ships
        self.board = Board(numbers_of_ships, rows)
        self.ships = [Ship(100) for _ in range(numbers_of_ships)]
        self.__locate_ships()
        self.number_of_dead_ships = 0
        self.number_of_shifts = 0
        self.current_player = None
        self.player_a = None
        self.player_b = None

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

    def init_game(self):
        while self.number_of_dead_ships != self.numbers_of_ships:
            jugada = self.current_player.getJugada()
            jugada.ejecutar()