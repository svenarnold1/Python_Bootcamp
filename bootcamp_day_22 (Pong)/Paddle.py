from turtle import Turtle


class Paddle:

    def __init__(self, direction):
        self.paddle = Turtle('square')
        self.paddle.color('white')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        if direction == "right":
            self.paddle.goto(350, 0)
        else:
            self.paddle.goto(-350, 0)

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)
