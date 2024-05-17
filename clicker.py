import tkinter as tk
from tkinter import messagebox

class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo Clicker")

        self.points = 0
        self.points_per_click = 1

        self.points_label = tk.Label(root, text="Pontos: 0", font=("Helvetica", 16))
        self.points_label.pack(pady=10)

        self.click_button = tk.Button(root, text="Clique Aqui!", font=("Helvetica", 16), command=self.click)
        self.click_button.pack(pady=20)

        self.upgrade_button = tk.Button(root, text="Loja de Upgrades", font=("Helvetica", 16), command=self.open_shop)
        self.upgrade_button.pack(pady=20)

        self.reset_button = tk.Button(root, text="Reset", font=("Helvetica", 16), command=self.reset)
        self.reset_button.pack(pady=20)

        self.shop_window = None

    def click(self):
        self.points += self.points_per_click
        self.points_label.config(text=f"Pontos: {self.points}")

    def reset(self):
        self.points = 0
        self.points_per_click = 1
        self.points_label.config(text="Pontos: 0")
        if self.shop_window:
            self.shop_window.destroy()
            self.shop_window = None

    def open_shop(self):
        if self.shop_window is None or not self.shop_window.winfo_exists():
            self.shop_window = tk.Toplevel(self.root)
            self.shop_window.title("Loja de Upgrades")

            self.upgrade1_button = tk.Button(self.shop_window, text="Upgrade 1 (+1 PPC) - 10 pontos", font=("Helvetica", 12), command=self.buy_upgrade1)
            self.upgrade1_button.pack(pady=10)

            self.upgrade2_button = tk.Button(self.shop_window, text="Upgrade 2 (+5 PPC) - 50 pontos", font=("Helvetica", 12), command=self.buy_upgrade2)
            self.upgrade2_button.pack(pady=10)

    def buy_upgrade1(self):
        if self.points >= 10:
            self.points -= 10
            self.points_per_click += 1
            self.points_label.config(text=f"Pontos: {self.points}")
            messagebox.showinfo("Upgrade Comprado", "Você comprou o Upgrade 1! (+1 PPC)")
        else:
            messagebox.showwarning("Pontos Insuficientes", "Você não tem pontos suficientes para comprar este upgrade.")

    def buy_upgrade2(self):
        if self.points >= 50:
            self.points -= 50
            self.points_per_click += 5
            self.points_label.config(text=f"Pontos: {self.points}")
            messagebox.showinfo("Upgrade Comprado", "Você comprou o Upgrade 2! (+5 PPC)")
        else:
            messagebox.showwarning("Pontos Insuficientes", "Você não tem pontos suficientes para comprar este upgrade.")

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()
