class player:
    def __init__(self,name,water):
        name = self.name
        water = self.water

class archeologist(player):
    def __init__(self,name,water):
        super().__init__(name,water)
    
    def clear2sand(self,tile):
        
