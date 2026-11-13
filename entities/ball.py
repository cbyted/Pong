import pygame
import random


"""
Class para la pelota
"""


class ball:
    def __init__(self, coord_x, coord_y, radio, speed, bounds):
        """
        bouds es una lista que contiene [up, bottom, left, right]
        """
        self.speed_x = speed
        self.speed_y = speed

        self.bounds = bounds
        self.pos = [coord_x, coord_y]
        self.radio = radio

    def draw(self, screen, color):
        """
        función para dibujar el jugador y retornar el objeto
        """
        pygame.draw.circle(screen, color, self.pos, self.radio)

    def get_rect(self):
        return pygame.Rect(
            self.pos[0] - self.radio,
            self.pos[1] - self.radio,
            self.radio * 2,
            self.radio * 2,
        )

    def bounce(self, sound):
        self.speed_x *= -1
        self.speed_y = random.randint(-8, 8)
        sound.play()

    def move(self):
        """
        Función para moder el jugador
        """
        self.pos[0] += self.speed_x
        self.pos[1] -= self.speed_y

        # Limite superior e inferior
        if (self.pos[1] < self.bounds[0]) or (self.pos[1] > self.bounds[1]):
            self.speed_y *= -1
