

class player:
    def __init__(self, name, water, position, cards):
        self.name = name
        self.water = water
        self.position = position
        self.cards = cards
    
    def move(self,tile):
        self.position[0] = tile.x
        self.position[1] = tile.y
    
    def clearSand(self,tile):
        tile["sand_markers"] -= 1
        return tile
    
    def excavate(self,tile):
        tile.excavated = True
        return tile
    
    def Pick_Up_Part(self,part):
        part.collected = True
        return part

    def getMethods(self):
        m=[method for method in dir(self) if callable(getattr(self, method)) and method[0:2]!="__" and method!="getMethods"]
    
    #def timeThrottle(self):
    #    if 

class archeologist(player):
    def __init__(self, name, water, position, cards):
        super().__init__(name, water, position, cards)

    def clearSand(self, tile):
        if tile.sand > 0:
            if tile.sand == 1:
                tile.sand = tile.sand - 1
            else:
                tile.sand = tile.sand - 2


class climber(player):
    def __init__(self, name, water, position, cards, ally):
        super().__init__(name, water, position, cards)
        self.ally = ally
    
    def carryPlayer(self,player):
        if player.position == self.position:
            ally = player
    
    def dropPlayer(self,player):
        ally = None
    
    def move(self,tile):
        if (self.ally).position != self.position:
            self.dropPlayer()
        self.position[0] = tile.x
        self.position[1] = tile.y
        if self.ally != None:
            (self.ally).move(tile)



class explorer(player):
    def __init__(self, name, water, position, cards):
        super().__init__(name, water, position, cards)

    def diagonal(self, tile):
        pass

class meteorologist(player):
    def __init__(self, name, water, position, cards):
        super().__init__(name, water, position, cards)
        
    def movestormcard(self, card):
        pass

    def drawLessCards(self, cardnum):
        pass

class navigator(player):
    def __init__(self, name, water, position, cards):
        super().__init__(name, water, position, cards)
        
    def movePlayer(self, tile):
        pass

class waterCarrier(player):
    def __init__(self, name, water, position, cards):
        super().__init__(name, water, position, cards)
        
    def take2water(self, tile):
        if tile.type == "water":
            self.water = self.water + 2
    def giveWater(self, player):
        player.water = player.water + 1
        self.water = self.water - 1

playerTypeDict = {
    "Archeologist" : archeologist("A",3,[0,0],[]),
    "Climber" : climber("B",3,[0,0],[],None),
    "Explorer" : explorer("C",4,[0,0],[]),
    "Meteorologist" : meteorologist("D",4,[0,0],[]),
    "Navigator" : navigator("E",4,[0,0],[]),
    "Water Carrier" : waterCarrier("F",5,[0,0],[])
    }
