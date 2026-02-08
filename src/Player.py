import pygame

from .assets import *



class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.size = (60, 90)
        self.direction = "down"
        self.sprites = {
            "up" : pygame.transform.scale(PLAYER_SPRITE_BACK_UP, self.size),
            "down" : pygame.transform.scale(PLAYER_SPRITE_FRONT_DOWN, self.size),
            "right" : pygame.transform.scale(PLAYER_SPRITE_FRONT_RIGHT, self.size),
            "left" : pygame.transform.scale(PLAYER_SPRITE_FRONT_LEFT, self.size)
        }

        self.image = self.sprites[self.direction]
        self.rect = self.sprites[self.direction].get_rect()
        self.rect.x = 50
        self.rect.y = 300


    def update(self, keys, vel, colliders):

        old_x, old_y = self.rect.topleft

        if keys[pygame.K_d]:
            self.rect.x += vel
            self.direction = "right"
        if keys[pygame.K_a]:
            self.rect.x -= vel
            self.direction = "left"

        hits = pygame.sprite.spritecollide(self, colliders, False)
        for hit in hits:
            if self.rect.colliderect(hit.rect):
                if self.rect.centerx > hit.rect.centerx:
                    self.rect.left = hit.rect.right
                else: 
                    self.rect.right = hit.rect.left

        if keys[pygame.K_w]:
            self.rect.y -= vel
            self.direction = "up"
        if keys[pygame.K_s]:
            self.rect.y += vel
            self.direction = "down"

        hits = pygame.sprite.spritecollide(self, colliders, False)
        for hit in hits:
            if self.rect.colliderect(hit.rect):
                if self.rect.centery > hit.rect.centery:
                    self.rect.top = hit.rect.bottom
                else: 
                    self.rect.bottom = hit.rect.top


        self.image = self.sprites[self.direction]
        print(self.rect)


