import pygame
from vars import *
from cell import *


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = []
        self.original_cells = []

        for r in range (0, ROWS):
            row = []
            for c in range (0, COLS):
                row.append(Cell(TEMP_BOARD[r][c], r, c, self.screen))
            self.cells.append(row)
        print(self.cells)
        self.original_cells = self.cells

    def draw(self):
        # draw the outline of the Sudoku grid
        self.screen.fill(BG_COLOR)
        for i in range(0, ROWS + 1):
            line_width = LINE_WIDTH_THICK if (i % 3 == 0) else LINE_WIDTH
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                line_width
            )
        for j in range(0, COLS + 1):
            line_width = LINE_WIDTH_THICK if (j % 3 == 0) else LINE_WIDTH
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (j * SQUARE_SIZE, 0),
                (j * SQUARE_SIZE, HEIGHT - SQUARE_SIZE),
                line_width
            )

        for r in range (0, ROWS):
            for c in range (0, COLS):
                self.cells[r][c].draw()

    def select(self, row, col):
        # selects cell
        self.cells[row][col].select()
        self.cells[row][col].draw()

    def click(self, x, y):
        # return tuple of of cell when clicked in form of (row, col), or none
        pass

    def clear(self):
        # clear cell value
        pass

    def sketch(self, value):
        # fill cell with user input
        # use draw function
        pass

    def place_number(self, value):
        # set cell with user input
        pass

    def reset_to_original(self):
        # reset board to original values
        self.cells = self.original_cells
        self.draw()

    def is_full(self):
        # return true or false if board is full
        # if 0 not in board:
        for i in self.cells:
            for j in self.cells:
                if j == 0:
                    return False
        return True

    def update_board(self):
        # set board to new values
        pass

    def find_empty(self):
        # find empty cell and return as tuple (x, y)
        pass

    def check_board(self):
        # check to see if board is solved

        # there is sometimes more than one correct solution, so this method only works sometimes
        # if self.cells == SOLVED_BOARD:
        #     return True

        # for rows in self.cells:
        #     x = 0
        #     for num in rows:
        #         x += num
        #     if x != 45:
        #         return False
        # for index in range(9):
        #     x = 0
        #     for rows in self.cells:
        #         x += rows[index]
        #     if x != 45:
        #         return False

        y = 0
        for row in self.cells:
            x = 0
            for number in range(9):
                for index in range(9):
                    if number + 1 == row[index]:
                        if x == 0:
                            x = 1
                        elif x == 1:
                            return False
            if x == 1:
                y += 1
        if y != 9:
            return False

        y = 0
        for number in range(9):
            x = 0
            for index in range(9):
                for row in self.cells:
                    if number + 1 == row[index]:
                        if x == 0:
                            x = 1
                        elif x == 1:
                            return False
            if x == 1:
                y += 1
        if y != 9:
            return False

        # check squares

        # top left square
        y = 0
        for rows in range(3):
            x = 0
            for columns in range(3):
                for number in range(9):
                    if self.cells[rows][columns] == number + 1:
                        if x == 0:
                            x += 1
            if x == 3:
                y += 1
            elif x != 3:
                return False

        # middle top square
        y = 0
        for rows in range(3):
            x = 0
            for columns in range(3, 6):
                for number in range(9):
                    if self.cells[rows][columns] == number + 1:
                        if x == 0:
                            x += 1
            if x == 3:
                y += 1
            elif x != 3:
                return False

        # right top square
        y = 0
        for rows in range(3):
            x = 0
            for columns in range(6, 9):
                for number in range(9):
                    if self.cells[rows][columns] == number + 1:
                        if x == 0:
                            x += 1
            if x == 3:
                y += 1
            elif x != 3:
                return False

        # middle left square
        y = 0
        for rows in range(3, 6):
            x = 0
            for columns in range(3):
                for number in range(9):
                    if self.cells[rows][columns] == number + 1:
                        if x == 0:
                            x += 1
            if x == 3:
                y += 1
            elif x != 3:
                return False

        # middle middle square
        y = 0
        for rows in range(3, 6):
            x = 0
            for columns in range(3, 6):
                for number in range(9):
                    if self.cells[rows][columns] == number + 1:
                        if x == 0:
                            x += 1
            if x == 3:
                y += 1
            elif x != 3:
                return False

        # middle right square
        y = 0
        for rows in range(3, 6):
            x = 0
            for columns in range(6, 9):
                for number in range(9):
                    if self.cells[rows][columns] == number + 1:
                        if x == 0:
                            x += 1
            if x == 3:
                y += 1
            elif x != 3:
                return False

        # bottom right square
        y = 0
        for rows in range(6, 9):
            x = 0
            for columns in range(3):
                for number in range(9):
                    if self.cells[rows][columns] == number + 1:
                        if x == 0:
                            x += 1
            if x == 3:
                y += 1
            elif x != 3:
                return False

        # bottom middle square
        y = 0
        for rows in range(6, 9):
            x = 0
            for columns in range(3, 6):
                for number in range(9):
                    if self.cells[rows][columns] == number + 1:
                        if x == 0:
                            x += 1
            if x == 3:
                y += 1
            elif x != 3:
                return False

        # bottom right square
        y = 0
        for rows in range(6, 9):
            x = 0
            for columns in range(6, 9):
                for number in range(9):
                    if self.cells[rows][columns] == number + 1:
                        if x == 0:
                            x += 1
            if x == 3:
                y += 1
            elif x != 3:
                return False

        # if it makes it this far, it is true
        return True
