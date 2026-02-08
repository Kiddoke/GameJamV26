
from src.gameoflife.Cell import Cell


class Target(Cell):
    def __init__(self, alive: bool, x: int, y: int, width: int, height: int):
        super().__init__(alive, x, y, width, height)
    
    def update(selv, events):
        pass