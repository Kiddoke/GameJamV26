import pygame
import sys

from .settings import *
from .assets import *

class GameOver:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(PIXELFONT, 60)
        self.text1 = self.font.render("UNEMPLOYMENT", True, WHITE)
    
    def show(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.draw()
            pygame.display.flip()
    
    def draw(self):
        self.screen.fill(BLACK)
        text_rect = self.text1.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(self.text1, text_rect.topleft)


            
