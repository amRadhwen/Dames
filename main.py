from numpy import zeros, flipud
import pygame

WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
DIMENSIONS = (8, 8)

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)

def createBoard(dimensions):
    return flipud(zeros(dimensions))

def fillBoard():
    pass

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Damme V1.0")

#loop controller
gameEnd = False

#clock
clock = pygame.time.Clock()

#change the screen color to white
screen.fill(WHITE)

pygame.draw.line(screen, BLACK, [0, 75], [WIDTH, 75], 5)


#update the display
pygame.display.update()

#Game main loop
while not gameEnd:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            gameEnd = True


pygame.quit()




