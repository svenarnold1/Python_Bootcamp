from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.setpos(STARTING_POSITION)
        self.finish_line = False

    def go_up(self):
        if self.ycor() == FINISH_LINE_Y:
            self.finish_line = True
            self.refresh()
        else:
            self.sety(self.position()[1] + MOVE_DISTANCE)

    def refresh(self):
        self.setpos(STARTING_POSITION)

