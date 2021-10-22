import turtle

fans = turtle.Turtle()
fans.speed(10)

fans.color("blue")
fans.begin_fill()
for i in range(361):
    fans.right(1)
    fans.forward(1)
fans.end_fill()

turtle.done()