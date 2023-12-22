from random import randint
from math import cos, sin, radians
from typing import Union

import pygame
from pygame import Surface, SurfaceType

from src.swarm.Nest import Nest


class AntWorld:
    nest: Nest
    pheroLayer: object

    drawAngle: bool

    def __init__(self, width: int, height: int):
        self.drawAngle = False

        self.WIDTH = width
        self.HEIGHT = height

    def init(self):
        # next import is only because python may import loop between files
        from src.swarm.AntPheromone import AntPheromone
        self.pheroLayer = AntPheromone(self)

        # pos_x = randint(50, self.HEIGHT - 50 * 2)
        # pos_y = randint(50, self.WIDTH - 50 * 2)
        pos_x = int(self.WIDTH / 2)
        pos_y = int(self.HEIGHT / 2)
        self.nest = Nest(self, pos_x, pos_y)

    def update(self, dt):
        self.nest.update(dt)

    def draw(self, surface: Surface):
        self.nest.draw(surface)

        if self.drawAngle:

            len = 2 * self.nest.ant_radius + 15

            for ant in self.nest.workers.sprites():
                x = ant.pos.x + cos(radians(ant.angle)) * len
                y = ant.pos.y + sin(radians(ant.angle)) * len

                pygame.draw.line(surface, "green", ant.pos, (x, y), 2)

            # draw line with 0 angle
            # x = self.nest.pos.x + cos(radians(10)) * len
            # y = self.nest.pos.y + sin(radians(10)) * len

            # pygame.draw.line(surface, "green", self.nest.pos, (x, y), 2)

        return surface

    def get_ant(self):
        return self.nest.get_ant()
