import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#Dimensionando a tela principal
larguraWin = 480
alturaWin = 700

tela = pygame.display.set_mode((larguraWin, alturaWin))
titulo = pygame.display.set_caption("SpaceWar Versão 1.0 - By Lairon Souza")

#Setando cores
preto = (0,0,0)

cor_tela = preto

#Chamadas de arquivos de midia do jogo
bg = pygame.image.load("assets/space.jpg")
bg = pygame.transform.scale(bg, (larguraWin, alturaWin))

fps = pygame.time.Clock()


#Chamadas para classes e funções do jogo
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        
        self.image = pygame.image.load("assets/nave.png")
        self.rect = self.image.get_rect()
        self.rect.top = alturaWin/2+220
        self.rect.left = larguraWin/2-20
        self.image = pygame.transform.scale(self.image, (154-100, 224-130))
    
    def movendo(self):
        if pygame.key.get_pressed()[K_w]:
            self.rect.top +=  -10
        if pygame.key.get_pressed()[K_s]:
            self.rect.top += +10
        if pygame.key.get_pressed()[K_a]:
            self.rect.left += -10
        if pygame.key.get_pressed()[K_d]:
            self.rect.left += +10
            
    def atirar(self):
        ...
        
    def update(self):
        ...


class Tiro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("assets/tiro.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (7,7))
        
        
    def update(self):
        ...
            
            
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("assets/asteroid.png")
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = larguraWin/2
        self.image = pygame.transform.scale(self.image, (50,50))
        
    def update(self):
        self.rect.y = self.rect.y + 1
        
        if self.rect.y > alturaWin:
            self.kill()
 

     
  
#Chamadas de classes e objetos
tiro = Tiro()
grupo_tiro = pygame.sprite.GroupSingle(tiro)

asteroid = Asteroid()
grupo_asteroid = pygame.sprite.GroupSingle(asteroid)

nave = Nave()
grupo_nave = pygame.sprite.GroupSingle(nave)



#Desenhando a Tela principal do jogo no loop principal While
while True:
    fps.tick(60)
    tela.fill(cor_tela)
    tela.blit(bg, (0,0)) 
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        #Controles da nave
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                print("atirou")
           
        nave.movendo()   
            
    
    #Exibindo os itens na tela
    grupo_nave.draw(tela)
    grupo_nave.update()
    grupo_asteroid.draw(tela)
    grupo_asteroid.update()
    grupo_tiro.draw(tela)
    grupo_tiro.update()
    

    pygame.display.flip()        