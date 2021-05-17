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


def main():
    # Ground
    draw_rect(EARTH, LIGHT, -5, 500, 710, 400)
    # Trees
    draw_rect(YELLOW, LIGHT, -5, -5, 75, 570)
    draw_rect(YELLOW, LIGHT, 105, -5, 175, 880)
    draw_rect(YELLOW, LIGHT, 500, -5, 80, 570)
    draw_rect(YELLOW, LIGHT, 630, -5, 58, 700)
    draw_hedgehog(360, 710, 220)  # Рисует ежа в точке x, y, шириной width
    draw_hedgehog(120, 770, 100)


def draw_hedgehog(x, y, width_hh):
    height_hh = width_hh/2
    width_paw_1 = width_hh/5.5
    height_paw_1 = width_paw_1* .375
    width_paw_2 = width_hh/11
    height_paw_2 = width_paw_2*0.9
    width_paw_3 = width_hh*0.15
    height_paw_3 = width_paw_3/1.83
    width_paw_4 = width_hh*0.118
    height_paw_4 = width_paw_4/1.52
    multiplier = width_hh / 220
    head_width = width_hh*0.318
    head_height = head_width/1.75
    draw_ell(BODY, LIGHT, x - 8, y + 60,  width_paw_1, height_paw_1)  # Paw
    draw_ell(BODY, LIGHT, x + 201, y + 65, width_paw_2, height_paw_2)  # Paw
    draw_ell(BODY, LIGHT, x, y, width_hh, height_hh)  # Body
    draw_spikes_1(x + 20, y + 50, multiplier)
    draw_ell(BODY, LIGHT, x + 13, y + 75, width_paw_3, height_paw_3)  # Paw
    draw_ell(BODY, LIGHT, x + 173, y + 82, width_paw_4, height_paw_4)  # Paw
    draw_spikes_4(x + 170, y + 30, multiplier)
    draw_spikes_4(x + 180, y + 70, multiplier)
    draw_spikes_4(x + 160, y + 70, multiplier)
    draw_spikes_3(x + 20, y + 30, multiplier)
    draw_spikes_3(x + 20, y + 50, multiplier)
    draw_amanita(x + 50, y - 70, multiplier)
    draw_mroom(x - 5, y - 10, multiplier)
    draw_apple(x + 124, y - 26, multiplier)
    draw_spikes_3(x + 15, y + 70, multiplier)
    draw_mroom(x + 10, y - 18, multiplier)
    draw_spikes_2(x + 50, y + 40,multiplier)
    draw_ell(BODY, LIGHT, x + 180, y + 30, head_width, head_height)  # Head
    draw_eyes_nose(585, 750, multiplier)


def draw_line(color, pos1, pos2, x, y, width):  # Draws a line
    line(screen, color, [pos1, pos2], [x, y], width)


def draw_rect(color, border, pos1, pos2, x, y,):  # Draws a rectangle
    rect(screen, color, [pos1, pos2, x, y])
    rect(screen, border, [pos1, pos2, x, y], 1)


def draw_eyes_nose(x, y,  multiplier):
    circle(screen, (0, 0, 0), (x, y), 5)
    circle(screen, LIGHT, (x, y), 5, 1)
    circle(screen, (0, 0, 0), (x - 15, y + 6), 5)
    circle(screen, LIGHT, (x - 15, y + 6), 5, 1)
    circle(screen, (0, 0, 0), (x + 24, y + 8), 4)
    circle(screen, LIGHT, (x + 24, y + 8), 4, 1)


def draw_ell(color, border, pos1, pos2, x, y):
    ellipse(screen, color, [pos1, pos2, x, y])
    ellipse(screen, border, [pos1, pos2, x, y], 1)


