import pygame
from pygame.locals import *
from sys import exit

pygame.init()

"""Definindo a tela"""
larguraWin = 650
alturaWin = 400

tela = pygame.display.set_mode((larguraWin, alturaWin))
titulo = pygame.display.set_caption("Pong 2")
font = pygame.font.SysFont("arial", 30, True, True)
fps = pygame.time.Clock()

"""Setando cores do jogo"""
branco = (255,255,255)
violeta = (107,35,142)
azul = (0,0,156)
amarelo = (255.255,0)
cor_bola = branco
cor_raquete = branco
cor_tela = branco

y_player1 = alturaWin/2-60
y_player2 = alturaWin/2-60

bola = pygame.Rect(larguraWin/2-10, alturaWin/2-10, 10,10)
bola_velx = 10
bola_vely = 10

pontosP1 = 0
pontosP2 = 0


"""Desenhando a tela principal"""
while True:
    mensagem = f"{pontosP1} - {pontosP2}"
    texto_pronto = font.render(mensagem, True, (255,255,255))
    fps.tick(40)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    player1 = pygame.draw.rect(tela, cor_raquete, (0, y_player1, 10,120))
    player2 = pygame.draw.rect(tela, cor_raquete, (larguraWin-10, y_player2, 10,120))
    linha = pygame.draw.line(tela, branco, (325,0), (325,400))
    ball = pygame.draw.ellipse(tela, cor_bola, bola)
    
    if pygame.key.get_pressed()[K_w]:
        y_player1 += -10
    if pygame.key.get_pressed()[K_s]:
        y_player1 += 10
    if pygame.key.get_pressed()[K_UP]:
        y_player2 += -10
    if pygame.key.get_pressed()[K_DOWN]:
        y_player2 += 10
    
    if y_player1 <= 0:
        y_player1 = 5
    if y_player1 >= 280:
        y_player1 = 275
    
    if y_player2 <= 0:
        y_player2 = 5
    if y_player2 >= 280:
        y_player2 = 275
    
    """Movendo a bola na diagonal"""   
    bola.x += bola_velx
    bola.y += bola_vely
    
    """Tabelando a bola"""
    if bola.top <= 0 or bola.bottom >= alturaWin:
        bola_vely *= -1
    if bola.left <= 0 or bola.right >= larguraWin:
        bola_velx *= -1
            
    """Colisão da bola na raquete"""
    if bola.colliderect(player1) or bola.colliderect(player2):
        bola_velx *= -1
        
    """Sistema de 
    pontuação"""
    if ball.left <= 0:
        pontosP2 += 1
        print(f"O player 1 marcou: {pontosP1}")
    if ball.right >= larguraWin:
        pontosP1 += 1
        print(f"O PLAYER 2 marcou: {pontosP2}")
    
    
    
    tela.blit(texto_pronto, (290, 20))
    pygame.display.update()
    