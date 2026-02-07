import pygame
import sys
import time
import os

from .settings import *
from .Player import Player


pygame.init()
vel = 3.5


def run():
    pygame.display.set_caption("IFI SPILL")
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # needed here by assets.py What is this??

    clock = pygame.time.Clock()


    #objects
    all_sprites = pygame.sprite.Group()
    p1 = Player()
    all_sprites.add(p1)

    def draw_frame():
        screen.fill(WHITE)
        pygame.draw.rect(screen, WHITE, (0, 690, WIDTH, 30))
        all_sprites.draw(screen)


    running = True
    while running:
        clock.tick(FRAMERATE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        p1.update(keys, vel)


        draw_frame()
        pygame.display.flip()

    pygame.quit()
    sys.exit()
