import turtle

fans = turtle.Turtle()
fans.speed(10)

fans.color("orange")
fans.begin_fill()
for i in range(3):
    fans.forward(100)
    fans.left(120)
fans.end_fill()

turtle.done()