from turtle import Screen
import time
from food import Food
from snake import SnakeClass
from scorecoard import ScoreBoard

BOUNDARY_BOX = 400

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Basic Man's Snake")
screen.tracer(0)


snake = SnakeClass()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_active = True
while game_active:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_increase()

    if snake.head.xcor() > BOUNDARY_BOX or snake.head.xcor() < -BOUNDARY_BOX or snake.head.ycor() > BOUNDARY_BOX or snake.head.ycor() < -BOUNDARY_BOX:
#        game_active = False
        scoreboard.reset()
        snake.reset()


    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
 #           game_active = False
            scoreboard.reset()
            snake.reset()


scoreboard.game_over()
screen.exitonclick()
