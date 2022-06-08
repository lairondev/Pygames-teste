import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange

"""Iniciando o pygame / Diretórios"""
pygame.init()
diretorio_principal = os.path.dirname(__file__)
print(f"AQUI >> {diretorio_principal}")
diretorio_imagens = os.path.join(diretorio_principal, "assets")
diretorio_sons = os.path.join(diretorio_principal, "sons")

"""Dimensões que a tela receberá"""
larguraWin = 640
alturaWin = 480

"""Cores"""
branco = (255,255,255)

"""Criando a tela"""
tela = pygame.display.set_mode((larguraWin, alturaWin))
titulo = pygame.display.set_caption("Dino Game")


sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, "dinoSprite.png")).convert_alpha()

"""Classes e Funções"""
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_dino = []
        for i in range(3):
            img = sprite_sheet.subsurface((i * 32,0), (32,32))
            img = pygame.transform.scale(img, (32*3, 32*3))
            self.img_dino.append(img)
            
        self.index_lista = 0
        self.image = self.img_dino[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (100, alturaWin - 90)
        
    def update(self):
        if self.index_lista > 2:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.img_dino[int(self.index_lista)]
        

class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 0), (32,32))
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50, 200, 50)
        self.rect.x = larguraWin - randrange(30, 300, 90)
        
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = larguraWin
            self.rect.y = randrange(50, 200, 50)
        self.rect.x -= 10

"""Variáveis chamadas e etc..."""
todas_sprites = pygame.sprite.Group()
dino = Dino()
todas_sprites.add(dino)

for i in range(4):
    nuvens = Nuvens()
    todas_sprites.add(nuvens)


"""Relógio de FPS"""
fps = pygame.time.Clock()
 
 
"""Loop principal | Desenha a tela no monitor"""
while True:
    fps.tick(30)
    tela.fill(branco)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    todas_sprites.draw(tela)
    todas_sprites.update()
    
    pygame.display.flip()
