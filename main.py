import random

from cell import Cell
from point import Point
from window import Window
from line import Line

def main():
    win = Window(800,600)
    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(50, 50, 100, 100)
    
    c2 = Cell(win)
    c2.has_top_wall = False
    c2.draw(100,100, 150, 150)
    
    c1.draw_move(c2)
    
    win.wait_for_close()
        

if __name__ == '__main__':
    main()