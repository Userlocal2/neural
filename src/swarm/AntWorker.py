from math import atan2, degrees, cos, radians, sin
from random import randint

import pygame
from pygame import Vector2

from src.swarm import Nest


class AntWorker(pygame.sprite.Sprite):
    pos: Vector2
    nest: Nest

    # world: object

    def __init__(self, nest: Nest, x: int, y: int):
        super().__init__()
        self.nest = nest
        # self.world = self.nest.world

        self.life = randint(90, 120)

        # init position
        self.pos = pygame.Vector2(x, y)

        # the ant needs to be turned away from the nest (Returns the arc tangent of y/x in radians)
        self.angle = degrees(atan2(self.pos.y - self.nest.pos.y, self.pos.x - self.nest.pos.x))
        self.angle = int(self.angle)
        # self.angle = 10

        print('Ant:', self)

        self.rot_center(self.nest.antImg, self.angle, self.pos)

        # self.desireDir = pygame.Vector2(cos(radians(self.angle)), sin(radians(self.angle)))
        # self.vel = pygame.Vector2(0, 0)

    def update(self, dt):
        self.life -= 0.1
        if 1 > self.life:
            self.kill()

        # randAng = randint(0, 360)

        # maxSpeed = 1
        # wandrStr = .01
        # steerStr = 5

        # self.desireDir += pygame.Vector2(1, 0).rotate(self.angle).normalize()

        # print('Rind dir:',cos(radians(randAng)), sin(radians(randAng)))
        # randDir = pygame.Vector2(cos(radians(randAng)), sin(radians(randAng)))
        # self.desireDir = pygame.Vector2(self.desireDir + randDir * wandrStr).normalize()
        # dzVel = self.desireDir * maxSpeed
        # dzStrFrc = (dzVel - self.vel) * steerStr
        # accel = dzStrFrc if pygame.Vector2(dzStrFrc).magnitude() <= steerStr else pygame.Vector2(dzStrFrc.normalize() * steerStr)
        # velo = self.vel + accel * 1
        # self.vel = velo if pygame.Vector2(velo).magnitude() <= maxSpeed else pygame.Vector2(velo.normalize() * maxSpeed)
        # self.pos += self.vel * 1

        # self.angle = degrees(atan2(self.vel.x, self.vel.y))
        # print('Ant angle:', self.angle)

        # self.pos = pygame.Vector2(self.nest.getNewWorkerPosition())
        # self.angle = degrees(atan2(self.pos.y - self.nest.pos.y, self.pos.x - self.nest.pos.x))
        self.rot_center(self.nest.antImg, self.angle, self.pos)
        pass

    def rot_center(self, image, angle, pos: pygame.Vector2):
        # offset from pivot to center
        image_rect = image.get_rect(topleft=(pos.x - self.nest.antW / 2, pos.y - self.nest.antH / 2))
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

        # rotated offset from pivot to center
        rotated_offset = offset_center_to_pivot.rotate(-angle)

        # rotated image center
        rotated_image_center = (pos.x - rotated_offset.x, pos.y - rotated_offset.y)

        # get a rotated image
        self.image = pygame.transform.rotate(image, -angle)
        self.rect = self.image.get_rect(center=rotated_image_center)

    def turn(self, mode: str):
        if mode == "left":
            self.angle -= 5

        if mode == "right":
            self.angle += 5

        if self.angle > 360:
            self.angle = self.angle - 360

        if self.angle < -360:
            self.angle = self.angle + 360

        print('Ant:', self)
        pass

    def move(self, mode):
        speed = 5
        velocity = pygame.Vector2(cos(radians(self.angle)), sin(radians(self.angle))).normalize() * speed

        if mode == "forward":
            self.pos += velocity

        if mode == "backward":
            self.pos -= velocity

        print('Ant:', self)
        pass

    def __str__(self):
        return "pos:" + str(self.pos) + " angle:" + str(self.angle)
