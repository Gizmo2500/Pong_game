from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.score_p1 = 0
        self.score_p2 = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(100, 200)
        self.write(self.score_p1, align="center", font=("Courier", 80, "normal"))
        self.goto(-100, 200)
        self.write(self.score_p2, align="center", font=("Courier", 80, "normal"))

    def p1_new_score(self):
        self.score_p1 += 1
        self.clear()
        self.update_scoreboard()

    def p2_new_score(self):
        self.score_p2 += 1
        self.clear()
        self.update_scoreboard()


