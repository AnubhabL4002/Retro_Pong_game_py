from turtle import Screen
from paddle import Paddle
import time

screen = Screen()

screen.title("Pong: The Arcade Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkey(paddle.up, "w")
screen.onkey(paddle.down, "s")

game_is_on= True
while game_is_on:
    screen.update()
    # time.sleep(0.1)


screen.exitonclick()
