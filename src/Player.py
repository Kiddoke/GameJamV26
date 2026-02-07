import pygame

from .assets import *
from .settings import *



class Player:
    
    def __init__(self):
        self.x = 50
        self.y = 50
        self.width = 40
        self.height = 50
        # self.sprite = pygame.transform.scale(PLAYER_SPRITE, self.size)
        self.color = (255, 0, 0)



    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))