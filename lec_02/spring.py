import turtle as trt
trt.shape('turtle')
trt.left(90)
trt.speed(10)
x = 1

while x <= 6:
    trt.circle(50,180,100)
    trt.circle(10,180,100)
    x += 1
trt.exitonclick()
