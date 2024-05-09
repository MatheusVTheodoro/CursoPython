import tkinter as tk

# Modelo
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -= decremento


# Visão
class CarroView:
    def __init__(self, master):
        self.master = master
        self.label = tk.Label(master, text="")
        self.label.pack()

    def atualizar_view(self, carro):
        self.label.config(text=f"Marca: {carro.marca}, Modelo: {carro.modelo}, Ano: {carro.ano}, Velocidade: {carro.velocidade}")


# Controlador
class CarroController:
    def __init__(self, carro, view):
        self.carro = carro
        self.view = view

    def acelerar(self, incremento):
        self.carro.acelerar(incremento)
        self.view.atualizar_view(self.carro)

    def frear(self, decremento):
        self.carro.frear(decremento)
        self.view.atualizar_view(self.carro)


def main():
    # Criando uma instância da classe Carro
    meu_carro = Carro("Toyota", "Corolla", 2022)

    # Criando uma instância da classe Tkinter
    root = tk.Tk()
    root.title("Carro")

    # Criando uma instância da classe CarroView
    view = CarroView(root)

    # Criando uma instância da classe CarroController
    controller = CarroController(meu_carro, view)

    # Botões para acelerar e frear
    btn_acelerar = tk.Button(root, text="Acelerar", command=lambda: controller.acelerar(10))
    btn_acelerar.pack()

    btn_frear = tk.Button(root, text="Frear", command=lambda: controller.frear(10))
    btn_frear.pack()

    # Atualizando a visão inicial
    view.atualizar_view(meu_carro)

    root.mainloop()


if __name__ == "__main__":
    main()
