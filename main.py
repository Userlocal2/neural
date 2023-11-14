import pygame
from src.Coordinates import *

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
coordinates = Coordinates(window_width * 0.45, window_height * 0.8)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(white)

    if event.type == pygame.KEYDOWN:
        coordinates.keyUpdate(event)
    else: 
        coordinates.updateYup(-1)
    screen.blit(carImg, (coordinates.get())) 

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)  

pygame.quit()