#main
import tkinter as tk
import random
from PIL import Image, ImageTk

#!new------
import player as p
#!---------

#?######################################
#? NEW FILE ############################
#?######################################

import difficultySelect as d
import playerNumber as n
import playerSelect as p
import menu as m
import main as ggagag

import tkinter as tk

root=tk.Tk()
root.wm_title("Forbidden Island: Player Select")
menubg = tk.PhotoImage(master=root,file = "./img/Menu.png")
playerTypes=[
        {"name":"Archeologist","imageName":r"./img/Players/archeologistImage.png"},
        {"name":"Climber","imageName":r"./img/Players/climberImage.png"},
        {"name":"Explorer","imageName":r"./img/Players/explorerImage.png"},
        {"name":"Meteorologist","imageName":r"./img/Players/meteorologistImage.png"},
        {"name":"Navigator","imageName":r"./img/Players/navigatorImage.png"},
        {"name":"Water Carrier","imageName":r"./img/Players/waterCarrierImage.png"}
            ]
for type in playerTypes: type["img"]=tk.PhotoImage(file=type["imageName"])

def callD(): d.main(root, menubg, callN, callM)
def callS():
    num=n.playerNum
    p.main(root, menubg, playerTypes, startGame, num,callN)
def callN(): n.main(root, menubg, callS, callD)
def startGame():
    ggagag.main()
def callM(): m.main(root, menubg, callD)
m.gx=menubg
n.gx=menubg
d.gx=menubg
p.gx=menubg
callM()

root.mainloop()
stormLevel = d.stormLevel
playerCount = n.playerNum
players = p.playersg
print(f"{stormLevel}\n\n{playerCount}\n\n{players}")

#?######################################
#? NEW FILE ############################
#?######################################

class tiles:
    def __init__(self, back, front, sandnum):
        self.back = back
        self.front = front
        self.sandnum= sandnum

windowDims = (1280,720)
window = tk.Tk()
window.wm_title("Forbidden Desert: Game")
window.geometry(f"{windowDims[0]}x{windowDims[1]}")

player_pos = []

GAME_BOARD_SIZE = 5
STARTING_WATER = 3
MAX_WATER = 8
MAX_SAND = 12
WIN_TILE = "F"

tiles_initial= [ "backOfCardImage.png",
          "crashSiteImage.png", "launchPadImage.png",
          "engineColumnImage.png", "engineRowImage.png",
          "navigationDeckColumnImage.png", "navigationDeckRowImage.png",
          "propellerColumnImage.png", "propellerRowImage.png",
          "solarCrystalColumnImage.png", "solarCrystalRowImage.png",
          "gear1Image.png", "gear2Image.png",
          "gear3Image.png", "gear4Image.png",
          "gear5Image.png", "gear6Image.png",
          "gear7Image.png", "gear8Image.png",
          "sandMarkerImage.png", "highSandMarkerImage.png",
          "waterTileImage.png", "wellImage.png",
          "tunnelImage.png", "stormImage.png",
          "mirageImage.png"
   ]

tiles = ["img/Tiles/"+s for s in tiles_initial]

#setting special tiles
special_tiles=[
    
               {"tilename": "water1", "back":tiles[21], "front":tiles[22]},
               {"tilename": "water2", "back":tiles[21], "front":tiles[22]},
               {"tilename": "water3", "back":tiles[21], "front":tiles[25]},
               {"tilename": "a1", "back":tiles[0], "front":tiles[3]},
               {"tilename": "a2", "back":tiles[0], "front":tiles[4]},
               {"tilename": "b1", "back":tiles[0], "front":tiles[5]},
               {"tilename": "b2", "back":tiles[0], "front":tiles[6]},
               {"tilename": "c1", "back":tiles[0], "front":tiles[7]},
               {"tilename": "c2", "back":tiles[0], "front":tiles[8]},
               {"tilename": "d1", "back":tiles[0], "front":tiles[9]},
               {"tilename": "d2", "back":tiles[0], "front":tiles[10]},
               {"tilename": "tunnel1", "back":tiles[0], "front":tiles[23]},
               {"tilename": "runnel2", "back":tiles[0], "front":tiles[23]},
               {"tilename": "tunnel3", "back":tiles[0], "front":tiles[23]},
               {"tilename": "launch_pad", "back":tiles[0], "front":tiles[2]},
               {"tilename": "crash_site", "back":tiles[1], "front":tiles[11]}
               
               ]

temp=[]
for i in range(len(special_tiles)):
    repeated = True
    while repeated == True:
        row = random.randint(0,4)
        col = random.randint(0,4)
        if [row, col] not in temp and [row, col]!=[2,2]:
            special_tiles[i]["location"]=[row, col]
            temp.append([row, col])
            repeated = False

#resize image

def getImage(x):
    image = Image.open(x)
    resize_image = image.resize((120, 120))
    return (ImageTk.PhotoImage(resize_image))



game_board = [
    ["", "", "x", "", ""],
    ["", "x", "", "x", ""],
    ["x", "", "", "", "x"],
    ["", "x", "", "x", ""],
    ["", "", "x", "", ""]
]



for row in range(GAME_BOARD_SIZE):
    for col in range(GAME_BOARD_SIZE):

        temp = game_board[row][col]

        #check if current tile is speical tile
        if  any(tile['location'] == [row,col] for tile in special_tiles):
            
            tile_info =  next(item for item in special_tiles if item["location"] == [row,col])
                        
            game_board[row][col] = {"back": getImage(tile_info["back"]), "front": getImage(tile_info["front"]), "sand_markers": 0}

        #storm eye
                        
        elif row == 2 and col == 2:
            game_board[row][col] = {"back": getImage(tiles[24]), "front": getImage(tiles[24]), "sand_markers": 0}

        #the rest of the tiles
                        
        else:
            game_board[row][col] = {"back": getImage(tiles[0]), "front": getImage(tiles[11]), "sand_markers": 0}
            
        #adding initial sand markers
        
        if  temp == "x":
            game_board[row][col]["sand_markers"] = 1

def update_board_display():
    global player_pos
    for row in range(GAME_BOARD_SIZE):
        for col in range(GAME_BOARD_SIZE):
            tile = game_board[row][col]
            if (row, col) in player_pos:
                button_text = "P"
            else:
                button_text = tile["sand_markers"]
            buttons[row][col].config(text=button_text)


buttons = []
for row in range(GAME_BOARD_SIZE):
    button_row = []
    for col in range(GAME_BOARD_SIZE):
        backOfCard = game_board[row][col]['back']
        button = tk.Button(window, text="", width=120, height=120, compound="center")
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

#! New -------------------------------

def update_func_display(funcs:dict):
    buttons = [tk.Button(window, text=v, command=funcs[v]) for v in funcs.keys()]
    for i,v in enumerate(buttons): button.grid(row=i, column=len(game_board[0]))

#!------------------------------------


#update_board_display()
#update_func_display({"a":lambda:print("a"),"b":lambda:print("b"),"c":lambda:print("c")})
window.mainloop()