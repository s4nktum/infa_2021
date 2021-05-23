import turtle as trt
import numpy as np
trt.shape('turtle')
n = 3
x = 50
def angle(n, x):
    a = 360 / n
    for i in range(1,n+1):
        trt.left(a)
        trt.forward(x)
    trt.penup()
    trt.right(a/2)
    trt.forward(200**0.5)
    trt.left(a/2 + 5)
    trt.pendown()
    
for i in range(1,11):
    angle(n,x)
    n += 1
    x += 10
    