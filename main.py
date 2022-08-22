import colorgram
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

# Extract 6 colors from an image.
# colors = colorgram.extract('mynewimage.jpeg', 80)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list = [(207, 160, 82), (54, 89, 130), (145, 91, 40), (140, 27, 49), (222, 206, 109), (132, 177, 203),
              (45, 55, 104),
              (158, 46, 83), (169, 160, 39), (129, 189, 143), (83, 20, 44), (38, 43, 67), (186, 94, 107),
              (186, 140, 170),
              (85, 120, 180), (59, 39, 31), (88, 157, 92), (79, 153, 165), (195, 79, 72), (161, 201, 219), (45, 74, 77),
              (79, 74, 44),
              (58, 125, 121), (218, 176, 187), (167, 206, 168), (220, 182, 168), (179, 188, 211), (149, 37, 35),
              (48, 73, 72), (44, 62, 61)]


def random_color(color_list):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_list = (r, g, b)
    return color_list


draw = Turtle()
draw.shape("arrow")
draw.penup()
draw.goto(-300, -200)

for _ in range(20):
    draw.penup()
    draw.dot(20, random_color(color_list))
    draw.fd(30)
draw.goto(-300, -150)
for _ in range(20):

    draw.penup()
    draw.dot(20, random_color(color_list))
    draw.fd(30)
draw.goto(-300, -100)
for _ in range(20):
    # draw.color(random.choice(color_list))
    draw.penup()
    draw.dot(20, random_color(color_list))
    draw.fd(30)
draw.goto(-300, -50)
for _ in range(20):
    # draw.color(random.choice(color_list))
    draw.penup()
    draw.dot(20, random_color(color_list))
    draw.fd(30)
draw.goto(-300, 0)
for _ in range(20):
    # draw.color(random.choice(color_list))
    draw.penup()
    draw.dot(20, random_color(color_list))
    draw.fd(30)
draw.goto(-300, 50)
for _ in range(20):
    # draw.color(random.choice(color_list))
    draw.penup()
    draw.dot(20, random_color(color_list))
    draw.fd(30)
draw.goto(-300, 100)
for _ in range(20):
    # draw.color(random.choice(color_list))
    draw.penup()
    draw.dot(20, random_color(color_list))
    draw.fd(30)
draw.goto(-300, 150)
for _ in range(20):
    # draw.color(random.choice(color_list))
    draw.penup()
    draw.dot(20, random_color(color_list))
    draw.fd(30)
draw.goto(-300, 200)
for _ in range(20):
    # draw.color(random.choice(color_list))
    draw.penup()
    draw.dot(20, random_color(color_list))
    draw.fd(30)
draw.goto(-300, 250)

screen = Screen()
screen.exitonclick()
