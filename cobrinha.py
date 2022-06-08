import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura_window = 640
altura_window  = 480
x_cobra = largura_window / 2
y_cobra = altura_window / 2


"""Define posição aleatória da bolinha - novo spawn"""
x_maca = randint(20, largura_window - 10)
y_maca = randint(20, altura_window - 10)

velocidade = 10
x_controle = velocidade
y_controle = 0

font = pygame.font.SysFont("candara", 30, True, True)
pontos = 0

pygame.mixer.music.set_volume(0.5)
bg_musica = pygame.mixer.music.load("assets/BoxCat.mp3")
music_control = pygame.mixer.music.play(-1)

som_colisao = pygame.mixer.Sound("assets/smw_coin.wav")
gameover_music = pygame.mixer.Sound("assets/gameover2.wav")

tela = pygame.display.set_mode((largura_window, altura_window))
titlulo = pygame.display.set_caption("SnakeGame - Por Lairon Souza")
fps = pygame.time.Clock()
lista_cobra = []
comprimento_inicial_cobra = 5
gameover = False

def aumenta_cobra(lista_cobra):
    for xy in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (xy[0],xy[1],20,20))
        
def reiniciar():
    global pontos, x_cobra, y_cobra, lista_cabeca, lista_cobra, gameover, comprimento_inicial_cobra, x_maca, y_maca, music_control
    pontos = 0
    x_cobra = largura_window / 2
    y_cobra = altura_window / 2
    lista_cabeca = []
    lista_cobra = []
    gameover = False
    comprimento_inicial_cobra = 5
    x_maca = randint(20, largura_window)
    y_maca = randint(20, altura_window)
    music_control = pygame.mixer.music.play(-1)
 

while True:
    fps.tick(20) # controlador de velocidade de movimento FPS, está sem uso no momento
    tela.fill((255,255,255))
    mensagem = f"Pontos: {pontos}"
    texto_formatado = font.render(mensagem, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
       
        """Condição de controle de movimentação da cobrinha"""
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = - velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == - velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:    
                    y_controle = - velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
                
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))
    #maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))
    maca = pygame.draw.circle(tela, (255,0,0), (x_maca,y_maca), 12)

    """IF de colisão"""
    if cobra.colliderect(maca):
        x_maca = randint(40, largura_window)
        y_maca = randint(40, altura_window)
        pontos = pontos + 1
        som_colisao.play()
        comprimento_inicial_cobra += 1
        
        
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)   
    lista_cobra.append(lista_cabeca)
    
    if lista_cobra.count(lista_cabeca) > 1:
        font2 = pygame.font.SysFont("arial", 20, True, True)
        msg_final = "Game Over! Para reiniciar aperte R "
        msg_final_formatada = font2.render(msg_final, True, (255,255,255))
        music_control = pygame.mixer.music.stop()
        gameover = True
        ret_texto = msg_final_formatada.get_rect()
        gameover_music.play()
        
        while gameover:
            tela.fill((30,144,255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:    
                    if event.key == K_r:
                        reiniciar()
                        
            
            ret_texto.center = (largura_window/2, altura_window/2)
            tela.blit(msg_final_formatada, ret_texto)
            pygame.display.update()
            
    
    if x_cobra > largura_window:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura_window
    if y_cobra > altura_window:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura_window
                    
    
    if len(lista_cobra) > comprimento_inicial_cobra:
        del lista_cobra[0]
    
    aumenta_cobra(lista_cobra)

    """Printa o texto de pontuação"""
    tela.blit(texto_formatado, (450,40))

    #pygame.draw.circle(tela, (0,255,0), (300,260), 40)
    #pygame.draw.line(tela, (255,255,0), (390,0), (390,600), 5)
    pygame.display.update()