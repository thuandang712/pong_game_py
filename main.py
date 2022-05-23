from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_pad = Paddle((380, 0))
l_pad = Paddle((-380, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_pad.up, "Up")
screen.onkey(r_pad.down, "Down")

screen.onkey(l_pad.up, "w")
screen.onkey(l_pad.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_pad) < 50 and ball.xcor() > 365 or ball.distance(l_pad) < 50 and ball.xcor() < -365:
        ball.bounce_x()

    # Detect missing r_pad
    if ball.xcor() > 390:
        ball.reset_pos()
        scoreboard.increase_l_score()

    # Detect missing l_pad
    if ball.xcor() < -390:
        ball.reset_pos()
        scoreboard.increase_r_score()

screen.exitonclick()
