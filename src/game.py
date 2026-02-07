import pygame
import sys
import time
import os

from .settings import *
from .Player import Player


pygame.init()
vel = 5


def run():
    pygame.display.set_caption("IFI SPILL")
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # needed here by assets.py What is this??

    clock = pygame.time.Clock()


    #objects
    p1 = Player()


    def draw_frame():
        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, WHITE, (0, 690, WIDTH, 30))
        p1.draw(screen)

    running = True
    while running:
        clock.tick(FRAMERATE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            p1.y -= vel
        if keys[pygame.K_a]:
            p1.x -= vel
        if keys[pygame.K_s]:
            p1.y += vel
        if keys[pygame.K_d]:
            p1.x += vel


        draw_frame()
        pygame.display.flip()

    pygame.quit()
    sys.exit()
