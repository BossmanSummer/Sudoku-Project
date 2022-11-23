import pygame
from vars import *


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

    def set_cell_value(self, value):
        pass

    def set_sketched_value(self, value):
        pass

    def draw(self, selected=False):
        if self.value != 0:
            num_font = pygame.font.Font(None, NUM_FONT)
            num_surf = num_font.render(str(self.value), 1, NUM_COLOR)
            num_rect = num_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            self.screen.blit(num_surf, num_rect)

        if self.selected:

            # top horizontal line
            pygame.draw.line(self.screen, SELECTION_COLOR,
                            (SQUARE_SIZE * self.col, SQUARE_SIZE * self.row),
                            (SQUARE_SIZE * self.col + SQUARE_SIZE, SQUARE_SIZE * self.row),
                            SELECTION_WIDTH)

            # bottom horizontal line
            pygame.draw.line(self.screen, SELECTION_COLOR,
                             (SQUARE_SIZE * self.col, SQUARE_SIZE * self.row + SQUARE_SIZE),
                             (SQUARE_SIZE * self.col + SQUARE_SIZE, SQUARE_SIZE * self.row + SQUARE_SIZE),
                             SELECTION_WIDTH)

            # left vertical line
            pygame.draw.line(self.screen, SELECTION_COLOR,
                             (SQUARE_SIZE * self.col, SQUARE_SIZE * self.row),
                             (SQUARE_SIZE * self.col, SQUARE_SIZE * self.row + SQUARE_SIZE),
                             SELECTION_WIDTH)

            # right vertical line
            pygame.draw.line(self.screen, SELECTION_COLOR,
                             (SQUARE_SIZE * self.col + SQUARE_SIZE, SQUARE_SIZE * self.row),
                             (SQUARE_SIZE * self.col + SQUARE_SIZE, SQUARE_SIZE * self.row + SQUARE_SIZE),
                             SELECTION_WIDTH)




