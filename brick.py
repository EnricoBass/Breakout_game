from turtle import Turtle


class Brick(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(str(color))
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def destroy(self):
        self.goto(1000, 0)