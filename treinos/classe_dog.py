import pygame as pg
from pygame.locals import *

pg.init()
tela = pg.display.set_mode((500,500))


class Asteroid:
    def __init__(self, lar, alt, x, y, cor, tela):
        self.lar = lar
        self.alt = alt
        self.x = x
        self.y = y
        self.cor = cor
        self.tela = tela
        self.ast = pg.Rect((self.x, self.y), (self.lar, self.alt))
        
    def draw(self):
        #ast = pg.draw.rect(self.tela, self.cor, (self.x, self.y, self.lar, self.alt))
        ast = pg.draw.rect(self.tela, self.cor, self.ast)


def colisao(asteroide1, asteroide2):
    if asteroide1.colliderect(asteroide2):
        print("Colidiu")
    else:
        print("Não colidiu")


asteroides1 = Asteroid(10, 10, 95, 95, (234,189,98), tela) 
asteroides2 = Asteroid(10, 10, 100, 100, (34,89,198), tela) 
      
asteroides_list = []
asteroides_list.append(asteroides1)
asteroides_list.append(asteroides2)

print(asteroides_list[0].cor)
colisao(asteroides_list[0].ast, asteroides_list[1].ast)


while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pygame.quit()
            
    
    for ast in asteroides_list:
        ast.draw()
    
    pg.display.flip()

