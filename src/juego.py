from barco import Barco
from tablero import Tablero

class Juego:
    
    def __ubicarBarcos(self):
        i = 0
        for barco in self.barcos:
            barco.register_observer(self.tablero)
            self.tablero.insertar(barco,0,i)
            i += 1
        
    def __init__(self,cols,rows,cantBarcos,cantMorteros):
        self.tablero = Tablero(cols,rows)
        self.barcos = [Barco(100) for _ in range(cantBarcos)]
        self.__ubicarBarcos() 
        return
        
    def __init__(self,tablero,listaBarcos,cantMorteros):
        self.tablero = tablero
        self.barcos = listaBarcos
        self.__ubicarBarcos()
        return