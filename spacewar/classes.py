import pygame as pg
import time
from random import randint, randrange
from pygame.locals import *

class Player:
    def __init__(self, tela, branco, azul, verde, tecla_a, tecla_d, tecla_s, tecla_w, px, py, hp, pontos, fps):    
        self.tela = tela
        self.fps = fps
        self.pontos = pontos
        self.hp = hp
        self.vidas = 3
        self.player_speed = 5
        self.player_lar = 30
        self.player_alt = 30
        self.px = px
        self.py = py
        self.branco = branco
        self.azul = azul
        self.verde = verde
        self.bg_hp_x = 35
        self.bg_hp_y = 12
        self.bg_hp_lar = 100
        self.hp_alt = 10
        self.tecla_a = tecla_a
        self.tecla_d = tecla_d
        self.tecla_w = tecla_w
        self.tecla_s = tecla_s
        self.endgame = False
        
        self.bg_bar = pg.Rect((self.bg_hp_x, self.bg_hp_y), (self.bg_hp_lar, self.hp_alt))
        #self.life_bar = pg.Rect((self.bg_hp_x, self.bg_hp_y), (self.hp_lar, self.hp_alt))
        
        self.player = pg.Rect((self.px, self.py), (self.player_lar, self.player_alt))
    
    
    def drawPlayer(self):
        self.player = pg.Rect((self.px, self.py), (self.player_lar, self.player_alt))
        nave = pg.draw.rect(self.tela, self.branco, self.player)
    
    def move(self):
        if self.tecla_a == "a":
            if pg.key.get_pressed()[K_a]:
                self.px -= self.player_speed
        if self.tecla_d == "d":
            if pg.key.get_pressed()[K_d]:
                self.px += self.player_speed
        if self.tecla_w == "w":
            if pg.key.get_pressed()[K_w]:
                self.py -= self.player_speed
        if self.tecla_s == "s":
            if pg.key.get_pressed()[K_s]:
                self.py += self.player_speed
            
    def limitMove(self):
        if self.px >= 460:
            self.px = 460
        if self.px <= 10:
            self.px = 10
        if self.py >= 555:
            self.py = 555
        if self.py <= 10:
            self.py = 10
        
    def draw_hp_bar(self):
        self.bg_bar1 = pg.draw.rect(self.tela, self.branco, self.bg_bar)
        self.life_bar1  = pg.draw.rect(self.tela, self.verde, (self.bg_hp_x, self.bg_hp_y, self.hp, self.hp_alt))
    
    def label_hp(self): 
        texto = "HP:"
        font = pg.font.SysFont("verdana", 10, True, False)
        texto_render = font.render(texto, True, self.branco)
        label = self.tela.blit(texto_render, (10,10))
        
    def nivelHp(self):
        texto = f"{self.hp}%"
        font = pg.font.SysFont("verdana", 10, True, False)
        texto_render = font.render(texto, True, (self.azul))
        label = self.tela.blit(texto_render, (70,10))
        
    def label_balas(self):
        texto = f"LIFES: {self.vidas}"
        font = pg.font.SysFont("verdana", 10, True, False)
        texto_render = font.render(texto, True, self.branco)
        label = self.tela.blit(texto_render, (10,30))
    
    def label_pontos(self):
        self.pontos += 1
        texto = f"SCORE: {self.pontos}"
        font = pg.font.SysFont("verdana", 10, True, False)
        texto_render = font.render(texto, True, self.branco)
        label = self.tela.blit(texto_render, (10,50))
    
    def label_fps(self):
        texto = f"FPS: {self.fps}"
        font = pg.font.SysFont("verdana", 10, True, False)
        texto_render = font.render(texto, True, self.branco)
        label = self.tela.blit(texto_render, (10,70))
            
    def gameover(self):
        if self.vidas <= 2:
            self.endgame = True
        
    def label_gameover(self):
        texto = "GAME OVER!"
        font = pg.font.SysFont("verdana", 25, True, False)
        texto_render = font.render(texto, True, self.branco)
        label = self.tela.blit(texto_render, (170,270))

class Asteroide:
    def __init__(self, tela, cor, x, y, lar, alt):
        self.tela = tela
        self.cor = cor
        
        self.speed = 10
        self.x = x
        self.y = y
        self.lar = lar
        self.alt = alt
        
        self.enemy = pg.Rect((self.x, self.y), (self.lar, self.alt))
        
        
    def draw(self): 
        self.enemy = pg.Rect((self.x, self.y), (self.lar, self.alt))
        ast = pg.draw.rect(self.tela, self.cor, self.enemy)
        
    
    def move(self):
        self.y += self.speed
        
        if self.y >= 600:
            self.y = randrange(-500,0,30)
            self.x = randrange(30,470,20)


class Itens:
    def __init__(self):
        pass