import pygame
from settings import *
from snake import Snake
from apple import Apple


class Main():
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.bg_rects = [pygame.Rect((col + int(row % 2 == 1)) * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE) for col in range(0, COLS, 2) for row in range(ROWS)]

        self.snake = Snake()
        self.apple = Apple(self.snake)

        self.update_event = pygame.event.custom_type()
        pygame.time.set_timer(self.update_event, 200)
        self.game_active = False

        self.eat_sound = pygame.mixer.Sound(join('.', 'sounds', 'crunch.wav'))
        self.background_music = pygame.mixer.Sound(join('.', 'sounds', 'Arcade.ogg'))
        self.background_music.set_volume(0.6)
        self.background_music.play(-1)


    def run(self):
        while True:
            keys = pygame.event.get()
            for event in keys:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == self.update_event and self.game_active:
                    self.snake.move()

                if event.type == pygame.KEYDOWN and not self.game_active:
                    self.game_active = True

            self.input()
            self.check_collision()
            self.draw_background()
            self.snake.draw_snake()
            self.apple.draw_apple()
            pygame.display.update()


    def draw_background(self):
        self.display_surface.fill(LIGHT_COLOR)
        for rect in self.bg_rects:
            pygame.draw.rect(self.display_surface, DARK_COLOR, rect)


    def input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.snake.direction.x != -1:
            self.snake.direction = pygame.Vector2(1, 0)

        if keys[pygame.K_LEFT] or keys[pygame.K_a] and self.snake.direction.x != 1:
            self.snake.direction = pygame.Vector2(-1, 0)

        if keys[pygame.K_UP] or keys[pygame.K_w] and self.snake.direction.y != 1:
            self.snake.direction = pygame.Vector2(0, -1)

        if keys[pygame.K_DOWN] or keys[pygame.K_s] and self.snake.direction.y != -1:
            self.snake.direction = pygame.Vector2(0, 1)


    def check_collision(self):
        if self.snake.body[0] == self.apple.pos:
            self.snake.ate = True
            self.apple.set_position()
            self.eat_sound.play()


        if self.snake.body[0] in self.snake.body[1:] or \
            not 0 <= self.snake.body[0].x < COLS or \
            not 0 <= self.snake.body[0].y < ROWS :
            self.snake.reset()
            self.game_active = False









if __name__ == '__main__':
    main = Main()
    main.run()
