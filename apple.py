import pygame
from random import choice
from settings import *
from math import sin



class Apple:
    def __init__(self, snake):
        self.pos = pygame.Vector2()
        self.display_surface = pygame.display.get_surface()
        self.snake = snake
        self.set_position()

        self.surface = pygame.image.load(join('.', 'pictures', 'apple.png')).convert_alpha()



    def draw_apple(self):
        # rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        # # pygame.draw.rect(self.display_surface, 'blue', rect)
        # self.display_surface.blit(self.surface,rect)
        scale = 1 + sin(pygame.time.get_ticks() / 500) / 3
        self.scaled_surface = pygame.transform.smoothscale_by(self.surface, scale)
        self.scaled_rect = self.scaled_surface.get_rect(center = (self.pos.x * CELL_SIZE + CELL_SIZE / 2, self.pos.y * CELL_SIZE + CELL_SIZE / 2))

        self.display_surface.blit(self.scaled_surface, self.scaled_rect)


    def set_position(self):
        available_positions = [pygame.Vector2(x, y) for x in range(COLS) for y in range(ROWS) if pygame.Vector2(x, y) not in self.snake.body]
        self.pos = choice(available_positions)



