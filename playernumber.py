#menu

from tkinter import *
from tkinter import ttk

windowDims = (500,500)

root = Tk()
root.wm_title("Forbidden Island: Menu")
root.geometry(f"{windowDims[0]}x{windowDims[1]}")
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

canvas= Canvas(root, width= 300, height= 100, bg="red")
canvas.create_text(150, 50, text="How Many Players?", fill="white", font=('Helvetica 15 bold'))
canvas.pack()
root.mainloop()

