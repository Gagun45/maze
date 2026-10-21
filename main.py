

import random
import sys
import tkinter

from maze import Maze
import maze
from window import Window

sys.setrecursionlimit(5000)

def main():
    maze = None
    num_rows = 10
    num_cols = 10
    margin = 20
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2*margin) / num_cols
    cell_size_y = (screen_y - 2*margin) / num_rows
    def solve_maze():
        if maze is not None:
            maze.solve()
    def start_maze():
        nonlocal maze
        
        seed = random.randint(0, 100)
        maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed, )
        
    win = Window(screen_x, screen_y, on_start=start_maze, on_solve=solve_maze)
    
    
    win.wait_for_close()
        

if __name__ == '__main__':
    main()