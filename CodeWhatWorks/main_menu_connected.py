#main
import tkinter as tk
import random
from PIL import Image, ImageTk


#?######################################
#? NEW FILE ############################
#?######################################

import difficultySelect as d
import playerNumber as n
import playerSelect as p
import player as playerTypes
import menu as m

window=tk.Tk()
window.wm_title("Forbidden Island: Player Select")
menubg = tk.PhotoImage(master=window,file = "./img/Menu.png")
playerTypes=[
        {"name":"Archeologist","imageName":r"./img/Players/archeologistImage.png"},
        {"name":"Climber","imageName":r"./img/Players/climberImage.png"},
        {"name":"Explorer","imageName":r"./img/Players/explorerImage.png"},
        {"name":"Meteorologist","imageName":r"./img/Players/meteorologistImage.png"},
        {"name":"Navigator","imageName":r"./img/Players/navigatorImage.png"},
        {"name":"Water Carrier","imageName":r"./img/Players/waterCarrierImage.png"}
            ]
for type in playerTypes: type["img"]=tk.PhotoImage(file=type["imageName"])

def callD(): d.main(window, menubg, callN, callM)
def callS():
    num=n.playerNum
    p.main(window, menubg, playerTypes, startGame, num,callN)
def callN(): n.main(window, menubg, callS, callD)
def startGame():
    main(window)
def callM(): m.main(window, menubg, callD)
m.gx=menubg
n.gx=menubg
d.gx=menubg
p.gx=menubg
callM()

stormLevel = d.stormLevel
playerCount = n.playerNum
players = p.playersg
print(f"{stormLevel}\n\n{playerCount}\n\n{players}")

#?######################################
#? NEW FILE ############################
#?######################################

