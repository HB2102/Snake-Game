import pygame
from settings import *
from os import walk


class Snake:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.body = [pygame.Vector2(START_COL - col, START_ROW) for col in range(START_LENGTH)]
        self.direction = pygame.Vector2(1, 0)
        self.ate = False
        self.draw_data = []

        self.surfaces = self.import_surfaces()
        self.draw_data = []
        self.head = self.surfaces['head_right']
        self.tail = self.surfaces['tail_left']

        self.update_body()



    def reset(self):
        self.body = [pygame.Vector2(START_COL - col, START_ROW) for col in range(START_LENGTH)]
        self.direction = pygame.Vector2(1, 0)

        self.update_head()
        self.update_tail()
        self.update_body()


    def move(self):
        if not self.ate:
            body_copy = self.body[:-1]
        else:
            body_copy = self.body[:]
            self.ate = False

        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy

        self.update_head()
        self.update_tail()
        self.update_body()


    def draw_snake(self):
        # for point in self.body:
        #     rect = pygame.Rect(point.x * CELL_SIZE, point.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        #     pygame.draw.rect(self.display_surface, 'red', rect)

        for surf, rect in self.draw_data:
            self.display_surface.blit(surf, rect)


    def import_surfaces(self):
        surface_dict = {}
        for folder_path, _, image_names in walk(join('.', 'pictures', 'snake_body')):
            for image in image_names:
                full_path = join(folder_path, image)
                surface = pygame.image.load(full_path).convert_alpha()
                surface_dict[image.split('.')[0]] = surface

        return surface_dict


    def update_body(self):
        self.draw_data = []
        for index, part in enumerate(self.body):
            x = part.x * CELL_SIZE
            y = part.y * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

            if index == 0:
                self.draw_data.append((self.head, rect))

            elif index == len(self.body) - 1 :
                self.draw_data.append((self.tail, rect))

            else:
                previous_part = self.body[index + 1] - part
                next_part = self.body[index - 1] - part

                if previous_part.x == next_part.x :
                    self.draw_data.append((self.surfaces['body_horizontal'], rect))

                elif previous_part.y == next_part.y :
                    self.draw_data.append((self.surfaces['body_vertical'], rect))

                else:
                    if (previous_part.x == -1 and next_part.y == -1) or (previous_part.y == -1 and next_part.x == -1):
                        self.draw_data.append((self.surfaces['body_tl'], rect))

                    elif (previous_part.x == -1 and next_part.y == 1) or (previous_part.y == 1 and next_part.x == -1):
                        self.draw_data.append((self.surfaces['body_bl'], rect))

                    elif (previous_part.x == 1 and next_part.y == -1) or (previous_part.y == -1 and next_part.x == 1):
                        self.draw_data.append((self.surfaces['body_tr'], rect))

                    if (previous_part.x == 1 and next_part.y == 1) or (previous_part.y == 1 and next_part.x == 1):
                        self.draw_data.append((self.surfaces['body_br'], rect))



    def update_head(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == pygame.Vector2(-1, 0):
            self.head = self.surfaces['head_right']

        elif head_relation == pygame.Vector2(1, 0):
            self.head = self.surfaces['head_left']

        elif head_relation == pygame.Vector2(0, -1):
            self.head = self.surfaces['head_down']

        elif head_relation == pygame.Vector2(0, 1):
            self.head = self.surfaces['head_up']


    def update_tail(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == pygame.Vector2(-1, 0):
            self.tail = self.surfaces['tail_right']

        elif tail_relation == pygame.Vector2(1, 0):
            self.tail = self.surfaces['tail_left']

        elif tail_relation == pygame.Vector2(0, -1):
            self.tail = self.surfaces['tail_down']

        elif tail_relation == pygame.Vector2(0, 1):
            self.tail = self.surfaces['tail_up']