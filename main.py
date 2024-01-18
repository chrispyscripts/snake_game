from turtle import Screen, Turtle
from Functions import *
screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.tracer()
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_segments = []

def initialize():
    for x in starting_positions:
        turtle = Turtle("square")
        turtle.color("white")
        turtle.goto(x)
        snake_segments.append(turtle)
    screen.update()

initialize()

print(snake_segments)

screen.exitonclick()