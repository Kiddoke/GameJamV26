import pygame
import sys
import time
import os

from .settings import *
from .Player import Player
from .npc import NPC
from .level import create_level_one


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
    npc1 = NPC()
    all_sprites.add(p1)
    all_sprites.add(npc1)
    all_other_sprites.add(npc1)



    def draw_frame():
        #screen.fill(WHITE)
        pygame.draw.rect(screen, WHITE, (0, 690, WIDTH, 30))
        all_sprites.draw(screen)
    
    def draw_background():
        hall.draw(screen)

        for door in hall.doors:
            door.draw(screen)


    running = True
    while running:
        clock.tick(FRAMERATE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        p1.update(keys, vel, all_other_sprites)

        # update door interaction
        for door in hall.doors:
            door.update(p1.rect)
            door.interact(keys)
        
        # close popup if "ESC" pressed
        for door in hall.doors:
            if door.popup.active and keys[pygame.K_ESCAPE]:
                door.popup.close()

        draw_background()

        # black bars
        pygame.draw.rect(screen, (0,0,0), (0,0, WIDTH, TOP_BAR_HEIGHT))
        pygame.draw.rect(screen, (0,0,0), (0, HEIGHT - BOTTOM_BAR_HEIGHT, WIDTH, BOTTOM_BAR_HEIGHT))

        draw_frame()
        pygame.display.flip()

    pygame.quit()
    sys.exit()
