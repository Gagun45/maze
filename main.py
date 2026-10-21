import random

from cell import Cell
from point import Point
from window import Window
from line import Line

def main():
    win = Window(800,600)
    c = Cell(win)
    c.has_right_wall = False
    c.draw(50, 50, 100, 100)
    
    c = Cell(win)
    c.has_top_wall = False
    c.draw(100,100, 150, 150)
    
    win.wait_for_close()
        

if __name__ == '__main__':
    main()