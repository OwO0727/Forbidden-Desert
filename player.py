class player:
    def __init__(self, image, water, position, cards, protected, ability):
        self.image = image
        self.water = water
        self.position = position
        self.cards = cards
        self.protected = protected
        self.ability = ability
    
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

class archeologist(player):
    def __init__(self, image, water, position, cards, protected, ability):
        super().__init__(image, water, position, cards, protected, ability)

    def clearSand(self, tile): # Clear 2 sand from 1 tile per action
        if tile.sand > 0:
            if tile.sand == 1:
                tile.sand = tile.sand - 1
            else:
                tile.sand = tile.sand - 2


class climber(player):
    def __init__(self, image, water, position, cards, protected, ability, ally):
        super().__init__(image, water, position, cards, protected, ability)
        self.ally = ally
    
    def carryPlayer(self,player): # You may take 1 other player with you when you move
        if player.position == self.position:
            self.ally = player
    
    def dropPlayer(self,player):
        self.ally = None
    
    def move(self,tile):
        if (self.ally).position != self.position:
            self.dropPlayer()
        self.position[0] = tile.x
        self.position[1] = tile.y
        if self.ally != None:
            (self.ally).move(tile)



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
        # Player must be able to choose a card and move it to the bottom of the pile
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
        
    def movePlayer(self, player, tile): # Move another player up to three unblocked tiles per action
        player.location = [tile.x,tile.y]
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

player1 = archeologist("./img/Players/archeologistImage.png",3,[0,0],[],False,None)
player2 = climber("./img/Players/climberImage.png",3,[0,0],[],False,False,"can move on blocked tiles") # The climber and other players on the same tile can't be buried
player3 = explorer("./img/Players/explorerImage.png",4,[0,0],[],False,"can move and influence tiles diagonally") # The explorer can move, clear sand and use dune blasters diagonally
player4 = meteorologist("./img/Players/meteorologistImage.png",4,[0,0],[],False,None)
player5 = navigator("./img/Players/navigatorImage.png",4,[0,0],[],False,None)
player6 = waterCarrier("./img/Players/waterCarrierImage.png",5,[0,0],[],False,None)
