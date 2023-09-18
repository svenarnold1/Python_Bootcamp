from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto((0, 270))
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)
