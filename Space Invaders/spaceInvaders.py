import turtle
import os

#screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
#make the square border
for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)
border_pen.hideturtle() #hide the arrow thingy

#player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

#move player use arrow keys
playerspeed = 15 #how far the player move
def left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

#keyboard bindings
turtle.listen()
turtle.onkey(left,"Left") #assign "Left" key to do function left()
turtle.onkey(right,"Right") #assign "Right" key to do function right()




delay = input("Press enter to finsih")