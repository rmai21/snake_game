from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.board()
        self.hideturtle()

    def board(self):
        self.write(f"Score = {self.score}", False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.board()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", True, align=ALIGNMENT, font=FONT)
