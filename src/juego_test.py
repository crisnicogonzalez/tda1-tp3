import unittest
from barco import Barco
from tablero import Tablero
from juegoException import JuegoException
from juego import Juego
class JuegoTest (unittest.TestCase):
    
    def test_insertar_barco_dentro_del_tablero_cuadrado_queda_bien_posicionado(self):
        titanic = Barco(100)
        oceano = Tablero(10,10)
        oceano.insertar(titanic,0,0)
        self.assertEqual(oceano.ver(0,0), titanic, "En la posicion 0,0 no se ve el barco")
        self.assertEqual(titanic.getPosX(), 0, "Posicion X no es 0")
        self.assertEqual(titanic.getPosY(), 0, "Posicion Y no es 0")
        
    def test_insertar_barco_dentro_del_borde_del_tablero_rectangular_queda_bien_posicionado(self):
        titanic = Barco(100)
        oceano = Tablero(10,20)
        oceano.insertar(titanic,9,2)
        self.assertEqual(oceano.ver(9,2), titanic, "En la posicion 9,2 no se ve el barco")
        self.assertEqual(titanic.getPosX(), 9, "Posicion X no es 9")
        self.assertEqual(titanic.getPosY(), 2, "Posicion Y no es 2")
        oceano.insertar(titanic,5,19)
        self.assertEqual(oceano.ver(5,19), titanic, "En la posicion 5,19 no se ve el barco")
        self.assertEqual(titanic.getPosX(), 5, "Posicion X no es 5")
        self.assertEqual(titanic.getPosY(), 19, "Posicion Y no es 19")
        
    def test_insertar_barco_fuera_del_tablero_falla_y_no_modifica_el_barco(self):
        titanic = Barco(100)
        oceano = Tablero(10,10)
        with self.assertRaises(JuegoException):
            oceano.insertar(titanic,15,2)
        self.assertEqual(titanic.getPosX(), None, "Posicion X no es nula")
        self.assertEqual(titanic.getPosY(), None, "Posicion Y no es nula")
        
    def test_ver_posicion_fuera_del_tablero_falla(self):
        oceano = Tablero(10,10)
        with self.assertRaises(JuegoException):
            oceano.ver(15,2)
    
    def test_crear_juego_ubica_los_barcos_en_el_tablero(self):
        titanic = Barco(100)
        santamaria = Barco(50)
        oceano = Tablero(10,10)
        juego = Juego(oceano,[titanic,santamaria],1)
        self.assertNotEqual(titanic.getPosX(), None, "Posicion X no fue seteada")
        self.assertNotEqual(titanic.getPosY(), None, "Posicion Y no fue seteada")
        self.assertEqual(oceano.ver(titanic.getPosX(),titanic.getPosY()), titanic, "El barco no se ubico en el tablero")
        self.assertNotEqual(santamaria.getPosX(), None, "Posicion X no fue seteada")
        self.assertNotEqual(santamaria.getPosY(), None, "Posicion Y no fue seteada")
        self.assertEqual(oceano.ver(santamaria.getPosX(),santamaria.getPosY()), santamaria, "El barco no se ubico en el tablero")
        
    def test_crear_juego_poner_barco_y_hacerlo_avanzar_actualiza_la_posicion_del_barco_y_tablero(self):
        titanic = Barco(100)
        oceano = Tablero(10,10)
        juego = Juego(oceano,[titanic],1)
        xInicial = titanic.getPosX()
        yInicial = titanic.getPosY()
        titanic.avanzar()
        self.assertEqual(titanic.getPosX(), xInicial + 1, "La posicion del barco en x no se modifico")
        self.assertEqual(titanic.getPosY(), yInicial, "La posicion del barco en y se modifico")
        self.assertEqual(oceano.ver(xInicial,yInicial), None, "El barco sigue en su posicion original")
        self.assertEqual(oceano.ver(xInicial + 1,yInicial), titanic, "El barco no avanzo en el tablero")
        
