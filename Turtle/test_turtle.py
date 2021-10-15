import turtle
import math

def curveo() :
    for i in range(60):
  
        man.right(3)
        man.forward(5)
def curvei() :
    for i in range(45):
  
        man.right(-4)
        man.forward(3)

def curvesi() :
    for i in range(55):
  
        man.right(4)
        man.forward(3)
def curveso() :
    for i in range(70):
  
        man.right(-3)
        man.forward(5)

def curved() :
    for i in range(30):
  
        man.right(3)
        man.forward(5)
def curvedi() :
    for i in range(21):
  
        man.right(-4)
        man.forward(3)


man = turtle.Turtle()
woop = turtle.Screen()
woop.bgcolor("#100C08")
man.speed(700)
man.penup()
man.goto(-270,0)
man.pendown()
def g():
    man.color("#4285F4", "#4285F4")
    man.begin_fill()
    man.left(180)
    man.forward(50)
    man.right(90)
    man.forward(50)
    man.right(90)
    man.forward(100)
    man.right(90)
    man.forward(100)
    curveo()
    man.forward(160)
    curveo()
    man.right(90)
    man.forward(50)
    man.right(90)
    curvei()
    man.forward(160)
    curvei()
    man.forward(100)
    man.end_fill()
def d():
    man.penup()
    man.right(90)
    man.forward(80)
    man.pendown()
    man.color("#DB4437", "#DB4437")

    man.begin_fill()
    man.left(90)
    man.forward(158)
    man.right(90)
    man.forward(50)
    curved()
    man.forward(160)
    curved()
    man.forward(45)
    man.right(90)
    man.forward(193)
    man.right(90)
    man.forward(50)
    man.right(90)
    man.forward(143)
    man.left(90)
    curvedi()
    man.setheading(90)
    man.forward(159)
    curvedi()
    man.forward(1)
    man.setheading(270)
    man.forward(97)
    man.end_fill()

def s():
    man.color("#F4B400", "#F4B400")
    man.penup()
    man.left(90)
    man.forward(230)
    man.pendown()

    man.begin_fill()
    man.setheading(135)
    man.forward(50)
    curvesi()
    man.setheading(0)
    man.forward(50)
    man.left(90)
    curveso()
    man.setheading(315)
    man.forward(160)
    curvesi()
    man.setheading(180)
    man.forward(50)
    man.left(90)
    curveso()
    man.setheading(135)
    man.forward(100)
    man.end_fill()

def c():
    man.color("#0F9D54", "#0F9D54")
    man.penup()
    man.setheading(0)
    man.forward(110)
    man.pendown()

    man.begin_fill()
    man.setheading(90)
    man.forward(80)
    curveo()
    man.setheading(180)
    man.forward(50)
    man.right(90)
    curvei()
    man.forward(160)
    curvei()
    man.setheading(0)
    man.forward(50)
    man.setheading(270)
    curveo()
    man.forward(100)
    man.end_fill()   

g()
d()
s()
c()

turtle.done()