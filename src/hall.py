import pygame
from .settings import * # lage options file der alt statiske verdier er

display = pygame.display.set_mode((WIDTH, HEIGHT)) # statiske verdier, para

class Hall:
    def __init__(self, x, y, image, name):
        self.name = name
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))

        self.doors = pygame.sprite.Group()
    
    def add_door(self, door):
        self.doors.add(door)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        # tegne dørene 
        self.doors.draw(screen)

    # def addClassroom(self, classroom):
        
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