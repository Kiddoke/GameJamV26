import pygame

from .assets import *
from .classroom import Classroom
from .hall import Hall
from .whiteboard import Whiteboard
from .trashcan import Trashcan
from .pant import Pant

def create_level_one():
    popup = Whiteboard()

    hall = Hall("1.semester")

    # doors
    cr1 = Classroom(500, 185, CLASSROOM_DOOR1, "java", popup)
    cr2 = Classroom(250, 185, CLASSROOM_DOOR2,  "python", popup)
    cr3 = Classroom(80, 185, CLASSROOM_DOOR1, "scheme", popup)

    # trashcans
    t = Trashcan(360, 220)
    t2 = Trashcan(600, 430)

    # pant
    pant_y = 187
    b = Pant(375, pant_y, BOTTLE)
    b2 = Pant(395, pant_y, BOTTLE)
    c = Pant(420, pant_y, CAN)

    pant_y2 = 400
    b3 = Pant(615, pant_y2, BOTTLE)
    b4 = Pant(640, pant_y2, BOTTLE)
    c2 = Pant(665, pant_y2, CAN)

    t.addBottle(b)
    t.addBottle(b2)
    t.addBottle(c)

    t2.addBottle(b3)
    t2.addBottle(b4)
    t2.addBottle(c2)

    hall.add_door(cr1)
    hall.add_door(cr2)
    hall.add_door(cr3)

    hall.add_trashcan(t)
    hall.add_trashcan(t2)

    return hall







