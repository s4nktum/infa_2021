import turtle

turtle.shape('turtle')
n = 10
for i in range(1,10):
    turtle.forward(n)
    turtle.right(90)
    turtle.forward(n)
    turtle.right(90)
    turtle.forward(n)
    turtle.right(90)
    turtle.forward(n)
    turtle.penup()
    turtle.left(45)
    turtle.forward(200**0.5)
    turtle.pendown()
    turtle.right(45+90)
    n +=20
