import pygame

from .assets import *
from .settings import *



class Player:

    def __init__(self):
        self.x = 50
        self.y = 50
        self.width = 40
        self.height = 50
        self.size = (60, 80)
        self.sprite = pygame.transform.scale(PLAYER_SPRITE_FRONT_RIGHT, self.size)
        self.direction = "down"

        self.sprites = {
            "up" : pygame.transform.scale(PLAYER_SPRITE_BACK_UP, self.size),
            "down" : pygame.transform.scale(PLAYER_SPRITE_FRONT_DOWN, self.size),
            "right" : pygame.transform.scale(PLAYER_SPRITE_FRONT_RIGHT, self.size),
            "left" : pygame.transform.scale(PLAYER_SPRITE_FRONT_LEFT, self.size)
        }



    def draw(self, screen):
        screen.blit(self.sprites[self.direction], (self.x, self.y))