def draw_spikes_1(x, y, spike_multiplier):
    d = 0
    base = 14*spike_multiplier
    spike_length = 4050**0.5*spike_multiplier
    for i in range(1, 8):
        polygon(screen, SPIKE, [(x + d, y),
                                (x + base + d, y - base),
                                (x - spike_length + d, y - spike_length)])
        polygon(screen, DARK, [(x + d, y),
                               (x + base + d, y - base),
                               (x - spike_length + d, y - spike_length)], 1)
        polygon(screen, SPIKE, [(x + 16 + d, y - 16),
                                (x + base + d + 16, y - base - 16),
                                (x - spike_length + d + 16, y - spike_length - 16)])
        polygon(screen, DARK, [(x + d + 16, y - 16),
                               (x + base + d + 16, y - base - 16),
                               (x - spike_length + d + 16,
                                y - spike_length - 16)], 1)
        d += 22


def draw_spikes_2(x, y, multiplier):
    base = 16*multiplier  # base of triangle
    spike_length = 90*multiplier
    dx = 0  # change pos of x
    dy = 0  # change pos of y

    polygon(screen, SPIKE, [(x + dx, y + dy), (x + dx + base, y + dy), (x + dx + base/2,
                                                                        y + dy - spike_length)])
    polygon(screen, DARK, [(x + dx, y + dy), (x + dx + base, y + dy), (x + base/2 + dx,
                                                                       y + dy - spike_length)], 1)
    dx = 32
    dy = -20
    polygon(screen, SPIKE, [(x + dx, y + dy), (x + dx + base, y + dy), (x + dx + base/2,
                                                                        y + dy - spike_length)])
    polygon(screen, DARK, [(x + dx, y + dy), (x + dx + base, y + dy), (x + base/2 + dx,
                                                                       y + dy - spike_length)], 1)
    dx = 50
    dy = -20
    polygon(screen, SPIKE, [(x + dx, y + dy), (x + dx + base, y + dy), (x + dx + base/2,
                                                                        y + dy - spike_length)])
    polygon(screen, DARK, [(x + dx, y + dy), (x + dx + base, y + dy), (x + base/2 + dx,
                                                                       y + dy - spike_length)], 1)
    dx = 25
    dy = 25
    polygon(screen, SPIKE, [(x + dx, y + dy), (x + dx + base, y + dy), (x + dx + base/2,
                                                                        y + dy - spike_length)])
    polygon(screen, DARK, [(x + dx, y + dy), (x + dx + base, y + dy), (x + base/2 + dx,
                                                                       y + dy - spike_length)], 1)
    dx = 40
    dy = 25
    polygon(screen, SPIKE, [(x + dx, y + dy), (x + dx + base, y + dy), (x + dx + base/2,
                                                                        y + dy - spike_length)])
    polygon(screen, DARK, [(x + dx, y + dy), (x + dx + base, y + dy), (x + base/2 + dx,
                                                                       y + dy - spike_length)], 1)
    dx = 70
    dy = 20
    polygon(screen, SPIKE, [(x + dx, y + dy), (x + dx + base, y + dy), (x + dx + base/2,
                                                                        y + dy - spike_length)])
    polygon(screen, DARK, [(x + dx, y + dy), (x + dx + base, y + dy), (x + 8 + dx,
                                                                       y + dy - spike_length)], 1)
    dx = 85
    dy = 5
    polygon(screen, SPIKE, [(x + dx, y + dy), (x + dx + base, y + dy), (x + dx + base/2,
                                                                        y + dy - spike_length)])
    polygon(screen, DARK, [(x + dx, y + dy), (x + dx + base, y + dy), (x + base/2 + dx,
                                                                       y + dy - spike_length)], 1)


def draw_spikes_3(x, y, multiplier):
    base = 8*multiplier  # base of triangle
    spike_length = 77.94*multiplier
    dx = 0  # change pos of x
    dy = 0  # change pos of y
    for i in range(1, 5):
        for i in range(1, 4):
            polygon(screen, SPIKE, [(x + dx, y - dy), (x + dx + 4 + base,
                                                       y - 6.9 - dy), (x + dx - 45 + base / 2, y - spike_length - dy)])
            polygon(screen, DARK, [(x + dx, y - dy), (x + dx + 4 + base,
                                                      y - 6.9 - dy), (x + dx - 45 + base / 2, y - spike_length - dy)], 1)
            dx += 12
            dy += 7
        dx += 10
        dy = 0


