from random import random
import pygame

from src.gameoflife.Cell import Cell
from src.gameoflife.Target import Target
from src.gameoflife.CellGrid import CellGrid



from .assets import *
from .settings import *

class Whiteboard:

    def __init__(self):
        self.image = WHITEBOARD
        self.active = False
        self.rect = self.image.get_rect()

        self.text = "Press ESC to close"
        self.font = pygame.font.Font(PIXELFONT, 24)


    def open(self):
        self.active = True

    def close(self):
        self.active = False

    def draw(self, screen):
        if self.active:
            self.rect.center = (screen.get_width() // 2, screen.get_height() // 2)
            screen.blit(self.image, self.rect.topleft)

            text_surf = self.font.render(self.text, True, WHITE)
            text_rect = text_surf.get_rect(center=(self.rect.centerx, self.rect.top - 15))

            screen.blit(text_surf, text_rect.topleft)
    
    def update(self, events):
        pass
        

# Brukt AI for å implementere/fikse opp i logikk som allerede var i gameoflife mappen :)
class GameOfLifeWhiteboard(Whiteboard):
    def __init__(self):
        super().__init__()

        # logical grid size
        self.ROWS = 9
        self.COLS = 9

        # simulation state
        self.simulate = False
        self.next_generation_counter = 0
        self.generations = 0
        self.grid_update_rate = 5  # 1 slow, 10 fast
        self.FPS = 60
        self.generations_since_targets_alive = 0
        self.tolerance = 15

        # runtime-created objects (initialized on first draw when sizes are known)
        self.grid = None
        self.targets = []
        self.group = None

    def _init_grid(self, cell_w: int, cell_h: int) -> None:
        if self.grid is not None:
            return

        # build underlying cell_grid matching expected CellGrid layout (grid[x][y])
        cell_grid = [
            [Cell(alive=False, x=x, y=y, width=cell_w, height=cell_h) for y in range(self.COLS)]
            for x in range(self.ROWS)
        ]

        # targets: center and four adjacent; alive when dy == 0
        center_x = self.ROWS // 2
        center_y = self.COLS // 2
        targets_pos = [
            ((center_x + dx, center_y + dy), dy == 0)
            for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
        ]

        self.targets = []
        for (tx, ty), alive in targets_pos:
            if 0 <= tx < self.ROWS and 0 <= ty < self.COLS:
                target = Target(alive=alive, x=tx, y=ty, width=cell_w, height=cell_h)
                cell_grid[tx][ty] = target
                self.targets.append(target)

        self.grid = CellGrid(self.ROWS, self.COLS, cell_w, cell_h, cell_grid)

        # create sprite group if cells are sprites
        self.group = pygame.sprite.Group(list(self.grid))

    def draw(self, screen):
        if not self.active:
            return

        # draw whiteboard background
        self.rect.center = (screen.get_width() // 2, screen.get_height() // 2)
        screen.blit(self.image, self.rect.topleft)

        # colors
        BLACK = pygame.Color(0, 0, 0)
        WHITE = pygame.Color(255, 255, 255)
        RED = pygame.Color(255, 0, 0)
        FAINT_RED = pygame.Color(100, 0, 0)

        # compute drawing area inside the whiteboard with a small padding
        pad = 20
        area_left = self.rect.left + pad
        area_top = self.rect.top + pad
        area_w = max(0, self.rect.width - 2 * pad)
        area_h = max(0, self.rect.height - 2 * pad)

        size = min(area_w, area_h)
        grid_left = area_left + (area_w - size) // 2
        grid_top = area_top + (area_h - size) // 2

        cell_w = max(1, size // self.ROWS)
        cell_h = max(1, size // self.COLS)

        # initialize logical grid now that we know cell sizes
        self._init_grid(cell_w, cell_h)

        # draw cells using the logical grid
        for cell in self.grid:
            # place the cell's own rect into the whiteboard coordinate space (reuse rect)
            cell.rect.topleft = (
            grid_left + getattr(cell, "x", 0) * cell.rect.width,
            grid_top + getattr(cell, "y", 0) * cell.rect.height,
            )

            is_target = cell in self.targets
            if is_target:
                color = RED if cell.is_alive() else FAINT_RED
            else:
            # non-target cells: black when dead, white when alive
                color = BLACK if cell.is_alive() else WHITE

            pygame.draw.rect(screen, color, cell.rect)

        # draw grid lines
        for y in range(self.COLS + 1):
            start = (grid_left, grid_top + y * cell_h)
            end = (grid_left + self.ROWS * cell_w, grid_top + y * cell_h)
            pygame.draw.line(screen, BLACK, start, end, 1)
        for x in range(self.ROWS + 1):
            start = (grid_left + x * cell_w, grid_top)
            end = (grid_left + x * cell_w, grid_top + self.COLS * cell_h)
            pygame.draw.line(screen, BLACK, start, end, 1)
            
        # simulate toggle button on the left of the grid
        button_w, button_h = 120, 40
        spacing = 10
        btn_right = grid_left - spacing
        btn_left = btn_right - button_w
        btn_top = grid_top + (size - button_h) // 2
        self.simulate_button_rect = pygame.Rect(btn_left, btn_top, button_w, button_h)

        # button colors (become retry after 50 generations without targets alive)
        is_retry = self.generations >= 50
        if is_retry:
            BTN_BG = pygame.Color(200, 50, 50)
            BTN_TEXT = pygame.Color(255, 255, 255)
        else:
            # disabled (gray) while simulating
            if self.simulate:
                BTN_BG = pygame.Color(200, 200, 200)
                BTN_TEXT = pygame.Color(100, 100, 100)
            else:
                BTN_BG = pygame.Color(50, 150, 50)
                BTN_TEXT = pygame.Color(255, 255, 255)
        BTN_BORDER = pygame.Color(0, 0, 0)

        pygame.draw.rect(screen, BTN_BG, self.simulate_button_rect)
        pygame.draw.rect(screen, BTN_BORDER, self.simulate_button_rect, 2)

        # render label
        font = pygame.font.SysFont(None, 24)
        label_text = "retry" if is_retry else "simulate"
        label = font.render(label_text, True, BTN_TEXT)
        label_rect = label.get_rect(center=self.simulate_button_rect.center)
        screen.blit(label, label_rect)

        # toggle on mouse-press edge (handle in draw to avoid changing update signature)
        mouse_pressed = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()
        prev = getattr(self, "_simulate_btn_pressed", False)
        if mouse_pressed and not prev and self.simulate_button_rect.collidepoint(mouse_pos):
            if is_retry:
            # reset logical grid so it will be reinitialized on next draw
                self.grid = None
                self.targets = []
                self.group = None
                self.simulate = False
                self.generations = 0
                self.next_generation_counter = 0
                self.generations_since_targets_alive = 0
            else:
            # button is disabled while simulating, only allow toggling when not simulating
                if not self.simulate:
                    self.simulate = not self.simulate
        self._simulate_btn_pressed = mouse_pressed

        if self.simulate:
            # advance generation counter and update grid at configured rate
            self.next_generation_counter += 1
            if self.next_generation_counter >= max(1, self.FPS // max(1, self.grid_update_rate)) and self.simulate:
                self.grid.update_grid()
                self.generations += 1
                self.next_generation_counter = 0
            if any(t.is_alive() for t in self.targets):
                self.generations_since_targets_alive = 0
            else:
                self.generations_since_targets_alive += 1
            if self.generations_since_targets_alive > self.tolerance:
                print("WIN")
                
    
    def update(self, events):
        if not self.grid or self.simulate:
            return
        for cell in self.grid:
            cell.update(events)