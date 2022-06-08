import pygame
from config import *
from pygame.locals import *
from sys import exit

pygame.init()

"""Definições da tela"""
tela = pygame.display.set_mode((LARGURA_WIN, ALTURA_WIN))
pygame.display.set_caption("Mapeamento")

tiles = pygame.image.load("img/itens.png").convert_alpha()
tree = pygame.image.load("img/arvore.png").convert_alpha()
floresta = pygame.image.load("img/floresta.png").convert_alpha()
char = pygame.image.load("img/char.png").convert_alpha()


arvore = tree.subsurface((0,0), (16,16))
arvore_nova = pygame.transform.scale(arvore, (BLK_WIDTH, BLK_HEIGHT))

img_grama_up = tiles.subsurface((16, 128), (16,16))
img_grama_up_nova = pygame.transform.scale(img_grama_up, (BLK_WIDTH, BLK_HEIGHT))

img_vaso = tiles.subsurface((48,48), (16,16))
img_vaso_nova = pygame.transform.scale(img_vaso, (BLK_WIDTH, BLK_HEIGHT))

img_flor = tiles.subsurface((64, 16), (16, 16))
img_flor_nova = pygame.transform.scale(img_flor, (BLK_WIDTH, BLK_HEIGHT))

img_parede = tiles.subsurface((32, 0), (16, 16))
img_parede_nova = pygame.transform.scale(img_parede, (BLK_WIDTH, BLK_HEIGHT))

img_montanha = tiles.subsurface((0, 144), (16, 16))
img_montanha_nova = pygame.transform.scale(img_montanha, (BLK_WIDTH, BLK_HEIGHT))

img_stone = floresta.subsurface((0, 32), (16,16))
img_stone_nova = pygame.transform.scale(img_stone, (BLK_WIDTH, BLK_HEIGHT))

img_grama_montanha = floresta.subsurface((0,0), (16,16))
img_grama_montanha_nova = pygame.transform.scale(img_grama_montanha, (BLK_WIDTH, BLK_HEIGHT))

img_grama = tiles.subsurface((48, 16), (16, 16))
img_grama_nova = pygame.transform.scale(img_grama, (BLK_WIDTH, BLK_HEIGHT))

"""for - que captura os bloquinhos na tela - mapeamento"""
for id_linha, linha in enumerate(mapa):
    for id_coluna, caracter in enumerate(linha):
        cor = PRETO
  
        x = id_coluna * BLK_WIDTH
        y = id_linha * BLK_HEIGHT
        
        if caracter == "p":
            #cor = AMARELO
            tela.blit(img_parede_nova, (x,y))
        if caracter == ".":
            tela.blit(img_grama_nova, (x,y))
        if caracter == "m":
            tela.blit(img_montanha_nova, (x, y))
        if caracter == "u":
            tela.blit(img_grama_up_nova, (x, y))
        if caracter == "f":
            tela.blit(img_flor_nova, (x, y))
        if caracter == "g":
            tela.blit(img_grama_montanha_nova, (x,y))
            
for id_linha, linha in enumerate(itens):
        for id_coluna, caracter in enumerate(linha):
            x = id_coluna * BLK_WIDTH
            y = id_linha * BLK_HEIGHT
            
            if caracter == "v":
                tela.blit(img_vaso_nova, (x,y))
            if caracter == "s":
                tela.blit(img_stone_nova, (x,y))
            if caracter == "t":
                tela.blit(arvore_nova, (x,y))
            
        #r = pygame.Rect((x,y), (BLK_WIDTH, BLK_HEIGHT))
        #pygame.draw.rect(tela, (cor), r, 1)

pygame.display.flip()       

"""Loop principal"""
while True:
    tela.fill(PRETO)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
         
    #pygame.display.flip()