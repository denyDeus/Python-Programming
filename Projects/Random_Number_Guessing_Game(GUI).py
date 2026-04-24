import tkinter as tk
from tkinter import messagebox
import random

class GuessingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # Game variables
        self.lowest_num = 1
        self.highest_num = 100
        self.round_number = 1
        self.max_attempts = 7

        self.setup_game()

        # UI Components
        self.title_label = tk.Label(root, text="Number Guessing Game", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        self.round_label = tk.Label(root, text="", font=("Arial", 12))
        self.round_label.pack()

        self.range_label = tk.Label(root, text="", font=("Arial", 12))
        self.range_label.pack()

        self.attempts_label = tk.Label(root, text="", font=("Arial", 12))
        self.attempts_label.pack(pady=5)

        self.entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.entry.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack()

        self.submit_btn = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.submit_btn.pack(pady=5)

        self.next_btn = tk.Button(root, text="Next Round", command=self.next_round, state=tk.DISABLED)
        self.next_btn.pack(pady=5)

        self.exit_btn = tk.Button(root, text="Exit", command=root.quit)
        self.exit_btn.pack(pady=10)

        self.update_labels()

    def setup_game(self):
        self.answer = random.randint(self.lowest_num, self.highest_num)
        self.attempts = 0

    def update_labels(self):
        self.round_label.config(text=f"Round: {self.round_number}")
        self.range_label.config(text=f"Guess between {self.lowest_num} and {self.highest_num}")
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")

    def check_guess(self):
        guess = self.entry.get()

        if not guess.isdigit():
            self.feedback_label.config(text="Invalid input! Enter a number.")
            return

        guess = int(guess)

        if guess < self.lowest_num or guess > self.highest_num:
            self.feedback_label.config(text="Out of range!")
            return

        self.attempts += 1
        self.update_labels()

        if guess < self.answer:
            self.feedback_label.config(text="Too low!")
        elif guess > self.answer:
            self.feedback_label.config(text="Too high!")
        else:
            self.feedback_label.config(text=f"Correct! Answer: {self.answer}")
            messagebox.showinfo("Win", f"You guessed it in {self.attempts} attempts!")
            self.submit_btn.config(state=tk.DISABLED)
            self.next_btn.config(state=tk.NORMAL)
            return

        if self.attempts == self.max_attempts:
            self.feedback_label.config(text=f"Game Over! Answer: {self.answer}")
            messagebox.showinfo("Game Over", f"The correct number was {self.answer}")
            self.submit_btn.config(state=tk.DISABLED)
            self.next_btn.config(state=tk.NORMAL)

        self.entry.delete(0, tk.END)

    def next_round(self):
        # Increase difficulty
        self.highest_num += 50
        self.round_number += 1

        self.setup_game()
        self.update_labels()

        self.feedback_label.config(text="")
        self.entry.delete(0, tk.END)

        self.submit_btn.config(state=tk.NORMAL)
        self.next_btn.config(state=tk.DISABLED)


# Run app
root = tk.Tk()
app = GuessingGameGUI(root)
root.mainloop()