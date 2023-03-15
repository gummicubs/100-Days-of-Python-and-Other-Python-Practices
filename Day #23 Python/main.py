import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def end_game():
    global game_is_on
    game_is_on = False

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score = Scoreboard()
player = Player()
car_manager = CarManager()

game_is_on = True


screen.listen()
car_manager.create_cars()

while game_is_on:
    screen.onkey(player.move_up, 'Up')
    car_manager.move_cars()
    car_manager.create_new_cars(score.score)
    # print(player.collide())   
    if player.next_level() == True:
        score.level()
        car_manager.update_speed()
    if car_manager.crash(player.ycor()) == True:
        game_is_on = False
    screen.update()    
    time.sleep(0.1)
    screen.onkey(end_game, 'space')

score.game_over()


screen.exitonclick()