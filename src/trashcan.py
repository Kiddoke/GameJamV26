import pygame

from .assets import *

class Trashcan(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite=TRASHCAN, offset=0, size=(100,65)):
        super().__init__()
        self.size = size
        self.image = pygame.transform.scale(sprite, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.height -= offset



    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    