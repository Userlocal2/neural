import pygame as pg
import numpy as np

FPS = 60

class APheromone:
    pRatio = 5
    def __init__(self, bigSize):
        self.surfSize = (int(bigSize[0] / self.pRatio), int(bigSize[1] / self.pRatio))
        self.image = pg.Surface(self.surfSize).convert()
        self.img_array = np.array(pg.surfarray.array3d(self.image), dtype=float)  # .astype(np.float64)

    def update(self, dt):
        self.img_array -= .2 * (60 / FPS) * ((dt / 10) * FPS)  # [self.img_array > 0] # dt might not need FPS parts
        self.img_array = self.img_array.clip(0, 255)
        pg.surfarray.blit_array(self.image, self.img_array)
        return self.image