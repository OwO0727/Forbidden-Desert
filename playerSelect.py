#playerSelect

import tkinter as tk

windowDims = (1280,720)
window = tk.Tk()
window.wm_title("Forbidden Island: Player Select")
window.geometry(f"{windowDims[0]}x{windowDims[1]}")
playerTypes=[
        {"name":"Archeologist","imageName":r"img/Players/archeologistImage.png"},
        {"name":"Climber","imageName":r"img/Players/climberImage.png"},
        {"name":"Explorer","imageName":r"img/Players/explorerImage.png"},
        {"name":"Meteorologist","imageName":r"img/Players/meteorologistImage.png"},
        {"name":"Navigator","imageName":r"img/Players/navigatorImage.png"},
        {"name":"Water Carrier","imageName":r"img/Players/waterCarrierImage.png"}
            ]
for type in playerTypes: type["img"]=tk.PhotoImage(file=type["imageName"])

def destroy(root): 
    for widget in window.winfo_children(): widget.destroy()

def playerSelectScrn(playerCount: int):
    maxRow=3
    players=['' for i in range(playerCount)]
    playerNum=1
    global playerTypes
    button = {'':'' for i in range(len(playerTypes))}
    
    def select(t):
        nonlocal players
        nonlocal playerNum
        nonlocal button
        nonlocal playerCount
        global window
        players[playerNum-1] = t
        playerNum+=1
        button[t]["state"] = tk.DISABLED
        print(players)
        if playerNum > playerCount:
            destroy(window)
            return
    
    for i,t in enumerate(playerTypes):
        button[t["name"]] = tk.Button(window, image=t["img"], borderwidth=0)
        button[t["name"]].place(x=windowDims[0]//2-(100*maxRow)+((i%maxRow)*200), y=windowDims[1]//2-(150*(len(playerTypes)//maxRow)) + (300*(i//maxRow)))
        button[t["name"]].config(command=lambda t=t["name"]: select(t))
        

playerSelectScrn(1)

window.mainloop()
