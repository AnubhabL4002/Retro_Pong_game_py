from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
scoreboard = Scoreboard()

screen.title("Pong: The Arcade Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball((0,0))

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "p")
screen.onkeypress(r_paddle.down, ";")

game_is_on= True
while game_is_on:
    screen.update()
    ball.move_ball()
    time.sleep(ball.move_speed)

    # Detect collision with the upper and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Using Pythagoras Theorem
    # if (ball.xcor() == 330 and ball.distance(r_paddle) < 63) or (ball.xcor() == -330 and ball.distance(l_paddle) < 63):
    #     ball.bounce_x()


    # Detect collision with paddles
    if (ball.distance(r_paddle) < 63 and ball.xcor() > 320 and ball.x_move > 0
            or ball.distance(l_paddle) <= 63 and ball.xcor() < -320
            and ball.x_move < 0):
        ball.bounce_x()


    # Detect collision with right paddle
    # if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
    #     ball.bounce_x_r_paddle()
    #
    # # Detect collision with left paddle
    # if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    #     ball.bounce_x_l_paddle()

    # Detect collision with right wall
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # Detect collision with left wall
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
