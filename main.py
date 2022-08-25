# Hirst painting

# import colorgram
#
# colors = colorgram.extract("hirst02b.jpg", 10)
#
# rgb_color = []
#
# for color in range(len(colors)):
#     each_color = colors[color].rgb
#     r, g, b = each_color.r, each_color.g, each_color.b
#     rgb_color.append((r, g, b))
#
# print(rgb_color)
import turtle
from turtle import Turtle, Screen
from random import choice

turtle.colormode(255)

color_list = [(240, 240, 244), (237, 233, 227), (238, 231, 236), (232, 239, 235), (26, 39, 60), (146, 80, 50),
              (52, 26, 33), (139, 160, 189), (24, 96, 159), (206, 145, 96)]

my_turtle = Turtle()
my_screen = Screen()
my_turtle.hideturtle()
my_turtle.speed("fastest")


def set_position_turtle():
    my_turtle.penup()
    width, height = my_screen.window_width()/2, my_screen.window_height()/2
    my_turtle.setpos(60/2 - width, 60/2 - height)
    my_turtle.pendown()


def draw_dot():
    for _ in range(10):
        my_turtle.pendown()
        my_turtle.dot(30, choice(color_list))
        my_turtle.penup()
        my_turtle.forward(100)


def move_to_top():
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(1000)
    my_turtle.setheading(0)


set_position_turtle()
for _ in range(9):
    draw_dot()
    move_to_top()

my_screen.exitonclick()
