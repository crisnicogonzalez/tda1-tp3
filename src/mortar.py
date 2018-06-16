class Mortar:
    def __init__(self, matrizDeDanios):
        self.matrizDeDanios = matrizDeDanios
        
    def attack(self, ship):
        ship.set_life_points(ship.get_life_points() - self.matrizDeDanios[ship.get_pos_x()][ship.get_pos_y()])