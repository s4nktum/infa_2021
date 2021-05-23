import turtle as trt
trt.shape('turtle')
trt.left(90)
def circle(x,y):
    n = 360//x
    for i in range(0,n):
        trt.left(x)
        trt.forward(y)
    for i in range(0,n):
        trt.right(x)
        trt.forward(y)
y = 5
x = 6
for i in range(0,9):
    circle(x,y)
    x += 3
    
    
    
    
