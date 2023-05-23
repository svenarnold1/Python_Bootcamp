# finding most used colors of input .jpg
# import colorgram
#
# # finding six colors in input picture
# colors = colorgram.extract('Damien_Hirst_spot_painting.jpg', 30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

# creating a painting

import turtle as t
import random

color_list = [
                (223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48),
                (26, 107, 159), (237, 225, 235), (209, 161, 111), (144, 29, 63),
                (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43),
                (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95),
                (108, 182, 90), (110, 99, 87), (193, 187, 46), (240, 204, 2),
                (1, 102, 119), (19, 22, 21), (50, 150, 109), (172, 212, 172), (118, 36, 34),
                (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210)
             ]

# create painting 10x10 rows
# diameter dot = 20 and space between dots = 50


timmy = t.Turtle()
t.colormode(255)
# hide turtle and set speed to fastest.
timmy.hideturtle()
timmy.speed('fastest')
timmy.penup()
# set position so whole painting is visible.
timmy.setpos(-230, -250)
# hide turtle and set speed to fastest.
timmy.hideturtle()
timmy.speed('fastest')


def hirst_painting():
    print(timmy.pos())

    def tuple_to_list(my_tuple):
        x = my_tuple[0]
        y = my_tuple[1]
        return [x, y]

    def create_dotline():
        for dots in range(0, 10):
            timmy.dot(20, random.choice(color_list))
            timmy.forward(50)

    for rows in range(0, 10):
        prev_pos = timmy.position()
        cor_list = tuple_to_list(prev_pos)
        create_dotline()
        timmy.goto(cor_list[0], cor_list[1] + 50)


hirst_painting()

screen = t.Screen()
screen.exitonclick()
