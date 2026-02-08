import pygame 

from .assets import *

class NPC(pygame.sprite.Sprite):

    def __init__(self, sprite):
        super().__init__()
        self.x = 200    
        self.y = 200

        self.size = (60, 90)
        self.direction = "left"
        self.image = pygame.transform.scale(sprite, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200


