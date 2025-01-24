from turtle import Turtle

MOVE_DISTANCE = 20
class Paddle:
    def __init__(self):
        self.p_body = Turtle("square")
        self.p_body.color("blue")
        self.p_body.shapesize(stretch_wid=5, stretch_len=1)
        self.p_body.penup()
        self.p_body.goto(x=350, y=0)

    def up(self):
        new_y = self.p_body.ycor() + MOVE_DISTANCE
        self.p_body.goto(self.p_body.xcor(),new_y)
    def down(self):
        new_y = self.p_body.ycor() - MOVE_DISTANCE
        self.p_body.goto(self.p_body.xcor(),new_y)