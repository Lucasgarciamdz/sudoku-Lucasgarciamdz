from sudoku_exceptions import *


class Sudoku:

    def __init__(self):
        self.board = []

    def create_blank_board(self):
        self.board = [[0 for column in range(9)] for row in range(9)]

    def insert_value(self, row, column, number):

        self.check_same_row(row, column, number)
        self.check_same_column(row, column, number)
        self.check_same_region(row, column, number)

        self.board[row][column] = number

    def remove_value(self, row, column):
        self.board[row][column] = 0

    def check_same_row(self, row, column, number):
        for c in range(9):
            if self.board[row][c] == number and c != column:
                raise SameNumberInRow

    def check_same_column(self, row, column, number):
        for r in range(9):
            if self.board[r][column] == number and r != row:
                raise SameNumberInColumn

    def check_same_region(self, row, column, number):
        for r in self.row_neighbor(row):
            for c in self.column_neighbor(column):
                if self.board[r][c] == number and r != row and c != column:
                    raise SameNumberInRegion

    def row_neighbor(self, row):
        if (row // 3) * 3 == 0:
            return [0, 1, 2]
        if (row // 3) * 3 == 3:
            return [3, 4, 5]
        if (row // 3) * 3 == 6:
            return [6, 7, 8]

    def column_neighbor(self, column):
        if (column // 3) * 3 == 0:
            return [0, 1, 2]
        if (column // 3) * 3 == 3:
            return [3, 4, 5]
        if (column // 3) * 3 == 6:
            return [6, 7, 8]
