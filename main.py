import pygame
pygame.init()

tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Jogo da Velha")

BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)
GREY = (50, 50, 50)
POS_X = 0
POS_Y = 0
LARGURA = 200
ALTURA = 200
STATUS = 'JOGANDO'
VEZ = 'JOGADOR1'

fundo = pygame.image.load("./fundo.jpg")
imgFundo = pygame.transform.scale(fundo, (190, 190))
#img = rect = pygame.draw.rect(tela, WHITE, (POS_X, POS_Y, LARGURA, ALTURA))
matrizTabuleiro = []


def desenha_tabuleiro():
    matrizTabuleiro = []
    for l in range(0, 3):
        linhaTabuleiro = []
        for c in range(0, 3):
            linhaTabuleiro.append(imgFundo)
        matrizTabuleiro.append(linhaTabuleiro)


    Y = POS_Y
    for l in range(0, 3):
        X = POS_X
        for c in range(0,3):
            #rect = pygame.draw.rect(tela, WHITE, (X, Y, LARGURA, ALTURA))
            tela.blit(matrizTabuleiro[l][c], (X, Y))
            X+=200
        Y+=200

def avalia_clique():
    mouse = pygame.mouse.get_pos()

    y = POS_Y
    for l in range(0, 3):
        x = POS_X
        for c in range(0, 3):
            if mouse[0] and matrizTabuleiro[l][c].get_rect(topleft=(x,y)).collidepoint(mouse):
                print("clique funcionando")

            x += 200
        y += 200

run = True
while run:
    if STATUS == 'JOGANDO':
        desenha_tabuleiro()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            avalia_clique()


    pygame.display.update()