# Difficulty selection

from tkinter import *
from tkinter import ttk
stormLevel=0
def main(root, bg, np):
    def setupSandStormTimer(difficulty):
        global stormLevel
        stormLevel = difficulty

    def confirm():
        nonlocal np
        nonlocal root
        for widget in root.winfo_children(): widget.destroy()
        np()
    # Window size
    root.geometry("1280x720")

    ttk.Label(root,text="Select Difficulty").pack()


    # The difficulty buttons
    ttk.Button(root,text="Novice",command=lambda: setupSandStormTimer(0)).pack()
    ttk.Button(root,text="Normal",command=lambda: setupSandStormTimer(1)).pack()
    ttk.Button(root,text="Elite",command=lambda: setupSandStormTimer(2)).pack()
    ttk.Button(root,text="Legendary",command=lambda: setupSandStormTimer(3)).pack()
    ttk.Button(root,text="Confirm",command=lambda: confirm()).pack()

