# Difficulty selection

from tkinter import *
from tkinter import ttk

playerCount = 2 #Placeholder

def setupSandStormTimer(difficulty,playerCount):
    # Calculate stormLevel using some calculation involving the number of players and the difficulty
    print("Difficulty:",difficulty,"Players:",playerCount) # Placeholder

root = Tk()

# Window size
root.geometry("500x500")

label = ttk.Label(root,text="Select Difficulty")
label.pack()

# The difficulty buttons
ttk.Button(root,text="Novice",command=lambda: setupSandStormTimer(0,playerCount)).pack()
ttk.Button(root,text="Normal",command=lambda: setupSandStormTimer(1,playerCount)).pack()
ttk.Button(root,text="Elite",command=lambda: setupSandStormTimer(2,playerCount)).pack()
ttk.Button(root,text="Legendary",command=lambda: setupSandStormTimer(3,playerCount)).pack()

root.mainloop()