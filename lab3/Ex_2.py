import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((700, 900))
screen.fill((102, 153, 102))
FPS = 30

RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (102, 153, 51)
YELLOW = (201, 153, 0)
EARTH = (153, 102, 51)
LIGHT = (180, 130, 130)
DARK = (0, 0, 0)
BROWN = (255, 153, 51)
SPIKE = (58, 44, 44)
BODY = (71, 61, 61)


def draw_line(color, pos1, pos2, x, y, width):  # Draws a line
    line(screen, color, [pos1, pos2], [x, y], width)


def draw_rect(color, border, pos1, pos2, x, y,):  # Draws a rectangle
    rect(screen, color, [pos1, pos2, x, y])
    rect(screen, border, [pos1, pos2, x, y], 1)


def draw_eyes_nose(x, y):
    circle(screen, (0, 0, 0), (x, y), 5)
    circle(screen, LIGHT, (x, y), 5, 1)
    circle(screen, (0, 0, 0), (x - 15, y + 6), 5)
    circle(screen, LIGHT, (x - 15, y + 6), 5, 1)
    circle(screen, (0, 0, 0), (x + 24, y + 8), 4)
    circle(screen, LIGHT, (x + 24, y + 8), 4, 1)


def draw_ell(color, border, pos1, pos2, x, y):
    ellipse(screen, color, [pos1, pos2, x, y])
    ellipse(screen, border, [pos1, pos2, x, y], 1)


def draw_spikes_1(x, y):
    d = 0
    for i in range(1, 8):
        polygon(screen, SPIKE, [(x + d, y),
                                (x + 14 + d, y - 14),
                                (x - 4050**0.5 + d, y - 4050**0.5)])
        polygon(screen, DARK, [(x + d, y),
                               (x + 14 + d, y - 14),
                               (x - 4050**0.5 + d, y - 4050**0.5)], 1)
        polygon(screen, SPIKE, [(x + 16 + d, y - 16),
                                (x + 14 + d + 16, y - 14 - 16),
                                (x - 4050 ** 0.5 + d + 16, y - 4050 ** 0.5 - 16)])
        polygon(screen, DARK, [(x + d + 16, y - 16),
                               (x + 14 + d + 16, y - 14 - 16),
                               (x - 4050 ** 0.5 + d + 16,
                                y - 4050 ** 0.5 - 16)], 1)
        d += 22


def draw_spikes_2(x, y):
    a = 16  # base of triangle
    dx = 0  # change pos of x
    dy = 0  # change pos of y

    polygon(screen, SPIKE, [(x + dx, y + dy), (x + dx + a, y + dy), (x + dx + a/2, y + dy - 90)])
    polygon(screen, DARK, [(x + dx, y + dy), (x + dx + a, y + dy), (x + 8 + dx,
                                                                    y + dy - 90)], 1)
    dx = 16
    polygon(screen, SPIKE, [(x + dx, y + dy), (x + dx + a, y + dy), (x + dx + a / 2, y + dy - 90)])
    polygon(screen, DARK, [(x + dx, y + dy), (x + dx + a, y + dy), (x + 8 + dx,
                                                                    y + dy - 90)], 1)
    dx = 32
    dy = -20
    polygon(screen, SPIKE, [(x + dx, y + dy), (x + dx + a, y + dy), (x + dx + a / 2, y + dy - 90)])
    polygon(screen, DARK, [(x + dx, y + dy), (x + dx + a, y + dy), (x + 8 + dx,
                                                                    y + dy - 90)], 1)
    dx = 50
    dy = -20
    polygon(screen, SPIKE, [(x + dx, y + dy), (x + dx + a, y + dy), (x + dx + a / 2, y + dy - 90)])
    polygon(screen, DARK, [(x + dx, y + dy), (x + dx + a, y + dy), (x + 8 + dx,
                                                                    y + dy - 90)], 1)
    dx = 25
    dy = 25
    polygon(screen, SPIKE, [(x + dx, y + dy), (x + dx + a, y + dy), (x + dx + a / 2, y + dy - 90)])
    polygon(screen, DARK, [(x + dx, y + dy), (x + dx + a, y + dy), (x + 8 + dx,
                                                                    y + dy - 90)], 1)
    dx = 40
    dy = 25
    polygon(screen, SPIKE, [(x + dx, y + dy), (x + dx + a, y + dy), (x + dx + a / 2, y + dy - 90)])
    polygon(screen, DARK, [(x + dx, y + dy), (x + dx + a, y + dy), (x + 8 + dx,
                                                                    y + dy - 90)], 1)
    dx = 70
    dy = 20
    polygon(screen, SPIKE, [(x + dx, y + dy), (x + dx + a, y + dy), (x + dx + a / 2, y + dy - 90)])
    polygon(screen, DARK, [(x + dx, y + dy), (x + dx + a, y + dy), (x + 8 + dx,
                                                                    y + dy - 90)], 1)
    dx = 85
    dy = 5
    polygon(screen, SPIKE, [(x + dx, y + dy), (x + dx + a, y + dy), (x + dx + a / 2, y + dy - 90)])
    polygon(screen, DARK, [(x + dx, y + dy), (x + dx + a, y + dy), (x + 8 + dx,
                                                                    y + dy - 90)], 1)


