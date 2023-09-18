from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"
SCORE_POSITION = (-270, 250)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.level = 0
        self.penup()
        self.goto(SCORE_POSITION)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.refresh()
