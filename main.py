#main
import tkinter as tk
import random


GAME_BOARD_SIZE = 4
STARTING_WATER = 3
MAX_WATER = 8
MAX_SAND = 12
WIN_TILE = "F"

game_board = [
    ["X", "S", "C", "C", "C"],
    ["C", "C", "S", "C", "C"],
    ["C", "S", "C", "C", "C"],
    ["C", "C", "C", "S", "C"]
]

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

def move_player(delta_x, delta_y):
    global player_pos
    new_pos = (player_pos[0] + delta_x, player_pos[1] + delta_y)
    if new_pos[0] < 0 or new_pos[0] >= GAME_BOARD_SIZE or new_pos[1] < 0 or new_pos[1] >= GAME_BOARD_SIZE:
        return
    new_tile = game_board[new_pos[0]][new_pos[1]]
    if new_tile == "S":
        player_water -= 1
        if player_water == 0:
            end_game(False)
    elif new_tile == WIN_TILE:
        end_game(True)
    player_pos = new_pos
    update_board_display()

def end_game(win):
    if win:
        message = "You won!"
    else:
        message = "You lost."
    message += " Play again?"
    if tk.messagebox.askyesno("Game Over", message):
        reset_game()
    else:
        window.quit()

def reset_game():
    global player_pos, player_water
    player_pos = (0, 0)
    player_water = STARTING_WATER
    random.shuffle(game_board)
    for row in range(GAME_BOARD_SIZE):
        random.shuffle(game_board[row])
    update_board_display()

window = tk.Tk()
window.title("Forbidden Desert")

buttons = []
for row in range(GAME_BOARD_SIZE):
    button_row = []
    for col in range(GAME_BOARD_SIZE):
        button = tk.Button(window, text="", width=5, height=2, command=lambda row=row, col=col: move_player(row-player_pos[0], col-player_pos[1]))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

update_board_display()

window.mainloop()
