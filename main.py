from turtle import Screen
from snake import *
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.tracer(0)
import time
screen.listen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_point()
        snake.add_body()
    screen.update()
    time.sleep(0.1)
    # screen.update() allows the screen to update every time this loop
    # occurs, eliminating the lag of movement of each snake segment
    if snake.head.xcor() > 320 or snake.head.xcor() < -320 or snake.head.ycor() > 320 or snake.head.ycor() < -320:
        game_on = False
        scoreboard.game_over()


screen.exitonclick()