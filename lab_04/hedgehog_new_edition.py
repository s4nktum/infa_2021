import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((102, 153, 102))

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

edging = LIGHT  # Цвет окантовки
spikes_color = SPIKE
spikes_edging = DARK


# Здесь мы будем рисовать
def main():
    draw_hedgehog(screen, 100, 100, 300, (71, 61, 61))


def draw_hedgehog(surface, x, y, width, color):
    """
    :param surface: объект pygame.surface
    :param x, y: коордианата левого верхнего угла изображения
    :param width, height: ширина и высота изображения
    :param color: цвет ежа
    """
    body_width = width*0.85
    body_height = body_width/2
    spike_size = -body_height * 0.95
    leg_size_1 = body_width/5.5
    leg_x_1 = x - leg_size_1/3.9
    leg_y_1 = y + body_height*2.2/3 - leg_size_1/4
    leg_size_2 = body_width/11
    leg_x_2 = x + body_width - leg_size_2/1.2
    leg_y_2 = y + 0.65*body_height
    draw_leg_1(surface, color, leg_x_1, leg_y_1, leg_size_1)
    draw_leg_2(surface, color, leg_x_2, leg_y_2, leg_size_2)

    draw_body(surface, color, x, y, body_width, body_height)

    leg_size_3 = body_width*0.15
    leg_x_3 = x + 0.07*body_width
    leg_y_3 = y + 0.78*body_height
    leg_size_4 = body_width*0.118
    leg_x_4 = x + body_width*0.8
    leg_y_4 = y + 0.8*body_height
    draw_leg_3(surface, color, leg_x_3, leg_y_3, leg_size_3)
    draw_leg_4(surface, color, leg_x_4, leg_y_4, leg_size_4)

    spike_left_x = x + body_width*0.72
    spike_left_y = y + body_height * 0.5
    draw_spikes_left(surface, spike_left_x, spike_left_y, spike_size)

    spike_right_x = x + body_width * 0.8
    spike_right_y = y + body_height * 0.5
    draw_spikes_right(surface, spike_right_x, spike_right_y, spike_size)
    spike_right_x = x + body_width * 0.85
    spike_right_y = y + body_height * 0.7
    draw_spikes_right(surface, spike_right_x, spike_right_y, spike_size)

    red_mroom_size = body_height*0.22
    red_mroom_x = x + body_width*0.38
    red_mroom_y = y - body_height*0.6
    draw_red_mroom(surface, red_mroom_x, red_mroom_y, red_mroom_size)

    mroom_size = 0.275*body_width
    mroom_x = x + 0.07*body_width
    mroom_y = y - 0.3*body_height
    draw_mroom(surface, mroom_x, mroom_y, mroom_size)

    apple_size = 0.310*body_width
    apple_x = x + 0.61*body_width
    apple_y = y - 0.302*body_height
    draw_apple(surface, apple_x, apple_y, apple_size)

    spike_left_x = x + body_width * 0.92
    spike_left_y = y + body_height * 0.4
    draw_spikes_left(surface, spike_left_x, spike_left_y, spike_size)

    spike_left_x = x + body_width * 0.81
    spike_left_y = y + body_height * 0.62
    draw_spikes_left(surface, spike_left_x, spike_left_y, spike_size)

    head_size = body_width * 0.318
    head_x = x + body_width - head_size/2
    head_y = y + body_height/2 - head_size/4
    draw_head(surface, color, head_x, head_y, head_size)

    spike_up_x = x + body_width*0.5
    spike_up_y = y + body_height*0.4
    draw_spikes_up(surface, spike_up_x, spike_up_y, spike_size)
    spike_up_x = x + body_width*0.7
    spike_up_y = y + body_height*0.5
    draw_spikes_up(surface, spike_up_x, spike_up_y, spike_size)
    spike_up_x = x + body_width*0.3
    spike_up_y = y + body_height*0.5
    draw_spikes_up(surface, spike_up_x, spike_up_y, spike_size)
    spike_up_x = x + body_width*0.45
    spike_up_y = y + body_height*0.8
    draw_spikes_up(surface, spike_up_x, spike_up_y, spike_size)
    spike_up_x = x + body_width*0.37
    spike_up_y = y + body_height*0.54
    draw_spikes_up(surface, spike_up_x, spike_up_y, spike_size)
    spike_up_x = x + body_width*0.6
    spike_up_y = y + body_height*0.5
    draw_spikes_up(surface, spike_up_x, spike_up_y, spike_size)


