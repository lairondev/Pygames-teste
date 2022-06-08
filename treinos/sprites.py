import pygame
from pygame.locals import *
from sys import exit

pygame.init()

"""Dimensões da tela"""
larguraWin = 600
alturaWin = 480

"""Cores"""
preto = (0,0,0)

"""Criando a tela"""
tela = pygame.display.set_mode((larguraWin, alturaWin))
titulo = pygame.display.set_caption("Teste")

class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("assets/attack_1.png"))
        self.sprites.append(pygame.image.load("assets/attack_2.png"))
        self.sprites.append(pygame.image.load("assets/attack_3.png"))
        self.sprites.append(pygame.image.load("assets/attack_4.png"))
        self.sprites.append(pygame.image.load("assets/attack_5.png"))
        self.sprites.append(pygame.image.load("assets/attack_6.png"))
        self.sprites.append(pygame.image.load("assets/attack_7.png"))
        self.sprites.append(pygame.image.load("assets/attack_8.png"))
        self.sprites.append(pygame.image.load("assets/attack_9.png"))
        self.sprites.append(pygame.image.load("assets/attack_10.png"))
 
        self.atual = 0
        self.image = self.sprites[self.atual]
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100
        
        self.animar = False
        
    def atacar(self):
        self.animar = True
        
    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128*3, 64*3))
        
    
    
todas_sprites = pygame.sprite.Group()
sapo = Sapo()
todas_sprites.add(sapo)

fps = pygame.time.Clock()#Preparando função que define o FPS

"""Looping principal que desenha a tela no monitor"""
while True:
    fps.tick(30)#definindo o FPS do jogo
    tela.fill(preto)#definindo cor de fundo da tela
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            sapo.atacar()
        
    todas_sprites.draw(tela)
    todas_sprites.update()
    pygame.display.flip()