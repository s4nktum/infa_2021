import turtle as trt
trt.shape('turtle')

p = 0.1
f = 15
for i in range(1,1000):
    trt.forward(p)
    trt.left(f)
    p += 0.1