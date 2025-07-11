# Simple Tic-Tac-Toe GUI game
import tkinter as tk
from tkinter import messagebox

# Function to check for a winner after each move
def check_winner():
    # All possible winning combinations
    combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for combo in combos:
        # Check if all three buttons in a combo have the same non-empty text
        if (
            buttons[combo[0]]['text'] != "" and
            buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text']
        ):
            # Highlight winning buttons
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            # Show winner message
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            global winner
            winner = True
            return

# Function called when a button is clicked
def button_click(index):
    global winner
    # Only allow move if button is empty and no winner yet
    if buttons[index]['text'] == "" and not winner:
        buttons[index]['text'] = current_player
        check_winner()
        toggle_player()

# Function to switch between players
def toggle_player():
    global current_player
    if not winner:
        # Switch player from 'X' to 'O' or vice versa
        current_player = "O" if current_player == "X" else "X"
        label.config(text=f"Player {current_player}'s turn")

# Create main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create 9 buttons for the game grid
buttons = [
    tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i))
    for i in range(9)
]

# Place buttons in a 3x3 grid
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

# Set initial player and winner flag
current_player = "X"
winner = False

# Label to show whose turn it is
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Start the GUI event loop
root.mainloop()