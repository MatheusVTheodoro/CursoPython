import tkinter as tk

class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo Clicker")

        self.points = 0

        self.points_label = tk.Label(root, text="Pontos: 0", font=("Helvetica", 16))
        self.points_label.pack(pady=10)

        self.click_button = tk.Button(root, text="Clique Aqui!", font=("Helvetica", 16), command=self.click)
        self.click_button.pack(pady=20)

        self.reset_button = tk.Button(root, text="Reset", font=("Helvetica", 16), command=self.reset)
        self.reset_button.pack(pady=20)

    def click(self):
        self.points += 1
        self.points_label.config(text=f"Pontos: {self.points}")

    def reset(self):
        self.points = 0
        self.points_label.config(text="Pontos: 0")

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()
