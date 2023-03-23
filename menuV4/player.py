class player:
    def __init__(self, image, water, position, cards, protected, ability):
        self.image = image
        self.water = water
        self.position = position
        self.cards = cards
        self.protected = protected
        self.ability = ability

    def move(self,column,row):
        self.position[0] = column
        self.position[1] = row

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

class archeologist(player):
    def __init__(self, image, water, position, cards, protected, ability):
        super().__init__(image, water, position, cards, protected, ability)

    def clearSand(self, tile): # Clear 2 sand from 1 tile per action
        if tile['sand_markers'] > 0:
            if tile['sand_markers'] == 1:
                tile['sand_markers'] = tile['sand_markers'] - 1
            else:
                tile['sand_markers'] = tile['sand_markers'] - 2

class climber(player):
    def __init__(self, image, water, position, cards, protected, ability, ally):
        super().__init__(image, water, position, cards, protected, ability)
        self.ally = ally
    
    def carryPlayer(self,player): # You may take 1 other player with you when you move
        if player.position == self.position:
            self.ally = player
    
    def dropPlayer(self,player):
        self.ally = None
    
    def move(self,column,row):
        if (self.ally).position != self.position:
            self.dropPlayer()
        self.position[0] = column
        self.position[1] = row
        if self.ally != None:
            (self.ally).move(column,row)

class explorer(player):
    def __init__(self, image, water, position, cards, protected, ability):
        super().__init__(image, water, position, cards, protected, ability)

class meteorologist(player):
    def __init__(self, image, water, position, cards, protected, ability):
        super().__init__(image, water, position, cards, protected, ability)
        
    def movestormcard(self, stormPile, cardnum, actionsLeft): # Spend 1 action to look at storm cards equivalent to storm level
        for i in range(cardnum):
            print(stormPile[i]) # Replace with tkinter equivalent
        # Code needed to look at all the top cards
        # Player must be able to choose a card and move it to the bottom of the pile if they want to
        x = 2 # Example card index
        temp = stormPile[x]
        stormPile.remove(stormPile[x]) # Optionally
        stormPile.append(temp)
        actionsLeft = actionsLeft - 1
        return stormPile, actionsLeft

    def drawLessCards(self, cardnum, actionsLeft): # Spend 1 action to draw fewer storm cards
        cardnum = cardnum - 1
        actionsLeft = actionsLeft - 1
        return cardnum, actionsLeft

class navigator(player):
    def __init__(self, image, water, position, cards, protected, ability):
        super().__init__(image, water, position, cards, protected, ability)
        
    def movePlayer(self, player, column,row): # Move another player up to three unblocked tiles per action
        player.position = [column,row] # The explorer and climber may be moved according to their special abilities
        return player

class waterCarrier(player):
    def __init__(self, image, water, position, cards, protected, ability):
        super().__init__(image, water, position, cards, protected, ability)
        
    def take2water(self, tile): # Take 2 water from excavated tiles for 1 action
        if tile.type == "water":
            self.water = self.water + 2
    def giveWater(self, player): # Give water to players on adjacent tiles for 1 action
        player.water = player.water + 1
        self.water = self.water - 1
        return player

playerTypeDict = {
    "Archeologist" : archeologist("./img/Players/archeologistImage.png",3,[0,0],[],False,None),
    "Climber" : climber("./img/Players/climberImage.png",3,[0,0],[],False,"can move on blocked tiles",None), # The climber and other players on the same tile can't be buried
    "Explorer" : explorer("./img/Players/explorerImage.png",4,[0,0],[],False,"can move and influence tiles diagonally"), # The explorer can move, clear sand and use dune blasters diagonally
    "Meteorologist" : meteorologist("./img/Players/meteorologistImage.png",4,[0,0],[],False,None),
    "Navigator" : ("./img/Players/navigatorImage.png",4,[0,0],[],False,None),
    "Water Carrier" : waterCarrier("./img/Players/waterCarrierImage.png",5,[0,0],[],False,None)
    }