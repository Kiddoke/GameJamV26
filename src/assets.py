import pygame

PLAYER_SPRITE_FRONT_RIGHT = pygame.image.load('./assets/sprites/player_sprite_front_right.png')
PLAYER_SPRITE_FRONT_LEFT = pygame.image.load('./assets/sprites/player_sprite_front_left.png')
PLAYER_SPRITE_FRONT_DOWN = pygame.image.load('./assets/sprites/player_sprite_front_down.png')
PLAYER_SPRITE_BACK_UP = pygame.image.load('./assets/sprites/player_sprite_back_up.png')
OJD_SPRITE_FRONT_LEFT = pygame.image.load('./assets/sprites/ojd_sprite_front_left.png')
# level
DOOR_SIZE = (70,98)
CLASSROOM_DOOR1 = pygame.image.load('./assets/sprites/door1.png')
CLASSROOM_DOOR2 = pygame.image.load('./assets/sprites/door2.png')
HALLWAY = pygame.image.load('./assets/sprites/HALLWAY_VERSION2.png')

# scale
CLASSROOM_DOOR1 = pygame.transform.scale(CLASSROOM_DOOR1, DOOR_SIZE)
CLASSROOM_DOOR2 = pygame.transform.scale(CLASSROOM_DOOR2, DOOR_SIZE)
