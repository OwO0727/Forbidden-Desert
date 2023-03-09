import random

class gearCard:
    def __init__(self,images):
        self.images = images

class duneBlaster(gearCard):
    def __init__(self,images):
        super().__init__(images)
    
    def clearSand(self,tile):
        tile.sand = 0

class jetpack(gearCard):
    def __init__(self,images):
        super().__init__(images)

    def move(self,player,tile):
        if tile.sand < 2:
            player.location[0] = tile.x
            player.location[1] = tile.y

class secretWaterReserve(gearCard):
    def __init__(self,images):
        super().__init__(images)
    
    def use(self,host,players):
        for player in players:
            if player.location == host.location:
                player.water = player.water + 2

class solarShield(gearCard):
    def __init__(self,images):
        super().__init__(images)
    
    def use(self,player):
        player.water = player.water # I don't know how to implement this

class terrascope(gearCard):
    def __init__(self,images):
        super().__init__(images)
    
    def peek(self,tile):
        # Show the tile using tkinter or something
        print(tile.type) # Replace with tkinter equivalent

class timeThrottle(gearCard):
    def __init__(self,images):
        super().__init__(images)
    
    def use(self,actionsLeft):
        actionsLeft = actionsLeft + 2

# 3 dune blasters
# 3 jet packs
# 1 secret water reserve
# 2 solar shields
# 2 terrascopes
# 1 time throttle
pile = []
for i in range(3):
    pile.append(duneBlaster(("./img/Equipments/duneBlasterImage.png", "./img/Equipments/haveDuneBlasterImage.png", "./img/Equipments/noDuneBlasterImage.png")))
for i in range(3):
    pile.append(jetpack(("./img/Equipments/jetPackImage.png", "./img/Equipments/haveJetPackImage.png", "./img/Equipments/noJetPackImage.png")))
pile.append(secretWaterReserve(("./img/Equipments/secretWaterReserveImage.png", "./img/Equipments/haveSecretWaterReserveImage.png", "./img/Equipments/noSecretWaterReserveImage.png")))
for i in range(2):
    pile.append(solarShield(("./img/Equipments/solarShieldImage.png", "./img/Equipments/haveSolarShieldImage.png", "./img/Equipments/noSolarShieldImage.png")))
for i in range(2):
    pile.append(terrascope(("./img/Equipments/terrascopeImage.png", "./img/Equipments/haveTerrascopeImage.png", "./img/Equipments/noTerrascopeImage.png")))
pile.append(timeThrottle(("./img/Equipments/timeThrottleImage.png", "./img/Equipments/haveTimeThrottleImage.png", "./img/Equipments/noTimeThrottleImage.png")))

random.shuffle(pile)
