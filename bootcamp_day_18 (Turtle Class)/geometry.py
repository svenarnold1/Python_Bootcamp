import turtle

timmy = turtle.Turtle()


def triangle():
    for _ in range(3):
        timmy.forward(100)
        timmy.left(120)


def square():
    for _ in range(4):
        timmy.forward(100)
        timmy.left(90)


def pentagon():
    for _ in range(5):
        timmy.forward(100)
        timmy.left(360 / 5)


def hexagon():
    for _ in range(6):
        timmy.forward(100)
        timmy.left(360 / 6)


def heptagon():
    for _ in range(7):
        timmy.forward(100)
        timmy.left(360 / 7)


def octagon():
    for _ in range(8):
        timmy.forward(100)
        timmy.left(360 / 8)


def nonagon():
    for _ in range(9):
        timmy.forward(100)
        timmy.left(360 / 9)


def decagon():
    for _ in range(10):
        timmy.forward(100)
        timmy.left(360 / 10)