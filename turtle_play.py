import turtle
from turtle import Turtle, Screen
from random import randint

my_turtle = Turtle()
my_turtle.shape("turtle")
# my_turtle.color("green")
turtle.colormode(255)


# for i in range(10):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()
#     # my_turtle.right(90)


# def produce(user_from, user_to):
#     for sides in range(user_from, user_to + 1):
#         angle = 360/sides
#         my_turtle.color(choice(color))
#         for _ in range(sides):
#             my_turtle.forward(100)
#             my_turtle.right(angle)
#
#
# def user_input():
#     sides_from = int(input("Enter the side that should start from:: "))
#     sides_to = int(input("Enter the side that should end to:: "))
#     produce(sides_from, sides_to)


# user_input()

# angle = [90, 0, 180, 270]
# my_turtle.pensize(10)
# my_turtle.speed("fastest")


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


# def perform():
#     i = 0
#     while i < 100:
#         my_turtle.color(random_color())
#         my_turtle.forward(50)
#         my_turtle.right(choice(angle))
#         i += 1

my_turtle.pensize(1)
my_turtle.speed("fastest")


def draw_spirograph(size_gap):
    for _ in range(int(360/size_gap)):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + size_gap)


draw_spirograph(5)

my_screen = Screen()
my_screen.exitonclick()
