import pygame

from .assets import *
from .classroom import Classroom
from .hall import Hall
from .whiteboard import Whiteboard

def create_level_one():
    popup = Whiteboard(WHITEBOARD)

    hall = Hall(0, 105, HALLWAY, "1.semester")

    # doors
    cr1 = Classroom(500, 185, CLASSROOM_DOOR1, "java", popup)
    cr2 = Classroom(250, 185, CLASSROOM_DOOR2,  "python", popup)
    cr3 = Classroom(80, 185, CLASSROOM_DOOR1, "scheme", popup)

    hall.add_door(cr1)
    hall.add_door(cr2)
    hall.add_door(cr3)

    return hall







