from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_paddle = 0
        self.r_paddle = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_paddle, move=False, align=ALIGNMENT, font=FONT)
        self.goto(0, 200)
        self.write(':', move=False, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_paddle, move=False, align=ALIGNMENT, font=FONT)

    def l_point(self):
        """tracks if left paddle made point."""
        self.l_paddle += 1
        self.update_scoreboard()

    def r_point(self):
        """tracks if right paddle made point."""
        self.r_paddle += 1
        self.update_scoreboard()
