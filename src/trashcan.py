import pygame

from .assets import *

class Trashcan:
    def __init__(self, x, y):
        self.image = TRASHCAN
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))