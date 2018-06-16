from .ship import Ship
from .board import Board
from .observer import Observer
from threading import *


class Game(Observer):
    
    def __locate_ships(self):
        i = 0
        for ship in self.ships:
            ship.register_observer(self.board)
            ship.register_observer(self)
            self.board.insert_item_in_position(ship, 0, i)
            i += 1
        
    def __init__(self, cols, rows, numbers_of_ships, number_of_mortars):
        super().__init__()
        self.board = Board(cols, rows)
        self.ships = [Ship(100) for _ in range(numbers_of_ships)]
        self.__locate_ships()


    def __init__(self, board, ships_list, number_of_mortars):
        super().__init__()
        self.board = board
        self.ships = ships_list
        self.__locate_ships()
        return
    
    def __init__(self, board, ships_list, mortars_list, player_a, player_b):
        super().__init__()
        self.board = board
        self.ships = ships_list
        self.mortars = mortars_list
        self.player_a = player_a
        self.player_b = player_b
        self.player_a.setBarcos(ships_list)
        self.player_b.setMorteros(mortars_list)
        self.__locate_ships()
        self.stop = False
        self.number_of_dead_ships = 0
        self.numbers_of_shift = 0
        return
    
    def notify(self):
        self.number_of_dead_ships += 1
        
    def __next(self):
        if self.cantTurnos%2 == 0:
            self.jugadorActual = self.jugadorA
        else:
            self.jugadorActual = self.jugadorB
        self.cantTurnos+=1
          
    def iniciar(self):
        self.ejecucion = Thread(target=__iniciar)
        self.ejecucion.start()
        
    def __iniciar(self):
        while not self.stop and cantBarcosMuertos != len(self.ships):
            self.__next()
            jugada = jugadorActual.getJugada()
            jugada.ejecutar()
    
    def detener(self):
        self.stop = True
        self.ejecucion.join(10)