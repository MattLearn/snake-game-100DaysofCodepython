from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.set_highscore()
        self.color("White")
        self.penup()
        self.goto(0, 320)
        self.hideturtle()
        self.update_scoreboard()

    def set_highscore(self):
        with open("data.txt") as data:
            self.highscore = int(data.read())

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
            self.set_highscore()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Highscore:{self.highscore}\nScore:{self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.reset()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))

    def score_increase(self):
        self.score += 1
        self.update_scoreboard()
