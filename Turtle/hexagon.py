import turtle

fans = turtle.Turtle()
fans.speed(10)

fans.color("blue")
fans.begin_fill()
for i in range(5):
    fans.forward(100)
    fans.left(60)
fans.end_fill()

turtle.done()