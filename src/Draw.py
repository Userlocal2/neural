import pygame as pg
import numpy as np

from src.swarm.Pheromone import *
from src.swarm.Ant import *
from src.swarm.Food import *


class Draw:
    FLLSCRN = False
    VSYNC = True  # limit frame rate to refresh rate
    SHOWFPS = True  # show framerate debug
    WIDTH = 800
    HEIGHT = 600
    ANTS = 42  # Number of Ants to spawn

    def __init__(self, width, height, fllscrm=False):
        # print("2. Initialize the new instance of Point.")
        self.WIDTH = width
        self.HEIGHT = height
        self.FLLSCRN = fllscrm

    def update(self):
        print(123)

    def main(self):
        pg.init()  # prepare window
        pg.display.set_caption("NAnts")
        # try:
        #     pg.display.set_icon(pg.img.load("nants.png"))
        # except:
        #     print("FYI: nants.png icon not found, skipping..")
        # setup fullscreen or window mode
        if self.FLLSCRN:  # screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
            currentRez = (pg.display.Info().current_w, pg.display.Info().current_h)
            screen = pg.display.set_mode(currentRez, pg.SCALED | pg.NOFRAME | pg.FULLSCREEN, vsync=self.VSYNC)
        else:
            screen = pg.display.set_mode((self.WIDTH, self.HEIGHT), pg.SCALED, vsync=self.VSYNC)

        cur_w, cur_h = screen.get_size()
        screenSize = (cur_w, cur_h)
        nest = (cur_w / 3, cur_h / 2)

        # background = pg.img.load("background.png").convert_alpha()

        workers = pg.sprite.Group()
        pheroLayer = APheromone(screenSize)

        for n in range(self.ANTS):
            workers.add(Ant(screen, nest, pheroLayer))

        foodList = []
        foods = pg.sprite.Group()
        font = pg.font.Font(None, 30)
        clock = pg.time.Clock()
        fpsChecker = 0
        # main loop
        while True:
            for e in pg.event.get():
                if e.type == pg.QUIT or e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                    return
                elif e.type == pg.MOUSEBUTTONDOWN:
                    mousepos = pg.mouse.get_pos()
                    if e.button == 1:  # and pg.Vector2(mousepos).distance_to(nest) > 242:
                        foodBits = 200
                        fRadius = 50
                        for i in range(0, foodBits):  # spawn food bits evenly within a circle
                            dist = pow(i / (foodBits - 1.0), 0.5) * fRadius
                            angle = 2 * pi * 0.618033 * i
                            fx = mousepos[0] + dist * cos(angle)
                            fy = mousepos[1] + dist * sin(angle)
                            foods.add(Food((fx, fy)))
                        foodList.extend(foods.sprites())
                    if e.button == 3:
                        for fbit in foodList:
                            if pg.Vector2(mousepos).distance_to(fbit.rect.center) < fRadius + 5:
                                fbit.pickup()
                        foodList = foods.sprites()

            dt = clock.tick(FPS) / 100

            pheroImg = pheroLayer.update(dt)
            pheroLayer.img_array[170:182, 0:80] = (50, 50, 50)  # wall

            workers.update(dt)

            screen.fill(0)  # fill MUST be after sensors update, so previous draw is visible to them

            rescaled_img = pg.transform.scale(pheroImg, (cur_w, cur_h))
            pg.Surface.blit(screen, rescaled_img, (0, 0))

            # workers.update(dt)  # enable here to see debug dots
            foods.draw(screen)

            pg.draw.circle(screen, [40, 10, 10], (nest[0], nest[1] + 6), 6, 3)
            pg.draw.circle(screen, [50, 20, 20], (nest[0], nest[1] + 4), 9, 4)
            pg.draw.circle(screen, [60, 30, 30], (nest[0], nest[1] + 2), 12, 4)
            pg.draw.circle(screen, [70, 40, 40], nest, 16, 5)

            # pg.draw.rect(screen, (50,50,50), [900, 0, 50, 500]) # test wall

            workers.draw(screen)

            if self.SHOWFPS: screen.blit(font.render(str(int(clock.get_fps())), True, [0, 200, 0]), (8, 8))

            pg.display.update()
