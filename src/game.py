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
from .trashcan import Trashcan
from .bachelor import EndScreen


pygame.init()
vel = 3.5
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # needed here by assets.py What is this??

def main():

    
    pygame.display.set_caption("IFI SPILL")

    menu = create_menu(screen)

    title_screen = True
    while title_screen:
        menu.mainloop(screen)

def create_menu(screen):
    menu = pygame_menu.Menu('IFI SPILL', WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button('Start', start_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    return menu


def start_game():
    run()


def run():

    
    clock = pygame.time.Clock()

    # background + doors
    level = create_level_one()

    # task counter
    finished_tasks = 3
    TOTAL_TASKS = 3

    #objects
    p1 = Player()
    npc1 = NPC(700, 205, OJD_SPRITE_FRONT_LEFT, (60, 90))
    top_bar = BlackBar(0,0, WIDTH, TOP_BAR_HEIGHT, 100)
    bottom_bar = BlackBar(0, HEIGHT - BOTTOM_BAR_HEIGHT, WIDTH, BOTTOM_BAR_HEIGHT)
    level_1_trashcans = level.hall.get_Trashcan()
    t1, t2 = level_1_trashcans[0], level_1_trashcans[1]
    sofa = NPC(180, 435, SOFA, (120, 60))

    wall_thickness = 1
    left_wall = Wall(0,0, wall_thickness, HEIGHT)
    right_wall = Wall(WIDTH - wall_thickness, 0, wall_thickness, HEIGHT)

    all_sprites = pygame.sprite.Group()
    all_other_sprites = pygame.sprite.Group()
    walls = pygame.sprite.Group()

    all_sprites.add(npc1, top_bar, bottom_bar, left_wall, right_wall, t1, p1, t2, sofa)
    all_other_sprites.add(npc1, top_bar, bottom_bar, left_wall, right_wall, t1, t2, sofa)
    walls.add(left_wall, right_wall)

    # healthbar + bottle counter
    bottleCounter = BottleCounter()
    healthbar = Healthbar()


    def draw_frame():
        #screen.fill(WHITE)
        pygame.draw.rect(screen, WHITE, (0, 690, WIDTH, 30))
        all_sprites.draw(screen)
    
    def draw_background():
        level.draw(screen)

        for door in level.hall.doors:
            door.draw(screen)
    
    # draw whiteboard - popup
    def draw_whiteboard():
        for door in level.hall.doors:
            door.draw_popup(screen)

    # update door interaction
    def update_doors():
        for door in level.hall.doors:
            door.update(p1.rect)
            door.interact(keys)

    # close popup if "ESC" pressed
    def close_popup():
        for door in level.hall.doors:
            if door.popup.active and keys[pygame.K_ESCAPE]:
                door.popup.close()
    
    # collect pant
    def collect_pant(p1):
        for pant in level.bottles: # copy list
            if p1.rect.colliderect(pant.rect):
                bottleCounter.add()
                level.bottles.remove(pant)

    # update tasks
    def update_tasks():
        if finished_tasks >= TOTAL_TASKS and p1.rect.right > WIDTH - 2:
            return True
        return False
    
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

        # collect pant
        collect_pant(p1)

        # draw level
        draw_background()
        level.draw(screen)

        draw_frame()

        # checking if u reached the goal
        if update_tasks():
            running = False

        # healthbar + bottle counter 
        draw_health()
        draw_bottleCounter()

        # whiteboard - should be on top of everything else
        draw_whiteboard()
        
        pygame.display.flip()
    
    # end scene
    end_screen = EndScreen(screen)
    end_screen.show()

    pygame.quit()
    sys.exit()
