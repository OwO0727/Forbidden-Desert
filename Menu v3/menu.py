#menu

from tkinter import *
from tkinter import ttk
import webbrowser

gx=""
def main(root,bg,np):
   windowDims = (1280,720)
   root.wm_title("Forbidden Island: Menu")
   root.geometry(f"{windowDims[0]}x{windowDims[1]}")

   global gx
   canvas1 = Canvas( root, width = 1280, height = 720)
   canvas1.pack(fill = "both", expand = True)
   canvas1.create_image(640, 0, image = gx, anchor = "n")

   frm = ttk.Frame(root, padding=10)

   def startGame():
      nonlocal np
      nonlocal root
      for widget in root.winfo_children(): widget.destroy()
      np()
      
   def startRulesMenu():
      webbrowser.open('https://themindcafe.com.sg/wp-content/uploads/2018/01/Forbidden-Desert.pdf')
      
   startButton = Button(root, text="Start Game", command=startGame)
   startButton.place(x=windowDims[0]//2-75, y=windowDims[1]//2-25, width=150, height=50)

   rulesButton = Button(root, text="Rules", command=startRulesMenu)
   rulesButton.place(x=windowDims[0]//2-25, y=windowDims[1]//2+50, width=50, height=20)

   quitButton = Button(root, text="Quit", command=lambda: root.destroy())
   quitButton.place(x=windowDims[0]//2-25, y=windowDims[1]//2+100, width=50, height=20)