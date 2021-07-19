from turtle import Screen
from brick import Brick
from paddle import Paddle
from ball import Ball
import time
TIME = 0.1

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)  # It is used to update the screen after a certain path.

# Wall deployment
bricks = {"green": [],
          "yellow": [],
          "red": [],}
y = 0

colors = ["green", "yellow", "red"]
for color in colors:
    y += 50

    for n in range(7):
        brick = Brick((-330 + n*110, y), color)
        bricks[color].append(brick)

paddle = Paddle((0, -200))

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_is_on = True
ball = Ball()

while game_is_on:
    screen.update()
    time.sleep(TIME)
    ball.move()

    # detect limits:
    if ball.xcor() > 370 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    # detect collision with paddle:
    if ball.ycor() < -170 and ball.distance(paddle) < 50:
        ball.bounce_y()

    # detect collision with bricks:
    # I have to extract singularly each brick from the dictionary
    for element in bricks:
        for i in range(7):
            el_brick = bricks[element][i]
            if element == "green":
                if 22.5 < ball.ycor() < 50   and ball.distance(el_brick) < 52:
                    ball.bounce_y()
                    el_brick.destroy()

            if element == "yellow":
                if 75 < ball.ycor() < 100   and ball.distance(el_brick) < 52:
                    ball.bounce_y()
                    el_brick.destroy()

            if element == "red":
                if 125 < ball.ycor() < 150   and ball.distance(el_brick) < 52:
                    ball.bounce_y()
                    el_brick.destroy()




screen.exitonclick()
