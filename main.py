import pygame
# import src.Draw
from src.Draw import *

black = (0,0,0)
white = (255,255,255)

window_width = 1280
window_height = 720

# pygame setup
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
running = True

carImg = pygame.image.load('imgs/racecar.png')

def car(x,y):
    screen.blit(carImg, (x,y))

x = (window_width * 0.45)
y = (window_height * 0.8)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(white)

    car(x,y)

    y -= 1

    # RENDER YOUR GAME HERE
    # draw = Draw()
    # draw.update()


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)  

pygame.quit()