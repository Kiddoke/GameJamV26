import pygame
from .settings import *

class Classroom(pygame.sprite.Sprite):

    def __init__(self, x, y, image, name):
        super().__init__()
        self.name = name
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))
    
    # press 'E'
    def interact(self):
        print(f"Entering {self.name}")
        # white board pop up

