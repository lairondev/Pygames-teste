import pygame
from config import *
from pygame.locals import *
from sys import exit
from random import randint
from datetime import datetime
from time import sleep

pygame.init()

tela = pygame.display.set_mode((LARGURA_WIN, ALTURA_WIN))
pygame.display.set_caption("Traffic Scape")

fundo = pygame.image.load("img/pista.jpg").convert_alpha()
fundo_formatado = pygame.transform.scale(fundo, (LARGURA_WIN, ALTURA_WIN))

"""Musicas do jogo"""
colisao = pygame.mixer.Sound("sound/colisao2.mp3")
motor = pygame.mixer.Sound("sound/engine-loop/motor.wav")
motor.play(-1)
motor.set_volume(0.9)

bg_music = pygame.mixer.Sound("sound/bg_music.mp3")
bg_music.play(-1)
bg_music.set_volume(0.2)

#pygame.mixer.music.set_volume(0.4)

"""Sprites do jogo"""
faixa_movimento = pygame.image.load("img/faixa_movimento.png").convert_alpha()
faixa_branca = pygame.image.load("img/faixa_branca.png").convert_alpha()
faixa_branca2 = pygame.image.load("img/faixa_branca.png").convert_alpha()
faixa_cinza = pygame.image.load("img/faixa_cinza.png").convert_alpha()
casa = pygame.image.load("img/casa.png").convert_alpha()
casa_new = pygame.transform.scale(casa, (120, 245))

arvores = pygame.image.load("img/arvore.png").convert_alpha()
arvores_new = pygame.transform.scale(arvores, (100, 300))

car_red = pygame.image.load("img/car_red.png").convert_alpha()
car_red_new = pygame.transform.scale(car_red, (60,130))

car_blue = pygame.image.load("img/car_blue.png").convert_alpha()
car_blue_new = pygame.transform.scale(car_blue, (60,130))

car_grey = pygame.image.load("img/car_grey.png").convert_alpha()
car_grey_new = pygame.transform.scale(car_grey, (60,130))

moto1 = pygame.image.load("img/moto1.png").convert_alpha()
moto1_new = pygame.transform.scale(moto1, (30,100))

moto2 = pygame.image.load("img/moto2.png").convert_alpha()
moto2_new = pygame.transform.scale(moto2, (30,100))

player = pygame.image.load("img/carro_player.png").convert_alpha()
player_formatado = pygame.transform.scale(player, (60,130))


# Carro do player
x_carro = 370
y_carro = 730
speed_carro = 7

# Faixa cinza, pista em movimento
fxm_y = -50
fxm_speed = 7

# Árvores do acostamento
y_arvore = -450
arvore_speed = 7

# Casa
y_casa = -600
casa_speed = 7

# Carro Azul
x_car_blue = LEFT_POS
y_car_blue = -700
car_blue_speed = 5

# Carro Vermelho
x_car_red = RIGHT_POS
y_car_red = -500
car_red_speed = 10

# Carro Cinza
x_car_grey = MID_POS
y_car_grey = -350
car_grey_speed = 3

#moto1
x_moto1 = FAIXA1_POS
y_moto1 = -800
moto1_speed = 3

#moto2
x_moto2 = FAIXA2_POS
y_moto2 = -1200
moto2_speed = 5

tempo = pygame.time.Clock()
jogo = RODANDO
gameover = False
pontos = 0

def reiniciar():
    global gameover, pontos, x_carro, y_carro, speed_carro, x_car_blue, y_car_blue, car_blue_speed, x_car_grey, y_car_grey, car_grey_speed, x_car_red, y_car_red, car_red_speed, x_moto1, y_moto1, moto1_speed, x_moto2, y_moto2, moto2_speed, motor, bg_music
    
    gameover = False
    pontos = 0
    x_carro = 370
    y_carro = 730
    speed_carro = 7
    x_car_blue = LEFT_POS
    y_car_blue = -700
    car_blue_speed = 5
    x_car_grey = MID_POS
    y_car_grey = -350
    car_grey_speed = 3
    x_car_red = RIGHT_POS
    y_car_red = -500
    car_red_speed = 10
    x_moto1 = FAIXA1_POS
    y_moto1 = -800
    moto1_speed = 3
    x_moto2 = FAIXA2_POS
    y_moto2 = -1200
    moto2_speed = 5
    motor.play()
    bg_music.play()



