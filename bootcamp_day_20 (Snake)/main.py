from turtle import Screen
from snake import Snake
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

# Enable to play with arrow keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.5)
    # make sure all segments created are following the segment index 0 (tail is following head).
    snake.move()


screen.exitonclick()

# (EoF) End of File
