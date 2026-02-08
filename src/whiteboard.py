import pygame

from .assets import *

class Whiteboard:

    def __init__(self):
        self.image = WHITEBOARD
        self.active = False
        self.rect = self.image.get_rect()

    def open(self):
        self.active = True

    def close(self):
        self.active = False

    def draw(self, screen):
        if self.active:
            self.rect.center = (screen.get_width() // 2, screen.get_height() // 2)
            screen.blit(self.image, self.rect.topleft)
        

