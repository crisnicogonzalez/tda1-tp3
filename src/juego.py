from barco import Barco
from tablero import Tablero
from observer import Observer
from threading import *

class Juego(Observer):
    
    def __ubicarBarcos(self):
        i = 0
        for barco in self.barcos:
            barco.register_observer(self.tablero)
            barco.register_observer(self)
            self.tablero.insertar(barco,0,i)
            i += 1
        
    def __init__(self,cols,rows,cantBarcos,cantMorteros):
        super().__init__()
        self.tablero = Tablero(cols,rows)
        self.barcos = [Barco(100) for _ in range(cantBarcos)]
        self.__ubicarBarcos() 
        return
        
    def __init__(self,tablero,listaBarcos,cantMorteros):
        super().__init__()
        self.tablero = tablero
        self.barcos = listaBarcos
        self.__ubicarBarcos()
        return
    
    def __init__(self,tablero,listaBarcos,listaMorteros,jugadorA,jugadorB):
        super().__init__()
        self.tablero = tablero
        self.barcos = listaBarcos
        self.morteros = listaMorteros
        self.jugadorA = jugadorA
        self.jugadorB = jugadorB
        self.jugadorA.setBarcos(listaBarcos)
        self.jugadorB.setMorteros(listaMorteros)
        self.__ubicarBarcos()
        self.detener = False
        self.cantBarcosMuertos = 0
        self.cantTurnos = 0
        return
    
    def notify(self):
        self.cantBarcosMuertos += 1
        
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
        while not self.detener and cantBarcosMuertos != len(self.barcos):
            self.__next()
            jugada = jugadorActual.getJugada()
            jugada.ejecutar()
    
    def detener(self):
        self.detener = True
        self.ejecucion.join(10)