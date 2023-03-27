

class player:
    def __init__(self, name, water, position, cards):
        self.name = name
        self.water = water
        self.position = position
        self.cards = cards

    #!OBSELETE
    def _move(self,tile):
        self.position[0] = tile.x
        self.position[1] = tile.y
    
    #!OBSELETE
    def _clearSand(self,tile):
        tile["sand_markers"] -= 1
        return tile
    
    #!OBSELETE
    def _excavate(self,tile):
        tile["excavate"] = True
        return tile
    
    #!OBSELETE
    def _Pick_Up_Part(self,part):
        part.collected = True
        return part

    #!USELESS
    def _getMethods(self):
        m=[method for method in dir(self) if callable(getattr(self, method)) and method[0:2]!="__" and method!="getMethods"]
    
    #def timeThrottle(self):
    #    if 

class archeologist(player):
    def __init__(self, name, water, position, cards):
        super().__init__(name, water, position, cards)

    def clearSand(self, tile):
        if tile["sand_markers"] > 0:
            if tile["sand_markers"] == 1:
                tile["sand_markers"] = tile["sand_markers"] - 1
            else:
                tile["sand_markers"] = tile["sand_markers"] - 2


class climber(player):
    def __init__(self, name, water, position, cards, ally):
        super().__init__(name, water, position, cards)
        self.ally = ally
    
    def carryPlayer(self,player):
        if player.position == self.position:
            ally = player
    
    def dropPlayer(self,player):
        ally = None
    
    def _move(self,tile):
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
        
    def _movestormcard(self, card):
        pass

    def _drawLessCards(self, cardnum):
        pass

class navigator(player):
    def __init__(self, name, water, position, cards):
        super().__init__(name, water, position, cards)
        
    def _movePlayer(self, tile):
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
