import pygame
from pygame.locals import *
from sys import exit
import os

pygame.init()

maindir = os.path.dirname(__file__)
imgdir = os.path.join(maindir, "assets")

larguraWin = 600
alturaWin = 480
cor_verde = (255,255,255)

tela = pygame.display.set_mode((larguraWin, alturaWin))
titulo = pygame.display.set_caption("Bolinha - by Nel Souza")

sprite_sheet = pygame.image.load(os.path.join(imgdir, "Hadouken3.png")).convert_alpha()

class Bolinha(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgs_bola = []
        for i in range(5):
            img = sprite_sheet.subsurface((i * 32,0), (32,32))
            img = pygame.transform.scale(img, (32*3, 32*3))          
            self.imgs_bola.append(img)
        
        self.index_lista = 0
        self.image = self.imgs_bola[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (250, alturaWin - 200)
        
    def update(self):
        if self.index_lista > 4:
            self.index_lista = 0
            print(999)
        self.index_lista += 0.25
        self.image = self.imgs_bola[int(self.index_lista)]
        
        
todasSprites = pygame.sprite.Group()
bolinha = Bolinha()
todasSprites.add(bolinha)

fps = pygame.time.Clock()
while True:
    fps.tick(27)
    tela.fill(cor_verde)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    todasSprites.draw(tela)
    todasSprites.update()
    pygame.display.flip()
