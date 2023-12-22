import random
from math import sqrt
from random import randint

import pygame
from pygame import Vector2, Surface

from src import AntWorld


class Nest(pygame.sprite.Sprite):
    ant_radius: int = 6
    pos: Vector2
    active_ant: int = 0

    def __init__(self, world: AntWorld, x: int, y: int):
        super().__init__()

        self.antImg = None
        self.world = world
        self.pos = pygame.Vector2(x, y)

        print('Nest:', self)
        self.energy = 500

        self.radius = int(self.energy / 20)

        self.load_images()

        self.workers = pygame.sprite.Group()
        # ants_count = randint(200, 2000)
        ants_count = 10
        for n in range(ants_count):
            self.addWorker()

    def addWorker(self):
        from src.swarm.AntWorker import AntWorker
        x, y = self.getNewWorkerPosition()
        self.workers.add(AntWorker(self, x, y))

    def getNewWorkerPosition(self):
        br = self.radius + self.ant_radius

        # (x-a)^2 + (y-b)^2 = r^2
        # x = rand(a-r, a+r)
        # y=sqrt(r^2 - (x-a)^2) + b
        x = randint(self.pos.x - br, self.pos.x + br)
        # x= self.pos_x

        discr = sqrt(pow(br, 2) - pow(x - self.pos.x, 2))
        discr = random.choice((-1, 1)) * discr

        y = int(discr) + self.pos.y

        return x, y

    def update(self, dt):
        self.energy -= 1

        if 1 > self.energy:
            # print('Nest: died', self)
            self.kill()

        self.radius = int(self.energy / 20)

        self.workers.update(dt)

    def draw(self, surface: Surface):
        pygame.draw.circle(surface, [40, 10, 10], self.pos, self.radius, self.radius)

        # draw dot in center of nest
        surface.set_at(self.pos, 'white')

        self.workers.draw(surface)

    def get_ant(self):
        ants = self.workers.sprites()

        if len(ants) == 0:
            print("Nest: No Ant found")
            return None

        return ants[self.active_ant]

    def load_images(self):

        # load image to speed up all ants draw

        # saved from first game
        self.antImg = pygame.image.load('imgs/ant_draw.png')

        # high resolution image but bad at small size
        # self.antImg = pygame.image.load('imgs/ant.png')
        # self.ant_radius = 6
        # use height because ants has height bigger than width on picture
        # scale = round(2 * self.ant_radius / self.antImg.get_height(), 2)

        # create dynamically
        # self.antImg = pygame.Surface((12, 21), pygame.SRCALPHA, 32).convert_alpha()
        # self.image.set_colorkey(0)
        # cBrown = (100, 42, 42, 255)
        # Draw Ant
        # pygame.draw.aaline(self.antImg, cBrown, [0, 5], [11, 15])
        # pygame.draw.aaline(self.antImg, cBrown, [0, 15], [11, 5])  # legs
        # pygame.draw.aaline(self.antImg, cBrown, [0, 10], [12, 10])
        # pygame.draw.aaline(self.antImg, cBrown, [2, 0], [4, 3])  # antena l
        # pygame.draw.aaline(self.antImg, cBrown, [9, 0], [7, 3])  # antena r
        # pygame.draw.ellipse(self.antImg, cBrown, [3, 2, 6, 6])  # head
        # pygame.draw.ellipse(self.antImg, cBrown, [4, 6, 4, 9])  # body
        # pygame.draw.ellipse(self.antImg, cBrown, [3, 13, 6, 8])  # rear

        # if not isfile("imgs/ant_draw.png"):
        #     pygame.image.save_extended(self.image, "imgs/ant_draw.png")

        # rotate to window coordinates
        # self.antImg = pygame.transform.rotozoom(self.antImg, -90, scale)
        self.antImg = pygame.transform.rotate(self.antImg, -90)

        self.antW = self.antImg.get_width()
        self.antH = self.antImg.get_height()
        pass

    def __str__(self):
        return "pos:" + str(self.pos)
