from turtle import Turtle, Screen



class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.setheading(90)
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.goto(position)
        self.up()
        self.down()


    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)