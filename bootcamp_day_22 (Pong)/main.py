from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
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

# Enable to play with arrow keys
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True
score_player_1 = 0
score_player_2 = 0
while game_is_on:
    screen.update()

    ball.move()

    # Detect collision with wall.
    if ball.collision_wall():
        ball.bounce()

    # Detect collision with right paddle.
    ball.colide_paddle(right_paddle.pos())
    ball.colide_paddle(left_paddle.pos())

    # Check if player made a point. (Other player couldnt bounce the ball with paddle)

    time.sleep(0.1)


screen.exitonclick()
