class player:
    def __init__(self, name, water, position):
        name = self.name
        water = self.water
        position = self.position
    
    def move(self,tile):
        position = tile
    
    def clearSand(self,tile):
        tile.sand = tile.sand - 1
        return tile
    
    def excavate(self,tile):
        tile.excavated = True
        return tile
    
    def pickUpPart(self,part):
        part.collected = True
        return part

class archeologist(player):
    def __init__(self, name, water, position):
        super().__init__(name, water, position)

    def clearSand(self, tile):
        if tile.sand > 0:
            if tile.sand == 1:
                tile.sand = tile.sand - 1
            else:
                tile.sand = tile.sand - 2


class climber(player):
    def __init__(self, name, water, position, ally):
        super().__init__(name, water, position)
        ally = self.ally

    def carryPlayer(self,player):
        if player.position == self.position:
            ally = player
    
    def dropPlayer(self,player):
        ally = ""



class explorer(player):
    def __init__(self, name, water, position):
        super().__init__(name, water, position)

    def diagonal(self, tile):
        pass

class meteorologist(player):
    def __init__(self, name, water, position):
        super().__init__(name, water, position)
        
    def movestormcard(self, card):
        pass

    def drawLessCards(self, cardnum):
        pass

class navigator(player):
    def __init__(self, name, water, position):
        super().__init__(name, water, position)
        
    def movePlayer(self, tile):
        pass

class water_carrier(player):
    def __init__(self, name, water, position):
        super().__init__(name, water, position)
        
    def take2water(self, tile):
        if tile.type == "water":
            self.water = self.water + 2
    def giveWater(self, player):
        player.water = player.water + 1
        self.water = self.water - 1
