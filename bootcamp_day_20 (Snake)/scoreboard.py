from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 16, "normal")

with open("snake_highscore.txt", mode='r') as file:
    HIGHSCORE = file.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.highscore = int(HIGHSCORE)
        self.penup()
        self.goto((0, 270))
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score : {self.score} Highscore: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("snake_highscore.txt", mode='w') as newhighscore:
                newhighscore.write(str(self.highscore))
        self.score = 0
        self.refresh()

    def increase_score(self):
        self.score += 1
        self.refresh()
