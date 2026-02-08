import pygame

from .assets import *
from .settings import *

class Whiteboard:

    def __init__(self):
        self.image = WHITEBOARD
        self.active = False
        self.rect = self.image.get_rect()

        self.text = "Press ESC to close"
        self.font = pygame.font.Font(PIXELFONT, 24)


    def open(self):
        self.active = True

    def close(self):
        self.active = False

    def draw(self, screen):
        if self.active:
            self.rect.center = (screen.get_width() // 2, screen.get_height() // 2)
            screen.blit(self.image, self.rect.topleft)

            text_surf = self.font.render(self.text, True, WHITE)
            text_rect = text_surf.get_rect(center=(self.rect.centerx, self.rect.top - 15))

            screen.blit(text_surf, text_rect.topleft)
        

