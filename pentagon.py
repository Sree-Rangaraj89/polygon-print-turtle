import turtle
screen = turtle.Screen()
screen.bgcolor("beige")  

pentagon = turtle.Turtle()
pentagon.color("red")


for _ in range(5):
    pentagon.forward(100)
    pentagon.left(72)

turtle.done()
