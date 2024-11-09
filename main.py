import tkinter as tk
from tkinter import messagebox
import random


class HousieGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Housie Game")
        self.picked_numbers = []
        self.remaining_numbers = list(range(1, 101))

        # Title Label
        self.title_label = tk.Label(root, text="Housie Game", font=("Arial", 20))
        self.title_label.pack(pady=10)

        # Frame to hold numbers grid and picked number area
        self.main_frame = tk.Frame(root)
        self.main_frame.pack()

        # Numbers Display
        self.numbers_frame = tk.Frame(self.main_frame)
        self.numbers_frame.grid(row=0, column=0, padx=20, pady=20)
        self.number_labels = {}
        for num in range(1, 101):
            label = tk.Label(self.numbers_frame, text=str(num), font=("Arial", 10), width=4, relief="ridge")
            label.grid(row=(num - 1) // 10, column=(num - 1) % 10, padx=1, pady=1)
            self.number_labels[num] = label

        # Picked Number Display
        self.picked_frame = tk.Frame(self.main_frame)
        self.picked_frame.grid(row=0, column=1, padx=20)
        self.picked_label = tk.Label(self.picked_frame, text="Picked Number:", font=("Arial", 14))
        self.picked_label.pack()
        self.current_number_label = tk.Label(self.picked_frame, text="", font=("Arial", 20), fg="red")
        self.current_number_label.pack()

        # Previous 5 Numbers Display
        self.previous_label = tk.Label(self.picked_frame, text="Last 5 Picks:", font=("Arial", 12))
        self.previous_label.pack(pady=(20, 5))
        self.previous_numbers = tk.Listbox(self.picked_frame, height=5, font=("Arial", 12), justify="center")
        self.previous_numbers.pack()

        # Next Button
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=20)
        self.next_button = tk.Button(self.buttons_frame, text="Next", font=("Arial", 12), command=self.pick_next_number)
        self.next_button.grid(row=0, column=0, padx=10)

        # Refresh Button
        self.refresh_button = tk.Button(self.buttons_frame, text="Refresh", font=("Arial", 12),
                                        command=self.confirm_refresh)
        self.refresh_button.grid(row=0, column=1, padx=10)

    def pick_next_number(self):
        if not self.remaining_numbers:
            self.next_button.config(state="disabled")
            return

        picked = random.choice(self.remaining_numbers)
        self.remaining_numbers.remove(picked)
        self.picked_numbers.append(picked)

        # Update picked number display
        self.current_number_label.config(text=str(picked))

        # Update last 5 numbers list
        self.previous_numbers.delete(0, tk.END)
        last_five = self.picked_numbers[-5:]
        for num in last_five:
            self.previous_numbers.insert(tk.END, str(num))

        # Disable picked number in grid
        if picked in self.number_labels:
            self.number_labels[picked].config(bg="gray", fg="white")

    def confirm_refresh(self):
        # Ask for confirmation before refreshing the game
        answer = messagebox.askyesno("Confirm Refresh", "Are you sure you want to refresh the game?")
        if answer:
            self.reset_game()

    def reset_game(self):
        # Reset the game to its initial state
        self.picked_numbers.clear()
        self.remaining_numbers = list(range(1, 101))
        self.current_number_label.config(text="")
        self.previous_numbers.delete(0, tk.END)

        for num, label in self.number_labels.items():
            label.config(bg="SystemButtonFace", fg="black")

        self.next_button.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    game = HousieGame(root)
    root.mainloop()
