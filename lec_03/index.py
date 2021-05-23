import turtle as trt

trt.shape('turtle')
trt.color('blue')
trt.left(90)
trt.pensize(5)
A = 1, 4, 1, 7, 0, 0


def draw_1():
    trt.penup()
    trt.backward(50)
    trt.pendown()
    trt.right(45)
    trt.forward(5000 ** 0.5)
    trt.left(45)
    trt.backward(100)
    trt.forward(100)
    trt.penup()
    trt.right(90)
    trt.forward(40)
    trt.left(90)
    trt.pendown()


def draw_4():
    trt.backward(50)
    trt.right(90)
    trt.forward(45)
    trt.right(90)
    trt.forward(50)
    trt.right(180)
    trt.forward(100)
    trt.penup()
    trt.right(90)
    trt.forward(40)
    trt.left(90)
    trt.pendown()


def draw_7():
    trt.right(90)
    trt.forward(50)
    trt.right(135)
    trt.forward(5000 ** 0.5)
    trt.left(45)
    trt.forward(50)
    trt.penup()
    trt.right(180)
    trt.forward(100)
    trt.right(90)
    trt.forward(90)
    trt.left(90)
    trt.pendown()


def draw_0():
    trt.right(90)
    trt.forward(50)
    trt.right(90)
    trt.forward(100)
    trt.right(90)
    trt.forward(50)
    trt.right(90)
    trt.forward(100)
    trt.penup()
    trt.right(90)
    trt.forward(90)
    trt.left(90)
    trt.pendown()


for elem in A:
    if elem == 1:
        draw_1()
    elif elem == 4:
        draw_4()
    elif elem == 7:
        draw_7()
    else:
        draw_0()
trt.done()
