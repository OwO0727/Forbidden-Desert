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

playersg=[]
def playerSelectScrn(playerCount: int):
    maxRow=3
    players=['' for i in range(playerCount)]
    playerNum=1
    global playerTypes
    button = {}
    
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
        global window
        global playersg
        nonlocal players
        destroy(window)
        playersg=players
        return

    def quit():
        global window
        destroy(window)
        return "no"
    
    for i,t in enumerate(playerTypes):
        button[t["name"]] = tk.Button(window, image=t["img"], borderwidth=0)
        button[t["name"]].place(x=windowDims[0]//2-(100*maxRow)+((i%maxRow)*200), y=windowDims[1]//2-(150*(len(playerTypes)//maxRow)) + (300*(i//maxRow)))
        button[t["name"]].config(command=lambda t=t["name"]: select(t))
    button["back"] = tk.Button(window, text="Back")
    button["back"].place(x=windowDims[0]//2-70, y=windowDims[1]//2+(len(playerTypes)//maxRow*150))
    button["back"].config(command=lambda: back(), state=tk.DISABLED)
    button["confirm"] = tk.Button(window, text="Confirm")
    button["confirm"].place(x=windowDims[0]//2+30, y=windowDims[1]//2+(len(playerTypes)//maxRow*150))
    button["confirm"].config(command=lambda: confirm(), state=tk.DISABLED)
    button["quit"] = tk.Button(window, text="Quit")
    button["quit"].place(x=windowDims[0]//2-10, y=windowDims[1]//2+(len(playerTypes)//maxRow*150))
    button["quit"].config(command=lambda: quit())

playerSelectScrn(5)
window.mainloop()
print(playersg)
