from turtle import Turtle, Screen

MOVE_DISTANCE = 20
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.all_snakes = []
        self.create_snake()

    def create_snake(self):
        for position in POSITIONS:
            new_snake = Turtle("square")
            new_snake.color("White")
            new_snake.penup()
            new_snake.goto(position)
            self.all_snakes.append(new_snake)

    def move(self):
        for snake_num in range(len(self.all_snakes) - 1, 0, -1):
            x_new = self.all_snakes[snake_num - 1].xcor()
            y_new = self.all_snakes[snake_num - 1].ycor()
            self.all_snakes[snake_num].goto(x_new, y_new)
        self.all_snakes[0].forward(MOVE_DISTANCE)

