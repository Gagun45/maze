import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        for c in [2,6,20]:
            for r in [4,6,8]:
                num_cols = c
                num_rows = r
                m1 = Maze(0,0,num_rows, num_cols, 10, 10)
                self.assertEqual(len(m1._Maze__cells), num_cols)
                self.assertEqual(len(m1._Maze__cells[0]), num_rows)
                self.assertEqual(m1._Maze__cells[0][0].has_top_wall, False)
                self.assertEqual(m1._Maze__cells[-1][-1].has_bottom_wall, False)
    def test_reset_cells_visited(self):
        m = Maze(0,0,12, 16, 10, 10)
        for col in m._Maze__cells:
            for cell in col:
                self.assertEqual(cell.visited, False)
    
    def test_solved(self):
        m = Maze(0,0,12, 16, 10, 10)
        m.solve()
        self.assertEqual(m._Maze__cells[-1][-1].visited, True)
            
if __name__ == '__main__':
    unittest.main()
    