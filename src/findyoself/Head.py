from random import random, randint, choice
import sys
import pygame

class Head(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, version: str, screen_width: int, screen_height: int, image: str, callback: None):
        super().__init__()
        
        self.image = pygame.image.load(image).convert_alpha()
        # scale image to 35px width, preserving aspect ratio
        orig_w, orig_h = self.image.get_size()
        new_w = 50
        new_h = int(orig_h * new_w / orig_w)
        self.image = pygame.transform.smoothscale(self.image, (new_w, new_h))
        self.rect = self.image.get_rect()
        
        self.pos = (x, y)
        
        self.version = version
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        self.callback = callback
    
    def move(self, move_type: str, speed: int):
        x, y = self.pos
        if x < 0:
            x = self.screen_width
        elif x > self.screen_width:
            x = 0
        if y < 0:
            y = self.screen_height
        elif y > self.screen_height:
            y = 0
        match move_type:
            case "STRAIGHT":
                if self.version == "1":
                    self.pos = x + speed, y
                else:
                    self.pos = x, y + speed
            case "RANDOM":
                self.pos = x + (speed if random() > 0.5 else speed * -1), y + (speed if random() > 0.5 else speed * -1)
            case "DIAGONAL":
                if self.version == "1":
                    self.pos = x + speed, y + speed
                else:
                    self.pos = x + speed, y - speed
        self.rect.topleft = self.pos
    
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.callback()