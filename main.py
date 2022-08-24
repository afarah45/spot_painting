import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_list = (r, g, b)
    return color_list


size_dif = -200

draw = Turtle()
draw.shape("arrow")
draw.penup()
draw.goto(-300, size_dif)
draw.speed(0)
draw.hideturtle()
# for aa in range(20):
#     size_dif += 25
#     for _ in range(20):
#         draw.penup()
#         draw.dot(15, random_color())
#         draw.fd(30)
#     draw.goto(-300, size_dif)

for aa in range(20):
    size_dif += 15
    for _ in range(20):
        draw.penup()
        draw.dot(10, random_color())
        draw.fd(20)
    draw.goto(-300, size_dif)
screen = Screen()
screen.exitonclick()
