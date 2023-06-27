from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.1

    def move(self):
        """Moves ball in steps given of value self.x_move and self.y_move."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        """Bounces ball if wall has been hit"""
        self.y_move *= -1

    def collision_wall(self):
        """Checks if ball colides with wall"""
        if -280 > self.ycor() or self.ycor() > 280:
            is_colided = True
        else:
            is_colided = False
        return is_colided

    def colide_paddle(self, paddle_pos):
        """Checks if ball hits a paddle"""
        paddle_x = paddle_pos[0]
        paddle_y = paddle_pos[1]

        if paddle_x > 0:
            if self.pos()[0] == paddle_x - 20 and paddle_y - 50 <= self.pos()[1] <= paddle_y + 50:
                self.x_move *= -1
                self.speed *= 0.95
            else:
                pass
        else:
            if self.pos()[0] == paddle_x + 20 and paddle_y - 50 <= self.pos()[1] <= paddle_y + 50:
                self.x_move *= -1
                self.speed *= 0.95
            else:
                pass

    def score(self):
        player = ''
        if self.xcor() > 380:
            self.x_move *= -1
            player = 'left'
        elif self.xcor() < -380:
            self.x_move *= -1
            player = 'right'
        return player

