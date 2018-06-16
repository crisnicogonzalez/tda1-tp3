from src.exception.juegoException import JuegoException
from .observer import Observable


class Board(Observable):

    def __init__(self, cols, rows):
        super().__init__()
        self.positions = [[None for i in range(rows)] for j in range(cols)]
        self.columns = cols
        self.rows = rows
    
    def insert_item_in_position(self, item, col, row):
        if col >= self.columns or row >= self.rows:
            raise JuegoException("Posicion ("+str(col)+","+str(row)+") fuera del tablero.")
        self.positions[col][row] = item
        item.set_pos_x(col)
        item.set_pos_y(row)
    
    def remove_from_position(self, col, row):
        if col >= self.columns or row >= self.rows:
            raise JuegoException("Posicion ("+str(col)+","+str(row)+") fuera del tablero.")
        self.positions[col][row] = None
        
    def get_item_from_position(self, col, row):
        if col >= self.columns or row >= self.rows :
            raise JuegoException("Posicion ("+str(col)+","+str(row)+") fuera del tablero.")
        return self.positions[col][row]
    
    def notify(self, ship, initial_x, initial_y, final_x, final_y):
        self.insert_item_in_position(ship, final_x % self.columns, final_y % self.rows)
        self.remove_from_position(initial_x, initial_y)