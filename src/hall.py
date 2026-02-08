import pygame

from .settings import * 
from .assets import * 

class Hall:
    def __init__(self, name):
        self.name = name
        self.image = HALLWAY
        self.x = 0
        self.y = 105
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.doors = []
        self.trashcans = []
    
    def add_door(self, door):
        self.doors.append(door)
    
    def add_trashcan(self, trashcan):
        self.trashcans.append(trashcan)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        # tegne dørene 
        for door in self.doors:
            door.draw(screen)
        
        # tegne trashcans
        for trashcan in self.trashcans:
            trashcan.draw(screen)
        
class BlackBar(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0,0,0)) #RGB
        self.rect = self.image.get_rect(topleft=(x,y))

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, alpha=0):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(alpha) #Usynlig
        self.rect = self.image.get_rect(topleft=(x,y))