def draw_spikes_3(x, y):
    a = 8  # base of triangle
    dx = 0  # change pos of x
    dy = 0  # change pos of y
    for i in range(1, 5):
        for i in range(1, 4):
            polygon(screen, SPIKE, [(x + dx, y - dy), (x + dx + 4 + a,
                                                       y - 6.9 - dy), (x + dx - 45 + a / 2, y - 77.94 - dy)])
            polygon(screen, DARK, [(x + dx, y - dy), (x + dx + 4 + a,
                                                      y - 6.9 - dy), (x + dx - 45 + a / 2, y - 77.94 - dy)], 1)
            dx += 12
            dy += 7
        dx += 10
        dy = 0


def draw_spikes_4(x, y):
    a = 8  # base of triangle
    dx = 0  # change pos of x
    dy = 0  # change pos of y
    for i in range(1, 5):
        for i in range(1, 4):
            polygon(screen, SPIKE, [(x + dx, y - dy - 6.9),
                                    (x + dx + 4 + a, y - dy), (x + dx + 45 + a / 2, y - 77.94 - dy)])
            polygon(screen, DARK, [(x + dx, y - dy - 6.9), (x + dx + 4 + a, y - dy),
                                   (x + dx + 45 + a / 2, y - 77.94 - dy)], 1)
            dx -= 18
            dy -= 7
        dx += 20
        dy = 0


def draw_amanita(x, y):
    ellipse(screen, WHITE, [(x + 63, y + 20), (- 30, 75)])
    ellipse(screen, RED, [(x, y), (100, 40)])
    ellipse(screen, LIGHT, [(x, y), (100, 40)], 1)
    ellipse(screen, WHITE, [(x + 10, y + 12), (10, 7)])
    ellipse(screen, LIGHT, [(x + 10, y + 12), (10, 7)], 1)
    ellipse(screen, WHITE, [(x + 30, y + 8), (9, 4)])
    ellipse(screen, LIGHT, [(x + 30, y + 8), (9, 4)], 1)
    ellipse(screen, WHITE, [(x + 27, y + 20), (11, 7)])
    ellipse(screen, LIGHT, [(x + 27, y + 20), (11, 7)], 1)
    ellipse(screen, WHITE, [(x + 50, y + 14), (12, 9)])
    ellipse(screen, LIGHT, [(x + 50, y + 14), (12, 9)], 1)
    ellipse(screen, WHITE, [(x + 65, y + 7), (10, 4)])
    ellipse(screen, LIGHT, [(x + 65, y + 7), (10, 4)], 1)
    ellipse(screen, WHITE, [(x + 75, y + 21), (12, 7)])
    ellipse(screen, LIGHT, [(x + 75, y + 21), (12, 7)], 1)


def draw_mroom(x, y):
    ellipse(screen, BROWN, [(x, y), (55, 60)])
    ellipse(screen, LIGHT, [(x, y), (55, 60)], 1)


def draw_apple(x, y):
    ellipse(screen, RED, [(x, y), (65, 65)])
    ellipse(screen, LIGHT, [(x, y), (65, 65)], 1)


# Ground
draw_rect(EARTH, LIGHT, -5, 500, 710, 400)
# Trees
draw_rect(YELLOW, LIGHT, -5, -5, 75, 570)
draw_rect(YELLOW, LIGHT, 105, -5, 175, 880)
draw_rect(YELLOW, LIGHT, 500, -5, 80, 570)
draw_rect(YELLOW, LIGHT, 630, -5, 58, 700)
draw_ell(BODY, LIGHT, 352, 770, 40, 15)  # Paw
draw_ell(BODY, LIGHT, 561, 775, 20, 18)  # Paw
draw_ell(BODY, LIGHT, 360, 710, 220, 100)  # Body
draw_spikes_1(380, 760)
draw_ell(BODY, LIGHT, 373, 785, 33, 18)  # Paw
draw_ell(BODY, LIGHT, 533, 792, 26, 17)  # Paw
draw_spikes_4(530, 740)
draw_spikes_4(540, 780)
draw_spikes_4(520, 780)
draw_spikes_3(380, 740)
draw_spikes_3(380, 760)
draw_amanita(410, 640)
draw_mroom(355, 700)
draw_apple(484, 684)
draw_spikes_3(375, 780)
draw_mroom(370, 692)
draw_spikes_2(410, 750)
draw_ell(BODY, LIGHT, 540, 740, 70, 40)  # Head
draw_eyes_nose(585, 750)


'''# coordinate grid
a = 100
b = 100
for i in range(1, 7):
    draw_line(WHITE, a, 0, a, 900, 2)
    a += 100

for i in range(1, 9):
    draw_line(WHITE, 0, b, 900, b, 2)
    b += 100'''

pygame.display.update()
clock = pygame.time.Clock()
pygame.display.flip()
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
