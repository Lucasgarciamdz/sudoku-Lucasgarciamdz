import unittest

from sudoku_class import Sudoku
from sudoku_exceptions import *


class TestSudoku(unittest.TestCase):

    def setUp(self):
        self.sudoku = Sudoku()

    def test_create_blank_sudoku(self):
        self.sudoku.create_blank_board()
        self.assertEqual(
            self.sudoku.board,
            [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]])

    def test_insert_value(self):
        self.sudoku.create_blank_board()
        self.sudoku.insert_value(1, 1, 5)
        self.assertEqual(self.sudoku.board[1][1], 5)

    def test_error_same_number_in_column(self):
        self.sudoku.create_blank_board()
        self.sudoku.insert_value(1, 1, 5)
        with self.assertRaises(SameNumberInColumn):
            self.sudoku.insert_value(3, 1, 5)

    def test_error_same_number_in_row(self):
        self.sudoku.create_blank_board()
        self.sudoku.insert_value(1, 1, 5)
        with self.assertRaises(SameNumberInRow):
            self.sudoku.insert_value(1, 7, 5)

    def test_remove_value(self):
        self.sudoku.create_blank_board()
        self.sudoku.insert_value(1, 1, 5)
        self.sudoku.remove_value(1, 1)
        self.assertEqual(self.sudoku.board[1][1], 0)

    def test_error_same_number_in_region(self):
        self.sudoku.create_blank_board()
        self.sudoku.insert_value(1, 1, 5)
        with self.assertRaises(SameNumberInRegion):
            self.sudoku.insert_value(2, 2, 5)

    def test_error_same_number_in_region_2(self):
        self.sudoku.create_blank_board()
        self.sudoku.insert_value(3, 3, 5)
        with self.assertRaises(SameNumberInRegion):
            self.sudoku.insert_value(4, 4, 5)

    def test_3_error_same_number_in_region(self):
        self.sudoku.create_blank_board()
        self.sudoku.insert_value(7, 7, 5)
        with self.assertRaises(SameNumberInRegion):
            self.sudoku.insert_value(8, 8, 5)


if __name__ == "__main__":
    unittest.main()