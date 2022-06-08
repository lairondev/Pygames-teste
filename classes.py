import pygame
from pygame.locals import *

pygame.init()

LARGURA = 600
ALTURA = 480

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Estudando Classes")
fps = pygame.time.Clock()

class Personagem:
    def __init__(self, nome, classe, atk, arm, lar, alt, cor, x, y, tela, moveCima, moveBaixo, moveEsquerda, moveDireita):
        self.nome = nome
        self.classe = classe
        self.atk = atk
        self.arm = arm
        self.lar = lar
        self.alt = alt
        self.cor = cor
        self.x = x
        self.y = y
        self.tela = tela
        self.vel = 5
        self.moveCima = moveCima
        self.moveBaixo = moveBaixo
        self.moveEsquerda = moveEsquerda
        self.moveDireita = moveDireita
        self.hp = 80
        self.tiroVel = 10
        self.tirox = self.x
        self.tiroy = self.y

    def infos(self):
        print(self.nome)
        print(self.classe)
        print(self.atk)
        print(self.arm)
        
    def draw(self):
        heroi = pygame.draw.rect(self.tela, self.cor, (self.x, self.y, self.lar, self.alt))
        return heroi

    def drawName(self):
        nome = self.nome
        font = pygame.font.SysFont("arial", 15, True, True)
        render = font.render(nome, True, (255,255,255))
        nome = self.tela.blit(render, (self.x-10,self.y-35))
        return nome

    def move(self):
        if self.moveCima == "w":
            if pygame.key.get_pressed()[K_w]:
                self.y -= self.vel
        if self.moveBaixo == "s":
            if pygame.key.get_pressed()[K_s]:
                self.y += self.vel
        if self.moveEsquerda == "a":
            if pygame.key.get_pressed()[K_a]:
                self.x -= self.vel
        if self.moveDireita == "d":
            if pygame.key.get_pressed()[K_d]:
                self.x += self.vel

        if self.moveCima == "up":
            if pygame.key.get_pressed()[K_UP]:
                self.y -= self.vel
        if self.moveBaixo == "down":
            if pygame.key.get_pressed()[K_DOWN]:
                self.y += self.vel
        if self.moveEsquerda == "left":
            if pygame.key.get_pressed()[K_LEFT]:
                self.x -= self.vel
        if self.moveDireita == "right":
            if pygame.key.get_pressed()[K_RIGHT]:
                self.x += self.vel

    def lifeBar(self):
        bgBar = pygame.draw.rect(self.tela, (255,255,255), (self.x-30, self.y-15, 80, 8))
        lifeBar = pygame.draw.rect(self.tela, (0,255,0), (self.x-30, self.y-15, self.hp, 8))
        if self.y <= 200:
            self.hp -= 2
        if self.hp <= 0:
            self.hp = 80

    def atirar(self):
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_r:
                    return True

    def tiro(self):
        tiro = pygame.draw.rect(self.tela, (255,255,255), (self.tirox, self.tiroy, 5, 5))
        self.tirox += self.tiroVel
                

heroi = Personagem("Twitch", "Atirador", 540, 150, 20, 40, (0,196,49), LARGURA/2-200, ALTURA/2, tela, "w", "s", "a", "d")
heroi2 = Personagem("Kaisa", "Atirador", 420, 150, 20, 40, (128,0,128), LARGURA/2+200, ALTURA/2, tela, "up", "down", "left", "right")


while True:
    tela.fill((0,0,0))
    fps.tick(60)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if heroi.atirar() == True:
            heroi.tiro()
    
    heroi.draw()
    heroi.drawName()
    heroi.lifeBar()
    heroi.move()
    #heroi.atirar()
    
    heroi2.draw()
    heroi2.drawName()
    heroi2.lifeBar()
    heroi2.move()
    
    pygame.display.flip()
