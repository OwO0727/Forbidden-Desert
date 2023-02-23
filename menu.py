#menu

from tkinter import *
from tkinter import ttk

windowDims = (500,500)

root = Tk()
root.wm_title("Forbidden Island: Menu")
root.geometry(f"{windowDims[0]}x{windowDims[1]}")
frm = ttk.Frame(root, padding=10)
def startGame(): print("Start")
def startOptionsMenu(): print("Start")
startButton = Button(root, text="Start Game", command=startGame)
startButton.place(x=windowDims[0]//2-75, y=windowDims[1]//2-25, width=150, height=50)
optionsButton = Button(root, text="Options", command=startOptionsMenu)
optionsButton.place(x=windowDims[0]//2, y=windowDims[1]//2+50)
quitButton = Button(root, text="Quit", command=lambda: root.quit())
quitButton.place(x=windowDims[0]//2, y=windowDims[1]//2+100)
root.mainloop()
