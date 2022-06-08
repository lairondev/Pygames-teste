import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 850
altura = 580
branco = (255,255,255)
lilas = (78,89,167)
verde = (0,255,0)


tela = pygame.display.set_mode((largura, altura))
titulo = pygame.display.set_caption("Pong para 2")

"""Jogadores"""
x_raquete1 = 10
y_raquete1 = altura/2 - 75


player1 = pygame.Rect(10, altura/2 - 75, 15,150)
player2 = pygame.Rect(largura - 25, altura/2 - 75, 15,150)
player1_speed = 0
player2_speed = 0

ball = pygame.Rect(largura/2-10, altura/2-10, 20,20)
ball_speedx = 10
ball_speedy = 10


def bola():
    global ball_speedx, ball_speedy
    
    """Movendo a bola na diagonal"""
    ball.x += ball_speedx
    ball.y += ball_speedy
    
    """Tabelando a bola"""
    if ball.top <= 0 or ball.bottom >= altura:
        ball_speedy *= -1
    if ball.left <= 0 or ball.right >= largura:
        ball_speedx *= -1
        
        
    """Colisão da bola na raquete"""
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speedx *= -1
        
        
fps = pygame.time.Clock()

while True:
    fps.tick(60)
    tela.fill(lilas)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:  
            if event.key == pygame.K_w:
                player1_speed += -7
            if event.key == pygame.K_s:
                player1_speed += 7
            if event.key == pygame.K_UP:
                player2_speed += -7
            if event.key == pygame.K_DOWN:
                player2_speed += 7
        
    
    bola()
    player1.y += player1_speed
    player2.y += player2_speed
    
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= altura:
        player1.bottom = altura
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= altura:
        player2.bottom = altura
    """ 
    Controle raquete direita
    if pygame.key.get_pressed()[K_UP]:
        y_raquete2 -= 10
    if pygame.key.get_pressed()[K_DOWN]:
        y_raquete2 += 10"""
        
    """Limitando área de colisão das raquetes"""
    
    
    pygame.draw.rect(tela, branco, player1)
    pygame.draw.rect(tela, branco, player2)
    pygame.draw.ellipse(tela, verde, ball)
    
    #raquete1 = pygame.draw.rect(tela, branco, (x_raquete1,y_raquete1,40,150))
    #raquete2 = pygame.draw.rect(tela, branco, (x_raquete2,y_raquete2,40,150))
    #bola = pygame.draw.rect(tela, verde, (x_bola, y_bola,20,20))
    
    """if y_bola >= altura:
        y_bola = 0
    y_bola += 5"""
            
    pygame.display.flip()