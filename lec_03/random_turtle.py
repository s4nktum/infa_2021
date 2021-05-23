import turtle as trt
from random import randint
trt.shape('turtle')
trt.color('red')
x = 1
while x < 2:
    d = randint(-10, 10)
    y = randint(-360, 360)
    trt.forward(d)
    if randint(1, 3) > 2:
        trt.right(y)
    else:
        trt.left(y)
trt.done()
