#menu

from tkinter import *
from tkinter import ttk
import webbrowser

windowDims = (1280,720)

root = Tk()

root.wm_title("Forbidden Island: Menu")
root.geometry(f"{windowDims[0]}x{windowDims[1]}")

bg = PhotoImage(file = "img/Menu.png")
canvas1 = Canvas( root, width = 1280, height = 720)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 640, 0, image = bg, anchor = "n")

frm = ttk.Frame(root, padding=10)

def startGame():
   print("Start")
   
def startRulesMenu():
   webbrowser.open('https://themindcafe.com.sg/wp-content/uploads/2018/01/Forbidden-Desert.pdf')
   
startButton = Button(root, text="Start Game", command=startGame)
startButton.place(x=windowDims[0]//2-75, y=windowDims[1]//2-25, width=150, height=50)

rulesButton = Button(root, text="Rules", command=startRulesMenu)
rulesButton.place(x=windowDims[0]//2-25, y=windowDims[1]//2+50, width=50, height=20)

quitButton = Button(root, text="Quit", command=lambda: root.destroy())
quitButton.place(x=windowDims[0]//2-25, y=windowDims[1]//2+100, width=50, height=20)

root.mainloop()
