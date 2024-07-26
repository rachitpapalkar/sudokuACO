import pygame

class GUICube:
    def __init__(self, win, row, col, size, dark_mode=False):
        self.win = win
        self.row = row
        self.col = col
        self.size = size
        self.dark_mode = dark_mode
        self.initial_cell = False

    def draw(self, val, pher_val):
        font = pygame.font.SysFont("dejavusansmono", 40)

        x = self.col * self.size
        y = self.row * self.size

        if self.initial_cell:
            pygame.draw.rect(self.win, (252, 211, 3), (x, y, self.size, self.size))

        if val == 0:
            text_color = (255, 255, 255) if self.dark_mode else (0, 0, 0)
            text = font.render(" ", 1, text_color)
        else:
            text_color = (255, 255, 255) if self.dark_mode else (0, 0, 0)
            text = font.render(str(val), 1, text_color)

        self.win.blit(text, (x + (self.size / 2 - text.get_width() / 2), y + (self.size / 2 - text.get_height() / 2)))

        font = pygame.font.SysFont("dejavusansmono", 20)

        if pher_val == 0:
            text = font.render(" ", 1, (255, 255, 255) if self.dark_mode else (0, 0, 0))
        else:
            text = font.render(str(pher_val), 1, (255, 255, 255) if self.dark_mode else (0, 0, 0))

        self.win.blit(text, (x + self.size - text.get_width(), y))
