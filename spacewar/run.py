import pygame as pg
from time import sleep
from config import *
from pygame.locals import *
from sys import exit
from classes import Player, Asteroide, Itens

pg.init()

"""Definindo tela"""
tela = pg.display.set_mode((LARGURA, ALTURA))
pg.display.set_caption("SPACE WAR")

"""Variáveis de configurações do loop"""
fps = pg.time.Clock()
run = True 
hp = 100
pontos = 0
time = 0
ast_speed = 10
 
"""Criando objetos"""
player = Player(tela, BRANCO, AZUL, VERDE, "a", "d", "s", "w", PX, PY, hp, pontos, time)
player.hp_lar = 100

asteroide1 = Asteroide(tela, (R,G,B), X, Y, 10, 10)
asteroide2 = Asteroide(tela, (R,G,B), X, Y, 10, 10)
asteroide3 = Asteroide(tela, (R,G,B), X, Y, 10, 10)
asteroide4 = Asteroide(tela, (R,G,B), X, Y, 10, 10)
asteroide5 = Asteroide(tela, (R,G,B), X, Y, 10, 10)
asteroide6 = Asteroide(tela, (R,G,B), X, Y, 10, 10)
asteroide7 = Asteroide(tela, (R,G,B), X, Y, 10, 10)

asteroide_list = []
asteroide_list.append(asteroide1)
asteroide_list.append(asteroide2)
asteroide_list.append(asteroide3)
asteroide_list.append(asteroide4)
asteroide_list.append(asteroide5)
asteroide_list.append(asteroide6)
asteroide_list.append(asteroide7)
 

"""Main Loop"""
while run:
    time = fps.tick(FPS)
    player.fps = time
    tela.fill(PRETO)

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
    
    for ast in asteroide_list:
        ast.draw()
        ast.move()
        
        if ast.enemy.colliderect(player.player):
            hp -= 9
            player.hp = hp
            ast.y = randrange(-500,0,30)
            ast.x = randrange(50,500,20)
            
            if player.hp <= 10:
                player.vidas -= 1
                hp = 110
    
    player.drawPlayer()
    player.draw_hp_bar()
    player.move()
    player.label_hp()
    player.label_pontos()
    player.label_fps()
    player.label_balas()
    player.nivelHp()
    player.limitMove()
    player.gameover()
    
    if player.endgame == True:
        while run:
            tela.fill(PRETO)
        
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
            
            for aste in asteroide_list:
                aste.draw()
                aste.move()
                
            player.label_gameover()
            pg.display.flip()
    
    pg.display.flip()