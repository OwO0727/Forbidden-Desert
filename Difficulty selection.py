# Difficulty selection

from tkinter import *
from tkinter import ttk

def setupSandStormTimer(difficulty):
    stormLevel = difficulty

root = Tk()

# Window size
root.geometry("1280x720")

ttk.Label(root,text="Select Difficulty").pack()


# The difficulty buttons
ttk.Button(root,text="Novice",command=lambda: setupSandStormTimer(0)).pack()
ttk.Button(root,text="Normal",command=lambda: setupSandStormTimer(1)).pack()
ttk.Button(root,text="Elite",command=lambda: setupSandStormTimer(2)).pack()
ttk.Button(root,text="Legendary",command=lambda: setupSandStormTimer(3)).pack()

root.mainloop()
