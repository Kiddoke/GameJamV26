


import pygame
from pygame.locals import *
import sys

from Cell import Cell
from CellGrid import CellGrid
from Target import Target


### COLORS
BLACK   = pygame.Color(0, 0, 0)      
WHITE   = pygame.Color(255, 255, 255)
RED     = pygame.Color(255, 0, 0)    
FAINT_RED = pygame.Color(100, 0, 0)

	
### DISPLAY
WIDTH = 1000 + 1 # +1 for last grid line
HEIGHT = 1000 + 1

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
FramePerSec = pygame.time.Clock()


### GRID
ROWS = 9
COLS = 9
CELL_WIDTH = WIDTH // ROWS
CELL_HEIGHT = HEIGHT // COLS

center_x = ROWS // 2
center_y = COLS // 2

targets_pos = [
    ((center_x + dx, center_y + dy), dy == 0)
    for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
]

cell_grid = [[Cell(
                alive = False,
                x = x,
                y = y,
                width = CELL_WIDTH,
                height = CELL_HEIGHT
            ) for x in range(ROWS)] for y in range(COLS)]
targets = []
for (x, y), alive in targets_pos: # level picked
    target = Target(
        alive = alive,
        x = x,
        y = y,
        width = CELL_WIDTH,
        height = CELL_HEIGHT
    )
    cell_grid[x][y] = target
    targets.append(target)

grid = CellGrid(ROWS, COLS, CELL_WIDTH, CELL_HEIGHT, cell_grid)

group = pygame.sprite.Group(iter(grid))

simulate = False
next_generation_counter = 0
grid_update_rate = 5 # 1 slow, 10 fast

generations_since_targets_alive = 0
tolerance = 15

while True:
    events = pygame.event.get()
    
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not simulate : # TRYKK ENTER FOR Å SIMULERE GAME OF LIFE
            simulate = not simulate
            
    
    
    SCREEN.fill(BLACK)
    
    # cells
    for cell in grid:
        if isinstance(cell, Target):
            cell_color = RED if cell.is_alive() else FAINT_RED
        else:
            cell_color = WHITE if cell.is_alive() else BLACK
        pygame.draw.rect(SCREEN, cell_color, cell.rect)
    
    # grid lines
    for y in range(ROWS+1):
        pygame.draw.line(SCREEN, WHITE, (0, y * CELL_HEIGHT), (COLS * CELL_WIDTH, y * CELL_HEIGHT), 1)
    for x in range(COLS+1):
        pygame.draw.line(SCREEN, WHITE, (x * CELL_WIDTH, 0), (x * CELL_WIDTH, ROWS * CELL_HEIGHT), 1)
    
    group.update(events)
    next_generation_counter += 1
    if next_generation_counter >= FPS//10 and simulate:
        grid.update_grid()
        next_generation_counter = 0
        print(list(map(lambda t: t.is_alive(), targets)))
        if any(map(lambda t: t.is_alive(), targets)):
            generations_since_targets_alive = 0
        else:
            generations_since_targets_alive += 1
        if generations_since_targets_alive > tolerance:
            print("WIN")
    
    pygame.display.update()
    FramePerSec.tick(FPS)