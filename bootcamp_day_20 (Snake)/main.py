from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setup the screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake_Game")
screen.tracer(0)  # turn off tracer so i can call update() whenever I want to refresh screen (seems fluent this way).


starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

# setup the snake
snake = Snake()
food = Food()
score = Scoreboard()

# Enable to play with arrow keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    # make sure all segments created are following the segment index 0 (tail is following head).
    snake.move()

    # Detect food collision.
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.score += 1
        score.refresh()
        snake.extend()

    # Detect wall collision
    if snake.segments[0].xcor() >= 300 or snake.segments[0].xcor() <= -300\
            or snake.segments[0].ycor() >= 300 or snake.segments[0].ycor() <= -300:
        is_game_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            is_game_on = False
            score.game_over()


screen.exitonclick()

# (EoF) End of File
