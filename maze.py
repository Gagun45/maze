import random
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
      seed: int | None = None,
   ) -> None:
        if seed:
            random.seed(seed)
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols 
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win: Window | None = win
        self.__cells: list[list[Cell]] = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
    
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
        if self.win is None:
            return
        x1 = self.x1 + self.cell_size_x*c
        y1 = self.y1 + self.cell_size_y*r
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        cell:Cell = self.__cells[c][r]
        cell.draw(x1,y1,x2,y2)
        self.__animate()
    
    def __animate(self):
        if self.win is None:
            return
        self.win.redraw()
        sleep(0.01)
    
    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(self.num_cols-1,self.num_rows-1)
    
    def __break_walls_r(self, i, j):
        cell: Cell = self.__cells[i][j]
        cell.visited = True
        while True:
            to_visit = []
            if i>0 and (not self.__cells[i-1][j].visited):
                to_visit.append((i-1,j))
            if i<self.num_cols-1 and (not self.__cells[i+1][j].visited):
                to_visit.append((i+1,j))
            if j>0 and (not self.__cells[i][j-1].visited):
                to_visit.append((i,j-1))
            if j<self.num_rows-1 and (not self.__cells[i][j+1].visited):
                to_visit.append((i,j+1))
            if len(to_visit)==0:
                self.__draw_cell(i,j)
                return
            fold = random.randint(0, len(to_visit)-1)
            c, r = to_visit[fold]
            if c > i:
                cell.has_bottom_wall = False
                self.__cells[c][r].has_top_wall = False
            if c < i:
                cell.has_top_wall = False
                self.__cells[c][r].has_bottom_wall = False
            if r > j:
                cell.has_right_wall = False
                self.__cells[c][r].has_left_wall = False
            if r < i:
                cell.has_left_wall = False
                self.__cells[c][r].has_right_wall = False
            self.__break_walls_r(c, r)