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

if __name__ == '__main__':
    unittest.main()
    