import turtle as trt

trt.shape('turtle')
trt.screensize(1800, 1600)
x = 0
y = 0
Vx = 20
Vy = 80
dt = 0.05
ay = -9.81
x1 = 0

def trtfall(y, Vx, Vy, dt, ay):
    global x
    while y >= 0:
        trt.goto(x, y)
        x += Vx * dt
        y += Vy * dt + ay * dt * 2 / 2
        Vy += ay * dt


for i in range(1, 7):
    trtfall(y, Vx, Vy, dt, ay)
    Vx *= 0.8
    Vy *= 0.8


trt.done()
