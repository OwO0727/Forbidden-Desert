#main
import tkinter as tk
import random
from PIL import Image, ImageTk

class tiles:
    def __init__(self, back, front, sandnum):
        self.back = back
        self.front = front
        self.sandnum= sandnum

windowDims = (1280,720)
window = tk.Tk()
window.wm_title("Forbidden Desert: Game")
window.geometry(f"{windowDims[0]}x{windowDims[1]}")


GAME_BOARD_SIZE = 5
STARTING_WATER = 3
MAX_WATER = 8
MAX_SAND = 12
WIN_TILE = "F"

tiles_initial= [ "backOfCardImage.png",
          "crashSiteImage.png", "launchPadImage.png",
          "engineColumnImage.png", "engineRowImage.png",
          "navigationDeckColumnImage.png", "navigationDeckRowImage.png",
          "propellerColumnImage.png", "propellerRowImage.png",
          "solarCrystalColumnImage.png", "solarCrystalRowImage.png",
          "gear1Image.png", "gear2Image.png",
          "gear3Image.png", "gear4Image.png",
          "gear5Image.png", "gear6Image.png",
          "gear7Image.png", "gear8Image.png",
          "sandMarkerImage.png", "highSandMarkerImage.png",
          "waterTileImage.png", "wellImage.png",
          "tunnelImage.png", "stormImage.png"
   ]


tiles = ["img/Tiles/"+s for s in tiles_initial]

image = Image.open(tiles[0])
resize_image = image.resize((120, 120))
backOfCard = ImageTk.PhotoImage(resize_image)

game_board = [
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""]
]

class tiles:
    def __init__(self, back, front, sandnum):
        self.back = back
        self.front = front
        self.sandnum= sandnum
        

player_pos = (0, 0)
player_water = STARTING_WATER

def update_board_display():
    for row in range(GAME_BOARD_SIZE):
        for col in range(GAME_BOARD_SIZE):
            tile = game_board[row][col]
            if (row, col) == player_pos:
                button_text = "P"
            else:
                button_text = tile
            buttons[row][col].config(text=button_text)


buttons = []
for row in range(GAME_BOARD_SIZE):
    button_row = []
    for col in range(GAME_BOARD_SIZE):
        button = tk.Button(window, text="", image = backOfCard, width=120, height=120, compound="center")
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

update_board_display()

window.mainloop()
