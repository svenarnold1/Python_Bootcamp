import random
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')

colors = ['red', 'blue', 'cornsilk3', 'coral', 'gold3', 'purple', 'khaki', 'DarkCyan', 'indianred', 'black',
          'orange', 'OliveDrab', 'orchid', 'moccasin', 'magenta', 'MediumOrchid', 'cyan',
          'deep sky blue'
          ]

used_colors = []


def set_color(used):
    """avoids choosing same color two times and returns color"""
    color = random.choice(colors)

    while color in used:
        color = random.choice(colors)
    # add chosen color to list user_colors
    used_colors.append(color)
    return color


# draw all the geometry bodies out of geometry file in one draw
def geometry_art():
    corners = 3
    while corners < 11:
        timmy.color(set_color(used_colors))
        for _ in range(corners):
            timmy.forward(100)
            timmy.right(360 / corners)
        corners += 1


def dashed_line():

    for _ in range(15):
        timmy.pendown()
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)


geometry_art()
timmy.forward(100)

screen = Screen()
screen.exitonclick()
# EoF (End of File)