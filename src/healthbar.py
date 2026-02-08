import pygame

from .assets import *

class Healthbar:
    def __init__(self):
        self.total = 3
        self.amount = 3
        self.x = 20
        self.y = 60
        self.full = FULL_HEART
        self.empty = EMPTY_HEART
    
    def lose_life(self):
        if self.amount >= 1:
            self.amount -= 1
    
    def add_life(self, amount = 1):
        self.amount = min(self.total, self.amount + amount) # no more than 3

    # TODO: connect to player
    def draw(self, screen):
        for i in range(self.total):
            if i < self.amount:
                screen.blit(self.full, (self.x + i * (HEART_SIZE[0] + 5), self.y))
            else:
                screen.blit(self.empty, (self.x + i * (HEART_SIZE[0] + 5), self.y))
                