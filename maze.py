from time import sleep

from cell import Cell
from window import Window


class Maze:
    def __init__(
      self,
      x1: int,
      y1: int,
      num_rows: int,
      num_cols: int,
      cell_size_x: float,
      cell_size_y: float,
      win: Window | None = None,
   ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols 
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win: Window | None = win
        self.__cells: list[list[Cell]] = []
        self.__create_cells()
    
    def __create_cells(self):
        for _ in range(self.num_cols):
            col: list[Cell] = []
            for _ in range(self.num_rows):
                col.append(Cell(self.win))
            self.__cells.append(col)
        for c in range(self.num_cols):
            for r in range(self.num_rows):
                self.__draw_cell(c,r,) 
              
              
              
    def __draw_cell(self, c, r):
        x1 = self.x1 + self.cell_size_x*c
        y1 = self.y1 + self.cell_size_y*r
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        cell = self.__cells[c][r]
        cell.draw(x1,y1,x2,y2)
        self.__animate()
    
    def __animate(self):
        if self.win is None:
            return
        self.win.redraw()
        sleep(0.05)
        