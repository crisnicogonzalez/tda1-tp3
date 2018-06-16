from juegoException import JuegoException
from observer import Observer
class Tablero(Observer):
    
    def __init__(self,cols,rows):
        self.posiciones = [[None for i in range(rows)] for j in range(cols)]
        self.columnas = cols
        self.filas = rows
    
    def insertar(self,item,col,row):
        if(col >= self.columnas or row >= self.filas):
            raise JuegoException("Posicion ("+str(col)+","+str(row)+") fuera del tablero.")
        self.posiciones[col][row] = item
        item.setPosX(col)
        item.setPosY(row)
    
    def remover(self,col,row):
        if(col >= self.columnas or row >= self.filas):
            raise JuegoException("Posicion ("+str(col)+","+str(row)+") fuera del tablero.")
        self.posiciones[col][row] = None
        
    def ver(self,col,row):
        if(col >= self.columnas or row >= self.filas):
            raise JuegoException("Posicion ("+str(col)+","+str(row)+") fuera del tablero.")
        return self.posiciones[col][row]
    
    def notify(self,barco,xInicial,yInicial,xFinal,yFinal):
        self.insertar(barco,xFinal%self.columnas,yFinal%self.filas)
        self.remover(xInicial, yInicial)