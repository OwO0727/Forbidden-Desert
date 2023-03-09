#menu

from tkinter import *
from tkinter import ttk

windowDims = (1280,720)
playerNum=0
gx=""
def main(root, bg, np, bp):
    root.geometry(f"{windowDims[0]}x{windowDims[1]}")
    global gx

    bg = PhotoImage(file = "img/Menu.png")
    canvas1 = Canvas( root, width = 1280, height = 720)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image( 640, 0, image = gx, anchor = "n")
    canvas1.create_text(640, 220, text="How Many Players?", fill="black", font=('Helvetica 18 bold'))
    canvas1.pack()

    frm = ttk.Frame(root, padding=10)

    def startGame():
        for widget in root.winfo_children(): widget.destroy()
        np()
    def two():
        global playerNum
        playerNum=2
    def three(): 
        global playerNum
        playerNum=3
    def four():
        global playerNum
        playerNum=4
    def five():
        global playerNum
        playerNum=2
    def back():
        for widget in root.winfo_children(): widget.destroy()
        bp()

    # back = Button(root, text="Back to Menu", command = menu)
    # back.place(x=windowDims[0] // 2-200 , y=windowDims[1] // 2+100 , width=100, height=50)
    p2 = Button(root, text="2", command = two)
    p2.place(x=windowDims[0] // 2 - 100, y=windowDims[1] // 2-100 , width=50, height=50)
    p3 = Button(root, text="3", command = three)
    p3.place(x=windowDims[0] // 2 - 50, y=windowDims[1] // 2 -100, width=50, height=50)
    p4 = Button(root, text="4", command = four)
    p4.place(x=windowDims[0] // 2 + 0, y=windowDims[1] // 2 -100, width=50, height=50)
    p5 = Button(root, text="5", command = five)
    p5.place(x=windowDims[0] // 2 + 50, y=windowDims[1] // 2 -100, width=50, height=50)
    c = Button(root, text="back", command = back)
    c.place(x=windowDims[0] // 2 - 150, y=windowDims[1] // 2-100 , width=50, height=50)
    b = Button(root, text="confirm", command = startGame)
    b.place(x=windowDims[0] // 2 + 100, y=windowDims[1] // 2-100 , width=50, height=50)




