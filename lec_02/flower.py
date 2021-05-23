import turtle as trt
trt.shape('turtle')
def circle():
    for i in range(1, 37):
        trt.forward(10)
        trt.left(10)
    trt.right(30)
    for i in range(1, 37):
        trt.forward(10)
        trt.right(10)
    trt.right(30)
for i in range(1,4):
    circle()