from turtle import Turtle, Screen
import time
from SnakeGame import Snake, Food, Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('Snake!!')
screen.tracer(0)

score = Scoreboard()
snake = Snake()
food = Food()
screen.update()
time.sleep(0.1)

def turn_off():
    global game
    game = 'off'

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(turn_off, 'c')


game = 'on'
f = 1
score.update_score(0)

while game == 'on':

    snake.move()
    game = snake.checks_walls()
    for n in range(1, len(snake.segments)):
        if snake.segments[0].distance(x = snake.segments[n].xcor(), y = snake.segments[n].ycor()) < 15:
            print(snake.segments[0].distance(x = snake.segments[n].xcor(), y = snake.segments[n].ycor()))
            game = 'off'
    if snake.segments[0].distance(x = food.xcor(), y = food.ycor()) <=20:
        food.refresh()
        f+=1
        snake.add_segment()
        score.update_score(10)
    screen.update()
    time.sleep(1/(f+4))

score.game_over()

     
screen.exitonclick()