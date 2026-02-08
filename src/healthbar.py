import pygame

from .assets import *

class Healthbar:
    def __init__(self):
        self.amount = 3
        self.x = 20
        self.y = 60
        self.full = FULL_HEART
        self.empty = EMPTY_HEART
    
    def wrongAnswer(self):
        if self.amount >= 1:
            self.amount -= 1
        # TODO: loses 3 hearts

    # TODO: connect to player
    def draw(self, screen):
        for i in range(self.amount):
            screen.blit(self.full, (self.x + i * (HEART_SIZE[0] + 5), self.y))