from turtle import Turtle

MOVE_DISTANCE = 20
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("dark violet")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    # def up(self):
    #     new_y = self.ycor() + MOVE_DISTANCE
    #     self.goto(self.xcor(),new_y)
    # def down(self):
    #     new_y = self.ycor() - MOVE_DISTANCE
    #     self.goto(self.xcor(),new_y)

    def up(self):
        if self.ycor() < 225:
            self.sety(self.ycor() + 20)

    def down(self):
        if self.ycor() > -225:
            self.sety(self.ycor() - 20)