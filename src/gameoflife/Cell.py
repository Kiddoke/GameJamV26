from random import random
from typing import List
import pygame


class Cell(pygame.sprite.Sprite):
    def __init__(self, alive: bool, x: int, y: int, width: int, height: int):
        super().__init__()
        self.isAlive = alive
        self.neighbours = []
        self.alive_neighbours = 0
        self.rect = pygame.Rect(x * width, y * height, width, height)
        self.x = x
        self.y = y
        
    def is_alive(self) -> bool:
        return self.isAlive
        
    def set_alive(self) -> None:
        self.isAlive = True
    
    def set_dead(self) -> None:
        self.isAlive = False
    
    def set_opposite(self) -> None:
        self.isAlive = not self.isAlive
        
    def set_neighbours(self, neighbours: List["Cell"]) -> None:
        self.neighbours = neighbours
        
    def update_alive_neighbours(self) -> None:
        self.alive_neighbours = sum(1 for n in self.neighbours if n.is_alive())

    def update_state(self) -> None:
        n_alive = self.alive_neighbours
        if self.isAlive and (n_alive < 2 or n_alive > 3):
            self.set_dead()
        elif not self.isAlive and n_alive == 3:
            self.set_alive()
            
    def update(self, events):
        for event in events:
            print(event)
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    print("UGEUGEWUFGIUWGHEIUGB")
                    self.set_opposite()
    
    def __str__(self) -> str:
        return "o" if self.isAlive else "."