#menu

from tkinter import *
from tkinter import ttk

windowDims = (1280,720)

root = Tk()
root.wm_title("Forbidden Island: Menu")
root.geometry(f"{windowDims[0]}x{windowDims[1]}")


bg = PhotoImage(file = "img/Menu.png")
canvas1 = Canvas( root, width = 1280, height = 720)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 640, 0, image = bg, anchor = "n")
canvas1.create_text(640, 220, text="How Many Players?", fill="black", font=('Helvetica 18 bold'))
canvas1.pack()

frm = ttk.Frame(root, padding=10)

def startGame(): print("Start")
def two(): print('Two players selected')
def three(): print('Three players selected')
def four(): print('Four players selected')
def five(): print('Five players selected')
def back(): print('Back to menu')

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


root.mainloop()



