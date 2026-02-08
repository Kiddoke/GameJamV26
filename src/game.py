import pygame
import pygame_menu
import sys

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
from .quiz import run_quiz
from .gameover import GameOver


pygame.init()
vel = 3.5
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 


def main():

    pygame.display.set_caption("CYCLE of IFI")

    menu = create_menu(screen)

    title_screen = True
    while title_screen:
        menu.mainloop(screen)


def create_menu(screen):
    mytheme = pygame_menu.Theme(
        background_color=(0, 0, 0, 0),
        title_background_color=(4, 47, 126),
    )

    myimage = pygame_menu.baseimage.BaseImage(
        image_path="./assets/sprites/ifi_pixel.png",
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_CENTER,
    )

    mytheme.background_color = myimage

    menu = pygame_menu.Menu("CYCLE of IFI", WIDTH, HEIGHT, theme=mytheme)

    menu.add.button("START", start_game)
    menu.add.button("QUIT", pygame_menu.events.EXIT)

    return menu


def start_game():
    run()


def run():

    tasks_font = pygame.font.Font(PIXELFONT, 40)
    exchange_font = pygame.font.Font(PIXELFONT, 30)
    clock = pygame.time.Clock()

    # background + doors
    level = create_level_one()

    # task counter
    finished_tasks = 0
    TOTAL_TASKS = 3

    # objects
    p1 = Player()
    npc1 = NPC(700, 205, (60, 90))
    top_bar = BlackBar(0, 0, WIDTH, TOP_BAR_HEIGHT, 100)
    bottom_bar = BlackBar(0, HEIGHT - BOTTOM_BAR_HEIGHT, WIDTH, BOTTOM_BAR_HEIGHT)
    level_1_trashcans = level.hall.get_Trashcan()
    t1, t2 = level_1_trashcans[0], level_1_trashcans[1]
    sofa = Trashcan(180, 435, SOFA, size=(120, 60))
    arrow = Trashcan(650, 325, ARROW_RIGHT, size=(120,60))

    wall_thickness = 1
    left_wall = Wall(0, 0, wall_thickness, HEIGHT)
    right_wall = Wall(WIDTH - wall_thickness, 0, wall_thickness, HEIGHT)

    all_sprites = pygame.sprite.Group()
    all_other_sprites = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    win_arrow = pygame.sprite.Group()

    all_sprites.add(npc1, top_bar, bottom_bar, left_wall, right_wall, t1, p1, t2, sofa)
    all_other_sprites.add(
        npc1, top_bar, bottom_bar, left_wall, right_wall, t1, t2, sofa
    )
    walls.add(left_wall, right_wall)
    win_arrow.add(arrow)

    # healthbar + bottle counter
    bottleCounter = BottleCounter()
    healthbar = Healthbar()

    def play_music():
        try: 
            pygame.mixer.music.load('assets/sprites/background_music.mp3')
        except pygame.error as e:
            print(f"Cannot load music file: {e}")
            sys.exit()
        pygame.mixer.music.play(-1)

    # play music
    play_music()

    def draw_frame():
        # screen.fill(WHITE)
        pygame.draw.rect(screen, WHITE, (0, 690, WIDTH, 30))
        all_sprites.draw(screen)

    def draw_task_counter():
        text = f"AAR: {finished_tasks}/{TOTAL_TASKS}"
        text_surf = tasks_font.render(text, True, WHITE)
        screen.blit(text_surf, (365, 60))

    # pant til hjerte
    def draw_exchange():
        text = f"PSST. Collect 3 pant to exchange for 1 life."
        text_surf = exchange_font.render(text, True, WHITE)
        screen.blit(text_surf, (20, 570))

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
        nonlocal finished_tasks  # refererer til run() sin variabel
        # door 1: quiz
        door1 = level.hall.doors[0]
        door1.update(p1.rect)
        door1.interact(keys)

        # quiz
        if door1.popup.active and keys[pygame.K_e]:
            correct = run_quiz(screen, door1.popup.rect)

            if correct:
                finished_tasks = min(
                    finished_tasks + 1, TOTAL_TASKS
                )  # mark task done            else:
            else:
                healthbar.lose_life()

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
        for pant in level.bottles:  # copy list
            if p1.rect.colliderect(pant.rect):
                bottleCounter.add()
                level.bottles.remove(pant)

    # update tasks
    def update_tasks():
        if finished_tasks >= TOTAL_TASKS and p1.rect.right > WIDTH - 2:
            QUIT_GAME = False
            return True
        return False

    def exchange_bottles_for_life():
        while bottleCounter.count >= 3 and healthbar.amount < 3:
            bottleCounter.count -= 3
            healthbar.add_life(1)

    # health bar
    def draw_health():
        healthbar.draw(screen)

    # counter for pant
    def draw_bottleCounter():
        bottleCounter.draw(screen)

    # check health to see if u dead or still alive
    def check_health():
        if healthbar.amount <= 0:
            game_over_screen = GameOver(screen)
            game_over_screen.show()
            running = False

    running = True
    while running:
        clock.tick(FRAMERATE)

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        p1.update(keys, vel, all_other_sprites)
        npc1.update(p1)

        # collect pant
        collect_pant(p1)
        exchange_bottles_for_life()

        # draw level
        draw_background()
        level.draw(screen)

        draw_frame()
        if finished_tasks == TOTAL_TASKS:
            win_arrow.draw(screen)

        draw_task_counter()
        draw_exchange()

        # checking if u reached the goal
        if update_tasks():
            running = False

        # healthbar + bottle counter
        draw_health()
        draw_bottleCounter()

        check_health()

        # whiteboard - should be on top of everything else
        draw_whiteboard()

        # whiteboard popup
        update_doors()
        close_popup()

        level.hall.update(events)

        pygame.display.flip()

    # end scene
    end_screen = EndScreen(screen)

    if finished_tasks == TOTAL_TASKS:
        end_screen.show()

    pygame.quit()
    sys.exit()
