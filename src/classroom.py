import pygame
from .settings import *
from .assets import *

class Classroom:

    def __init__(self, x, y, image, name, popup):
        super().__init__()
        self.name = name
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))
        self.popup = popup
        self.highlighted = False

    def update(self, player_rect):
        self.highlighted = self.rect.colliderect(player_rect.inflate(-20,-80))
    
    # press 'E'
    def interact(self, key_pressed):
        if self.highlighted and key_pressed[pygame.K_e]:
            self.popup.open()
    
    def draw(self, screen):
        if self.highlighted:
            pygame.draw.rect(screen, (255, 255, 0), self.rect.inflate(8, 8))

            # text above door
            font = pygame.font.Font(PIXELFONT , 20)
            text = font.render("Press E", True, (255,255,255))
            text_rect = text.get_rect(center=(self.rect.centerx, self.rect.top - 15))
            screen.blit(text, text_rect.topleft)

        # door
        screen.blit(self.image, self.rect.topleft)
    
    def draw_popup(self, screen):
        # popup if active
        self.popup.draw(screen)

    def update_whiteboard(self, events):
        self.popup.update(events)

    

        


