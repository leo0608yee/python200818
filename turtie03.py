import turtle


i=1
A=turtle.Turtle()
B=turtle.Turtle()

screen = turtle.Screen()
screen.title('泡菜頭')
screen.bgcolor('lightblue')

A.pensize(5)
B.pensize(10)

for i in range(0,361):
    A.forward(1)
    A.left(1)
    
for i in range(0,361):
    B.forward(1)
    B.right(1)
    
