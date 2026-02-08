import pygame

from .assets import *

class Pant:
    def __init__(self, x, y, image, value = 1, offset=0):
        self.x = x
        self.y = y
        self.image = image
        self.value = value

        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.collected = False
        self.rect.height += offset
        print(self.rect.height)

    def draw(self, screen):
        if not self.collected:
            screen.blit(self.image, (self.x, self.y))