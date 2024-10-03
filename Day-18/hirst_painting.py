from turtle import Turtle, Screen
import random
import colorgram


"""Extracts colours from the original Hirst painting"""
colours = colorgram.extract("download.jpeg", 30)
colours_tuples = []

for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    new_colour = (r, g, b)
    colours_tuples.append(new_colour)

colour_list = [(247, 231, 237), (206, 166, 127), (231, 237, 241), (232, 246, 235), (163, 168, 36),
               (243, 79, 54), (145, 51, 103), (236, 67, 129), (9, 145, 65), (240, 219, 75), (235, 110, 163),
               (4, 142, 183), (70, 199, 222), (161, 57, 50), (24, 170, 130), (250, 232, 0), (120, 37, 90),
               (29, 190, 209), (119, 195, 164), (240, 162, 188), (229, 173, 163), (153, 212, 191), (1, 118, 26),
               (136, 39, 35), (87, 28, 81), (132, 216, 229), (163, 194, 222)]


screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.pencolor(255, 0, 0)
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)


def hirst(number_of_dots):
    """Recreates a Hirst painting with 10*10 dots"""
    for i in range(1, number_of_dots+1):
        timmy.dot(20, random.choice(colour_list))
        timmy.forward(50)
        if i %10 ==0:
            timmy.setheading(90)
            timmy.forward(50)
            timmy.setheading(180)
            timmy.forward(500)
            timmy.setheading(0)

hirst(100)


screen.exitonclick()





