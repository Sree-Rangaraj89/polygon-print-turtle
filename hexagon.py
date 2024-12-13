import turtle
screen = turtle.Screen()
screen.bgcolor("beige")  

hexagon= turtle.Turtle()
hexagon.color("red")


for _ in range(6):
    hexagon.forward(100)
    hexagon.left(60)

turtle.done()
