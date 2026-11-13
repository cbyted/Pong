import pygame

"""
Class para el jugador 
"""


class Paddle:
    def __init__(self, coord_x, coord_y, width, height, speed, bounds):
        """
        bouds es una lista que contiene [up, bottom]
        """
        self.speed = speed
        self.bounds = bounds
        self.pos = coord_y
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.width = width
        self.height = height

    def draw(self, screen, color):
        """
        Función para dibujar el jugador y retornar el objeto
        """
        rect = pygame.Rect(self.coord_x, self.pos, self.width, self.height)
        pygame.draw.rect(screen, color, rect)

    def get_rect(self):
        return pygame.Rect(self.coord_x, self.pos, self.width, self.height)

    def start_pos(self, coord_y):
        self.pos = coord_y

    def move(self, key):
        """
        Función para moder el jugador
        """
        if key == "UP":
            if (self.pos - self.speed) > self.bounds[0]:
                self.pos -= self.speed
            else:
                self.pos = 0
        if key == "DOWN":
            if (self.pos + self.speed) < self.bounds[1]:
                self.pos += self.speed
            else:
                self.pos = self.bounds[1]
