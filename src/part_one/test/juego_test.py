import unittest
from barco import Barco
from tablero import Tablero
from juegoException import JuegoException
from juego import Juego
from mortero import Mortero
class JuegoTest (unittest.TestCase):
    
    def test_insertar_barco_dentro_del_tablero_cuadrado_queda_bien_posicionado(self):
        titanic = Barco(100)
        oceano = Tablero(10,10)
        oceano.insert_item_in_position(titanic, 0, 0)
        self.assertEqual(oceano.get_item_from_position(0, 0), titanic, "En la posicion 0,0 no se ve el barco")
        self.assertEqual(titanic.get_column(), 0, "Posicion X no es 0")
        self.assertEqual(titanic.get_row(), 0, "Posicion Y no es 0")
        
    def test_insertar_barco_dentro_del_borde_del_tablero_rectangular_queda_bien_posicionado(self):
        titanic = Barco(100)
        oceano = Tablero(10,20)
        oceano.insert_item_in_position(titanic, 9, 2)
        self.assertEqual(oceano.get_item_from_position(9, 2), titanic, "En la posicion 9,2 no se ve el barco")
        self.assertEqual(titanic.get_column(), 9, "Posicion X no es 9")
        self.assertEqual(titanic.get_row(), 2, "Posicion Y no es 2")
        oceano.insert_item_in_position(titanic, 5, 19)
        self.assertEqual(oceano.get_item_from_position(5, 19), titanic, "En la posicion 5,19 no se ve el barco")
        self.assertEqual(titanic.get_column(), 5, "Posicion X no es 5")
        self.assertEqual(titanic.get_row(), 19, "Posicion Y no es 19")
        
    def test_insertar_barco_fuera_del_tablero_falla_y_no_modifica_el_barco(self):
        titanic = Barco(100)
        oceano = Tablero(10,10)
        with self.assertRaises(JuegoException):
            oceano.insert_item_in_position(titanic, 15, 2)
        self.assertEqual(titanic.get_column(), None, "Posicion X no es nula")
        self.assertEqual(titanic.get_row(), None, "Posicion Y no es nula")
        
    def test_ver_posicion_fuera_del_tablero_falla(self):
        oceano = Tablero(10,10)
        with self.assertRaises(JuegoException):
            oceano.get_item_from_position(15, 2)
    
    def test_crear_juego_ubica_los_barcos_en_el_tablero(self):
        titanic = Barco(100)
        santamaria = Barco(50)
        oceano = Tablero(10,10)
        juego = Juego(oceano,[titanic,santamaria],1)
        self.assertNotEqual(titanic.get_column(), None, "Posicion X no fue seteada")
        self.assertNotEqual(titanic.get_row(), None, "Posicion Y no fue seteada")
        self.assertEqual(oceano.get_item_from_position(titanic.get_column(), titanic.get_row()), titanic, "El barco no se ubico en el tablero")
        self.assertNotEqual(santamaria.get_column(), None, "Posicion X no fue seteada")
        self.assertNotEqual(santamaria.get_row(), None, "Posicion Y no fue seteada")
        self.assertEqual(oceano.get_item_from_position(santamaria.get_column(), santamaria.get_row()), santamaria, "El barco no se ubico en el tablero")
        
    def test_crear_juego_poner_barco_y_hacerlo_avanzar_actualiza_la_posicion_del_barco_y_tablero(self):
        titanic = Barco(100)
        oceano = Tablero(10,10)
        juego = Juego(oceano,[titanic],1)
        xInicial = titanic.get_column()
        yInicial = titanic.get_row()
        titanic.advance_to_new_position()
        self.assertEqual(titanic.get_column(), xInicial + 1, "La posicion del barco en x no se modifico")
        self.assertEqual(titanic.get_row(), yInicial, "La posicion del barco en y se modifico")
        self.assertEqual(oceano.get_item_from_position(xInicial, yInicial), None, "El barco sigue en su posicion original")
        self.assertEqual(oceano.get_item_from_position(xInicial + 1, yInicial), titanic, "El barco no avanzo en el tablero")
    
    def test_mortero_ataca_a_barco_y_le_saca_vida(self):
        titanic = Barco(100)
        mortero = Mortero([[40,40,40,40,40],[40,40,40,40,40],[40,40,40,40,40],[40,40,40,40,40],[40,40,40,40,40]])
        oceano = Tablero(5,5)
        juego = Juego(oceano,[titanic],[mortero])
        mortero.attack(titanic)
        self.assertEqual(titanic.get_life_points(), 60, "El barco no perdio vida")
    
    def test_barco_avanza_y_el_mortero_lo_va_atacando_hasta_destruirlo(self):    
        titanic = Barco(100)
        mortero = Mortero([[40,40,40,40,40],[30,30,30,30,30],[20,20,20,20,20],[15,15,15,15,15],[40,40,40,40,40]])
        oceano = Tablero(5,5)
        juego = Juego(oceano,[titanic],[mortero])
        mortero.attack(titanic)
        self.assertEqual(titanic.get_life_points(), 60, "El barco no perdio vida")
        titanic.advance_to_new_position()
        mortero.attack(titanic)
        self.assertEqual(titanic.get_life_points(), 30, "El barco no perdio vida")
        titanic.advance_to_new_position()
        mortero.attack(titanic)
        self.assertEqual(titanic.get_life_points(), 10, "El barco no perdio vida")
        titanic.advance_to_new_position()
        mortero.attack(titanic)
        self.assertTrue(titanic.is_dead(), "El barco no murio")
                
    def test_barco_avanza_hasta_el_final_y_da_la_vuelta(self):
        titanic = Barco(100)
        oceano = Tablero(3,3)
        juego = Juego(oceano,[titanic],1)
        xInicial = titanic.get_column()
        yInicial = titanic.get_row()
        titanic.advance_to_new_position()
        self.assertEqual(titanic.get_column(), xInicial + 1, "La posicion del barco en x no se modifico")
        self.assertEqual(oceano.get_item_from_position(xInicial + 1, yInicial), titanic, "El barco no avanzo en el tablero")
        titanic.advance_to_new_position()
        self.assertEqual(titanic.get_column(), xInicial + 2, "La posicion del barco en x no se modifico")
        self.assertEqual(oceano.get_item_from_position(xInicial + 2, yInicial), titanic, "El barco no avanzo en el tablero")
        titanic.advance_to_new_position()
        self.assertEqual(titanic.get_column(), xInicial, "El barco no dio la vuelta")
        self.assertEqual(titanic.get_row(), yInicial, "La posicion del barco en y se modifico")
        self.assertEqual(oceano.get_item_from_position(xInicial, yInicial), titanic, "El barco no dio la vuelta en el tablero")
        self.assertEqual(oceano.get_item_from_position(xInicial + 2, yInicial), None, "El barco no se fue del final del tablero")
        
        
        
        
        
        
        
