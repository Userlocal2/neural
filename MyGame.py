import math

import pygame

from src.AntsGame import AntsGame

# initial constants
WIDTH = 1280
HEIGHT = 720
FPS = 60

# describe window work
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED, vsync=True)

ants_game = AntsGame(WIDTH, HEIGHT)

font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()

# main loop
running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN:
            ants_game.event(event.key)

    dt = clock.tick(FPS) / 100
    # print('Delta:', dt)

    ants_game.update(dt)

    surface = ants_game.draw()
    screen.blit(surface, surface.get_rect())

    # draw FPS counter
    screen.blit(font.render(str(int(clock.get_fps())), True, [0, 200, 0]), (8, 8))

    pygame.display.update()
