import tkinter as tk
import time

class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Clicker Game")

        self.score = 0
        self.time_left = 30

        self.score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 20))
        self.score_label.pack(pady=20)

        self.time_label = tk.Label(root, text="Time Left: 30s", font=("Helvetica", 20))
        self.time_label.pack(pady=20)

        self.click_button = tk.Button(root, text="Click Me!", font=("Helvetica", 20), command=self.increase_score)
        self.click_button.pack(pady=20)

        self.update_timer()

    def increase_score(self):
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"Time Left: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            self.click_button.config(state=tk.DISABLED)
            self.time_label.config(text="Time's Up!")

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()
