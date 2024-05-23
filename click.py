import tkinter as tk

class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Clicker Game")

        self.score = 0

        self.score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 20))
        self.score_label.pack(pady=20)

        self.click_button = tk.Button(root, text="Click Me!", font=("Helvetica", 20), command=self.increase_score)
        self.click_button.pack(pady=20)

    def increase_score(self):
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()
