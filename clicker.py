import tkinter as tk
from tkinter import ttk

class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Clicker Game")
        
        self.score = 0
        self.multiplier = 1
        self.auto_clickers = 0
        
        # Interface
        self.score_label = ttk.Label(root, text="Score: 0")
        self.score_label.pack()

        self.click_button = ttk.Button(root, text="Click me!", command=self.click)
        self.click_button.pack()

        self.upgrade_button = ttk.Button(root, text="Buy Multiplier (Cost: 10)", command=self.buy_multiplier)
        self.upgrade_button.pack()

        self.auto_clicker_button = ttk.Button(root, text="Buy Auto Clicker (Cost: 50)", command=self.buy_auto_clicker)
        self.auto_clicker_button.pack()

        self.progress_bar = ttk.Progressbar(root, length=200, mode='determinate')
        self.progress_bar.pack()
        self.progress_bar['maximum'] = 100

        # Auto Clicker Loop
        self.auto_click()

    def click(self):
        self.score += self.multiplier
        self.update_score()

    def buy_multiplier(self):
        if self.score >= 10:
            self.score -= 10
            self.multiplier += 1
            self.update_score()

    def buy_auto_clicker(self):
        if self.score >= 50:
            self.score -= 50
            self.auto_clickers += 1
            self.update_score()

    def auto_click(self):
        if self.auto_clickers > 0:
            self.score += self.auto_clickers * self.multiplier
            self.update_score()
        
        # Atualiza a barra de progresso
        self.progress_bar['value'] += self.auto_clickers
        if self.progress_bar['value'] >= 100:
            self.progress_bar['value'] = 0
            self.score += 10 * self.auto_clickers * self.multiplier
            self.update_score()
        
        self.root.after(1000, self.auto_click)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")
        self.upgrade_button.config(text=f"Buy Multiplier (Cost: 10)")
        self.auto_clicker_button.config(text=f"Buy Auto Clicker (Cost: 50)")

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()
