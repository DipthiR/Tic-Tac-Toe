import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root, mode="player"):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.current_player = "X"
        self.board = [None] * 9
        self.buttons = []
        self.mode = mode  # "player" or "computer"
        
        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            button = tk.Button(self.root, text=" ", font=("Arial", 24), width=5, height=2, command=lambda i=i: self.make_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def make_move(self, index):
        if self.board[index] is None:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif all(self.board):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O" and self.mode == "computer":
                    self.computer_move()

    def computer_move(self):
        available_moves = [i for i, x in enumerate(self.board) if x is None]
        if available_moves:
            move = random.choice(available_moves)
            self.board[move] = "O"
            self.buttons[move].config(text="O")
            if self.check_winner():
                messagebox.showinfo("Game Over", "Computer wins!")
                self.reset_game()
            elif all(self.board):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "X"

    def check_winner(self):
        win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                            (0, 4, 8), (2, 4, 6)]             # diagonals
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != None:
                return True
        return False

    def reset_game(self):
        self.board = [None] * 9
        for button in self.buttons:
            button.config(text=" ")
        self.current_player = "X"

if __name__ == "__main__":
    mode = input("Enter 'player' for Player vs Player, 'computer' for Player vs Computer: ").strip().lower()
    root = tk.Tk()
    game = TicTacToe(root, mode)
    root.mainloop()
