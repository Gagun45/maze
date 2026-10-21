

import random
import sys

from maze import Maze
from window import Window

sys.setrecursionlimit(5000)

def main():
    num_rows = 80
    num_cols = 80
    margin = 20
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2*margin) / num_cols
    cell_size_y = (screen_y - 2*margin) / num_rows
    win = Window(screen_x, screen_y)
    seed = random.randint(0, 100)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed)
    maze.solve()
    
    win.wait_for_close()
        

if __name__ == '__main__':
    main()