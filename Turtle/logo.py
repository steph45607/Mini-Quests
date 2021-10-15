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
wrp.speed(0)

#set mid position
wrp.penup()
wrp.setposition(-280,0)
wrp.pendown()

wrp.color("#DB4437")
wrp.begin_fill()
wrp.setheading(0)
wrp.left(15)
wrp.forward(40)
curvel(180)
wrp.forward(80)
curvel(45)
wrp.end_fill()

# wrp.penup()
# wrp.setposition(-280,0)
# wrp.pendown()
wrp.color("#4285F4")
wrp.begin_fill()
curvel(80)
wrp.forward(80)
curvel(180)
wrp.forward(80)
curvel(90)


# wrp.setheading(180)
# wrp.right(15)
# #start middle bottom pill
# wrp.right(15)
# wrp.forward(40)
# curvel(180)
# wrp.forward(80)
# curvel(180)
# wrp.forward(40)
wrp.end_fill()
# curve(360)
# wrp.forward(40)

# wrp.setheading(180)
# wrp.right(15)
# wrp.forward(40)
# curvel(180)
# wrp.forward(80)
# curve(90)


turtle.done()