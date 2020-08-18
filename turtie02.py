import turtle


i=1
A=turtle.Turtle()

screen = turtle.Screen()
screen.title('泡菜頭')
screen.bgcolor('lightblue')

A.pensize(5)

while i<361:
    A.forward(1)
    A.left(1)
    i=i+1
