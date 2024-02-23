import pygame
from random import choice

from settings import *


class Apple:
    def __init__(self, snake):
        self.pos = pygame.Vector2()
        self.display_surface = pygame.display.get_surface()
        self.snake = snake
        self.set_position()


    def draw_apple(self):
        rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.display_surface, 'blue', rect)


    def set_position(self):
        available_positions = [pygame.Vector2(x, y) for x in range(COLS) for y in range(ROWS) if pygame.Vector2(x, y) not in self.snake.body]
        self.pos = choice(available_positions)


