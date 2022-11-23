from board import *
import cell
import sudoku_generator
import pygame, sys
from vars import *

# creating board
pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
num_font = pygame.font.Font(None, NUM_FONT)




def welcome_screen():
  screen.fill(BG_COLOR)

  welcome_font = pygame.font.Font(None, TITLE_FONT)
  welcome_text = "Welcome to Sudoku"
  welcome_surf = welcome_font.render(welcome_text, 1, LINE_COLOR)
  welcome_rect = welcome_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
  screen.blit(welcome_surf, welcome_rect)

  welcome_font = pygame.font.Font(None, DESC_FONT)
  welcome_text = "Select Game Mode"
  welcome_surf = welcome_font.render(welcome_text, 1, LINE_COLOR)
  welcome_rect = welcome_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
  screen.blit(welcome_surf, welcome_rect)

  # TO DO: ADD BUTTONS

def game_screen():
  board.draw()

  # TO DO: ADD BUTTONS

def win_screen():
  screen.fill(BG_COLOR)

  end_font = pygame.font.Font(None, TITLE_FONT)
  end_text = "GAME WON!"
  end_surf = end_font.render(end_text, 1, LINE_COLOR)
  end_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
  screen.blit(end_surf, end_rect)


def lose_screen():
  screen.fill(BG_COLOR)

  end_font = pygame.font.Font(None, TITLE_FONT)
  end_text = "GAME OVER!"
  end_surf = end_font.render(end_text, 1, LINE_COLOR)
  end_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
  screen.blit(end_surf, end_rect)

game_playing = False
begin_game = True
win_game = False
lose_game = False



if __name__ == "__main__":
  welcome_screen()
  while True:
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN and begin_game:
        # create different mode based on board played
        begin_game = False
        game_playing = True
        mode = "easy"
        board = Board(WIDTH, HEIGHT, screen, mode)
        board.draw()

      if event.type == pygame.MOUSEBUTTONDOWN and game_playing:
        x, y = event.pos
        row = int(y // SQUARE_SIZE)
        col = int(x // SQUARE_SIZE)

        for r in board.cells:
           for cell in r:
             cell.deselect()

        board.cells[row][col].select()
        board.cells[row][col].draw()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
          win_game = True
          game_playing = False
          lose_game = False
          begin_game = False
          win_screen()

        if event.key == pygame.K_l:
          lose_game = True
          win_game = False
          begin_game = False
          game_playing = False
          lose_screen()

      if event.type == pygame.QUIT:
        pygame.quit()

    if game_playing:
      board.draw()


    pygame.display.update()