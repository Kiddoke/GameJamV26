import pygame
import pygame_menu
import sys
import time
import os

from .settings import *
from .Player import Player
from .npc import NPC
from .level import create_level_one
from .hall import BlackBar, Wall
from .assets import *
from .bottleCounter import BottleCounter
from .healthbar import Healthbar


pygame.init()
vel = 3.5
screen = pygame.display.set_mode(OPTIONS["resolution"]) # needed here by assets.py What is this??

def main():

    
    pygame.display.set_caption("IFI SPILL")

    menu = create_menu(screen)

    title_screen = True
    while title_screen:
        menu.mainloop(screen)

def create_menu(screen):
    menu = pygame_menu.Menu('IFI SPILL', OPTIONS["resolution"][0], OPTIONS["resolution"][1], theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button('Start', start_game)
    menu.add.button('Settings', lambda: open_settings(menu))
    menu.add.button('Quit', pygame_menu.events.EXIT)

    return menu

def open_settings(menu):
    settings_menu = pygame_menu.Menu(
        'Settings',
        OPTIONS["resolution"][0],
        OPTIONS["resolution"][1],
        theme=pygame_menu.themes.THEME_BLUE
    )

    def set_resolution(value, resolution):
        OPTIONS["resolution"] = resolution
        pygame.display.set_mode(resolution)


    settings_menu.add.selector(
        'Resolution',
        [
            ('800 x 600', (800, 600)),
            ('1024 x 768', (1024, 768)),
            ('1280 x 720', (1280, 720)),
            ('1920 x 1080', (1980, 720))
        ],
        onchange=set_resolution
    )
    
    settings_menu.add.button('Back', menu)
    settings_menu.mainloop(screen)

def start_game():
    run()


def run():

    
    clock = pygame.time.Clock()
    # background + doors
    hall = create_level_one()

    #objects
    p1 = Player()
    npc1 = NPC(OJD_SPRITE_FRONT_LEFT)
    top_bar = BlackBar(0,0, OPTIONS["resolution"][0], TOP_BAR_HEIGHT)
    bottom_bar = BlackBar(0, OPTIONS["resolution"][1] - BOTTOM_BAR_HEIGHT, OPTIONS["resolution"][0], BOTTOM_BAR_HEIGHT)

    wall_thickness = 1
    left_wall = Wall(0,0, wall_thickness, OPTIONS["resolution"][1])
    right_wall = Wall(OPTIONS["resolution"][0] - wall_thickness, 0, wall_thickness, OPTIONS["resolution"][1])

    all_sprites = pygame.sprite.Group()
    all_other_sprites = pygame.sprite.Group()
    walls = pygame.sprite.Group()

    all_sprites.add(p1, npc1, top_bar, bottom_bar, left_wall, right_wall)
    all_other_sprites.add(npc1, top_bar, bottom_bar, left_wall, right_wall)
    walls.add(left_wall, right_wall)

    # healthbar + bottle counter
    bottleCounter = BottleCounter()
    healthbar = Healthbar()


    def draw_frame():
        #screen.fill(WHITE)
        pygame.draw.rect(screen, WHITE, (0, 690, OPTIONS["resolution"][0], 30))
        all_sprites.draw(screen)
    
    def draw_background():
        hall.draw(screen)

        for door in hall.doors:
            door.draw(screen)

    # update door interaction
    def update_doors():
        for door in hall.doors:
            door.update(p1.rect)
            door.interact(keys)

    # close popup if "ESC" pressed
    def close_popup():
        for door in hall.doors:
            if door.popup.active and keys[pygame.K_ESCAPE]:
                door.popup.close()
    
    # health bar
    def draw_health():
        healthbar.draw(screen)
    
    # counter for pant
    def draw_bottleCounter():
        bottleCounter.draw(screen)


    running = True
    while running:
        clock.tick(FRAMERATE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        p1.update(keys, vel, all_other_sprites)

        # whiteboard popup
        update_doors()
        close_popup()

        # draw hall 
        draw_background()

        hall.draw(screen)

        # healthbar + bottle counter
        draw_health()
        draw_bottleCounter()

        draw_frame()
        pygame.display.flip()

    pygame.quit()
    sys.exit()
