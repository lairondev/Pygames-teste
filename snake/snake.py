import pygame
import pygame, random
from config import *
from pygame.locals import*


def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 470)
    return (x//10 * 10, y//10 * 10)
    
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

class Cobra:
    def __init__(self, my_direction):
        self.velocidade = 10
        self.xcontrol = self.velocidade
        self.ycontrol = 0
        self.snake = [(200, 200), (210, 200), (220, 200)]
        self.snake_skin = pygame.Surface((10, 10))
        self.snake_skin.fill((255,255,255))
        
        self.my_direction = my_direction
    
    def desenha(self):
        for pos in self.snake:
            screen.blit(self.snake_skin, pos)
        
    def move(self):
        if self.my_direction == UP:
            self.snake[0] = (self.snake[0][0], self.snake[0][1] -10)
        if self.my_direction == DOWN:
            self.snake[0] = (self.snake[0][0], self.snake[0][1] +10)
        if self.my_direction == RIGHT:
            self.snake[0] = (self.snake[0][0] +10, self.snake[0][1])
        if self.my_direction == LEFT:
            self.snake[0] = (self.snake[0][0] -10, self.snake[0][1])

pygame.init()
screen = pygame.display.set_mode((LARGURA_WIN, ALTURA_WIN))
pygame.display.set_caption("Jogo da Cobrinha")



apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = LEFT

# Criando objetos
cobra = Cobra(my_direction)


clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT
    
    """if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
    
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
    
"""
    """Movimentação da cobrinha"""    
    cobra.move()
    
    
    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    cobra.desenha()
        
    
    pygame.display.flip()