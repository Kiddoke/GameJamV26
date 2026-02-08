from random import random
from typing import List
from src.gameoflife.Cell import Cell


class CellGrid:
    def __init__(self, rows: int, cols: int, cell_width: int, cell_height: int, cell_grid: List[Cell] = None):
        self.ROWS = rows
        self.COLS = cols
        
        self.grid = cell_grid if cell_grid else [[Cell(
                alive = random() > 0.5,
                x = x,
                y = y,
                width = cell_width,
                height = cell_height
            ) for x in range(cols)] for y in range(rows)]
        self.connect_grid()
        
    
    def get_neighbours(self, x: int, y: int) -> List["Cell"]:
        neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if abs(i) + abs(j) == 0:
                    continue
                elif x + i < 0 or x + i >= self.ROWS:
                    continue
                elif y + j < 0 or y + j >= self.COLS:
                    continue
                neighbours.append(self.grid[x+i][y+j])
        return neighbours
        
    def connect_grid(self) -> None:
        for x in range(self.ROWS):
            for y in range(self.COLS):
                neighbours = self.get_neighbours(x, y)
                cell = self.grid[x][y]
                cell.set_neighbours(neighbours)
    
    def update_grid(self) -> None:
        for cell in self:
            cell.update_alive_neighbours()
        
        for cell in self:
            cell.update_state()
        
    def __iter__(self):
        for row in self.grid:
            for cell in row:
                yield cell
    
    def __str__(self) -> str:
        return "\n".join(["".join(map(lambda cell: str(cell), row)) for row in self.grid])