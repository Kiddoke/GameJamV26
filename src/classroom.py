import pygame
from .settings import *

class Classroom:

    def __init__(self, x, y, image, name, popup):
        super().__init__()
        self.name = name
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))
        self.popup = popup
        self.highlighted = False

    def update(self, player_rect):
        self.highlighted = self.rect.colliderect(player_rect.inflate(40,40))
    
    # press 'E'
    def interact(self, key_pressed):
        if self.highlighted and key_pressed[pygame.K_e]:
            self.popup.open()
    
    def draw(self, screen):
        if self.highlighted:
            pygame.draw.rect(screen, (255, 255, 0), self.rect.inflate(10, 10))
        
        # door
        screen.blit(self.image, self.rect.topleft)

        # popup if active
        self.popup.draw(screen)
    

        


