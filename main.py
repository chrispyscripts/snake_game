from turtle import Screen
from snake import *
screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.tracer(0)
import time
screen.listen()
snake = Snake()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    # screen.update() allows the screen to update every time this loop
    # occurs, eliminating the lag of movement of each snake segment





print(segments)
screen.exitonclick()