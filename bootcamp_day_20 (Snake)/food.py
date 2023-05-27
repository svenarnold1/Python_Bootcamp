from turtle import Turtle

import random


class Food(Turtle):  # food class is inheriting of superclass Turtle()

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("blue")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

