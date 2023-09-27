import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_state = turtle.textinput(title="Guess the State", prompt="Name a state of the US")
print(answer_state)

screen.exitonclick()
