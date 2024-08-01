from turtle import Turtle, Screen
import time
import snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)        # turns off the animation

snake = snake.Snake()
screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
