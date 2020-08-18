import turtle

A=turtle.Turtle()

screen = turtle.Screen()
screen.title('泡菜頭')
screen.bgcolor('lightblue')

A.pensize(5)

n =int(input("請問有幾個邊"))

D=360/n

for i in range(0,n):
    A.forward(30)
    A.left(D)
