from src.exception.juegoException import JuegoException
import logging

FORMAT = "%(class)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
log_info = {'class': 'Board'}


class Board:
    def __init__(self, cols, rows):
        super().__init__()
        self.positions = [[None for i in range(cols)] for j in range(rows)]
        self.columns = cols
        self.rows = rows

    def print(self):
        matrix = '\n'.join([''.join(['{} '.format(int(item is not None)) for item in row])
                         for row in self.positions])
        logging.debug('\n{}'.format(matrix), extra=log_info)

    def insert_item_in_position(self, item, row, col):
        self.positions[row][col % self.columns] = item
        item.set_column(col % self.columns)
        item.set_row(row)
    
    def remove_from_position(self, col, row):
        if col >= self.columns or row >= self.rows:
            raise JuegoException("Posicion ("+str(col)+","+str(row)+") fuera del tablero.")
        self.positions[col][row] = None
        
    def get_item_from_position(self, col, row):
        if col >= self.columns or row >= self.rows:
            raise JuegoException("Posicion ("+str(col)+","+str(row)+") fuera del tablero.")
        return self.positions[row][col]
    
    def notify(self, ship, initial_x, initial_y, final_x, final_y):
        self.insert_item_in_position(ship, final_x % self.columns, final_y % self.rows)
        self.remove_from_position(initial_x, initial_y)