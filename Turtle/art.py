import turtle
import math

def curve():
    for i in range(120):
  
        bob.right(3)
        bob.forward(5)

bob = turtle.Turtle()
mark = turtle.Screen()
bob.speed(1000)

mark.bgcolor("black")
bob.color("green")

ang = 3
while True:
    curve()
    bob.right(ang)
    ang += 3
    if ang == 360:
        break

turtle.done()