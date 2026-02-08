import pygame

from .assets import *
from .classroom import Classroom
from .hall import Hall
from .whiteboard import GameOfLifeWhiteboard, Whiteboard
from .trashcan import Trashcan
from .pant import Pant

def create_level_one():
    popup = Whiteboard()
    
    game_of_life_popup = GameOfLifeWhiteboard()

    hall = Hall("1.semester")

    # doors
    cr1 = Classroom(500, 185, CLASSROOM_DOOR1, "java", popup)
    cr2 = Classroom(250, 185, CLASSROOM_DOOR2,  "python", game_of_life_popup)
    cr3 = Classroom(80, 185, CLASSROOM_DOOR1, "scheme", popup)

    # trashcans
    t1 = Trashcan(360, 215, offset=60)
    t2 = Trashcan(600, 430)

    hall.add_door(cr1)
    hall.add_door(cr2)
    hall.add_door(cr3)

    hall.add_trashcan(t1)
    hall.add_trashcan(t2)
    
    # pant
    pant_y = 176
    b = Pant(375, pant_y, BOTTLE, offset=10)
    b2 = Pant(395, pant_y, BOTTLE, offset=10)
    c = Pant(420, pant_y, CAN, offset=10)

    pant_y2 = 390
    b3 = Pant(615, pant_y2, BOTTLE)
    b4 = Pant(640, pant_y2, BOTTLE)
    c2 = Pant(665, pant_y2, CAN)

    bottles = [b, b2, b3, b4, c, c2]

    return Level(hall, bottles, game_of_life_popup)

class Level:
    def __init__(self, hall, bottles, gml):
        self.hall = hall
        self.bottles = bottles
        self.gml = gml

    def draw(self, screen):
        self.hall.draw(screen)

        for pant in self.bottles:
            pant.draw(screen)




