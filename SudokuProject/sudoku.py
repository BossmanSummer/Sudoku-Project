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

  sub_font = pygame.font.Font(None, DESC_FONT)
  sub_text = "Select Game Mode"
  sub_surf = sub_font.render(sub_text, 1, LINE_COLOR)
  sub_rect = sub_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))
  screen.blit(sub_surf, sub_rect)

  btn_font = pygame.font.Font(None, BTN_FONT)

  levels = ["Easy", "Medium", "Hard"]


  for i, level in enumerate(levels):

    x_coord =  WIDTH // 2  + MODE_SPACER * (i - 1) + MODE_BTN_WIDTH * (i - 1)
    btn = pygame.draw.rect(screen, BTN_COLOR,
                           pygame.Rect(x_coord - MODE_BTN_WIDTH//2, MODE_BTN_Y - MODE_BTN_HEIGHT//2,
                                       MODE_BTN_WIDTH, MODE_BTN_HEIGHT))
    btn_text = level
    btn_surf = btn_font.render(btn_text, 1, LINE_COLOR)
    btn_rect = btn_surf.get_rect(center=(x_coord, MODE_BTN_Y))
    screen.blit(btn_surf, btn_rect)


def game_screen(board):
  board.draw()

  btn_font = pygame.font.Font(None, BTN_FONT)

  btns = ["Reset", "Restart", "Exit"]

  for i, btn_text in enumerate(btns):
    x_coord = WIDTH // 2 + GAME_SPACER * (i - 1) + GAME_BTN_WIDTH * (i - 1)
    btn = pygame.draw.rect(screen, BTN_COLOR,
                           pygame.Rect(x_coord - GAME_BTN_WIDTH // 2, GAME_BTN_Y - GAME_BTN_HEIGHT // 2,
                                       GAME_BTN_WIDTH, GAME_BTN_HEIGHT))
    btn_surf = btn_font.render(btn_text, 1, LINE_COLOR)
    btn_rect = btn_surf.get_rect(center=(x_coord, GAME_BTN_Y))
    screen.blit(btn_surf, btn_rect)


def win_screen():
  screen.fill(BG_COLOR)

  end_font = pygame.font.Font(None, TITLE_FONT)
  end_text = "GAME WON!"
  end_surf = end_font.render(end_text, 1, LINE_COLOR)
  end_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
  screen.blit(end_surf, end_rect)



  exit_btn = pygame.draw.rect(screen, BTN_COLOR,
                              pygame.Rect(WIDTH // 2 - END_BTN_WIDTH//2, END_BTN_Y - END_BTN_HEIGHT//2,
                                          END_BTN_WIDTH, END_BTN_HEIGHT))
  btn_font = pygame.font.Font(None, BTN_FONT)
  btn_text = "EXIT"
  btn_surf = btn_font.render(btn_text, 1, LINE_COLOR)
  btn_rect = btn_surf.get_rect(center = (WIDTH//2, END_BTN_Y))
  screen.blit(btn_surf, btn_rect)



def lose_screen():
  screen.fill(BG_COLOR)

  end_font = pygame.font.Font(None, TITLE_FONT)
  end_text = "GAME OVER!"
  end_surf = end_font.render(end_text, 1, LINE_COLOR)
  end_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
  screen.blit(end_surf, end_rect)

  restart_btn = pygame.draw.rect(screen, BTN_COLOR,
                                 pygame.Rect(WIDTH // 2 - END_BTN_WIDTH // 2, END_BTN_Y - END_BTN_HEIGHT // 2,
                                             END_BTN_WIDTH, END_BTN_HEIGHT))
  btn_font = pygame.font.Font(None, BTN_FONT)
  btn_text = "RESTART"
  btn_surf = btn_font.render(btn_text, 1, LINE_COLOR)
  btn_rect = btn_surf.get_rect(center=(WIDTH // 2, END_BTN_Y))
  screen.blit(btn_surf, btn_rect)

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
        x, y = event.pos

        # checks if the user clicked any of the buttons
        if (y > MODE_BTN_Y - MODE_BTN_HEIGHT//2) and (y < MODE_BTN_Y + MODE_BTN_HEIGHT//2):
          levels = ["Easy", "Medium", "Hard"]

          for i, level in enumerate(levels):
            x_coord = WIDTH // 2 + MODE_SPACER * (i - 1) + MODE_BTN_WIDTH * (i - 1)
            if x > x_coord - MODE_BTN_WIDTH//2 and x < x_coord + MODE_BTN_WIDTH//2:
              begin_game = False
              game_playing = True
              board = Board(WIDTH, HEIGHT, screen, level)

              game_screen(board)




      if event.type == pygame.MOUSEBUTTONDOWN and game_playing:
        for r in board.cells:
           for cell in r:
             cell.deselect()
        x, y = event.pos

        # checks if the user clicked any of the cells
        row = int(y // SQUARE_SIZE)
        col = int(x // SQUARE_SIZE)
        if row < 9 and col < 9:
          board.cells[row][col].select()
          board.cells[row][col].draw()


        # checks for user hitting one of the buttons
        if (y > GAME_BTN_Y - GAME_BTN_HEIGHT//2) and (y < GAME_BTN_Y + GAME_BTN_HEIGHT//2):

          # checks if the user selected the RESET button
          # RESET GAME HASN'T BEEN CODED
          x_coord = WIDTH // 2 - GAME_SPACER - GAME_BTN_WIDTH
          if x > x_coord - GAME_BTN_WIDTH//2 and x < x_coord + GAME_BTN_WIDTH//2:
            pass

          # checks if the user selected the RESTART button
          x_coord = WIDTH // 2
          if x > x_coord - GAME_BTN_WIDTH // 2 and x < x_coord + GAME_BTN_WIDTH // 2:
            begin_game = True
            game_playing = False
            welcome_screen()

          # checks if user selected the EXIT button
          x_coord = WIDTH // 2 + GAME_SPACER + GAME_BTN_WIDTH
          if x > x_coord - GAME_BTN_WIDTH // 2 and x < x_coord + GAME_BTN_WIDTH // 2:
            pygame.quit()

      # checks if user restarted after losing
      if event.type == pygame.MOUSEBUTTONDOWN and lose_game:
        x, y = event.pos
        in_y_range = (y > END_BTN_Y - END_BTN_HEIGHT // 2) and (y < END_BTN_Y + END_BTN_HEIGHT//2)
        in_x_range = (x > WIDTH//2 - END_BTN_WIDTH//2) and (x < WIDTH//2 + END_BTN_WIDTH//2)

        if in_y_range and in_x_range:
          begin_game = True
          game_playing = False
          welcome_screen()

      # checks if user exitted after winning
      if event.type == pygame.MOUSEBUTTONDOWN and win_game:
        x, y = event.pos
        in_y_range = (y > END_BTN_Y - END_BTN_HEIGHT // 2) and (y < END_BTN_Y + END_BTN_HEIGHT//2)
        in_x_range = (x > WIDTH//2 - END_BTN_WIDTH//2) and (x < WIDTH//2 + END_BTN_WIDTH//2)

        if in_y_range and in_x_range:
          pygame.quit()




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
      game_screen(board)


    pygame.display.update()