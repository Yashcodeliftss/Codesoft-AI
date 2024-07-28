import tkinter as tk
from tkinter import messagebox

# Initialize the game board
board = [[0, 0, 0] for _ in range(3)]

# Function to check for a winner
def check_winner(board):
    lines = []
    for i in range(3):
        lines.append(board[i])  # Rows
        lines.append([board[j][i] for j in range(3)])  # Columns
    
    lines.append([board[i][i] for i in range(3)])  # Diagonal \
    lines.append([board[i][2 - i] for i in range(3)])  # Diagonal /

    for line in lines:
        if line[0] == line[1] == line[2] and line[0] != 0:
            return line[0]

    return 0  # No winner

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 1:
        return 10 - depth
    elif winner == 2:
        return depth - 10
    elif all(cell != 0 for row in board for cell in row):
        return 0  # Draw

    if is_maximizing:
        best_value = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1  # AI move
                    value = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = 0  # Undo move
                    best_value = max(best_value, value)
                    alpha = max(alpha, best_value)
                    if beta <= alpha:
                        return best_value
        return best_value
    else:
        best_value = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 2  # Opponent move
                    value = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = 0  # Undo move
                    best_value = min(best_value, value)
                    beta = min(beta, best_value)
                    if beta <= alpha:
                        return best_value
        return best_value

# Function to find the best move for AI
def find_best_move(board):
    best_value = -float('inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 1  # AI move
                move_value = minimax(board, 0, False, -float('inf'), float('inf'))
                board[i][j] = 0  # Undo move
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)
    return best_move

# Function to handle button clicks
def on_button_click(row, col):
    if board[row][col] == 0:
        board[row][col] = 2
        buttons[row][col].config(text="O")
        if check_winner(board) or all(cell != 0 for row in board for cell in row):
            game_over()
            return

        # AI move
        ai_move = find_best_move(board)
        if ai_move != (-1, -1):
            board[ai_move[0]][ai_move[1]] = 1
            buttons[ai_move[0]][ai_move[1]].config(text="X")
            if check_winner(board) or all(cell != 0 for row in board for cell in row):
                game_over()

# Function to end the game and show the result
def game_over():
    winner = check_winner(board)
    if winner == 1:
        messagebox.showinfo("Game Over", "AI wins!")
    elif winner == 2:
        messagebox.showinfo("Game Over", "You win!")
    else:
        messagebox.showinfo("Game Over", "It's a draw!")
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create a frame for the board and center it in the window
frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

# Create the buttons for the board
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(frame, text="", width=10, height=3, command=lambda i=i, j=j: on_button_click(i, j))
        buttons[i][j].grid(row=i, column=j)

# Configure grid weight to center the frame
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Set the size of the window
root.geometry("300x300")

# Start the Tkinter event loop
root.mainloop()
