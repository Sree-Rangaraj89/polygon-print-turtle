import turtle

screen = turtle.Screen()
screen.bgcolor("beige") 

triangle = turtle.Turtle()
triangle.color("red") 

for _ in range(3):
    triangle.forward(100)  
    triangle.left(120) 

square = turtle.Turtle()
square.color("green")

for _ in range(4):
    square.forward(100)
    square.left(90)
turtle.done()