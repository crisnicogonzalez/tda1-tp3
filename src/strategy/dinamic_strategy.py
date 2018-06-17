from src.utils.quicksort import quicksort


class DynamicStrategy:
    def __init__(self, game=None, damage_table=None, shooters=None):
        self.game = game
        self.known_states = {}
        self.damage_table = damage_table
        self.shooters = shooters
        self.game_manager = game

    def step(self, column):
        if column in self.known_states:
            return self.known_states[column]
        else:
            priority_list = quicksort(self.damage_table[column])
            self.known_states[column] = priority_list
        return priority_list

    def execute(self):
        index = self.game.get_current_column()
        priority_list = self.step(index)
        for i in range(self.shooters):
            index_priority = 0
            ship_position = priority_list[index_priority]
            while not self.attack(ship_position):
                index_priority += 1
            self.known_states[index] = priority_list[index_priority:]

    def attack(self, ship_position):
        if self.game.ship_of_position_is_alive(ship_position):
            self.game.attack_to_position(ship_position)
            return True
        else:
            return False

    def set_game_manager(self, game_manager):
        self.game_manager = game_manager
