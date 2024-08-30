from turtle import *

space = Screen()
space.bgcolor("black")

width = 480  # Largura
height = 720  # Altura (360 * 16/9 para manter a proporção)

# Ajusta o tamanho da tela
space.setup(width=width, height=height)

turtle = Turtle()
turtle.penup()
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.pendown()

colors = ["red", "blue", "green", "orange"]

R = 20

for repeats in range(R):
    turtle.forward(10)
    turtle.right(360/R)
    color = colors[repeats % len(colors)]
    turtle.color(color)

    for sides in range(5):
        turtle.forward(100)
        turtle.right(72)


done()