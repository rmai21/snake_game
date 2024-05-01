from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("scores.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.board()

    def update(self):
        self.score += 1
        self.clear()
        self.board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("scores.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.board()

    def board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)
