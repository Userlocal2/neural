import pygame as pg
import numpy as np

from src.AntWorld import AntWorld

FPS = 60


class AntPheromone:
    pRatio = 5

    def __init__(self, world: AntWorld):
        self.surfSize = (int(world.WIDTH / self.pRatio), int(world.HEIGHT / self.pRatio))
        self.image = pg.Surface(self.surfSize).convert()
        self.img_array = np.array(pg.surfarray.array3d(self.image), dtype=float)  # .astype(np.float64)

    def update(self, dt):
        self.img_array -= .2 * (60 / FPS) * ((dt / 10) * FPS)  # [self.img_array > 0] # dt might not need FPS parts
        self.img_array = self.img_array.clip(0, 255)
        pg.surfarray.blit_array(self.image, self.img_array)
        return self.image
