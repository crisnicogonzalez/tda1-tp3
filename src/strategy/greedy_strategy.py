
class GreedyStrategy:
    def __init__(self, game_manager=None,number_of_shooters=0,damage_table=None,ships=None):
        self.game_manager=game_manager
        self.number_of_shooters = number_of_shooters
        self.damage_table = damage_table
        self.alive_ships = ships

    def execute(self):
        damage_by_ship = {}
        for alive_ship in self.alive_ships:
            current_damage = self.damage_table[alive_ship.get_row()][alive_ship.get_column()]
            damage_by_ship[alive_ship] = alive_ship.get_life_points() - current_damage
