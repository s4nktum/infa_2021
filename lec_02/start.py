import turtle as trt
trt.shape('turtle')
trt.left(180)
def star(n):
    a = 720/n
    for i in range(0,n):
        trt.forward(150)
        trt.left(a)
star(5)