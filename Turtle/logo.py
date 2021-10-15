import turtle

def curve(num):
    for i in range(num):
        wrp.right(1)
        wrp.forward(0.4)
def curvel(num):
    for i in range(num):
        wrp.left(1)
        wrp.forward(0.4)

wrp = turtle.Turtle()
wrp.speed(100)

wrp.penup()
wrp.setposition(-280,0)
wrp.pendown()

wrp.right(15)
wrp.forward(40)
curve(180)
wrp.forward(80)
curve(120)
wrp.forward(80)
curve(180)
wrp.forward(40)

wrp.setheading(180)
wrp.right(15)
wrp.forward(40)
curvel(100)


turtle.done()