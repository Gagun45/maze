import random

from point import Point
from window import Window
from line import Line

def main():
    win = Window(800,600)
    for _ in range(4):
        x1 = random.randint(0,400)
        y1 = random.randint(0,400)
        x_shift = random.randint(20,150)
        y_shift = random.randint(4,200)
        point_1 = Point(x1, y1)
        point_2 = Point(x1+x_shift, y1+y_shift)
        line = Line(point_1, point_2)
        win.draw_line(line, 'red')
    win.wait_for_close()
        

if __name__ == '__main__':
    main()