def draw_spikes_4(x, y, multiplier):
    base = 8 * multiplier  # base of triangle
    spike_length = 77.94 * multiplier
    dx = 0  # change pos of x
    dy = 0  # change pos of y
    for i in range(1, 5):
        for i in range(1, 4):
            polygon(screen, SPIKE, [(x + dx, y - dy - 6.9),
                                    (x + dx + 4 + base, y - dy), (x + dx + 45 + base/2, y - spike_length - dy)])
            polygon(screen, DARK, [(x + dx, y - dy - 6.9), (x + dx + 4 + base, y - dy),
                                   (x + dx + 45 + base/2, y - spike_length - dy)], 1)
            dx -= 18
            dy -= 7
        dx += 20
        dy = 0


def draw_amanita(x, y, multiplier):
    foot_width = 35*multiplier
    foot_heigth = foot_width/0.4
    hat_width = foot_width/0.35
    hat_height = hat_width*0.4
    spot_width_1 = foot_width/3.5
    spot_height_1 = spot_width_1*0.7
    spot_width_2 = foot_width/3.888
    spot_height_2 = spot_width_2/2.25
    spot_width_3 = foot_width/3.1818
    spot_height_3 = spot_width_3*0.636
    spot_width_4 = foot_width/2.917
    spot_height_4 = spot_width_4*0.75
    spot_width_5 = foot_width/3.5
    spot_height_5 = spot_width_5*0.4
    spot_width_6 = foot_width/2.917
    spot_height_6 = spot_width_6*0.583
    ellipse(screen, WHITE, [(x + 33, y + 20), (foot_width, foot_heigth)])
    ellipse(screen, RED, [(x, y), (hat_width, hat_height)])
    ellipse(screen, LIGHT, [(x, y), (hat_width, hat_height)], 1)
    ellipse(screen, WHITE, [(x + 10, y + 12), (spot_width_1, spot_height_1)])
    ellipse(screen, LIGHT, [(x + 10, y + 12), (spot_width_1, spot_height_1)], 1)
    ellipse(screen, WHITE, [(x + 30, y + 8), (spot_width_2, spot_height_2)])
    ellipse(screen, LIGHT, [(x + 30, y + 8), (spot_width_2, spot_height_2)], 1)
    ellipse(screen, WHITE, [(x + 27, y + 20), (spot_width_3, spot_height_3)])
    ellipse(screen, LIGHT, [(x + 27, y + 20), (spot_width_3, spot_height_3)], 1)
    ellipse(screen, WHITE, [(x + 50, y + 14), (spot_width_4, spot_height_4)])
    ellipse(screen, LIGHT, [(x + 50, y + 14), (spot_width_4, spot_height_4)], 1)
    ellipse(screen, WHITE, [(x + 65, y + 7), (spot_width_5, spot_height_5)])
    ellipse(screen, LIGHT, [(x + 65, y + 7), (spot_width_5, spot_height_5)], 1)
    ellipse(screen, WHITE, [(x + 75, y + 21), (spot_width_6, spot_height_6)])
    ellipse(screen, LIGHT, [(x + 75, y + 21), (spot_width_6, spot_height_6)], 1)


def draw_mroom(x, y, multiplier):
    mroom_width = 55*multiplier
    mroom_height = mroom_width*0.917
    ellipse(screen, BROWN, [(x, y), (mroom_width, mroom_height)])
    ellipse(screen, LIGHT, [(x, y), (mroom_width, mroom_height)], 1)


def draw_apple(x, y, multiplier):
    apple_size = 65*multiplier
    ellipse(screen, RED, [(x, y), (apple_size, apple_size)])
    ellipse(screen, LIGHT, [(x, y), (apple_size, apple_size)], 1)


main()


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
