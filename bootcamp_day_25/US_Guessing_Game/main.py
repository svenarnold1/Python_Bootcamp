import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


def create_state(x, y):
    """Creates a turtle as text ans puts in to given coordinates."""
    new_text = turtle.Turtle()
    new_text.penup()
    new_text.hideturtle()
    new_text.goto(x, y)
    new_text.write(answer_state)


with open("50_states.csv") as state_file:
    states_data = pandas.read_csv(state_file)

states_list = states_data["state"].to_list()


already_guessed = []
while len(already_guessed) < len(states_list):
    answer_state = turtle.textinput(title=f"{len(already_guessed)} /  {len(states_list)} States Correct",
                                    prompt="Name a state of the US").title()
    if answer_state == "Exit":
        break
    elif answer_state in states_list and answer_state not in already_guessed:
        already_guessed.append(answer_state)
        state_cor = states_data[states_data.state == answer_state]
        create_state(float(state_cor.x), float(state_cor.y))


# states to learn.csv
if len(already_guessed) < len(states_list):
    missing_states = set(states_list) - set(already_guessed)  # find missing states in list and store as set
    # missing = [state for state in states_list if state not in already_guessed]
    to_learn_dict = {"States to learn": list(missing_states)}
    pandas.DataFrame(to_learn_dict).to_csv("states_to_learn.csv")
screen.exitonclick()
# EoF (End of File)
