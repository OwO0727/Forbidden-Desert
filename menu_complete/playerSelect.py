#playerSelect

import tkinter as tk
import random

windowDims = (1280,720)
playersg=[]
gx=""
def main(window, bgimg, playerTypes, func, num, bp):
    def destroy(root): 
        for widget in window.winfo_children(): widget.destroy()

    def playerSelectScrn(playerCount: int):
        maxRow=3
        players=['' for i in range(playerCount)]
        playerNum=1
        nonlocal playerTypes
        button = {}
        canvas1 = tk.Canvas(window, width = 1280, height = 720)
        canvas1.pack(fill = "both", expand = True)
        canvas1.create_image(640, 0, image = gx, anchor = "n")
        
        activeButtons = []
        def select(t):
            nonlocal players
            nonlocal playerNum
            nonlocal button
            nonlocal playerCount
            nonlocal activeButtons
            global window
            players[playerNum-1] = t
            playerNum+=1
            button[t]["state"] = tk.DISABLED
            button["back"]["state"] = tk.NORMAL
            if playerNum > playerCount:
                for key in button.keys():
                    if not key in ["quit","confirm","back"]:
                        if button[key]["state"] == tk.NORMAL:
                            activeButtons+=[key]
                        button[key]["state"] = tk.DISABLED
                button["confirm"]["state"] = tk.NORMAL
        
        def back():
            nonlocal players
            nonlocal playerNum
            nonlocal button
            nonlocal playerCount
            nonlocal activeButtons
            playerNum -= 1
            lastPlayerType=players[playerNum-1]
            players = players[:playerNum-1] + [''] + players[playerNum:]
            if playerNum==1: button["back"]["state"] = tk.DISABLED
            button[lastPlayerType]["state"] = tk.NORMAL
            button["confirm"]["state"] = tk.DISABLED
            for key in activeButtons: button[key]["state"] = tk.NORMAL
        
        def confirm():
            nonlocal window
            global playersg
            nonlocal players
            destroy(window)
            playersg=players
            func()

        def selectR():
            nonlocal players
            select(random.choice([a["name"] for a in playerTypes if not a["name"] in players]))

        def quit():
            nonlocal window
            destroy(window)
            bp()
        
        for i,t in enumerate(playerTypes):
            button[t["name"]] = tk.Button(window, image=t["img"], borderwidth=0, width=200, height=300)
            button[t["name"]].place(x=windowDims[0]//2-(100*maxRow)+((i%maxRow)*200), y=windowDims[1]//2-(150*(len(playerTypes)//maxRow)) + (300*(i//maxRow)))
            button[t["name"]].config(command=lambda t=t["name"]: select(t))
        button["back"] = tk.Button(window, text="Back", width=21)
        button["back"].place(x=windowDims[0]//2-150, y=windowDims[1]//2+(len(playerTypes)//maxRow*150))
        button["back"].config(command=lambda: back(), state=tk.DISABLED)
        button["confirm"] = tk.Button(window, text="Confirm", width=21)
        button["confirm"].place(x=windowDims[0]//2+150, y=windowDims[1]//2+(len(playerTypes)//maxRow*150))
        button["confirm"].config(command=lambda: confirm(), state=tk.DISABLED)
        button["quit"] = tk.Button(window, text="Cancel", width=21)
        button["quit"].place(x=windowDims[0]//2-300, y=windowDims[1]//2+(len(playerTypes)//maxRow*150))
        button["quit"].config(command=lambda: quit())
        button["rdm"] = tk.Button(window, text="Random", width=21, command=lambda: selectR())
        button["rdm"].place(x=windowDims[0]//2, y=windowDims[1]//2+(len(playerTypes)//maxRow*150))
    playerSelectScrn(num)
    print("done")