import board
import cell
import sudoku_generator
import pygame, sys
from vars import *

# creating board
pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
num_font = pygame.font.Font(None, NUM_FONT)
end_font = pygame.font.Font(None, GAME_OVER_FONT)

board = Board(screen, "easy")


def __main__():
  pass


if __name__ == "__main__":
  __main__()
