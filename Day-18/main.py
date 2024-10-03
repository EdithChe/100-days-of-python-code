import turtle
from turtle import Turtle, Screen
import random



timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
# timmy.pensize(10)
turtle.colormode(255)


"""Draw dashed line"""
for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

colours = ["blue", "pink", "brown", "green", "magenta", "purple", "DeepSkyBlue", "DarkOrchid", "yellow", "aquamarine", "gold"]
actions = [0, 90, 180, 270]



def random_colour():
    """Returns a random colour"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color



def draw_spirograph(gap_size):
    """Draws a spirograph using random colours"""
    for _ in range(int(360/ gap_size)):
        timmy.color(random_colour())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_size)
        timmy.speed("fastest")


draw_spirograph(5)

"""Creates random walk"""
for _ in range(200):

    timmy.forward(30)
    timmy.setheading(random.choice(actions))
    timmy.color(random_colour())
    timmy.speed("fast")


def draw_shape(num_sides):
    """Draw different shapes: from triangle to decagon"""
    angle = 360/ num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3, 11):
    timmy.color(random.choice(colours))
    draw_shape(shape_side_n)



screen = Screen()
screen.exitonclick()