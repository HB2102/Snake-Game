import pygame
from settings import *
from snake import Snake


class Main():
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.bg_rects = [pygame.Rect((col + int(row % 2 == 1)) * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE) for col in range(0, COLS, 2) for row in range(ROWS)]

        self.snake = Snake()


    def run(self):
        while True:
            keys = pygame.event.get()
            for event in keys:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.display_surface.fill(LIGHT_COLOR)
            self.draw_background()
            self.snake.draw_snake()
            pygame.display.update()


    def draw_background(self):
        self.display_surface.fill(LIGHT_COLOR)
        for rect in self.bg_rects:
            pygame.draw.rect(self.display_surface, DARK_COLOR, rect)








if __name__ == '__main__':
    main = Main()
    main.run()
