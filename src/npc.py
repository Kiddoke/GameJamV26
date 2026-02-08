import pygame 

from .assets import *

class NPC(pygame.sprite.Sprite):

    def __init__(self, x, y, sprite, size):
        super().__init__()
        self.x = 200    
        self.y = 200

        self.size = size
        self.direction = "left"
        self.image = pygame.transform.scale(sprite, self.size)
        self.rect = self.image.get_rect()
        self.image_offset = pygame.Vector2(0, 100)
        self.rect.x = x
        self.rect.y = y


