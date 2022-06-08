from random import randint, randrange

LARGURA = 500
ALTURA = 600

BRANCO = (255,255,255)
PRETO = (0,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
VERMELHO = (255,0,0)

R = randint(0,255)
G = randint(0,255)
B = randint(0,255)

X = randrange(10,790,30)
Y = randrange(-500,0,30)

PX = LARGURA/2 - 40
PY = ALTURA - 55

FPS = 60