import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((192, 192, 192))
FPS = 30
# face
circle(screen, (255, 255, 0), (300, 300), 200)
circle(screen, (0, 0, 0), (300, 300), 200, 3)
# left eye
circle(screen, (255, 0, 0), (225, 225), 35)
circle(screen, (0, 0, 0), (225, 225), 35, 1)
circle(screen, (0, 0, 0), (225, 225), 15)
# right eye
circle(screen, (255, 0, 0), (375, 225), 30)
circle(screen, (0, 0, 0), (375, 225), 30, 1)
circle(screen, (0, 0, 0), (375, 225), 13)

line(screen, (0, 0, 0), (120, 120), (270, 210), 15)
line(screen, (0, 0, 0), (460, 175), (330, 210), 15)
line(screen, (0, 0, 0), (200, 390), (400, 390), 28)


pygame.display.update()
clock = pygame.time.Clock()
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()