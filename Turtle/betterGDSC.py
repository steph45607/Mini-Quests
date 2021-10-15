import turtle

def outcurve(num):
    for i in range(num):
        wrp.right(1)
        wrp.forward(2)

def incurve(num):
    for i in range(num):
        wrp.left(1)
        wrp.forward(1.2)

wrp = turtle.Turtle()
wrp.speed(100)
wrp.color("blue")

wrp.begin_fill()
wrp.setheading(270)
outcurve(320)
wrp.right(90)
wrp.forward(50)
wrp.right(90)
incurve(300)
wrp.setheading(180)
wrp.forward(40)
wrp.right(90)
wrp.forward(40)
wrp.right(90)
wrp.forward(92)
wrp.right(90)
outcurve(7)
wrp.end_fill()



turtle.done()