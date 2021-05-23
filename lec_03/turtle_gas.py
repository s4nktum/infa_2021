from random import randint
import turtle

number_of_turtles = 40
steps_of_time_number = 100


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(randint(0, 10))
    unit.setpos(randint(-400, 400), randint(-400,400))
    unit.goto(randint(-400,400), randint(-400,400))


for i in range(steps_of_time_number):
    for unit in pool:
        if randint(1, 3) >= 2:
            unit.left(randint(-360, 360))
            unit.forward(randint(-30, 30))
        else:
            unit.right(randint(-360, 360))
            unit.forward(randint(-30, 30))