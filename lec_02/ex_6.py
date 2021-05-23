import turtle as trt

trt.shape('turtle')
x = 30
for i in range(0,12):
    trt.forward(100)
    trt.stamp()
    trt.right(180)
    trt.forward(100)
    trt.right(180+x)