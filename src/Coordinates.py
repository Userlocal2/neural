import pygame

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 3

    def keyUpdate(self, event):
        print('keyUpdate: ', event)
        if event.key == pygame.K_LEFT:
            self.x -= self.speed
        if event.key == pygame.K_RIGHT:
            self.x += self.speed
        if event.key == pygame.K_UP:
            self.y -= self.speed
        if event.key == pygame.K_DOWN:
            self.y += self.speed

    def updateYup(self, y):
        self.y += y

    def get(self):
        print('get: ', self.x, self.y)
        return self.x, self.y
