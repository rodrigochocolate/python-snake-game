# Configurações inicias
import pygame
import random

pygame.init()
pygame.display.set_caption('Jogo Snake Python') # Nome da tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura)) # Criar tela
relogio = pygame.time.Clock()

# Cores RGB
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# Parametros da cobra
tamanho_pixel = 10
velocidade_cobra = 15

def rodar_jogo():
    fim_jogo = False

    while not fim_jogo:
        tela.fill(preto) # Preencher tela com cor
        for evento in pygame.event.get(): # retorna inputs do usuário
            if evento.type == pygame.QUIT:
                fim_jogo = True
# Criar um loop infinito


# Desenhar os objetos do jogo na tela
# pontuação
# cobrinha
# comida

# Criar a lógica de terminar o jogo
# cobra bateu na parede
# a cobra bateu nela mesmo

# Pegar interações do usuário
# fechou a tela
# apertou teclas para mover a cobra

rodar_jogo()