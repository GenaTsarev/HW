import turtle
turtle.shape('turtle')
turtle.shapesize(1)
turtle.color('red')


def square_trtl(x):
    for i in range(4):
        turtle.forward(x)
        turtle.left(90)

square_trtl(85)


