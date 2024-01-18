starting_positions = [(0, 0), (-20, 0), (-40, 0)]
from turtle import Turtle

def initialize():
    for x in starting_positions:
        turtle = Turtle("square")
        turtle.color("white")
        turtle.goto(x)
