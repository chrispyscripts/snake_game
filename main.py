from turtle import Screen, Turtle
from Functions import *
screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
import time

def initialize():
    # initializes the starting position of the first
    # three segments of the snake body
    for x in starting_positions:
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(x)
        segments.append(segment)
    screen.update()

initialize()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    # screen.update() allows the screen to update every time this loop
    # occurs, eliminating the lag of movement of each snake segment

    for seg_num in range(len(segments) - 1, 0, -1):
        # sorts through all of the segments of the snake, starting with the
        # last segment in the list, and moves them all one spot forward
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)



print(segments)
screen.exitonclick()