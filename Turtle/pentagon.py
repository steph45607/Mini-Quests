import turtle

fans = turtle.Turtle()
fans.speed(10)

fans.color("blue")
fans.begin_fill()
for i in range(4):
    fans.forward(100)
    fans.left(73)
fans.end_fill()

turtle.done()