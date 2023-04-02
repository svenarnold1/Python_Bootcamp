## first contact with turtle
#
#from turtle import Turtle, Screen
#
#timmy = Turtle()
#print(timmy)
#
## changing appereance of timmy (turtle)
#timmy.shape("turtle")
#timmy.color("green")
#timmy.shapesize(5)
## timmy.settiltangle(-45)
#
## show screen
#my_screen = Screen()
#print(my_screen.canvheight)
#
## move the turtle
#timmy.forward(100)
#timmy.left(90)
#timmy.forward(100)
#timmy.left(90)
#timmy.forward(100)
#timmy.left(90)
#timmy.forward(100)
#timmy.home()
#
## exits program with click
#
#my_screen.exitonclick()

# installed pretty table ( File-Settings-current project-python intepreter- + sign and add it)

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)



