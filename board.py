import pygame


class Board:
  def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty
    
  def draw(self):
    
    # draw the outline of the Sudoku grid
    pass

  def select(self, row, col):
    # make selected cell
    pass

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
    # reset board to origianl values
    pass

  def is_full(self):
    # return true or false if board is full
    # if 0 not in board:
    pass

  def update_board(self):
    # set board to new values
    pass

  def find_empty(self):
    # find empty cell and return as tuple (x, y)
    pass

  def check_board(self):
    # check to see if board is solved
    pass


