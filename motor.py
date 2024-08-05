from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

def up(self):
    if self.head.heading() != DOWN:
        self.head.setheading(UP)


def down(self):
    if self.head.heading() != UP:
        self.head.setheading(DOWN)


def left(self):
    if self.head.heading() != RIGHT:
        self.head.setheading(LEFT)


def right(self):
    if self.head.heading() != LEFT:
        self.head.setheading(RIGHT)

