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
ESCOLHA = 'X'

tela.fill(WHITE)



#desenha linhas para determinar o tabuleiro
def desenha_tabuleiro():

    pygame.draw.line(tela, (BLACK), (200, 0), (200, 600), 10)
    pygame.draw.line(tela, (BLACK), (400, 0), (400, 600), 10)
    pygame.draw.line(tela, (BLACK), (0, 200), (600, 200), 10)
    pygame.draw.line(tela, (BLACK), (0, 400), (600, 400), 10)

#define qual imagem será desenhada para cada jogador
def joga(pos):

    x, y = pos
    if VEZ == 'JOGADOR1':
        peca_X = pygame.image.load("./x.png").convert_alpha()
        imgX = pygame.transform.scale(peca_X, (100, 100))
        tela.blit(imgX, (x - 50, y - 50))
    else:
        peca_O = pygame.image.load("./O.png").convert_alpha()
        imgO = pygame.transform.scale(peca_O, (100, 100))
        tela.blit(imgO, (x - 50, y - 50))

def verifica_pos():
    mouse = pygame.mouse.get_pos()
    for i in listaRects:
        if event.type == pygame.MOUSEBUTTONDOWN and i.collidepoint(mouse):
            if i == rect1:
                confirma_jogada(0, [100, 100])
            if i == rect2:
                confirma_jogada(1, [300, 100])
            if i == rect3:
                confirma_jogada(2, [500, 100])
            if i == rect4:
                confirma_jogada(3, [100, 300])
            if i == rect5:
                confirma_jogada(4, [300, 300])
            if i == rect6:
                confirma_jogada(5, [500, 300])
            if i == rect7:
                confirma_jogada(6, [100, 500])
            if i == rect8:
                confirma_jogada(7, [300, 500])
            if i == rect9:
                confirma_jogada(8, [500, 500])

def confirma_jogada(indice, pos):
    global VEZ
    if marcacao_tabuleiro[indice] == 'X':
        print('X')
    elif marcacao_tabuleiro[indice] == 'O':
        print('O')
    else:
        marcacao_tabuleiro[indice] = ESCOLHA
        joga(pos)
        print(marcacao_tabuleiro)
        if VEZ == 'JOGADOR1':
            VEZ = 'JOGADOR2'
        else:
            VEZ = 'JOGADOR1'
#marca as posições do tabuleiro
marcacao_tabuleiro = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
]

#cria objetos rects para delimitar a área entre as linhas
rect1 = pygame.Rect((0, 0), (200, 200))
rect2 = pygame.Rect((200, 0), (200, 200))
rect3 = pygame.Rect((400, 0), (200, 200))
rect4 = pygame.Rect((0, 200), (200, 200))
rect5 = pygame.Rect((200, 200), (200, 200))
rect6 = pygame.Rect((400, 200), (200, 200))
rect7 = pygame.Rect((0, 400), (200, 200))
rect8 = pygame.Rect((200, 400), (200, 200))
rect9 = pygame.Rect((400, 400), (200, 200))

#adiciona rects em lista para melhor acesso
listaRects = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9]


run = True
while run:
    if STATUS == 'JOGANDO':
        desenha_tabuleiro()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if VEZ == 'JOGADOR1':
                    ESCOLHA = 'X'
                    verifica_pos()
                else:
                    ESCOLHA = 'O'
                    verifica_pos()

    pygame.display.update()