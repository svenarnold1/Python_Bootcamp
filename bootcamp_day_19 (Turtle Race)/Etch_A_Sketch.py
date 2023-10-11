from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move():
    tim.forward(10)


def move_back():
    tim.backward(10)


def right():
    tim.right(10)


def left():
    tim.left(10)


def go_home():
    screen.resetscreen()
    tim.home()


screen.listen()
screen.onkey(fun=move, key="w")
screen.onkey(fun=move_back, key="s")
screen.onkey(fun=right, key="d")
screen.onkey(fun=left, key="a")
screen.onkey(fun=go_home, key="c")
screen.exitonclick()
