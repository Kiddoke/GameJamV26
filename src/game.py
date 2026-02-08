import pygame
import sys
import time
import os

from .settings import *
from .Player import Player
from .npc import NPC
from .level import create_level_one
from .assets import *


pygame.init()
vel = 3.5


def run():
    pygame.display.set_caption("IFI SPILL")
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # needed here by assets.py What is this??

    clock = pygame.time.Clock()

    # background + doors
    hall = create_level_one()

    #objects
    all_sprites = pygame.sprite.Group()
    all_other_sprites = pygame.sprite.Group()
    p1 = Player()
    npc1 = NPC(OJD_SPRITE_FRONT_LEFT)
    all_sprites.add(p1)
    all_sprites.add(npc1)
    all_other_sprites.add(npc1)



    def draw_frame():
        #screen.fill(WHITE)
        pygame.draw.rect(screen, WHITE, (0, 690, WIDTH, 30))
        all_sprites.draw(screen)


    running = True
    while running:
        clock.tick(FRAMERATE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        p1.update(keys, vel, all_other_sprites)

        hall.draw(screen)

        # black bars
        pygame.draw.rect(screen, (0,0,0), (0,0, WIDTH, TOP_BAR_HEIGHT))
        pygame.draw.rect(screen, (0,0,0), (0, HEIGHT - BOTTOM_BAR_HEIGHT, WIDTH, BOTTOM_BAR_HEIGHT))

        draw_frame()
        pygame.display.flip()

    pygame.quit()
    sys.exit()
