import turtle

def curve(num):
    for i in range(num):
        wrp.left(1)
        wrp.forward(0.4)

wrp = turtle.Turtle()
wrp.speed(1000)
wrp.hideturtle()

#set mid position
wrp.penup()
wrp.setposition(-280,0)
wrp.pendown()

#set red part
wrp.color("#DB4437")
wrp.begin_fill()
wrp.setheading(0)
wrp.left(15)
wrp.forward(40)
curve(180)
wrp.forward(80)
curve(45)
wrp.end_fill()

#set blue part
wrp.color("#4285F4")
wrp.begin_fill()
curve(80)
wrp.forward(80)
curve(180)
wrp.forward(80)
curve(90)
wrp.end_fill()

#set to initial position
wrp.penup()
wrp.setposition(-280,0)
wrp.left(115)
wrp.forward(150)
wrp.pendown()

#make the >
#make yellow part
wrp.color("#F4B400")
wrp.begin_fill()
wrp.right(150)
wrp.forward(40)
curve(180)
wrp.forward(80)
curve(45)
wrp.end_fill()

#green part
wrp.color("#0F9D54")
wrp.begin_fill()
curve(80)
wrp.forward(80)
curve(180)
wrp.forward(80)
curve(90)
wrp.end_fill()

# wrp.hideturtle()

turtle.done()