"""Loop principal do jogo"""
while True:
    tempo.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    
        """Controles do jogo"""
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if jogo != PAUSADO:
                    jogo = PAUSADO
                    motor.stop()
                    bg_music.stop()
                    msg_pause = "Pausado"
                    font1 = pygame.font.SysFont("verdana", 25, True, True)
                    msg_pause_render = font1.render(msg_pause, True, (BRANCO))
                    
                else:
                   jogo = RODANDO
                   motor.play(-1)
                   bg_music.play(-1)
    
    
    tela.blit(fundo_formatado, (0,0))
    tela.blit(faixa_cinza, (395,15))
    tela.blit(faixa_branca, (318, 0))
    tela.blit(faixa_branca2, (477, 0))
    tela.blit(faixa_movimento, (250, fxm_y))
    tela.blit(casa_new, (RIGHT_POS+150, y_casa))
    tela.blit(arvores_new, (40, y_arvore))
    
    playerbloco = tela.blit(player_formatado, (x_carro, y_carro-250))
    blocoblue = tela.blit(car_blue_new, (x_car_blue, y_car_blue))
    blocored = tela.blit(car_red_new, (x_car_red, y_car_red))
    blocogrey = tela.blit(car_grey_new, (x_car_grey, y_car_grey))
    blocomoto1 = tela.blit(moto1_new, (x_moto1, y_moto1))
    blocomoto2 = tela.blit(moto2_new, (x_moto2, y_moto2))
    
    if jogo == PAUSADO:
        tela.blit(msg_pause_render, (LARGURA_WIN/2, ALTURA_WIN/2))
        continue
        
        
        
    """controles do carro"""
    if pygame.key.get_pressed()[K_UP]:
        y_carro -= speed_carro
    if pygame.key.get_pressed()[K_DOWN]:
        y_carro += speed_carro
    if pygame.key.get_pressed()[K_LEFT]:
        x_carro -= speed_carro
    if pygame.key.get_pressed()[K_RIGHT]:
        x_carro += speed_carro
        
    
    
        
    """Limitando o player na pista"""
    if x_carro <= 190:
        x_carro = 190
    if x_carro >= 550:
        x_carro = 550
    if y_carro >= 740:
        y_carro = 740
    if y_carro <= 255:
        y_carro = 255
    
    """carros inimigos descendo"""   
    y_car_blue += car_blue_speed
    y_car_red += car_red_speed
    y_car_grey += car_grey_speed
    y_moto1 += moto1_speed
    y_moto2 += moto2_speed
    
    if y_car_blue >= 680:
        y_car_blue = randint(-750,-150) 
        lista1 = [(LEFT_POS), (MID_POS), (RIGHT_POS)]
        posblue = randint(0,2)
        x_car_blue = lista1[posblue]
        
    if y_car_red >= 680:
        y_car_red = randint(-3750,-1000)
        lista2 = [(LEFT_POS), (MID_POS), (RIGHT_POS)]
        posred = randint(0,2)
        x_car_red = lista2[posred]
    
    if y_car_grey >= 680:
        y_car_grey = randint(-450,-100)
        lista3 = [(LEFT_POS), (MID_POS), (RIGHT_POS)]
        posgrey = randint(0,2)
        x_car_grey = lista3[posgrey]
        
    if y_moto1 >= 680:
        y_moto1 = randint(-800, -250)
        lista4 = [(LEFT_POS), (MID_POS), (RIGHT_POS), (FAIXA1_POS), (FAIXA2_POS)]
        posmoto1 = randint(0,4)
        x_moto1 = lista4[posmoto1]
        
    if y_moto2 >= 680:
        y_moto2 = randint(-1200, -400)
        lista5 = [(LEFT_POS), (MID_POS), (RIGHT_POS), (FAIXA1_POS), (FAIXA2_POS)]
        posmoto1 = randint(0,4)
        x_moto2 = lista5[posmoto1]
      
    
    
    """Descida de itens do cenário"""
    fxm_y += fxm_speed
    if fxm_y >= 680:
        fxm_y = -50
        
    y_arvore += arvore_speed
    if y_arvore >= 680:
        y_arvore = -450
        
    y_casa += casa_speed
    if y_casa >= 680:
        y_casa = -600
    
   
    
    
    """Colisão dos carros"""
    if playerbloco.colliderect(blocoblue) or playerbloco.colliderect(blocored) or playerbloco.colliderect(blocogrey) or playerbloco.colliderect(blocomoto1) or playerbloco.colliderect(blocomoto2):
        colisao.play()
        gameover = True
        motor.stop()
        bg_music.stop()
        sleep(1)
        
        msg_gameover = "Game Over!"
        font2 = pygame.font.SysFont("verdana", 25, True, True)
        msg_gameover_render = font2.render(msg_gameover, True, (BRANCO))
        
        msg_gameover2 = "Aperte R para recomeçar..."
        font2 = pygame.font.SysFont("verdana", 25, True, True)
        msg_gameover_render2 = font2.render(msg_gameover2, True, (BRANCO))
        
        msg_quit = "Ou S para sair"
        font2 = pygame.font.SysFont("verdana", 25, True, True)
        msg_quit_render = font2.render(msg_quit, True, (BRANCO))
        
        while gameover:
            tela.fill(AZUL)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        print("Reiniciar")
                        reiniciar()
                    if event.key == K_s:
                        kill()
            
            tela.blit(msg_gameover_render, (LARGURA_WIN/2-280, ALTURA_WIN/2-80))
            tela.blit(msg_gameover_render2, (LARGURA_WIN/2-220, ALTURA_WIN/2-40))
            tela.blit(msg_quit_render, (LARGURA_WIN/2+20, ALTURA_WIN/2))
            pygame.display.flip()
                    
    else:
        pontos += 1
            
        msg_pontos = f"Km: {pontos}"
        font3 = pygame.font.SysFont("verdana", 15, True, True)
        pontos_render = font3.render(msg_pontos, True, (BRANCO))
        
        tela.blit(pontos_render, (10, 10))
                    
    pygame.display.flip()