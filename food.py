from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # create a 10 by 10 pixle turtle
        self.color("yellow")
        self.speed("fastest")
        random_xcor = random.randint(-280, 280)
        random_ycor = random.randint(-290, 280)
        self.goto(random_xcor, random_ycor)
        self.refresh()

    def refresh(self):
        random_xcor = random.randint(-280, 280)
        random_ycor = random.randint(-290, 280)
        self.goto(random_xcor, random_ycor)
