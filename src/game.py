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
from .bachelor import EndScreen
from .quiz import run_quiz


pygame.init()
vel = 3.5
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # needed here by assets.py What is this??
QUIT_GAME = True

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
    finished_tasks = 2
    TOTAL_TASKS = 3

    #objects
    p1 = Player()
    npc1 = NPC(OJD_SPRITE_FRONT_LEFT)
    top_bar = BlackBar(0,0, WIDTH, TOP_BAR_HEIGHT)
    bottom_bar = BlackBar(0, HEIGHT - BOTTOM_BAR_HEIGHT, WIDTH, BOTTOM_BAR_HEIGHT)

    wall_thickness = 1
    left_wall = Wall(0,0, wall_thickness, HEIGHT)
    right_wall = Wall(WIDTH - wall_thickness, 0, wall_thickness, HEIGHT)

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
        nonlocal finished_tasks # refererer til run() sin variabel
        # door 1: quiz
        door1 = level.hall.doors[0]
        door1.update(p1.rect)
        door1.interact(keys)

        # quiz
        if door1.popup.active and keys[pygame.K_e]:
            correct = run_quiz(screen, door1.popup.rect)

            if correct:
                finished_tasks += 1  # mark task done

            door1.popup.close()

        door2 = level.hall.doors[1]
        door2.update(p1.rect)
        door2.interact(keys)

        door3 = level.hall.doors[2]
        door3.update(p1.rect)
        door3.interact(keys)


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
            QUIT_GAME = False
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

        # whiteboard popup
        update_doors()
        close_popup()
        
        pygame.display.flip()
    
    # end scene
    end_screen = EndScreen(screen)

    if finished_tasks == TOTAL_TASKS:
        end_screen.show()

    pygame.quit()
    sys.exit()