def draw_body(surface, color, x, y, body_width, body_height):
    ellipse(surface, color, [(x, y), (body_width, body_height)])
    ellipse(surface, edging, [(x, y), (body_width, body_height)], 1)
    print('Рисую тело')


def draw_head(surface, color, head_x, head_y, head_size):
    eye_1_x = head_x + head_size*0.45
    eye_1_y = head_y + head_size/1.75*0.42
    eye_2_x = head_x + head_size*0.65
    eye_2_y = head_y + head_size/1.75*0.2
    nose_x = head_x + head_size - head_size/15/2
    nose_y = head_y + head_size/4 + head_size/15/2/1.75
    ellipse(surface, color, [(head_x, head_y), (head_size, head_size/1.75)])
    ellipse(surface, edging, [(head_x, head_y), (head_size, head_size / 1.75)], 1)
    circle(screen, (0, 0, 0), (eye_1_x, eye_1_y), head_size/12)
    circle(screen, edging, (eye_1_x, eye_1_y), head_size/12, 1)
    circle(screen, (0, 0, 0), (eye_2_x, eye_2_y), head_size/12)
    circle(screen, edging, (eye_2_x, eye_2_y), head_size/12, 1)
    circle(screen, (0, 0, 0), (nose_x, nose_y), head_size/15)
    circle(screen, edging, (nose_x, nose_y), head_size/15, 1)
    print('Рисую голову')


def draw_leg_1(surface, color, leg_x, leg_y, leg_size):
    ellipse(surface, color, [(leg_x, leg_y), (leg_size, leg_size*0.375)])
    ellipse(surface, edging, [(leg_x, leg_y), (leg_size, leg_size*0.375)], 1)


def draw_leg_2(surface, color, leg_x, leg_y, leg_size):
    ellipse(surface, color, [(leg_x, leg_y), (leg_size, leg_size*0.9)])
    ellipse(surface, edging, [(leg_x, leg_y), (leg_size, leg_size*0.9)], 1)


def draw_leg_3(surface, color, leg_x, leg_y, leg_size):
    ellipse(surface, color, [(leg_x, leg_y), (leg_size, leg_size/1.83)])
    ellipse(surface, edging, [(leg_x, leg_y), (leg_size, leg_size/1.83)], 1)


def draw_leg_4(surface, color, leg_x, leg_y, leg_size):
    ellipse(surface, color, [(leg_x, leg_y), (leg_size, leg_size/1.52)])
    ellipse(surface, edging, [(leg_x, leg_y), (leg_size, leg_size/1.52)], 1)


def draw_spikes_up(surface, spike_x, spike_y, spike_size):
    base = spike_size / 6.5
    polygon(surface, spikes_color, [(spike_x, spike_y), (spike_x + base, spike_y), (spike_x + base/2,
                                                                                    spike_y + spike_size)])
    polygon(surface, spikes_edging, [(spike_x, spike_y), (spike_x + base, spike_y), (spike_x + base / 2,
                                                                                     spike_y + spike_size)], 1)


def draw_spikes_left(surface, spike_x, spike_y, spike_size):
    base = spike_size / 6.5
    y = spike_y
    for i in range(1, 4):
        for i in range(1, 4):
            polygon(surface, spikes_color, [(spike_x, spike_y),
                                            (spike_x + base*3**0.5/2, spike_y - base/2),
                                            (spike_x + spike_size/2, spike_y + spike_size*3**0.5/2)])
            polygon(surface, spikes_edging, [(spike_x, spike_y),
                                             (spike_x + base * 3 ** 0.5 / 2, spike_y - base / 2),
                                             (spike_x + spike_size / 2, spike_y + spike_size * 3 ** 0.5 / 2)], 1)
            spike_x += base*3**0.5/2
            spike_y -= base/2
            x = spike_x
        spike_y = y
        spike_x = x/1.03


def draw_spikes_right(surface, spike_x, spike_y, spike_size):
    base = spike_size / 6.5
    y = spike_y
    for i in range(1, 4):
        for i in range(1, 4):
            polygon(surface, spikes_color, [(spike_x, spike_y),
                                            (spike_x - base*3**0.5/2, spike_y - base/2),
                                            (spike_x - spike_size/2, spike_y + spike_size*3**0.5/2)])
            polygon(surface, spikes_edging, [(spike_x, spike_y),
                                             (spike_x - base * 3 ** 0.5 / 2, spike_y - base / 2),
                                             (spike_x - spike_size / 2, spike_y + spike_size * 3 ** 0.5 / 2)], 1)
            spike_x += base*1.02

            x = spike_x
        spike_y = y
        spike_x = x/1.03


