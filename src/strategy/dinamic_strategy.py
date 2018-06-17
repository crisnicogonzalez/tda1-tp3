
class DinamicStrategy():
    def __init__(self, game=None, damage_table=None, shooters=None):
        self.game = game
        self.known_states = {}
        self.damage_table = damage_table
        self.shooters = shooters
        self.game_manager = game

    def step(self,state):
        priority_list = []
        if state in self.known_states:
            return self.known_states[state]
        else:
            priority_list = self.order_by_max_damage(self.damage_table[state])
            self.known_states[state] = priority_list
        return priority_list

    def order_by_max_damage(self,list):
        return list
    
    def pop_first_from(self,list):
        return list[0]

    def execute(self):
        index = self.game.get_current_column()
        priority_list = self.step(index)
        for i in range(self.shooters):
            ship_position = priority_list.pop()
            if self.game.ship_of_position_is_alive(ship_position):
                self.game.attack_to_position(ship_position)

    def set_game_manager(self, game_manager):
        self.game_manager = game_manager
