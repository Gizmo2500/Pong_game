from turtle import Screen
from paddles import Paddle
from ball import Ball
from score_board import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
width = screen.window_width() / 2
height = screen.window_height() / 2

screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()
scores = Score()
screen.listen()


# on key no brackets
screen.onkey(key="Up", fun=paddle_1.up)
screen.onkey(key="Down", fun=paddle_1.down)
screen.onkey(key="w", fun=paddle_2.up)
screen.onkey(key="s", fun=paddle_2.down)

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce()

    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    # if ball.distance(paddle_2) < 50 and ball.xcor() < -320:
    #     ball.paddle_bounce()
    # player 1 side
    if ball.xcor() >= 380:
        ball.reset_ball()
        scores.p2_new_score()

    # player 2 side
    if ball.xcor() <= -380:
        ball.reset_ball()
        scores.p1_new_score()

screen.exitonclick()
