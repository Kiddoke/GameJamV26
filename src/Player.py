import pygame

from .assets import *
from .settings import *



class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = 50
        self.width = 40
        self.height = 50
        self.size = (60, 80)
        self.direction = "down"
        self.sprites = {
            "up" : pygame.transform.scale(PLAYER_SPRITE_BACK_UP, self.size),
            "down" : pygame.transform.scale(PLAYER_SPRITE_FRONT_DOWN, self.size),
            "right" : pygame.transform.scale(PLAYER_SPRITE_FRONT_RIGHT, self.size),
            "left" : pygame.transform.scale(PLAYER_SPRITE_FRONT_LEFT, self.size)
        }

        self.image = self.sprites[self.direction]
        self.rect = self.sprites[self.direction].get_rect()


    def update(self, keys, vel):

        if keys[pygame.K_w]:
            self.rect.y -= vel
            self.direction = "up"
        if keys[pygame.K_s]:
            self.rect.y += vel
            self.direction = "down"

        if keys[pygame.K_d]:
            self.rect.x += vel
            self.direction = "right"
        if keys[pygame.K_a]:
            self.rect.x -= vel
            self.direction = "left"

        self.image = self.sprites[self.direction]
