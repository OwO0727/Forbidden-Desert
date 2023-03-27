#main
import tkinter as tk
import random
from PIL import Image, ImageTk


#?######################################
#? NEW FILE ############################
#?######################################

import time as t
import difficultySelect as d
import playerNumber as n
import playerSelect
import player as playerTypeMod
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
    playerSelect.main(window, menubg, playerTypes, startGame, num,callN)
def callN(): n.main(window, menubg, callS, callD)
def startGame():
    main(window)
def callM(): m.main(window, menubg, callD)
m.gx=menubg
n.gx=menubg
d.gx=menubg
playerSelect.gx=menubg
#callM()

stormLevel = d.stormLevel
playerCount = n.playerNum
players = playerSelect.playersg
print(f"{stormLevel}\n\n{playerCount}\n\n{players}")

#?######################################
#? NEW FILE ############################
#?######################################

def main(window):
    window.wm_title("Forbidden Desert: Game")


    GAME_BOARD_SIZE = 5
    MAX_SAND = 48
    stormLevel = "Novice"
    playerCount = 5
    LOST = False

    c = tk.Canvas(window, width=1280, height=720, bg="#F7DC6F")
    c.place(x=0, y=0)


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

    parts_initial=[
        "engineImage.png", "navegationDeckImage.png", "propellerImage.png", "solarCrystalImage.png"
    ]

    tiles = ["img/Tiles/"+s for s in tiles_initial]

    parts_photos = ["img/Tiles/"+s for s in parts_initial]

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
                {"tilename": "tunnel2", "back":tiles[0], "front":tiles[23]},
                {"tilename": "tunnel3", "back":tiles[0], "front":tiles[23]},
                {"tilename": "launch_pad", "back":tiles[0], "front":tiles[2]},
                {"tilename": "crash_site", "back":tiles[1], "front":tiles[11]}
                
                ]

    parts = [["a1", "a2"], ["b1", "b2"], ["c1", "c2"], ["d1", "d2"]]
    parts_location = []

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

    #Setting number of storm cards to be picked each round
    two_players=[2,3,3,3,4,4,4,4,5,5,5,6,6, "dead"]
    three_or_four_players=[2,3,3,3,3,4,4,4,4,5,5,5,6,6, "dead"]
    five_players=[2,3,3,3,3,3,4,4,4,4,5,5,5,6,6, "dead"]

    if playerCount == 2:
        sand_storm_meter = two_players
    elif playerCount == 5:
        sand_storm_meter = five_players
    else: 
        sand_storm_meter = three_or_four_players

    if stormLevel == "Novice":
        sand_storm_level = 0
    elif stormLevel == "Normal":
        sand_storm_level = 1
    elif stormLevel == "Elite":
        sand_storm_level = 2
    else:
        sand_storm_level = 3

    #resize image
    def getImage(x):
        image = Image.open(x)
        resize_image = image.resize((120, 120))
        return (ImageTk.PhotoImage(resize_image))

    #excavate tiles
    def excavate():
        nonlocal current_player #! NEW
        row,col = current_player.position #! NEW

        buttonname = game_board[row][col]
        frontOfCard = game_board[row][col]['front']
        #if player_pos == (row, col): #check if player on the tile
        if buttonname["excavate"]==True: #check if tile is excavated already
            print("Already excavated")
        elif game_board[row][col]['sand_markers']<1: #excavate if sand marker less than 1
            buttonname["id"].config(image=frontOfCard)
            buttonname["excavate"]=True
        else: #cannot excavate if tile is blocked
            print("Tile is blocked, cannot be excavate")
        #else:
            #print("player not on targeted tile")
        
        end_turn() #! NEW

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
                
                if any(tile_info["tilename"] in x for x in parts):
                    parts_location.append({"tilename": tile_info["tilename"], "location": (row, col)})
                    parts_location = sorted(parts_location, key=lambda x: x["tilename"])
                

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

            game_board[row][col]["excavate"]=False

    #moving storm eye
    storm_eye_location = [2, 2]
    current_storm_deck = []
    def storm_eye_moving():
        nonlocal storm_eye_location
        nonlocal game_board
        nonlocal MAX_SAND
        nonlocal current_storm_deck
        nonlocal sand_storm_level
        nonlocal players
        card_count = sand_storm_meter[sand_storm_level]
        if card_count == "dead":
            print("GAME LOST")
            LOST = True
        else:
            for i in range(card_count):
                if len(current_storm_deck)== 0:
                    current_storm_deck = storm_card.copy()
                    print("reshuffle")
                cardpicked = random.choice(current_storm_deck)
                current_storm_deck.remove(cardpicked)
                window.after(1000*i, do_storm_card, cardpicked)

    def do_storm_card(cardpicked):
        print(cardpicked)
        nonlocal storm_eye_location, game_board, MAX_SAND, current_storm_deck, sand_storm_level, players
        sandstormname = game_board[storm_eye_location[0]][storm_eye_location[1]]["id"]
        if cardpicked["type"]=="storm picks up":
            sand_storm_level += 1
        elif cardpicked["type"]=="sun beats down":
            for player in players: player.water-=1
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
                
                #relocate parts location if storm eye moved
                if  any(tile['location'] == (newlocation[0],newlocation[1]) for tile in parts_location):
                    for tile in parts_location:
                        if tile["location"] == (newlocation[0],newlocation[1]):
                            tile["location"] = (storm_eye_location[0],storm_eye_location[1])
                
                for player in players:
                    if player.position == newlocation: player.position = storm_eye_location
                    

                MAX_SAND-=1
                storm_eye_location = newlocation
                if MAX_SAND == 0:
                    print("GAME LOST")
                    LOST = True
                update_board_display()

    #setting location of parts
    list_of_parts = [0, 0, 0, 0]

    def locating_parts():
        global list_of_parts
        
        count = 0
        for i in range(0, 8, 2):
            location1_row, location1_col = parts_location[i]["location"]
            location2_row, location2_col = parts_location[i+1]["location"]
            if game_board[location1_row][location1_col]["excavate"] == True and game_board[location2_row][location2_col]["excavate"] == True:
                list_of_parts[count] = [location2_row, location1_col]
            count+=1
        
    sandtile = Image.open(tiles[19]).resize((120, 120))
    blockedsandtile = Image.open(tiles[20]).resize((120, 120))
    mask= sandtile.convert("L")
    new_image = 0
    tileimage = 0
    temp_array = []
    sandtile = Image.open(tiles[19]).resize((120, 120))
    blockedsandtile = Image.open(tiles[20]).resize((120, 120))
    mask_image = sandtile.convert("L")
    sandtile.putalpha(mask_image)
    blockedsandtile.putalpha(mask_image)
    def update_board_display():
        nonlocal players, tileimage, new_image, temp_array #! NEW
        for row in range(GAME_BOARD_SIZE):
            for col in range(GAME_BOARD_SIZE):
                tile = game_board[row][col]
                #sandtile
                if tile["excavate"]:
                    tileimage = ImageTk.getimage(tile["front"])
                else:
                    tileimage = ImageTk.getimage(tile["back"])
                if tile["sand_markers"] != 0:
                    if tile["sand_markers"] == 1:
                        tileimage.paste(sandtile, (0, 0), mask)
                    elif tile["sand_markers"] >= 2:
                        tileimage.paste(blockedsandtile, (0, 0), mask)
                temp_array.append(ImageTk.PhotoImage(tileimage))
                tile["id"].config(image=temp_array[-1])

                #add parts if both hints are excavated
                flag = False
                for i in range(4):
                    if flag == False:
                        if list_of_parts[i] == [row, col]:
                            button_text = "\nPart "+str(i)+"\n"+"S"*tile["sand_markers"]
                            flag = True
                        else:
                            button_text = "\n\n\n"+"S"*tile["sand_markers"]
                
                #!CHANGED

                button_text = str([player.name for player in players if player.position==[row,col]])+button_text
                tile["id"].config(text=button_text)


    for row in range(GAME_BOARD_SIZE): 
        for col in range(GAME_BOARD_SIZE): 
            backOfCard = game_board[row][col]['back']
            button = tk.Button(window, text="", image = backOfCard, width=120, height=120, compound="center", command = lambda rw=row, cl=col: selectTile([rw,cl])) # ! CHANGED
            button.grid(row=row, column=col)
            game_board[row][col]["id"]=button

    testbutton = tk.Button(window, command=lambda:[storm_eye_moving(),update_board_display()], text="storm card")
    testbutton.grid(row=5, column=0)


    #* NEW________________________________________________

    current_tile=None
    def selectTile(tilePos):
        nonlocal current_tile, current_player
        tileRange = checkTileRange(current_player.position, tilePos)
        if not tileRange:
            return
            print(f"failed to move to {tilePos}")
        if tileRange > 1:
            return
            print(f"failed to move to {tilePos}")
        print(f"moved to {tilePos}")
        current_tile = tilePos
    
    def checkTileRange(playerPos, newPos):
        distx, disty = playerPos[0]-newPos[0], playerPos[1]-newPos[1]
        totalDist = abs(distx) + abs(disty)
        if newPos == storm_eye_location: return False
        return totalDist

    def movePlayer():
        nonlocal turnNum, players, turnActions, current_player, current_tile
        row,col = current_tile
        print(current_player.position,[row,col])
        if checkTileRange(current_player.position,[row,col]) > 1: return
        current_player.position=[row,col]
        print(current_tile)
        end_turn()
    
    def clearSand():
        nonlocal current_tile, game_board
    
        if ["game_board[current_tile[0]][current_tile[1]]sand_markers"] !=0:
            game_board[current_tile[0]][current_tile[1]]["sand_markers"] -= 1
            end_turn()

    turnNum = 0
    turnActions = 4
    playerSelect.playersg = ["Archeologist","Climber"] #! TESTING
    players = [playerTypeMod.playerTypeDict[pt] for pt in playerSelect.playersg]
    current_player = players[0]
    for p in players:
        p.position = special_tiles[-1]["location"]
    
    playerDefaultFuncs = {
        "Move": movePlayer,
        "Excavate": lambda: [excavate() for _ in [0] if current_tile == current_player.position],
        "Clear sand": lambda: clearSand()
    }
    print(playerDefaultFuncs)

    def update_func_display(funcs:dict):
        nonlocal playerDefaultFuncs

        buttonsSF = [tk.Button(window, text=v, command=funcs[v], width=8, height=8) for v in funcs.keys()]
        buttonsDF = [tk.Button(window, text=v, command=playerDefaultFuncs[v], width=8, height=8) for v in playerDefaultFuncs.keys()]
        #for _b in buttonsDF: print()
        for i,v in enumerate(buttonsSF): v.grid(row=i%GAME_BOARD_SIZE, column=6+len(playerDefaultFuncs)//5+(i//GAME_BOARD_SIZE))
        for i,v in enumerate(buttonsDF): v.grid(row=i%GAME_BOARD_SIZE, column=7+len(playerDefaultFuncs)//5+(i//GAME_BOARD_SIZE))
    
    def do_turn():
        nonlocal turnNum, players, turnActions, current_player
        
        current_player = players[turnNum%len(players)]
        newActions = {m:getattr(current_player, m) for m in dir(current_player) if not m.startswith("_") and callable(getattr(current_player, m))}
        turnActions=4

        update_func_display(newActions)
    
    def end_turn():
        nonlocal turnNum, turnActions, sand_storm_level
        update_board_display()
        turnActions-=1
        if turnActions == 0:
            turnNum+=1
            storm_eye_moving()
            do_turn()
        else: return

    update_board_display()
    do_turn()

    #*____________________________________________________
main(window)
window.mainloop()
