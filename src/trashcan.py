import pygame

from .assets import *

class Trashcan(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite=TRASHCAN, offset=0):
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.height -= 60



    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))