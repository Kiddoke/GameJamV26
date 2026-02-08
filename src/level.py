import pygame

from .assets import *
from .classroom import Classroom
from .hall import Hall

def create_level_one():
    hall = Hall(0, 105, HALLWAY, "1.semester")

    # doors
    cr1 = Classroom(500, 185, CLASSROOM_DOOR1, "java")
    cr2 = Classroom(250, 185, CLASSROOM_DOOR2,  "python")
    cr3 = Classroom(80, 185, CLASSROOM_DOOR1, "scheme")

    hall.add_door(cr1)
    hall.add_door(cr2)
    hall.add_door(cr3)

    return hall







