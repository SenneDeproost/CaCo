import pygame, sys
from pygame.locals import *

pygame.init()

WHITE=(255,255,255)
BLUE=(0,0,255)

class ScreenSim:

    def __int__(self):
        pygame.init()
        self.display = pygame.display.set_mode((500, 400), 0, 32)
        self.display.fill(WHITE)
        while (True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break

    def draw(self):
        pygame.init()
        pygame.display.flip()

screen = ScreenSim()
screen.draw()


