class gearCard:
    def __init__(self,name):
        name = self.name

class duneBlaster(gearCard):
    def __init__(self,name):
        super().__init__(name)
    
    def clearSand(self,tile):
        tile.sand = 0

class jetpack(gearCard):
    def __init__(self,name):
        super().__init__(name)

    def move(self,player,tile):
        if tile.sand < 2:
            player.location[0] = tile.x
            player.location[1] = tile.y

class secretWaterReserve(gearCard):
    def __init__(self,name):
        super().__init__(name)
    
    def use(self,host,players):
        for player in players:
            if player.location == host.location:
                player.water = player.water + 2

class solarShield(gearCard):
    def __init__(self,name):
        super().__init__(name)
    
    def use(self,player):
        player.water = player.water # I don't know how to implement this

class terrascope(gearCard):
    def __init__(self,name):
        super().__init__(name)
    
    def peek(self,tile):
        # Show the tile using tkinter or something
        print(tile.type) # Replace with tkinter equivalent

class timeThrottle(gearCard):
    def __init__(self,name):
        super().__init__(name)
    
    def use(self,actionsLeft):
        actionsLeft = actionsLeft + 2