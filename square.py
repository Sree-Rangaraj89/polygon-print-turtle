import turtle
screen = turtle.Screen()
screen.bgcolor("beige")  

square = turtle.Turtle()
square.color("red")


for _ in range(4):
    square.forward(100)
    square.left(90)

turtle.done()
