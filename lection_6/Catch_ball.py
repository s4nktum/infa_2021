import pygame
from pygame.draw import *
from random import randint
pygame.init()
screen = pygame.display.set_mode((1200, 900))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
score = 0  # Начальное количество очков


# Константы рисования и движения круга
x = randint(200, 1100)
y = randint(100, 800)
r = randint(20, 50)
color = COLORS[randint(0, 5)]
v = 7  # максимальная скорость шара
v_min = 3  # минимальная скорость шара
dx = randint(-v, v)
dy = randint(-v, v)

# Константы рисования и движения прямоугольника
x_r = randint(200, 1100)
y_r = randint(100, 800)
w_r = randint(70, 120)
color_r = COLORS[randint(0, 5)]
v_r = 7  # максимальная скорость шара
v_min_r = 3  # минимальная скорость шара
dx_r = randint(-v, v)
dy_r = randint(-v, v)


def new_ball():
    """
     Функция случайного создания шариков в точке x, y, радиусом r
     и цветом color
    """
    global x, y, r, dx, dy, color, v, v_min

    circle(screen, color, (x + dx, y + dy), r)
    circle(screen, (255, 255, 255), (x + dx, y + dy), r, 3)
    # Далее идут условия для отражения от границ экрана
    if x >= 1200 - 3/2 * r:
        dx = randint(v_min, v)*-1
        dy = randint(-v, v)
    elif y >= 900 - 3/2 * r:
        dx = randint(-v, v)
        dy = randint(v_min, v)*-1
    elif x <= 0 + 3/2 * r:
        dx = randint(v_min, v)
        dy = randint(-v, v)
    elif y <= 0 + 3/2*r:
        dx = randint(-v, v)
        dy = randint(v_min, v)
    # Скорость перемещения по осям
    x += dx
    y += dy


def new_rect():
    """
    Функция случайного создания прямоугольника аналагична new_ball()
    """
    global x_r, y_r, dx_r, dy_r, v_r, v_min_r, w_r

    rect(screen, color_r, ((x_r, y_r), (w_r, w_r)))
    rect(screen, (255, 255, 255), ((x_r, y_r), (w_r, w_r)), 3)
    # Далее идут условия для отражения от границ экрана
    if x_r >= 1200 - w_r:
        dx_r = randint(v_min_r, v_r) * -1
        dy_r = randint(-v_r, v_r)
    elif y_r >= 900 - w_r:
        dx_r = randint(-v_r, v_r)
        dy_r = randint(v_min_r, v_r) * -1
    elif x_r <= 0:
        dx_r = randint(v_min_r, v_r)
        dy_r = randint(-v_r, v_r)
    elif y_r <= 0:
        dx_r = randint(-v_r, v_r)
        dy_r = randint(v_min_r, v_r)
    # Скорость перемещения по осям
    x_r += dx_r
    y_r += dy_r


def click():
    """
    Подсчет попаданий по кругу в точке x, y
    в зависимости от клика в точке event.x, event.y
    hit - расстояние между (x,y) и event.pos
    """
    global score, x, y, r, color, dx, dy, x_r, y_r, w_r, color_r, dx_r, dy_r
    event.x = event.pos[0]
    event.y = event.pos[1]
    hit = ((event.x - x)**2 + (event.y - y)**2)*0.05
    # цикл подсчета очков, за попадание +10 за круг или +7 за прямоугольник, за промах -5
    # и генератор новой фигуры, по которой попали
    if hit <= r:
        score += 10
        screen.fill(BLACK)
        x = randint(200, 1100)
        y = randint(100, 800)
        r = randint(20, 50)
        color = COLORS[randint(0, 5)]
        dx = randint(-v, v)
        dy = randint(-v, v)
    elif x_r <= event.x <= x_r + w_r and y_r <= event.y <= y_r + w_r * 2 / 3:
        score += 7
        screen.fill(BLACK)
        x_r = randint(200, 1100)
        y_r = randint(100, 800)
        w_r = randint(70, 120)
        color_r = COLORS[randint(0, 5)]
        dx_r = randint(-v_r, v_r)
        dy_r = randint(-v_r, v_r)
    elif hit >= r:
        score += -5


pygame.display.update()
clock = pygame.time.Clock()
finished = False
FPS = 60

while not finished:
    clock.tick(FPS)  # Количество обновлений экрана в секунду
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.K_ESCAPE:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click()
            screen.fill(BLACK)
    new_ball()
    new_rect()
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()

# Вывод количества попаданий и запрос никнейма
name = input('Say your name, player: ')
print("Well done, ", name, ". Your score: ", score)
scoreboard = open('C:\infa_2021\lection_6\Scoreboard', 'a')
name_score = str(name) + ': ' + str(score)
scoreboard.write(name_score + '\n')
scoreboard.close()
