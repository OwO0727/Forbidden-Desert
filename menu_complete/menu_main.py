import difficultySelect as d
import playerNumber as n
import playerSelect as p
import menu as m

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
def startGame(): print("start")
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