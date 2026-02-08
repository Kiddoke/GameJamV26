import pygame
from .settings import * # lage options file der alt statiske verdier er

display = pygame.display.set_mode((WIDTH, HEIGHT)) # statiske verdier, para

class Hall:
    def __init__(self, x, y, image, name):
        self.name = name
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))

        self.doors = []
    
    def add_door(self, door):
        self.doors.append(door)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        # tegne dørene 
        for door in self.doors:
            door.draw(screen)
        
