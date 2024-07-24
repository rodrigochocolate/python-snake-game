# Configurações inicias
import pygame
import random

pygame.init()
pygame.display.set_caption('Jogo Snake Python') # Nome da tela
largura, altura = 1000, 600
tela = pygame.display.set_mode((largura, altura)) # Criar tela
relogio = pygame.time.Clock()

# Cores RGB
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# Parametros da cobra
tamanho_pixel = 20
velocidade_jogo = 15

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_pixel) / float(tamanho_pixel)) * float(tamanho_pixel)
    comida_y = round(random.randrange(0, altura - tamanho_pixel) / float(tamanho_pixel)) * float(tamanho_pixel)
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho, tamanho]) # Desenhar retangulo

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, verde, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont('Helvetica', 30)
    texto = fonte.render(f'Pontos: {pontuacao}', True, branco)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN or tecla == pygame.K_s:
        velocidade_x = 0
        velocidade_y = tamanho_pixel
    elif tecla == pygame.K_UP or tecla == pygame.K_w:
        velocidade_x = 0
        velocidade_y = -tamanho_pixel
    elif tecla == pygame.K_RIGHT or tecla == pygame.K_d:
        velocidade_x = tamanho_pixel
        velocidade_y = 0
    elif tecla == pygame.K_LEFT or tecla == pygame.K_a:
        velocidade_x = -tamanho_pixel
        velocidade_y = 0
    else:
        velocidade_x = velocidade_y = 0
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False

    # posição inicial da cobra, vulgo meio da tela
    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()


    while not fim_jogo:
        tela.fill(preto) # Preencher tela com cor

        for evento in pygame.event.get(): # retorna inputs do usuário
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        # Desenhar comida
        desenhar_comida(tamanho_pixel, comida_x, comida_y)

        # Atualizar posição da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        x += velocidade_x
        y += velocidade_y

        # Desenhar cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        # Se a cobrinha bateu no próprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        desenhar_cobra(tamanho_pixel, pixels)
        desenhar_pontuacao(tamanho_cobra - 1)
        # Desenhar pontos

        # Atualização do jogo
        pygame.display.update() # Atualizar tela

        # Criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()

        relogio.tick(velocidade_jogo)

rodar_jogo()