import pygame, sys

class Game:
    def __init__(self):

        pygame.init()
        self.tela = pygame.display.set_mode((500,500))
        self.clock = pygame.time.Clock()

    def fade(self):
        fade = pygame.Surface((500,500))
        fade.fill((0,0,0))
        for alpha in range(0, 300):
            fade.set_alpha(alpha)
            redrawWindow()
            self.tela.blit(fade, (0,0))
            pygame.display.flip()
            pygame.time.delay(5)
        return
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    fade()

            self.tela.fill((0,0,150))
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()

    
"""
import turtle

class Game:
    def __init__(self):
        self.fd = turtle.fd(0)
        self.speed = turtle.speed(0)
        self.bgcolor = turtle.bgcolor("red")

    def run(self):
        fd = self.fd
        speed = self.speed
        bg = self.bgcolor

        delay = raw_input("Pressione enter para sair >< ")


if __name__ == "__main__":
    game = Game()
    game.run()
"""
