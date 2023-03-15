from turtle import Turtle, Screen
from pieces import Paddle, Ball, Scoreboard
import time

def exit():
    global play
    play = False



screen = Screen()
screen.bgcolor('black')
screen.screensize(canvwidth = 600, canvheight=600)
screen.tracer(0)

player1 = Paddle(1)
player2 = Paddle(2)
ball = Ball()
score = Scoreboard()

play = True
while play:
    screen.update()

    # game_on = True

    screen.listen()

    # screen.onkey(ball.next, 'space')

    while ball.game_on:
        
        screen.onkey(exit, 'c')
        screen.onkeypress(player1.move_up, 'w')
        screen.onkeypress(player1.move_down, 's')
        screen.onkeypress(player2.move_up, 'r')
        screen.onkeypress(player2.move_down, 'f')
        ball.move()
        screen.update()
        ball.left_paddle_reflect(player1)
        ball.right_paddle_reflect(player2)
        time.sleep(0.1)
        # if (ball.hit_walls() == '1') or (ball.hit_walls() == '2'):
        score.update_score(ball.hit_walls())
        
    screen.onkey(ball.next, 'space')


score.game_over()


screen.exitonclick()