# Difficulty selection

from tkinter import *
from tkinter import ttk
stormLevel=0
gx=""
def main(root, bg, np ,bp):

    windowDims = (1280,720)

    global gx
    canvas1 = Canvas( root, width = 1280, height = 720)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image(640, 0, image = gx, anchor = "n")

    def setupSandStormTimer(difficulty):
        global stormLevel
        stormLevel = difficulty

    def confirm():
        nonlocal np
        nonlocal root
        for widget in root.winfo_children(): widget.destroy()
        np()
    def back():
        nonlocal bp
        nonlocal root
        for widget in root.winfo_children(): widget.destroy()
        bp()

    ttk.Label(root,text="Select Difficulty").pack()


    # The difficulty buttons
    Button(root,text="Novice",command=lambda: setupSandStormTimer(0)).place(width=100, height=60, x=windowDims[0]//2-50, y=10)
    Button(root,text="Normal",command=lambda: setupSandStormTimer(1)).place(width=100, height=60, x=windowDims[0]//2-50, y=70)
    Button(root,text="Elite",command=lambda: setupSandStormTimer(2)).place(width=100, height=60, x=windowDims[0]//2-50, y=130)
    Button(root,text="Legendary",command=lambda: setupSandStormTimer(3)).place(width=100, height=60, x=windowDims[0]//2-50, y=190)
    Button(root,text="Confirm",command=lambda: confirm()).place(width=100, height=60, x=windowDims[0]//2-50, y=250)
    Button(root,text="Back",command=lambda: back()).place(width=100, height=60, x=windowDims[0]//2-50, y=310)

