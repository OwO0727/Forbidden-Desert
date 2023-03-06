class player:
    def __init__(self, name, water, position, cards):
        name = self.name
        water = self.water
        position = self.position
        cards = self.cards
    
    def move(self,tile):
        self.position[0] = tile.x
        self.position[1] = tile.y
    
    def clearSand(self,tile):
        tile.sand = tile.sand - 1
        return tile
    
    def excavate(self,tile):
        tile.excavated = True
        return tile
    
    def pickUpPart(self,part):
        part.collected = True
        return part
    
    def timeThrottle(self):
        if 

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
        ally = self.ally
    
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

player1 = archeologist("A",3,[0,0],[])
player2 = climber("B",3,[0,0],[],None)
player3 = explorer("C",4,[0,0],[])
player4 = meteorologist("D",4,[0,0],[])
player5 = navigator("E",4,[0,0],[])
player6 = waterCarrier("F",5,[0,0],[])

player2.ally = player1
