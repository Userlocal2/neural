from typing import Union, Any

import pygame
from pygame import Surface

from src.AntWorld import AntWorld
from src.swarm.Pheromone import APheromone


class AntsGame:
    HEIGHT: str
    WIDTH: str

    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height

        self.antsWorld = AntWorld(width, height)
        self.antsWorld.init()

        self.surface = Surface((width, height))

    def draw(self):
        self.surface.fill(0)
        surface = self.antsWorld.draw(self.surface)
        # Optimize the images after they're drawn
        surface.convert()
        return surface

    def update(self, dt):
        self.antsWorld.update(dt)

    def event(self, key: int):
        from src.swarm.AntWorker import AntWorker
        ant: AntWorker = self.antsWorld.get_ant()

        if key == pygame.K_LEFT:
            ant.turn("left")

        if key == pygame.K_RIGHT:
            ant.turn("right")

        if key == pygame.K_UP:
            ant.move("forward")

        if key == pygame.K_DOWN:
            ant.move("backward")

        if key == pygame.K_a:
            self.antsWorld.drawAngle = not self.antsWorld.drawAngle
        pass
