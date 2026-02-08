import pygame

# pixel font
PIXELFONT = "./assets/sprites/ByteBounce.ttf"

PLAYER_SPRITE_FRONT_RIGHT = pygame.image.load('./assets/sprites/player_sprite_front_right.png')
PLAYER_SPRITE_FRONT_LEFT = pygame.image.load('./assets/sprites/player_sprite_front_left.png')
PLAYER_SPRITE_FRONT_DOWN = pygame.image.load('./assets/sprites/player_sprite_front_down.png')
PLAYER_SPRITE_BACK_UP = pygame.image.load('./assets/sprites/player_sprite_back_up.png')
OJD_SPRITE_FRONT_LEFT = pygame.image.load('./assets/sprites/ojd_sprite_front_left.png')
LT_SPRITE_GIF = pygame.image.load('./assets/sprites/game_charac_right_1.gif')

# level
DOOR_SIZE = (70,98)
CLASSROOM_DOOR1 = pygame.image.load('./assets/sprites/door1.png')
CLASSROOM_DOOR2 = pygame.image.load('./assets/sprites/door2.png')
HALLWAY = pygame.image.load('./assets/sprites/HALLWAY_VERSION2.png')

# whiteboard
WHITEBOARD = pygame.image.load('./assets/sprites/whiteboard.png')

# healthbar
HEART_SIZE = (30, 30)
FULL_HEART = pygame.image.load('./assets/sprites/full_heart.png')
EMPTY_HEART = pygame.image.load('./assets/sprites/empty_heart.png')

# bottle counter
PANT_SIZE = (20, 40)
BOTTLE = pygame.image.load('./assets/sprites/pant.png')
CAN = pygame.image.load('./assets/sprites/wonster.png')

# trashcan
TRASHCAN_SIZE = (95, 65)
TRASHCAN = pygame.image.load('./assets/sprites/trashcan.png')

# diploma + job application
DIPLOMA_SIZE = (200,200)
JOBB_SIZE = (200,200)
DIPLOMA = pygame.image.load('./assets/sprites/diploma.png')
JOBB = pygame.image.load('./assets/sprites/jobb.png')

# scale
CLASSROOM_DOOR1 = pygame.transform.scale(CLASSROOM_DOOR1, DOOR_SIZE)
CLASSROOM_DOOR2 = pygame.transform.scale(CLASSROOM_DOOR2, DOOR_SIZE)
WHITEBOARD = pygame.transform.scale(WHITEBOARD, (510, 300))
FULL_HEART = pygame.transform.scale(FULL_HEART, HEART_SIZE)
EMPTY_HEART = pygame.transform.scale(EMPTY_HEART, HEART_SIZE)
BOTTLE = pygame.transform.scale(BOTTLE, PANT_SIZE)
CAN = pygame.transform.scale(CAN, PANT_SIZE)
TRASHCAN = pygame.transform.scale(TRASHCAN, TRASHCAN_SIZE)
DIPLOMA = pygame.transform.scale(DIPLOMA, DIPLOMA_SIZE)
JOBB = pygame.transform.scale(JOBB, JOBB_SIZE)




