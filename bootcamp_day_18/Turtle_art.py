import turtle
import turtle as t
import random


timmy = t.Turtle()
t.colormode(255)
timmy.shape('turtle')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuble = (r, g, b)
    return color_tuble


def random_walk():
    timmy.pensize(15)
    dir = [0, 90, 180, 270]
    timmy.speed('fastest')
    for i in range(0, 301):
        timmy.color(random_color())
        timmy.forward(30)
        timmy.setheading(random.choice(dir))


def circle(set_distance):
    timmy.speed('fastest')
    for angles in range(int(360 / set_distance)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + set_distance)


circle(5)

screen = t.Screen()
screen.exitonclick()

# EoF (End of File)