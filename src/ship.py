from .observer import Observable


class Ship(Observable):
    
    def __init__(self, initial_life_points):
        super().__init__()
        self.posX = None
        self.posY = None
        self.life_points = initial_life_points
        
    def get_pos_x(self):
        return self.posX
    
    def set_pos_x(self, pos):
        self.posX = pos
        
    def get_pos_y(self):
        return self.posY
    
    def set_pos_y(self, pos):
        self.posY = pos
        
    def get_life_points(self):
        return self.life_points
    
    def set_life_points(self, vida):
        self.life_points = vida
    
    def is_dead(self):
        return self.life_points <= 0
        
    def advance_to_new_position(self):
        initial_x = self.posX
        initial_y = self.posY
        self.posX = initial_x + 1
        self.notify_observers(initial_x, initial_y, initial_x+1, initial_y)