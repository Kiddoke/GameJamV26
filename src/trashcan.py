import pygame

from .assets import *

class Trashcan:
    def __init__(self, x, y):
        self.image = TRASHCAN
        self.x = x
        self.y = y

        self.bottles = []
    
    def addBottle(self, bottle):
        self.bottles.append(bottle)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

        # tegne pant
        for bottle in self.bottles:
            bottle.draw(screen)