def main(window):
    window.wm_title("Forbidden Desert: Game")


    GAME_BOARD_SIZE = 5
    STARTING_WATER = 3
    MAX_WATER = 8
    MAX_SAND = 48
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

    #setting storm cards

    storm_card=[]    
    direction = ["left", "right", "up", "down"]
    for j in range(4):
        for i in range(1,4):
            storm_card.append({"type": "direction", "left": 0, "right": 0, "up": 0, "down": 0})
            storm_card[-1][direction[j]]=i
            storm_card.append({"type": "direction", "left": 0, "right": 0, "up": 0, "down": 0})
            storm_card[-1][direction[j]]=i
    storm_card.extend([{"type": "storm picks up"}]*3)
    storm_card.extend([{"type": "sun beats down"}]*4)



    #resize image

    def getImage(x):
        image = Image.open(x)
        resize_image = image.resize((120, 120))
        return (ImageTk.PhotoImage(resize_image))

    #excavate tiles

    def excavate(row, col):
        buttonname = game_board[row][col]["id"]
        frontOfCard = game_board[row][col]['front']
        if buttonname.cget('image') == str(frontOfCard): #check if tile is excavated already
            print("Already excavated")
        elif game_board[row][col]['sand_markers']<2: #excavate if sand marker less than 2
            buttonname.config(image=frontOfCard)
        else: #cannot excavate if tile is blocked
            print("Tile is blocked, cannot be excavate")


    #setting game board, locating initial sand location    

    game_board = [
        ["", "", "x", "", ""],
        ["", "x", "", "x", ""],
        ["x", "", "", "", "x"],
        ["", "x", "", "x", ""],
        ["", "", "x", "", ""]
    ]

    #setting up the infomation of each tiles

    normalGearIndex=11
    for row in range(GAME_BOARD_SIZE):
        for col in range(GAME_BOARD_SIZE):
            temp = game_board[row][col]
            #check if current tile is speical tile
            if  any(tile['location'] == [row,col] for tile in special_tiles):
                
                tile_info =  next(item for item in special_tiles if item["location"] == [row,col])
                            
                game_board[row][col] = {"back": getImage(tile_info["back"]), "front": getImage(tile_info["front"]), "sand_markers": 0}

                if tile_info["tilename"] == "crash_site":
                    player_pos=(row, col)
            #storm eye                   
            elif row == 2 and col == 2:
                game_board[row][col] = {"back": getImage(tiles[24]), "front": getImage(tiles[24]), "sand_markers": 0}
            #the rest of the tiles                 
            else:
                game_board[row][col] = {"back": getImage(tiles[0]), "front": getImage(tiles[normalGearIndex]), "sand_markers": 0}
                if normalGearIndex <18:
                    normalGearIndex+=1
                else:
                    normalGearIndex=11    
            #adding initial sand markers 
            if  temp == "x":
                game_board[row][col]["sand_markers"] = 1
                MAX_SAND-=1


    player_water = STARTING_WATER

    def update_board_display():
        for row in range(GAME_BOARD_SIZE):
            for col in range(GAME_BOARD_SIZE):
                tile = game_board[row][col]

                if (row, col) == player_pos:
                    button_text = "P\n\n\n"+"S"*tile["sand_markers"]
                else:
                    button_text = "\n\n\n"+"S"*tile["sand_markers"]
                game_board[row][col]["id"].config(text=button_text)


    #moving storm eye
    storm_eye_location = [2, 2]
    current_storm_deck = []
    def storm_eye_moving():
        nonlocal storm_eye_location
        nonlocal game_board
        nonlocal MAX_SAND
        nonlocal current_storm_deck

        if len(current_storm_deck)== 0:
            current_storm_deck = storm_card.copy()
            print("reshuffle")

        
        cardpicked = random.choice(current_storm_deck)
        current_storm_deck.remove(cardpicked)

        sandstormname = game_board[storm_eye_location[0]][storm_eye_location[1]]["id"]
        if cardpicked["type"]=="storm picks up":
            print("storm picks up")
        elif cardpicked["type"]=="sun beats down":
            print("sun beats down")
        else:

            count= max(cardpicked["up"], cardpicked["down"], cardpicked["right"], cardpicked["left"])
            for i in range(count):
                
                if cardpicked["up"]>0:
                    newlocation = [storm_eye_location[0]-1, storm_eye_location[1]]
                elif cardpicked["down"]>0:
                    newlocation = [storm_eye_location[0]+1, storm_eye_location[1]]
                elif cardpicked["right"]>0:
                    newlocation = [storm_eye_location[0], storm_eye_location[1]+1]
                else:
                    newlocation = [storm_eye_location[0], storm_eye_location[1]-1]

                if  newlocation[0]<0 or newlocation[0]>4 or newlocation[1]<0 or newlocation[1]>4:
                    break
                
                newsandstormname = game_board[newlocation[0]][newlocation[1]]["id"]

                button1_info = sandstormname.grid_info()
                button1_command = sandstormname['command']
                button2_info = newsandstormname.grid_info()
                button2_command = newsandstormname['command']

                sandstormname['command'] = button2_command
                sandstormname.grid(row=button2_info['row'], column=button2_info['column'])
                newsandstormname['command'] = button1_command
                newsandstormname.grid(row=button1_info['row'], column=button1_info['column'])
                
                temp = game_board[newlocation[0]][newlocation[1]]
                game_board[newlocation[0]][newlocation[1]] = game_board[storm_eye_location[0]][storm_eye_location[1]]
                game_board[storm_eye_location[0]][storm_eye_location[1]] = temp


                game_board[storm_eye_location[0]][storm_eye_location[1]]["sand_markers"]+=1
                MAX_SAND-=1

                storm_eye_location = newlocation




    for row in range(GAME_BOARD_SIZE): 
        for col in range(GAME_BOARD_SIZE): 
            backOfCard = game_board[row][col]['back']
            button = tk.Button(window, text="", image = backOfCard, width=120, height=120, compound="center", command = lambda rw=row, cl=col: excavate(rw, cl))
            button.grid(row=row, column=col)
            game_board[row][col]["id"]=button

    testbutton = tk.Button(window, command=lambda:[storm_eye_moving(),update_board_display()], text="storm card")
    testbutton.grid(row=10, column=10)

    update_board_display()


    #* NEW________________________________________________

    turnNum = 0
    players = []

    def update_func_display(funcs:dict):
        buttonsF = [tk.Button(window, text=v, command=funcs[v], width=8, height=8) for v in funcs.keys()]
        for i,v in enumerate(buttonsF): v.grid(row=i, column=5)
    
    def do_turn():
        nonlocal turnNum, players
        
        thisPlayer = players[turnNum%len(players)]
        newActions = {m:getattr(thisPlayer["playerAttr"], m) for m in thisPlayer["type"].getMethods()}
        print(newActions)

    #update_func_display({"a":lambda:print("a"),"b":lambda:print("b"),"c":lambda:print("c")})

    #*____________________________________________________

window.mainloop()
