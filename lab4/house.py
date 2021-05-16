import pygame
from pygame import *

pygame.init()


def draw_house(x, y, width, height):
    """
    Нарисовать домик ширины width и высоты height от опорной точки (x, y), которая нахоится
    в середине нижней точки фундамента.
    :param x: координата x середины домика
    :param y: координата y низа фундамента
    :param width: полная ширина домика (фундамент или вылеты крыши включены)
    :param height: полная высота домика
    :return: None
    """
    print(x, y, width, height)
    pass


x, y = 300, 200
width, height = 200, 300


draw_house(x, y, width, height)

