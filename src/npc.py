import pygame 
import time

from .assets import *

class NPC(pygame.sprite.Sprite):

    def __init__(self, x, y, size):
        super().__init__()

        self.size = size
        self.sprites = {
            "tveita1": pygame.transform.scale(LARS_TVEITA_1, self.size),
            "tveita2": pygame.transform.scale(LARS_TVEITA_2, self.size),
        }

        self.mode = "tveita1"
        self.image = self.sprites[self.mode]
        self.rect = self.image.get_rect(topleft=(x, y))

        self.last_switch = pygame.time.get_ticks()
        self.switch_delay = 500  # ms

    def update(self, player):
        now = pygame.time.get_ticks()

        if now - self.last_switch >= self.switch_delay:
            self.mode = "tveita2" if self.mode == "tveita1" else "tveita1"
            self.image = self.sprites[self.mode]
            self.last_switch = now

