from turtle import Screen, Turtle
from Paddle import Paddle


# Setup the screen.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong_Game")
screen.tracer(0)

# show two paddle on screen
right_paddle = Paddle('right')
left_paddle = Paddle('left')


# Enable to play with arrow keys
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()