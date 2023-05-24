from turtle import Turtle, Screen
import random

# screen settings.
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Welcome to the Turtle race!")

# lists needed to create the race
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


def create_race():

    # create 6 turtle classes including pre made settings.
    for turtle_index in range(0, 6):
        new_turtle = Turtle("turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)

    user_bet = screen.textinput(title="Make a bet", prompt="What color is going to win the race?: ")
    if user_bet not in colors:
        while user_bet not in colors:
            user_bet = screen.textinput(title="Make a bet", prompt="What color is going to win the race?: ")
        race_is_on = True
    else:
        race_is_on = True

    while race_is_on:

        for turtle in all_turtles:

            if turtle.xcor() > 230:
                race_is_on = False
                winner_turtle = turtle.pencolor()

                if winner_turtle == user_bet:
                    print(f"You have Won! The winner is the {winner_turtle} Turtle!")
                else:
                    print(f"You Loose! The winner is the {winner_turtle} Turtle!")

            # random choice of speed
            move_forward = random.randint(0, 10)
            turtle.forward(move_forward)


create_race()

# check if user wants to race again.
race_again = input("Do you want to start another race? Type 'y' or 'n': ").lower()
while race_again == "y":
    screen.clear()
    all_turtles = []
    create_race()
    race_again = input("Do you want to start another race? Type 'y' or 'n': ").lower()
else:
    print("See you next time!")


screen = Screen()
screen.exitonclick()
