import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def setup_screen():
    """setup the screen the player can play on."""
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.title("Turtle crossing game!")


# create objects
screen = Screen()
setup_screen()
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


# Enable to play with arrow keys
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
amount_of_loops = 0
create_a_car = 6
while game_is_on:

    # Create random cars
    if amount_of_loops == create_a_car:
        car_manager.create_car()
        amount_of_loops = 0
    else:
        amount_of_loops += 1

    # Move all cars
    car_manager.move_cars()

    # Detect Collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Increase level if finish line has been reached.
    if player.finish_line:
        car_manager.increase_speed()
        scoreboard.increase_level()
        player.finish_line = False

    time.sleep(0.1)
    screen.update()


screen.exitonclick()

# EoF ( End of File)
