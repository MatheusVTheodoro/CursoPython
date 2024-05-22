import tkinter as tk
from tkinter import ttk

class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Clicker Game")
        
        self.batatas = 0
        self.multiplier = 1
        self.auto_clickers = 0
        
        # Interface
        self.batatas_label = ttk.Label(root, text="Batatas: 0")
        self.batatas_label.pack()


        self.click_button = ttk.Button(root, text="Clique em mim!", command=self.click)
        self.click_button.pack()

        self.upgrade_button = ttk.Button(root, text="Comprar Multiplicador (Custo: 10)", command=self.buy_multiplier)
        self.upgrade_button.pack()

        self.auto_clicker_button = ttk.Button(root, text="Comprar Auto Clicker (Custo: 50)", command=self.buy_auto_clicker)
        self.auto_clicker_button.pack()

        self.progress_bar = ttk.Progressbar(root, length=200, mode='determinate')
        self.progress_bar.pack()
        self.progress_bar['maximum'] = 100

        # Auto Clicker Loop
        self.auto_click()

    def click(self):
        self.batatas += self.multiplier
        self.update_batatas()

    def buy_multiplier(self):
        if self.batatas >= 10:
            self.batatas -= 10
            self.multiplier += 1
            self.update_batatas()

    def buy_auto_clicker(self):
        if self.batatas >= 50:
            self.batatas -= 50
            self.auto_clickers += 1
            self.update_batatas()

    def auto_click(self):
        if self.auto_clickers > 0:
            self.progress_bar['value'] += 10
            if self.progress_bar['value'] >= 100:
                self.progress_bar['value'] = 0
                self.batatas += self.auto_clickers * self.multiplier
                self.update_batatas()
        
        self.root.after(1000, self.auto_click)

    def update_batatas(self):
        self.batatas_label.config(text=f"Batatas: {self.batatas}")
        self.upgrade_button.config(text=f"Comprar Multiplicador (Custo: 10)")
        self.auto_clicker_button.config(text=f"Comprar Auto Clicker (Custo: 50)")

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()
