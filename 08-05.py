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
    def imprimir_carro(self, carro):
        print(f"Marca: {carro.marca}, Modelo: {carro.modelo}, Ano: {carro.ano}, Velocidade: {carro.velocidade}")


# Controlador
class CarroController:
    def __init__(self, carro, view):
        self.carro = carro
        self.view = view

    def acelerar(self, incremento):
        self.carro.acelerar(incremento)
        self.view.imprimir_carro(self.carro)

    def frear(self, decremento):
        self.carro.frear(decremento)
        self.view.imprimir_carro(self.carro)


# Criando uma instância da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2022)

# Criando uma instância da classe CarroView
view = CarroView()

# Criando uma instância da classe CarroController
controller = CarroController(meu_carro, view)

# Imprimindo informações do carro antes de acelerar
controller.acelerar(0)

# Acelerando o carro
controller.acelerar(50)

# Freando o carro
controller.frear(20)