def draw_red_mroom(surface, red_mroom_x, red_mroom_y, red_mroom_size):
    foot_height = red_mroom_size/0.4
    hat_width = red_mroom_size/0.35
    hat_height = hat_width*0.4
    spot_width_1 = red_mroom_size/3.5
    spot_height_1 = spot_width_1*0.7
    spot_width_2 = red_mroom_size/3.888
    spot_height_2 = spot_width_2/2.25
    spot_width_3 = red_mroom_size/3.1818
    spot_height_3 = spot_width_3*0.636
    spot_width_4 = red_mroom_size/2.917
    spot_height_4 = spot_width_4*0.75
    spot_width_5 = red_mroom_size/3.5
    spot_height_5 = spot_width_5*0.4
    spot_width_6 = red_mroom_size/2.917
    spot_height_6 = spot_width_6*0.583
    ellipse(surface, WHITE, [(red_mroom_x + hat_width/2 - red_mroom_size/2, red_mroom_y + hat_height*0.40),
                             (red_mroom_size, foot_height)])
    ellipse(surface, RED, [(red_mroom_x, red_mroom_y), (hat_width, hat_height)])
    ellipse(surface, LIGHT, [(red_mroom_x, red_mroom_y), (hat_width, hat_height)], 1)
    ellipse(surface, WHITE,
            [(red_mroom_x + hat_width*0.23,  red_mroom_y + hat_height*0.1), (spot_width_1, spot_height_1)])
    ellipse(surface, LIGHT,
            [(red_mroom_x + hat_width*0.23,  red_mroom_y + hat_height*0.1),(spot_width_1, spot_height_1)], 1)
    ellipse(surface, WHITE,
            [(red_mroom_x + hat_width*0.15, red_mroom_y + hat_height*0.55), (spot_width_2, spot_height_2)])
    ellipse(surface, LIGHT,
            [(red_mroom_x + hat_width*0.15, red_mroom_y + hat_height*0.55),(spot_width_2, spot_height_2)], 1)
    ellipse(surface, WHITE,
            [(red_mroom_x + hat_width*0.8, red_mroom_y + hat_height*0.5),(spot_width_3, spot_height_3)])
    ellipse(surface, LIGHT,
            [(red_mroom_x + hat_width*0.8, red_mroom_y + hat_height*0.5),(spot_width_3, spot_height_3)], 1)
    ellipse(surface, WHITE,
            [(red_mroom_x + hat_width*0.35, red_mroom_y + hat_height*0.35), (spot_width_4, spot_height_4)])
    ellipse(surface, LIGHT,
            [(red_mroom_x + hat_width*0.35, red_mroom_y + hat_height*0.35),  (spot_width_4, spot_height_4)], 1)
    ellipse(surface, WHITE,
            [(red_mroom_x + hat_width*0.55, red_mroom_y + hat_height*0.2),  (spot_width_5, spot_height_5)])
    ellipse(surface, LIGHT,
            [(red_mroom_x + hat_width*0.55, red_mroom_y + hat_height*0.2), (spot_width_5, spot_height_5)], 1)
    ellipse(surface, WHITE,
            [(red_mroom_x + hat_width*0.5,  red_mroom_y + hat_height*0.5), (spot_width_6, spot_height_6)])
    ellipse(surface, LIGHT,
            [(red_mroom_x + hat_width*0.5,  red_mroom_y + hat_height*0.5),   (spot_width_6, spot_height_6)], 1)


def draw_mroom(surface, mroom_x, mroom_y, mroom_size):
    mroom_height = mroom_size*0.917
    ellipse(surface, BROWN, [(mroom_x, mroom_y), (mroom_size, mroom_height)])
    ellipse(surface, LIGHT, [(mroom_x, mroom_y), (mroom_size, mroom_height)], 1)
    ellipse(surface, BROWN, [(mroom_x + mroom_size/2, mroom_y + mroom_height/3), (mroom_size, mroom_height)])
    ellipse(surface, LIGHT, [(mroom_x + mroom_size/2, mroom_y + mroom_height/3), (mroom_size, mroom_height)], 1)


def draw_apple(surface, apple_x, apple_y, apple_size ):
    ellipse(surface, RED, [(apple_x, apple_y), (apple_size, apple_size)])
    ellipse(surface, LIGHT, [(apple_x, apple_y), (apple_size, apple_size)], 1)


main()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()