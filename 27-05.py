import pygame
import random

# Inicialização do Pygame
pygame.init()

# Dimensões da janela
largura_janela = 800
altura_janela = 600

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Configurações da janela
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption('Pong')

# Parâmetros da raquete
largura_raquete = 15
altura_raquete = 100

# Parâmetros da bola
dimensao_bola = 20

# Velocidades
velocidade_raquete = 5
velocidade_bola = [random.choice([-4, 4]), random.choice([-4, 4])]

# Posições iniciais
posicao_raquete1 = [(largura_janela - largura_raquete - 10), (altura_janela // 2 - altura_raquete // 2)]
posicao_raquete2 = [10, (altura_janela // 2 - altura_raquete // 2)]
posicao_bola = [largura_janela // 2, altura_janela // 2]

# Função principal do jogo
def jogo():
    clock = pygame.time.Clock()
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Movimentação das raquetes
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] and posicao_raquete1[1] > 0:
            posicao_raquete1[1] -= velocidade_raquete
        if teclas[pygame.K_DOWN] and posicao_raquete1[1] < altura_janela - altura_raquete:
            posicao_raquete1[1] += velocidade_raquete
        if teclas[pygame.K_w] and posicao_raquete2[1] > 0:
            posicao_raquete2[1] -= velocidade_raquete
        if teclas[pygame.K_s] and posicao_raquete2[1] < altura_janela - altura_raquete:
            posicao_raquete2[1] += velocidade_raquete

        # Movimentação da bola
        posicao_bola[0] += velocidade_bola[0]
        posicao_bola[1] += velocidade_bola[1]

        # Colisões com a parede superior e inferior
        if posicao_bola[1] <= 0 or posicao_bola[1] >= altura_janela - dimensao_bola:
            velocidade_bola[1] = -velocidade_bola[1]

        # Colisões com as raquetes
        if (posicao_bola[0] <= posicao_raquete2[0] + largura_raquete and
            posicao_raquete2[1] <= posicao_bola[1] <= posicao_raquete2[1] + altura_raquete):
            velocidade_bola[0] = -velocidade_bola[0]
        if (posicao_bola[0] >= posicao_raquete1[0] - dimensao_bola and
            posicao_raquete1[1] <= posicao_bola[1] <= posicao_raquete1[1] + altura_raquete):
            velocidade_bola[0] = -velocidade_bola[0]

        # Desenho dos elementos na tela
        janela.fill(preto)
        pygame.draw.rect(janela, branco, (*posicao_raquete1, largura_raquete, altura_raquete))
        pygame.draw.rect(janela, branco, (*posicao_raquete2, largura_raquete, altura_raquete))
        pygame.draw.ellipse(janela, branco, (*posicao_bola, dimensao_bola, dimensao_bola))
        pygame.draw.aaline(janela, branco, (largura_janela // 2, 0), (largura_janela // 2, altura_janela))

        # Atualização da tela
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Executar o jogo
if __name__ == "__main__":
    jogo()
