from tkinter import Canvas

from line import Line
from point import Point
from window import Window

class Cell:
    def __init__(self, window: Window | None = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1.0
        self.__x2 = -1.0
        self.__x1 = -1.0
        self.__x2 = -1.0
        self.visited = False
        self.__win: Window | None = window
    
    def draw(self, x1,y1,x2,y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.__win is None:
            return
        
        left_wall = Line(Point(x1, y1), Point(x1, y2))
        color = 'black' if self.has_left_wall else 'white'
        self.__win.draw_line(left_wall, color)
        
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        color = 'black' if self.has_top_wall else 'white'
        self.__win.draw_line(top_wall, color)
        
        right_wall = Line(Point(x2, y1), Point(x2, y2))
        color = 'black' if self.has_right_wall else 'white'
        self.__win.draw_line(right_wall, color)
        
        bottom_wall = Line(Point(x1, y2), Point(x2, y2))
        color = 'black' if self.has_bottom_wall else 'white'
        self.__win.draw_line(bottom_wall, color)
    
    def draw_move(self, to_cell: Cell, undo: bool = False) -> None:
        if self.__win is None:
            return
        color = 'gray' if undo else 'red'
        p1 = Point((self.__x1 + self.__x2) // 2, (self.__y1 + self.__y2)//2)
        p2 = Point((to_cell.__x1 + to_cell.__x2) // 2, (to_cell.__y1 + to_cell.__y2)//2)
        line = Line(p1, p2)
        self.__win.draw_line(line, color)
        