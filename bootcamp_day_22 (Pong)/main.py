from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from pong_Scoreboard import Scoreboard
import time


# Setup the screen.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong_Game")
screen.tracer(0)

# show two paddle on screen
right_paddle = Paddle('right')
left_paddle = Paddle('left')
ball = Ball()
scoreboard = Scoreboard()

# Enable to play with arrow keys
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True
speed = 0.1
while game_is_on:
    screen.update()

    ball.move()

    # Detect collision with wall.
    if ball.collision_wall():
        ball.bounce()

    # increase score
    scorer = ball.score()
    print(scorer)
    if scorer == 'left':
        scoreboard.l_point()
    elif scorer == 'right':
        scoreboard.r_point()

    # Detect collision with right or left paddle.
    ball.colide_paddle(right_paddle.pos())
    ball.colide_paddle(left_paddle.pos())

    # increase speed of ball.
    time.sleep(ball.speed)


screen.exitonclick()
