import pygame
import sys

from .settings import *
from .assets import *

class EndScreen:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.jobb = JOBB
        self.diploma = DIPLOMA

        self.rect = self.diploma.get_rect(center=(WIDTH//2, HEIGHT//2))

        # font
        self.font = pygame.font.Font(PIXELFONT, 40)
        self.text1 = self.font.render("YOU GOT UR BACHELOR!", True, WHITE)

        # Timing
        self.start_time = pygame.time.get_ticks()
        self.display_time = 3000
        self.fade_time = 2000

        self.alpha = 255
        self.state = "first"
    
    def show(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.update()
            self.draw()

            pygame.display.flip()

    def update(self):
        current_time = pygame.time.get_ticks()

        if self.state == "first":
            if current_time - self.start_time > self.display_time:
                self.state = "fade"
                self.fade_start = current_time
        
        elif self.state == "fade":
            elapsed = current_time - self.fade_start
            progress = elapsed / self.fade_time
            self.alpha = max(0, 255 - int(255 * progress))

            if self.alpha == 0:
                self.state = "second"

        elif self.state == "second":
            pass  # waiting to quit
    
    def draw(self):
        self.screen.fill(BLACK)

        if self.state in ("first", "fade"):
            self.diploma.set_alpha(self.alpha)
            self.text1.set_alpha(self.alpha)
            
            self.screen.blit(self.diploma, self.rect)
            self.screen.blit(self.text1, (WIDTH//2 - 100, HEIGHT//2 + 150))

        elif self.state == "second":
            self.screen.blit(self.jobb, self.rect)

            
