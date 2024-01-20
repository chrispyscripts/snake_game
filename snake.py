from turtle import *
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# starting positions for the initial 3 segments of the snake body
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        # list of all the segments of the snake body
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # initializes the starting position of the first
        # three segments of the snake body
        for x in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(x)
            self.segments.append(segment)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # sorts through all of the segments of the snake, starting with the
            # last segment in the list, and moves them all one spot forward
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def add_body(self):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        self.segments.append(segment)
