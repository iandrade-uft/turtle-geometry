from turtle import *


space = Screen()
turtle = Turtle()
n = 20
ang = 360/n
turtle.penup()
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.pendown()
for sides in range(n):
    turtle.forward(50)
    turtle.right(ang)

done()

