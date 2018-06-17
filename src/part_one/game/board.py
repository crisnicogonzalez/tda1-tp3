import logging

log_info = {'class': 'Board'}

class Board:
    def __init__(self, rows, cols):
        super().__init__()
        self.positions = [[None for i in range(cols)] for j in range(rows)]
        self.columns = cols
        self.rows = rows

    def print(self):
        matrix = '\n'.join([''.join(['{} '.format(int(item is not None)) for item in row])
                         for row in self.positions])
        logging.debug('\n{}'.format(matrix), extra=log_info)

    def insert_item_in_position(self, item, row, col):
        logging.debug('cantidad de columnas={} col {}=nueva posicion={} row={}'.format(self.columns,col,col % self.columns,row), extra=log_info)
        logging.debug('self.positions[{}][{}] '.format(row, col%self.columns), extra=log_info)
        self.positions[row][col % self.columns] = item
        item.set_column(col % self.columns)
        item.set_row(row)
    
    def remove_from_position(self, row, col):
        self.positions[row][col%self.columns] = None
        
    def get_item_from_position(self, row, col):
        return self.positions[row][col%self.columns]
    
    def notify(self, ship, initial_x, initial_y, final_x, final_y):
        self.insert_item_in_position(ship, final_x % self.columns, final_y % self.rows)
        self.remove_from_position(initial_x, initial_y)